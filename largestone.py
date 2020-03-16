print('enter 3 number')
x= int(input('Enter number 1:'))
y= int(input('Enter number 2:'))
z= int(input('Enter number 3:'))
if x>y>z or x>z>y:
    print('x is largest')
elif y>x>z or y>z>x :
    print('y is largest')
elif z>x>y or z>y>x :
    print('z is largest')
