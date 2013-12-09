
'''

Move to bitstring

'''

from bitstring import BitArray

class IAS:

    def __init__():
        self.ops = {
        '00000001': load #LOAD M(X) Transfer M(X) to the accumulator
        '00000010': loadNeg  #LOAD ÐM(X) Transfer -M(X) to the accumulator
        '00000011': loadAbs #LOAD |M(X)| Transfer absolute value of M(X) to the accumulator
        '00000100': loadNegAbs #LOAD -|M(X)| Transfer -|M(X)| to the accumulator
        '00000101': add #ADD M(X) Add M(X) to AC; put the result in AC
        '00000111': addAbs #ADD |M(X)| Add |M(X)| to AC; put the result in AC
        '00000110': sub #SUB M(X) Subtract M(X) from AC; put the result in AC
        '00001000': subRem #SUB |M(X)| Subtract |M(X)} from AC; put the remainder in AC
        '00001001': loadToMQ #LOAD MQ,M(X) Transfer contents of memory location X to MQ
        '00001010': loadToAC #LOAD MQ Transfer contents of register MQ to the accumulator AC
        '00001011': mul #MUL M(X) Multiply M(X) by M(Q); put most significant bits of result in AC, put less significant bits in M(Q)
        '00001100': div #DIV M(X) Divide AC by M(X); put the quotient in MQ and the remainder in AC
        '00001101': jumpL #JUMP M(X,0:19) Take next instruction from left half of M(X)
        '00001110': jumpR #JUMP M(X,20:39) Take next instruction from right half of M(X)
        '00001111': condJumpL #JUMP+M(X,0:19) If number in the accumulator is nonnegative, take next instruction from left half of M(X)
        '00010000': condJumpR #JUMP+M(X,20:39) If number in the accumulator is nonnegative , take next instruction from right half of M(X)
        '00010100': ls #LSH Multiply accumulator by 2 (i.e., shift left one bit position)
        '00010101': rs #RSh Divide accumulator by 2 (i.e., shift right one bit position)
        '00100001': store #STOR M(X) Transfer contents of accumulator to memory location X
        '00010010': storL #STOR M(X,8:19) Replace left address field at M(X) by 12 right-most bits of AC
        '00010011': storR #STOR M(X,28:39) Replace right address field at M(X) by 12 right-most bits of AC
        }
        self.AC = BitArray('0x00000000')
        self.MQ = BitArray('0x00000000')
        self.selectron = Array()
        while i < 4096:
            self.selectron[i] = BitArray('0x00000000')
            i++

        self.neg.frombytes('0x8000000000')

    def input(address, value)
        selectron[register] = BitArray(int=value, length=40)

    def instruction(opcode, address):

        bopcode = BitArray(opcode)
        baddress = BitArray(address)

        ops[opcode](address)


    def loadToAC (register): #LOAD MQ Transfer contents of register MQ to the accumulator AC
        AC = MQ

    def loadToMQ(register): #LOAD MQ,M(X) Transfer contents of memory location X to MQ
        MQ = selectron[register]

    def store(register): #STOR M(X) Transfer contents of accumulator to memory location X
        selectron[register] = AC

    def load(register): #LOAD M(X) Transfer M(X) to the accumulator
        AC = selectron[register]

    def loadNeg (register): #LOAD -M(X) Transfer -M(X) to the accumulator
        AC = selectron[register] | neg

    def loadAbs(register): #LOAD |M(X)| Transfer absolute value of M(X) to the accumulator
        mask = selectron[register]>>31
        mask ^ selectron[register]
        AC = (mask^n) - mask

    def loadNegAbs(register): #LOAD -|M(X)| Transfer -|M(X)| to the accumulator
        mask = selectron[register]>>31
        mask ^ selectron[register]
        AC = ((mask^n) - mask) | 0x8000000000

    def jumpL(register): #JUMP M(X,0:19) Take next instruction from left half of M(X)
        ops[selectron[register][0:19]](register)

    def jumpR(register): #JUMP M(X,20:39) Take next instruction from right half of M(X)
        ops[selectron[register][20:39]](register)

    def condJumpL(register): #JUMP+M(X,0:19) If number in the accumulator is nonnegative, take next instruction from left half of M(X)
        if(AC[0] == 1):
            ops[selectron[register][0:7]](selectron[register][8:19].int)

    def condJumpL(register): #JUMP+M(X,20:39) If number in the accumulator is nonnegative , take next instruction from right half of M(X)
        if(AC[0] == 1):
            ops[selectron[register][20:27]](selectron[register][28:40].int)

    def add(register): #ADD M(X) Add M(X) to AC; put the result in AC
        AC = AC(int=AC.int + selectron[register].int, length=40)

    def addAbs(register): #ADD |M(X)| Add |M(X)| to AC; put the result in AC
        AC = AC(int=AC.int + selectron[register].uint, length=40)

    def sub(register): #SUB M(X) Subtract M(X) from AC; put the result in AC
        AC = AC(int=AC.int - selectron[register].int, length=40)

    def subRem(register): #SUB |M(X)| Subtract |M(X)} from AC; put the remainder in AC
        AC = AC(int=AC.int + selectron[register].uint, length=40)

    def mul(register): #MUL M(X) Multiply M(X) by M(Q); put most significant bits of result in AC, put less significant bits in M(Q)
        res = AC(int=MQ.int * selectron[register].int, length=80)
        AC = res[40:79]
        MQ = res[0:39]

    def div(register): #DIV M(X) Divide AC by M(X); put the quotient in MQ and the remainder in AC
        quo = AC(int=AC.int / selectron[register].int, length=40)
        rem = AC(int=AC.int % selectron[register].int, length=40)
        AC = quo
        MQ = rem

    def ls(register): #LSH Multiply accumulator by 2 (i.e., shift left one bit position)
        AC <<= 1

    def rs(register): #RSh Divide accumulator by 2 (i.e., shift right one bit position)
        AC >>= 1

    def storL(register): #STOR M(X,8:19) Replace left address field at M(X) by 12 right-most bits of AC
        selectron[register][20:39] = AC[0:19]

    def storR(register): #STOR M(X,28:39) Replace right address field at M(X) by 12 right-most bits of AC
        selectron[register][0:19] = AC[0:19]

    end