# TWISTER!
a = ('right hand red')
b = ('right hand yellow')
c = ('right hand blue')
d = ('right hand green')
e = ('left hand red')
f = ('left hand yellow')
g = ('left hand blue')
h = ('left hand green')
i = ('right foot red')
j = ('right foot yellow')
k = ('right foot blue')
l = ('right foot green')
m = ('left foot red')
n = ('left foot yellow')
o = ('left foot blue')
p = ('left foot green')
list = (a , b , c , d , e , f , g , h , i , j , k , l , m , n , o , p)
import random
input('To play Twister, press enter! ')
text = input(random.choice(list))
required_number = ' '
# to end game press space then enter
while True:
    number = input()
    if number == required_number:
        print("Game Over!")
        break
    else:
        input(random.choice(list))