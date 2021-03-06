#!/usr/bin/env python
from ooi_port_agent.agents import Packet
import sys


def main():
    # check that there is only one parameter on the command line
    if len(sys.argv) < 2:
        sys.stderr.write('Expected one or more files to decode, got 0!\n')
        sys.exit(1)

    files = sys.argv[1:]

    for filename in files:
        with open(filename, "rb") as fh:
            while True:
                packet = Packet.packet_from_fh(fh)
                if packet is None:
                    break
                print packet

if __name__ == '__main__':
    main()
