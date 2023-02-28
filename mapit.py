"""mapit.py

Launch a map in the browser using an address from the command line or clipboard.
"""

import webbrowser
import sys

if len(sys.argv) > 1:
    print(sys.argv)
    # Get address from command line.
    address = " ".join(sys.argv[1:])
    print(address)

# TODO: Get address from clipboard.