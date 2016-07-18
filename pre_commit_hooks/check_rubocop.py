from __future__ import print_function

import argparse
import subprocess
import sys


def check_rubocop(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help='auto fix', action='store_true')
    parser.add_argument('filenames', nargs='*', help='filenames to check.')
    args = parser.parse_args(argv)

    retval = 0

    command = ["rubocop", "--force-exclusion", "--display-cop-names"] + args.filenames

    if args.a == True:
        command += ["-a"]

    try:
        retval = subprocess.check_call(command, shell=False)
    except subprocess.CalledProcessError as err:
        print('{0}: rubocop failed ({1})'.format(args.filenames, err))
        retval = 1

    return retval


if __name__ == '__main__':
    sys.exit(check_rubocop())
