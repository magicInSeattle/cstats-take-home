# Take-Home Solutions

## Part 1 - Hash Application Problem.
**Note**: Figuring the solution to this problem was taking longer than I expected. So, I ended up searching for a solution and unfortunately found one that exactly solves the problem...see link [here](https://gist.github.com/srph/925ba1ba511fb5348443). This was the basis for my solution. I ended up rewriting it in python3 just to make sure I understood what it was doing. Here is my solution

```python3
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

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
  <meta content="text/html;charset=utf-8" http-equiv="Content-Type">
  <meta content="utf-8" http-equiv="encoding">
  <style>
        * {
            box-sizing: border-box;
            padding: 0;
            margin: 0;
        }

        body {
            text-align: center;
        }

        .container {
            display: grid;
            grid-template-areas:
                "header header header"
                "nav content sidebar"
                "nav footer footer";
            grid-template-columns: 150px 1fr 150px;
            grid-template-rows: 200px 1fr 200px;
            min-height: 100vh;
        }

        header { grid-area: header; }
        nav { grid-area: nav; }
        content { grid-area: content; }
        aside { grid-area: sidebar; }
        footer { grid-area: footer; }


        /* make borders obvious */
        .container {
            background-color: rgba(252, 252, 252, 0.995);
            border: 2px solid rgb(85,190,230);
        }
        header, nav, content, aside, footer {
            padding: 10px;
            border: 2px solid rgb(85,190,230);
        }


        @media (max-width: 1024px) {
            .container {
                grid-template-areas:
                    'header'
                    'nav'
                    'sidebar'
                    'content'
                    'footer';
                grid-template-columns: 1fr;
                grid-template-rows: repeat(5, minmax(0,1fr));
            }
        }

    </style>
    <title>CSTATS Take Home Page Layout Solution</title>
</head>

<body>
```
