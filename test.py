
'''
= add =

0000:	0000 0001	0000 0000 0010	; load data at address 2 into AC
0001:	0000 0101	0000 0000 0011	; add data at address 3 to the AC
0010:	0010 0001	0000 0000 0100	; store value in AC to address 4
'''

'''
= mul =

0000:   0000 1001   0000 0000 0010  ; load data from address 2 into MQ
0001:	0000 1011	0000 0000 0011	; mul data at address 3
0011:	0010 0001	0000 0000 0101	; store value from AC into address 5
'''


from IAS50 import IAS

addRoutine = [['00000001','000000000010'],['00000101','000000000011'],['00100001','000000000100']]
mulRoutine = [['00001001','000000000010'],['00001011','000000000011'],['00100001','000000000101']]

ias = IAS()
ias.input('000000000011', 10)
ias.input('000000000010', 20)

for instruction in addRoutine:
	ias.instruction(instruction[0], instruction[1])

#what'd we add?
print ias.read('000000000100')

for instruction in mulRoutine:
	ias.instruction(instruction[0], instruction[1])

#what'd we multiply?
print ias.read('000000000101')