# Take-Home Solutions

## Part 1 - Hash Application Problem.
**Note**: Figuring the solution to this problem was taking more time than I allocated. So, I ended up searching for a solution and unfortunately found one that exactly solves the problem...see link [here](https://gist.github.com/srph/925ba1ba511fb5348443). This was the basis for my solution. I ended up rewriting it in python3 just to make sure I understood what it was doing. Here is my solution

```python3
import math

class Hasher(object):
    CONST_HASH = 7
    CONST_MULT = 37
    LETTERS = 'acdefgilnoprstuw'
    
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
```

A little testing
```python
def runner(arr):
    for h in arr:
        print(Hasher.decode(h))
        
runner([934605031880300, 677842960118, 1317985395605002507])

leapfrogs
gleeful
westernista
```

 

## Part 2 - Web Design Application Problem

### For this problem, I used grids and media query.

See layout.html 

[Preview](https://htmlpreview.github.io/?https://raw.githubusercontent.com/magicInSeattle/cstats-take-home/master/layout.html?token=AC3RXSWSTWYFCKCS36FO6XLAVQK7Q)
