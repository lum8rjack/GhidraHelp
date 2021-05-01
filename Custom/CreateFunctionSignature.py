#Creates a signature based on the function name provided

# Specifying the function name, the script will identify
# the first X bytes of the function that can be used to create 
# a signature. 

#@author lum8rjack
#@category FunctionID
#@keybinding 
#@menupath
#@toolbar 

from binascii import hexlify
from ghidra.program.flatapi import FlatProgramAPI

def sigToArray(sig):
    outSig = "["
    for i in range(0,len(sig),2):
    	outSig = outSig + "0x" + sig[i:i+2] + ", "
    	
    outSig = outSig[:-2] + "]"
    return outSig

def sigToHex(sig):
    outSig = ""
    for i in range(0,len(sig),2):
        outSig = outSig + "\\x" + sig[i:i+2]

    return outSig

def sigToSpace(sig):
    outSig = ""
    for i in range(0,len(sig),2):
        outSig = outSig + sig[i:i+2] + " "

    return outSig


def checkSig(sig):
    # Scan the file to see how many time the signature occurs
    o = 0
    arrayAddrs = findBytes(None, sig, 5)
    o= len(arrayAddrs)
    return o

# Inform the user of the current program
state = getState()
currentProgram = state.getCurrentProgram()
name = currentProgram.getName()
print("The currently loaded program is: '{}'".format(name))

# Get the name of the function
fname = askString("Function name", "Function name: ")
print("Creating signature for the function: {}").format(fname)

# Get a FunctionManager reference for the current program
functionManager = currentProgram.getFunctionManager()

funcs = functionManager.getFunctions(True) # True means 'forward'
addr = None
for func in funcs: 
    if func.getName() == fname:
        addr = func.getEntryPoint()
        print("Function: {} @ 0x{}".format(func.getName(), func.getEntryPoint()))

# Make sure the user specified a correct function
if addr != None:
    # Start the signature by getting the first 5 bytes
    sigLength = 5
    sig = hexlify(getBytes(addr, sigLength))
    sigReadable = sigToHex(sig)

    # Check if the signature is unique
    # If not, then add one byte more until it is
    while checkSig(sigReadable) != 1:
        # Add one more byte
        sigLength = sigLength + 1
        sig = hexlify(getBytes(addr, sigLength))
        sigReadable = sigToHex(sig)

    # Print the signature
    print("Signature length: {}").format(str(sigLength))
    print("Signature: {}").format(sig)
    print("Signature: {}").format(sigToArray(sig))
    print("Signature: {}").format(sigToSpace(sig))
    print("Signature: {}").format(sigReadable)

    # Create a mask based on the signature
    mask = ""
    for x in range(sigLength):
        mask = mask + "x"

    print("Mask: {}").format(mask)

else:
    print("Could not find the function: {}").format(fname)
