class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        size = len(bits)
        if size == 1: return True                          #if only one bit then return True
        i = 0
        while(i < size):
            i += bits[i] + 1                               #if bits[i] == 1 then increment counter by 2 else increment counter by 1

            remaining_bits = size - i
            if remaining_bits == 2: return not bits[-2]    #if 2 bits remaining and first bit is 1 then it must be either 10 or 11 hence return False else return True
            if remaining_bits == 1 : return True           #if only one bit remaining then return True
