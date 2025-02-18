## Solve explanation
This is an interger overflow problem mixed with a ret2win at the end. <br/>
The ```catch``` variable is defined as a short int. Therefore adding 1 to it repeatedly will cause an integer overflow. <br/>
Then, we will execute a simple buffer overflow that returns to the ```hero()``` function and gives us a shell.
