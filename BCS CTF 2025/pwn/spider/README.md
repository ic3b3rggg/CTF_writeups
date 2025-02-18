## Solve Explanation
This is a GOT_overwrite problem. <br/>
Take a look at the assembly code,
```asm
0x40135f  mov  qword ptr[rax],  rdx
```
This means this will write the input after the ```How?``` prompt at the address given after the ```proof?``` prompt. <br/> 
I used the leaked address of ```printf``` to find the ```libc_base```.<br/>
I input ```/bin/sh``` after the first prompt to provide the argument.<br/>
Then I replaced ```elf.got.puts``` with ```libc.symbols.system```.<br/>
This gives us a shell.
