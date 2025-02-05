#!/usr/bin/env python3
import os
import json
import subprocess
from sphinx_action import action

# This is the entrypoint called by Github when our action is run. All the
# Github specific setup is done here to make it easy to test the action code
# in isolation.
if __name__ == "__main__":
    print("[sphinx-action] Starting sphinx-action build.")

    print("Running pre-build")
    if "INPUT_PRE-BUILD-COMMAND" in os.environ:
        pre_command = os.environ["INPUT_PRE-BUILD-COMMAND"]
        print("Running: {}".format(pre_command))
        result = subprocess.run(pre_command, shell=True)
    print("Done running-pre-build")

    github_env = action.GithubEnvironment(
        build_command=os.environ.get("INPUT_BUILD-COMMAND"),
    )

    # We build the doc folder passed in the inputs.
    action.build_all_docs(github_env, [os.environ.get("INPUT_DOCS-FOLDER")])
