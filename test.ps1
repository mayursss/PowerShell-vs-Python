2 + 2
50 - 5*6
(50 - 5*6) / 4
8 / 5 
#######
17 /3 
17 % 3
5 * 3 + 2 
[math]::Floor(17/3)
#######
[math]::Pow(5,2)
[math]::Pow(2,7)
#######
$width = 20
$height = 5 * 9
width * height


$s= "`"Yes,`" he said."
$s
##$s= '\'yes,\' he said' ## wont work POSH need "" to escape character
$s
$s= "`"Isn't,`" she said."
$s 

$word = 'Python'
$word[0..2] ## in Python it uses [0:3]  #characters from position 0 (included) to 3 (excluded)
$word[0..-1] ## in Python it uses [0:3]  #characters from position 0 (included) to 3 (excluded)
$word[0] = 'J'  ## In both POSH and Python you cannot replace or add char in same array.
$word[0..2]
'J'+$word[1..($word.Length)] ##to get to the last char in python its easy we just leave second val blank like word[0:<blank>]
$s = 'supercalifragilisticexpialidocious'
$s.Length ## in Python we use len() function
$squares = (1, 4, 9, 16, 25)
$squares[3]=17
$squares += 64
[math]::Pow(7,3)  ## easy in Python just use (7 ** 3)