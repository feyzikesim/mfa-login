#!/usr/bin/python3

import base64
import hashlib
import hmac
import os
import struct
import sys
import time


sys.path.append(os.environ.get("HOME") + "/mfa_login")

import sqlite_ops as sqlite_ops


def get_hotp_token(secret, intervals_no):
    if len(secret) % 4:
        secret += '=' * (4 - len(secret) % 4)
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = h[19] & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h


def get_totp_token():
    secret = sqlite_ops.read_secret_from_db(sys.argv[1])
    if secret is not None:
        code = str(get_hotp_token(secret, intervals_no=int(time.time())//30))
        if len(code) < 6:
            code = "0" * (6 - len(code)) + code
        return code
    else:
        return -1


if __name__ == "__main__":
    sys.stdout.write(get_totp_token())
