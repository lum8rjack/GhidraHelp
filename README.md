# GhidraHelp
Repository containing different Ghidra scripts and resources

## Custom
Custom Ghidra scripts.

* CreateFunctionSignature.py - Creates a signature of the specified function that can be used for function hooking.

```
CreateFunctionSignature.py> Running...
The currently loaded program is: 'test.bin'
Creating signature for the function: sum
Function: sum @ 0x00101189
Signature length: 9
Signature: f30f1efa554889e589
Signature: [0xf3, 0x0f, 0x1e, 0xfa, 0x55, 0x48, 0x89, 0xe5, 0x89]
Signature: f3 0f 1e fa 55 48 89 e5 89 
Signature: \xf3\x0f\x1e\xfa\x55\x48\x89\xe5\x89
Mask: xxxxxxxxx
CreateFunctionSignature.py> Finished!
```


## OtherRepos
Ghidra scripts I pulled from other repos to have them all in one area.

* [ApplySig.py](https://github.com/NWMonster/ApplySig/blob/master/ApplySig.py) - Apply IDA FLIRT signatures for Ghidra

* [FindBannedFunctions.py](https://github.com/VDA-Labs/GHIDRA-Scripts/blob/master/FindBannedFunctions.py) - Searches through a program for the use of any unsafe functions
    * https://vdalabs.com/2019/03/09/automating-ghidra-writing-a-script-to-find-banned-functions/

* [SavePatch.py](https://github.com/schlafwandler/ghidra_SavePatch) - Save small patches back to the executable file

* [SystemCallAuditor.py](https://gist.github.com/cetfor/807c50add3cce7fbc36fa90252d7fba7) - Checks system calls for command injection patterns
    * https://www.youtube.com/watch?v=UVNeg7Vqytc&t=268s

* [ghidra-scripts](https://github.com/0x6d696368/ghidra_scripts) - Additional scripts


## Resources

* Additional scripts
    * https://github.com/ghidraninja/ghidra_scripts
    * https://github.com/0x6d696368/ghidra_scripts

* [BinDiffHelper](https://github.com/ubfx/BinDiffHelper)

* [Cheat Sheet](https://ghidra-sre.org/CheatSheet.html)

* [Ghidra Snippets](https://github.com/HackOvert/GhidraSnippets)

* [Ghidra Website](https://ghidra.re)
    * [Scripting with Notes](https://ghidra.re/courses/GhidraClass/Intermediate/Scripting_withNotes.html#Scripting.html)
    * [Ghidra API Docs](https://ghidra.re/ghidra_docs/api/index.html)

* [Introduction to Ghidra's primary components](https://byte.how/posts/what-are-you-telling-me-ghidra/)

* [Introduction to Reverse Engineering with Ghidra](https://hackaday.io/course/172292-introduction-to-reverse-engineering-with-ghidra)

    * Github - https://github.com/wrongbaud/hackaday-u
* [Patch Diffing with Ghidra](https://blog.threatrack.de/2019/10/02/ghidra-patch-diff/)

* [Patching Binaries](https://materials.rangeforce.com/tutorial/2020/04/12/Patching-Binaries/)

* [Using Ghidra's YaraGhidraGUIScript.java plugin to generate a YARA signature](https://www.youtube.com/watch?v=tBvxVkJrkh0)

* [Using Old Windows Symbols with Ghidra in Linux](https://dannyquist.github.io/windows-symbols-ghidra/)

* [Reverse Engineering Go Binaries](https://cujo.com/reverse-engineering-go-binaries-with-ghidra/)

* [Scripting Ghidra with Python](https://deadc0de.re/articles/ghidra-scripting-python.html)

* [IDA FLIRT Signatures](https://github.com/push0ebp/sig-database)
