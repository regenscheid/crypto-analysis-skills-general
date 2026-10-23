#!/usr/bin/env python3
"""Check that the numbers a document claims are the numbers its commands produce.

    python3 reproduce.py DOC.md            # list what it would run, and the claims
    python3 reproduce.py DOC.md --run      # actually run them and compare

Step 3 of `verify-claim`, made mechanical. The failure it exists to catch is
specific and was observed rather than imagined: a parameter set changed, some
downstream numbers were recomputed and others were carried forward, and a
key-recovery figure ended up 10.2 bits wrong inside a rubric whose stated
tolerance was +/-0.5. Nothing in the document looked wrong. Every number was
plausible, formatted identically, and sitting next to the command that was
supposed to have produced it.

A human re-reading the file cannot catch that. Running the commands can.

The check is deliberately one-directional and blunt: for every `2^x` the prose
claims, does SOME listed command actually emit it? That is weaker than mapping
each claim to its own command, and it is what can be done without the document
declaring a machine-readable link between the two. It catches stale values,
transposed digits and numbers no command produces at all -- which is the whole
observed failure population.

Commands are NOT run without `--run`, and only commands from fenced blocks in the
document are ever considered. Read them before passing the flag. A fenced
invocation of this verifier is documentation, not a command that generates a
claim, and is excluded to prevent recursive self-execution.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys

# A claimed cost: 2^218.6, `2^-781`, 2^158.2 -- optionally in backticks/bold.
#
# The negative lookbehind excludes FIELD notation. "F_2^71" is a field, not a
# cost, and matching it produced a confident false positive on the first run --
# a checker that cries wolf gets ignored, which is the failure mode it exists to
# prevent. Same for "F_{q^r}" style subscripts.
CLAIM = re.compile(r"(?<![_{])2\^(-?\d+(?:\.\d+)?)")
FENCE = re.compile(r"```(?:bash|sh|console)?\n(.*?)```", re.S)
# Shell variable assignment, e.g. S=/path/to/sage
ASSIGN = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)=(\S+)\s*$")
SELF_INVOCATION = re.compile(r"(?:^|[\s/])reproduce\.py(?:\s|$)")


def parse(path):
    """Return (commands, claimed_numbers) from a markdown document."""
    text = open(path, encoding="utf-8").read()
    env, cmds = {}, []
    for block in FENCE.findall(text):
        # Join continuation lines so a wrapped invocation stays one command.
        joined, buf = [], ""
        for raw in block.splitlines():
            line = raw.rstrip()
            if not line.strip() or line.strip().startswith("#"):
                continue
            buf += line[:-1] + " " if line.endswith("\\") else line
            if not line.endswith("\\"):
                joined.append(buf)
                buf = ""
        for line in joined:
            m = ASSIGN.match(line)
            if m:
                env[m.group(1)] = m.group(2)
                continue
            cmds.append(line)

    # Expand $VAR / ${VAR} from assignments seen in the document itself.
    def expand(c):
        for k, v in env.items():
            c = c.replace("${%s}" % k, v).replace("$" + k, v)
        return os.path.expanduser(c)

    cmds = [expand(c) for c in cmds]
    # A document may include the command that audits itself. It cannot generate
    # any of the document's claims, and executing it recursively re-parses and
    # re-runs the same block forever.
    cmds = [c for c in cmds if not SELF_INVOCATION.search(c)]

    # Claims come from the prose, not from inside the command blocks -- a number
    # that only appears in a command is an input, not a claim about output.
    prose = FENCE.sub("", text)
    claims = sorted({float(m) for m in CLAIM.findall(prose)})
    return cmds, claims


def run(cmds, cwd, timeout):
    out = []
    for c in cmds:
        sys.stderr.write("  running: %s\n" % c[:96])
        try:
            r = subprocess.run(c, shell=True, cwd=cwd, timeout=timeout,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            out.append((c, r.stdout.decode("utf-8", "replace")))
        except subprocess.TimeoutExpired:
            out.append((c, "<<TIMEOUT after %ds>>" % timeout))
        except Exception as exc:                       # noqa: BLE001
            out.append((c, "<<FAILED: %s>>" % exc))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("doc")
    ap.add_argument("--run", action="store_true", help="actually execute")
    ap.add_argument("--cwd", default=".", help="working directory for commands")
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--tolerance", type=float, default=0.05,
                    help="exponent tolerance when matching a claim to output")
    args = ap.parse_args()

    cmds, claims = parse(args.doc)
    print("%s\n  commands found: %d\n  numeric claims: %d"
          % (args.doc, len(cmds), len(claims)))

    if not args.run:
        print("\nWould run (re-invoke with --run):")
        for c in cmds:
            print("   %s" % c)
        print("\nClaims: %s" % ", ".join("2^%g" % c for c in claims))
        return 0

    results = run(cmds, args.cwd, args.timeout)
    produced = set()
    for _, text in results:
        produced.update(float(m) for m in CLAIM.findall(text))

    # Numeric comparison with a tolerance, not string equality. "2^-781" in prose
    # and "2^-781.0" in output are the same claim, and a checker that calls them
    # different teaches its user to skim the output.
    def hit(c):
        return any(abs(c - p) <= args.tolerance for p in produced)

    missing = [c for c in claims if not hit(c)]
    broken = [c for c, t in results if t.startswith("<<")]

    print("\n  numbers produced by some command: %d" % len(produced))
    print("  claims reproduced: %d of %d" % (len(claims) - len(missing), len(claims)))

    if broken:
        print("\nCOMMANDS THAT DID NOT COMPLETE")
        for c in broken:
            print("   %s" % c[:96])

    if missing:
        print("\nCLAIMED BUT NOT PRODUCED -- each is unsupported until explained")
        for c in missing:
            print("   2^%g" % c)
        print("\nA claim may legitimately appear here if it is derived by hand"
              "\n(a probability, a difference of two costs) rather than printed."
              "\nSay which, in the document, next to the number.")
    else:
        print("\nEvery claimed number was produced by a listed command.")
    return 1 if (missing or broken) else 0


if __name__ == "__main__":
    sys.exit(main())
