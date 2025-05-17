#!/usr/bin/env python3
"""
Script to calculate CRC16-CCITT checksum for a given
firmware binary and write to auxiliary file firmware.inf
as required by the default bootloader of BoogieBoard.

Copyright (C) 2025 Sandro Pischinger <mail+klipper@sandropischinger.de>

"""
from __future__ import with_statement
import optparse
import binascii


def main():
    usage = "%prog <input_path> <output_path> <command>"
    opts = optparse.OptionParser(usage)
    options, args = opts.parse_args()
    if len(args) != 3:
        opts.error("Incorrect number of arguments.")
    input_path, output_path, command = args

    if command == "crc16-ccitt":
        with open(input_path, "rb") as f:
            crc_bytes = binascii.crc_hqx(f.read(), 0xFFFF)
        with open(output_path, "wb") as f:
            f.write(crc_bytes.to_bytes(2, 'big'))


if __name__ == '__main__':
    main()
