Hello Friends, Today I will go through python v3.6.4 documentation and will compare commands given in tutorial section PowerShell commands

so lests start with section 3.1. Using Python as a Calculator

**Python**
```python
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating point number
1.6
```
**PowerShell**
```powershell
PS>2 + 2
4
PS>50 - 5*6
20
PS>(50 - 5*6) / 4
5
PS>8 / 5
1.6
PS>
```
Ok so this will be almost same in Powershell with only difference for expression `(50 - 5*6) / 4` here the output will be 5 compared to 5.0 in Python

The integer numbers e.g. `(2, 4, 20)` have type `int`, the ones with a fractional part e.g. `(5.0, 1.6)` have type `float`. Division `/` always returns a float.
To do floor division and get an integer result (discarding any fractional result) you can use the `//` operator.
To calculate the remainder you can use `%`

**Python**
```python
>>> 17 / 3    # classic division returns a float
5.666666666666667
>>> 17 % 3    # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2 # result * divisor + remainder
17
>>> 17 // 3   # floor division discards the fractional part
5
```
**PowerShell**
```powershell
PS>17 /3
5.66666666666667
PS>17 % 3
2
PS>5 * 3 + 2
17
PS>[math]::Floor(17/3)
5
```
So you might have noticed that only difference here is calculating floor value. PowerShell is using .Net `[math]` class and Python is just using `//` operator so we can say python is bit easy here but .Net `[math]` class has many more options which we will see later.

With Python, it is possible to use the `**` operator to calculate powers 
**Python**
``` Python
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128
```
**PowerShell**
``` PowerShell
PS>[math]::Pow(5,2)
25
PS>[math]::Pow(2,7)
128
```
As you have already noticed we are using operator `**` in Python and .Net `[math]` class in powershell to calculate power.

The equal sign `=` is used to assign a value to a variable. Afterwards, no result is displayed before the next interactive prompt

``` python
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```
``` PowerShell
PS>$width = 20
PS>$height = 5 * 9
PS>$width * $height
900
```
In both Powershell and Python `=` is used to assign value to variable. Difference here is that in PowerShell variable starts with `$` sign.

In Python there is full support for floating point; operators with mixed type operands convert the integer operand to floating point

