2 + 2 
50 - 5*6
(50 - 5*6) / 4
8 / 5
##########
17 / 3  # classic division returns a float
17 // 3  # floor division discards the fractional part
17 % 3  # the % operator returns the remainder of the division
5 * 3 + 2  # result * divisor + remainder

s= "\"Yes,\" he said."
print(s)
s= '\'yes,\' he said'
print(s)
s= '"Isn\'t," she said.'
print(s)
s= "\"Isn't,\" she said." ## Like Powershell just escape char is different i.e \ instead "`"
print(s)

word = 'Python'
## [n_Included:n_Included] # if start to end like [0:5] for 6 char word
## [n_Included:n_Excluded] # if second n is not the end like [0:4] for 6 char word
word[0:3] ## output 'Py'    // in POSH it uses [0..2]  # characters start from position 0 to 2 (included)
word[2:5] ## output 'thon   //'characters from position 2 (included) to 5 (excluded)
word[2:-1] ## output 'thon   //'characters from position 2 (included) to -1 (excluded)
word[:2] + word[2:] ## output 'Python' // char 0to2 (0 included:2 excluded) + 2 (2 included:end_included)
word[:4] + word[4:] ## output 'Python' // char 0to4 (0 included:4 excluded) + 4 (4 included:end_included)
#word[0] = 'J'  ## In both POSH and Python you cannot replace or add char in same array.
'J' + word[1:]
s = 'supercalifragilisticexpialidocious'
len(s) ## in POSH we use .lenght property
squares = [1, 4, 9, 16, 25]  ## in POSH we use array () instead []
squares.append(216)  # add the cube of 6
squares.append(7 ** 3)  ## in POSH we need to use .net [Math] class like [math]::Pow(7,3) and its very powerfull
