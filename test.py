
'''
= add =

0000:   0000 0001   0000 0000 0010    ; load data at address 2 into AC
0001:   0000 0101   0000 0000 0011    ; add data at address 3 to the AC
0010:   0010 0001   0000 0000 0100    ; store value in AC to address 4
'''

'''
= mul =

0000:   0000 1001   0000 0000 0010    ; load data from address 2 into MQ
0001:   0000 1011   0000 0000 0011    ; mul data at address 3
0010:   0010 0001   0000 0000 0101    ; store value from AC into address 5
'''

'''
= div =

0000:   0000 0001   0000 0000 0010    ; load data from address 2 into MQ
0001:   0000 1100   0000 0000 0011    ; div MQ by address 3 (that's how div works)
0011:   0010 0001   0000 0000 0101    ; store value from AC into address 5 so we can read in
0100:   0000 1010   0000 0000 0000    ; store MQ into AC so we can read it
0101:   0010 0001   0000 0000 0110    ; store value from AC into address 6 so we can read in
'''


from IAS50 import IAS

addRoutine = [['00000001','000000000010'],['00000101','000000000011'],['00100001','000000000100']]
mulRoutine = [['00001001','000000000010'],['00001011','000000000011'],['00100001','000000000101']]
divRoutine = [['00000001','000000000010'],['00001100','000000000011'],['00100001','000000000101'],['00001010','000000000000'],['00100001','000000000110']]

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

for instruction in divRoutine:
    ias.instruction(instruction[0], instruction[1])

print ias.read('000000000101') # read the quo
print ias.read('000000000111') # read the remainder