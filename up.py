#!/usr/bin/env python2
import sys
import os
from argparse import ArgumentParser
from subprocess import call

def _args():
    p = ArgumentParser("rancher-oauth")
    p.add_argument("-u", "--upstream")
    p.add_argument("-p", "--port", type=int, default=80)
    p.add_argument("-s", "--stack")
    p.add_argument("fqdn", nargs="*", help="Fully qualified domain names")
    return p.parse_args()

def _run(args):
    cmd = ["rancher", "up", "-s", args.stack]
    if os.path.exists("environment"):
        cmd.extend(["--env-file", "environment"])

    env = {}
    env["UPSTREAM_HOST"] = args.upstream
    env["UPSTREAM_PORT"] = str(args.port)
    if args.fqdn:
        env["OAUTH_FQDN"] = ",".join(args.fqdn)

    print env

    env.update(os.environ.copy())

    return call(cmd, env=env)

if __name__ == "__main__":
    args = _args()
    code = _run(args)
    sys.exit(code)