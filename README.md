The IAS Instruction Set (replicated lightly in Python)
-------------------------

What's this all about? John Von Neumann designed a computer now called the IAS (after the Princeton Institute for Advanced Studies) in the 1940s and along with Julian Bigelow, Hewitt Crane, Herman Goldstine, Gerald Estrin, Arthur Burks and Willis Ware and James Pomerene (among many many others) then built this computer in the 1950. This machine can be called the father of all modern computers since it was one of the first computers that stored both the program and the data in memory (unlike the earlier ENIAC machines). Now you too can experience the joy of programming in binary code using only two registers and 163840 bits (2k) of memory and program space.

Architcturally IAS has an accumulator register, AC, and an arithmetic register called MQ (Multiplier/Quotient) to store the results of operations. Each register has 40 bits, a seemingly strange but workable word-length. There is a memory is called Selectron and it has up to 4096 (that is, 212) 40-bit memory locations. There are also several other registers that are used internally by the computer but are invisible to the machine-language programmer so they're not available here. The image in this archive shows the architecture of the IAS system

Data transfer
-------------------------

Here's all the instructions to transfer from one address to either AR or MQ

<pre>
00001010 LOAD MQ Transfer contents of register MQ to the accumulator AC
00001001 LOAD MQ,M(X) Transfer contents of memory location X to MQ
00100001 STOR M(X) Transfer contents of accumulator to memory location X
00000001 LOAD M(X) Transfer M(X) to the accumulator
00000010 LOAD ÐM(X) Transfer -M(X) to the accumulator
00000011 LOAD |M(X)| Transfer absolute value of M(X) to the accumulator
00000100 LOAD -|M(X)| Transfer -|M(X)| to the accumulator
</pre>

Unconditional branch
-------------------------

How to logic

<pre>
00001101 JUMP M(X,0:19) Take next instruction from left half of M(X)
00001110 JUMP M(X,20:39) Take next instruction from right half of M(X)
</pre>

Conditional branch
-------------------------

How to logic, Part 2

<pre>
00001111 JUMP+M(X,0:19) If number in the accumulator is nonnegative, take next instruction from left half of M(X)
00010000 JUMP+M(X,20:39) If number in the accumulator is nonnegative , take next instruction from right half of M(X)
</pre>

Arithmetic
-------------------------

Basic addition

<pre>
00000101 ADD M(X) Add M(X) to AC; put the result in AC
00000111 ADD |M(X)| Add |M(X)| to AC; put the result in AC
00000110 SUB M(X) Subtract M(X) from AC; put the result in AC
00001000 SUB |M(X)| Subtract |M(X)} from AC; put the remainder in AC
00001011 MUL M(X) Multiply M(X) by M(Q); put most significant bits of result in AC, put less significant bits in M(Q)
00001100 DIV M(X) Divide AC by M(X); put the quotient in MQ and the remainder in AC
00010100 LSH Multiply accumulator by 2 (i.e., shift left one bit position)
00010101 RSh Divide accumulator by 2 (i.e., shift right one bit position)
</pre>

Address modify
-------------------------

Storing instructions

<pre>
00010010 STOR M(X,8:19) Replace left address field at M(X) by 12 right-most bits of AC
00010011 STOR M(X,28:39) Replace right address field at M(X) by 12 right-most bits of AC
</pre>



check out http://cs.colby.edu/courses/S12/cs232/ias.php

