from meta import githubUrl
from textwrap import dedent
from glob import glob
import is_git_repo_clean
import os
import subprocess
import sys


def printErr(msg):
    print(msg, file=sys.stderr)


if not is_git_repo_clean.checkSync():
    printErr(
        dedent(
            """
            the git repo is not clean
            aborting build\
            """
        )
    )
    exit(1)

pypiWarning = dedent(
    f"""\
    *Note: This document is best viewed [on github]({githubUrl}).
    Pypi's headers are all caps which presents inaccurate information*"
    """
)
pypiWarnComment = "<!-- pypiwarn -->"

with open("./README.md", "r") as f:
    commentedWarn = f.read()

with open("./README.md", "w") as f:
    f.write(commentedWarn.replace(pypiWarnComment, pypiWarning, 1))

for f in glob("dist/*"):
    os.remove(f)

subprocess.run([sys.executable, "setup.py", "sdist"])

with open("README.md", "w") as f:
    f.write(commentedWarn)

print("donezo!")
