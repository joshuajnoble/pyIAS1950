The IAS Instruction Set (replicated lightly in Python)
================================

Data transfer
-------------------------
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
<pre>
00001101 JUMP M(X,0:19) Take next instruction from left half of M(X)
00001110 JUMP M(X,20:39) Take next instruction from right half of M(X)
</pre>

Conditional branch
-------------------------
<pre>
00001111 JUMP+M(X,0:19) If number in the accumulator is nonnegative, take next instruction from left half of M(X)
00010000 JUMP+M(X,20:39) If number in the accumulator is nonnegative , take next instruction from right half of M(X)
</pre>

Arithmetic
-------------------------
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
<pre>
00010010 STOR M(X,8:19) Replace left address field at M(X) by 12 right-most bits of AC
00010011 STOR M(X,28:39) Replace right address field at M(X) by 12 right-most bits of AC
</pre>

check out http://cs.colby.edu/courses/S12/cs232/ias.php

