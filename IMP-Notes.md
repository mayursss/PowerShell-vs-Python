In Python `{}` are not used, instead `:` followed by indent is used.

Example
``` python
for x in range(5,10):
  print (x)
```
      

Python does not have support for higher-order conditionals
like `"switch-case"` in other languages

Python has only while and for loop

normally the `for` loop in Python does not use an `index` variable. Like, there's no loop counter like you'd see in JavaScript. 
We can get one if really needed using `enumerate()` function
Example
``` python
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for i, d in enumerate(days):
    print (i, d)
>>> ##console output
0 Mon
1 Tue
2 Wed
3 Thu
4 Fri
5 Sat
6 Sun
```
