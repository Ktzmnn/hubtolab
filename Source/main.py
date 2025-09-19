import lib.supadinterface.SUPadInterface as supad
import argparse
import sys
from pathlib import Path

#### Configuration of the script name and version
proj = supad.scriptVersion()
proj.name = "testCI.exe"
proj.major = 1 
proj.minor = 0
proj.patch = 0

# Description of the script name and version
des = supad.SUPADScript()
des.description= 'just a test for CI'
des.doc = ''
des.supportedPlugIns.lgc.supported = True
des.expectedInput = ""
des.alias = "TestCI"
des.version = proj

# Configuring all the argument needed
parser = argparse.ArgumentParser(prog=des.getName(), description= des.getSUPADConfigText(),formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-i","--input", required=True, type=Path, help="Valid path to an LGC JSON result file")
parser.add_argument("-v","--version",  action="version", version=des.getVersionText() )

args = parser.parse_args()

print("Hello World!")

sys.exit(0)
