import math

class Hasher(object):
    CONST_HASH = 7
    CONST_MULT = 37
    LETTERS = 'acdefgilnoprstuw'

    @classmethod
    def get_hash(cls, s :str) -> int:
        h = cls.CONST_HASH
        for i,_ in enumerate(s):
            h = h * cls.CONST_MULT + cls.LETTERS.index(s[i])
        return h
    
    @classmethod
    def decode(cls, hash :int) -> str:
        index_list = []
        decoded = ''
        while hash > cls.CONST_MULT:
            hash, idx = divmod(hash, cls.CONST_MULT)
            index_list.append(idx)
        index_list.reverse()
        for indx in index_list:
            decoded += cls.LETTERS[indx]
        return decoded
      
if __name__ == '__main__':
  assert(Hasher.decode(Hasher.get_hash('gleeful')) == 'gleeful')
  for h in [934605031880300, 677842960118, 1317985395605002507]:
    print(f'{h} -> {Hasher.decode(h)}')
          
