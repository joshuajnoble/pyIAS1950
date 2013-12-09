
'''

Move to bitstring

'''

from bitstring import BitStream

class IAS:

    def read(self, address):
        baddress = BitStream('0b'+address)
        return self.selectron[baddress.int]

    def input(self, address, value):
        baddress = BitStream('0b'+address)
        self.selectron[baddress.int] = BitStream(int=value, length=40)

    def instruction(self, opcode, address):
    	# you don't put the 0b, I do, you just punch the cards right
        bopcode = BitStream('0b'+opcode)
        baddress = BitStream('0b'+address)

        self.ops[bopcode.read('bin:8')](baddress.int)


    def loadToAC (self, register): #LOAD self.MQ Transfer contents of register self.MQ to the accumulator self.AC
        self.AC = self.MQ

    def loadToMQ(self, register): #LOAD self.MQ,M(X) Transfer contents of memory location X to self.MQ
        self.MQ = BitStream(int=self.selectron[register].int, length=40)

    def store(self, register): #STOR M(X) Transfer contents of accumulator to memory location X
        self.selectron[register] = self.AC

    def load(self, register): #LOAD M(X) Transfer M(X) to the accumulator
        self.AC = self.selectron[register]

    def loadNeg (self, register): #LOAD -M(X) Transfer -M(X) to the accumulator
        self.AC = self.selectron[register] | 0x8000000000

    def loadAbs(self, register): #LOAD |M(X)| Transfer absolute value of M(X) to the accumulator
        mask = self.selectron[register]>>39
        mask ^ self.selectron[register]
        self.AC = (mask^n) - mask

    def loadNegAbs(self, register): #LOAD -|M(X)| Transfer -|M(X)| to the accumulator
        mask = self.selectron[register]>>39
        mask ^ self.selectron[register]
        self.AC = ((mask^n) - mask) | 0x8000000000

    def jumpL(self, register): #JUMP M(X,0:19) Take next instruction from left half of M(X)
        ops[self.selectron[register][0:19]](register)

    def jumpR(self, register): #JUMP M(X,20:39) Take next instruction from right half of M(X)
        ops[self.selectron[register][20:39]](register)

    def condJumpL(self, register): #JUMP+M(X,0:19) If number in the accumulator is nonnegative, take next instruction from left half of M(X)
        if(self.AC[39] == 1):
            ops[self.selectron[register][0:7]](self.selectron[register][8:19].int)

    def condJumpR(self, register): #JUMP+M(X,20:39) If number in the accumulator is nonnegative , take next instruction from right half of M(X)
        if(self.AC[39] == 1):
            ops[self.selectron[register][20:27]](self.selectron[register][28:40].int)

    def add(self, register): #ADD M(X) Add M(X) to AC; put the result in self.AC
        self.AC = BitStream(int=self.AC.int + self.selectron[register].int, length=40)

    def addAbs(self, register): #ADD |M(X)| Add |M(X)| to AC; put the result in self.AC
        self.AC = BitStream(int=self.AC.int + abs(self.selectron[register].int), length=40)

    def sub(self, register): #SUB M(X) Subtract M(X) from AC; put the result in self.AC
        self.AC = BitStream(int=self.AC.int - self.selectron[register].int, length=40)

    def subRem(self, register): #SUB |M(X)| Subtract |M(X)} from AC; put the remainder in self.AC
        self.AC = BitStream(int=self.AC.int + abs(self.selectron[register].int), length=40)

    def mul(self, register): #MUL M(X) Multiply M(X) by M(Q); put most significant bits of result in AC, put less significant bits in M(Q)
        res = BitStream(int=self.MQ.int * self.selectron[register].int, length=80)
        self.AC = BitStream(int=res[40:80].int, length=40)
        self.MQ = BitStream(int=res[0:39].int, length=40)

    def div(self, register): #DIV M(X) Divide AC by M(X); put the quotient in MQ and the remainder in AC
        quo = BitStream(int=(self.AC.int / self.selectron[register].int), length=40)
        rem = BitStream(int=self.AC.int % self.selectron[register].int, length=40)
        self.AC = quo
        self.MQ = rem

    def ls(self, register): #LSH Multiply accumulator by 2 (i.e., shift left one bit position)
        self.AC <<= 1

    def rs(self, register): #RSh Divide accumulator by 2 (i.e., shift right one bit position)
        self.AC >>= 1

    def storL(self, register): #STOR M(X,8:19) Replace left address field at M(X) by 12 right-most bits of AC
        self.selectron[register][20:39] = self.AC[0:19]

    def storR(self, register): #STOR M(X,28:39) Replace right address field at M(X) by 12 right-most bits of AC
        self.selectron[register][0:19] = self.AC[0:19]

    def __init__(self):
        self.ops = {
        '00000001': self.load, #LOAD M(X) Transfer M(X) to the accumulator
        '00000010': self.loadNeg,  #LOAD -M(X) Transfer -M(X) to the accumulator
        '00000011': self.loadAbs, #LOAD |M(X)| Transfer absolute value of M(X) to the accumulator
        '00000100': self.loadNegAbs, #LOAD -|M(X)| Transfer -|M(X)| to the accumulator
        '00000101': self.add, #ADD M(X) Add M(X) to AC; put the result in AC
        '00000111': self.addAbs, #ADD |M(X)| Add |M(X)| to AC; put the result in AC
        '00000110': self.sub, #SUB M(X) Subtract M(X) from AC; put the result in AC
        '00001000': self.subRem, #SUB |M(X)| Subtract |M(X)} from AC; put the remainder in AC
        '00001001': self.loadToMQ, #LOAD MQ,M(X) Transfer contents of memory location X to MQ
        '00001010': self.loadToAC, #LOAD MQ Transfer contents of register MQ to the accumulator AC
        '00001011': self.mul, #MUL M(X) Multiply M(X) by M(Q); put most significant bits of result in AC, put less significant bits in M(Q)
        '00001100': self.div, #DIV M(X) Divide AC by M(X); put the quotient in MQ and the remainder in AC
        '00001101': self.jumpL, #JUMP M(X,0:19) Take next instruction from left half of M(X)
        '00001110': self.jumpR, #JUMP M(X,20:39) Take next instruction from right half of M(X)
        '00001111': self.condJumpL, #JUMP+M(X,0:19) If number in the accumulator is nonnegative, take next instruction from left half of M(X)
        '00010000': self.condJumpR, #JUMP+M(X,20:39) If number in the accumulator is nonnegative , take next instruction from right half of M(X)
        '00010100': self.ls, #LSH Multiply accumulator by 2 (i.e., shift left one bit position)
        '00010101': self.rs, #RSh Divide accumulator by 2 (i.e., shift right one bit position)
        '00100001': self.store, #STOR M(X) Transfer contents of accumulator to memory location X
        '00010010': self.storL, #STOR M(X,8:19) Replace left address field at M(X) by 12 right-most bits of AC
        '00010011': self.storR, #STOR M(X,28:39) Replace right address field at M(X) by 12 right-most bits of AC
        }
        self.AC = BitStream(int=0, length=40)
        self.MQ = BitStream(int=0, length=40)
        self.selectron = []
        i = 0
        while i < 4096:
            self.selectron.append(BitStream(int=0, length=40))
            i+=1

