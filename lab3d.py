#!/usr/bin/env python3
'''Lab 3 - Script to get free disk space on Linux root directory'''
# Author ID: [bb-c1]

import subprocess

def free_space():
    command_output = subprocess.check_output(["df", "-h"]).decode("utf-8")
    root_partition = [line.split() for line in command_output.splitlines() if line.endswith(" /")][0]
    return root_partition[3]

if __name__ == "__main__":
    print(free_space().strip())
