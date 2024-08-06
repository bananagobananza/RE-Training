# Write-Up

## Challenge Information
**Name:** W32

**Category:** Reverse engineering

## Tools Used
- **Tool 1:** ghidra

## Approach and Solution

First we running the exe file
![Image](W32/exe.png)

The file had been patched to print only correct answer, we need to patch to view only the wrong answer

Base on the output, we search for the reference of `Congrat! You did it.`
![Image](W32/1.png)
![Image](W32/2.png)

Follow it in the dump, we have
![Image](W32/3.png)

we see 2 suspicious `nop`, which is equivalent to a "short" jump operation, which may be the operation to jump to the address printing `You idiot`   

We assemble a new instruction for it
![Image](W32/patch.png)

And get the result
![Image](W32/4.png)
![Image](W32/result.png)