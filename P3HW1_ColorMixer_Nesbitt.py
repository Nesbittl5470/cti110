print('CTI-110')
print('P3HW1 - Color Mixer')
print('Legrantt Nesbitt')
print('Feb 17 2019')


#User Inputs Primary Colors

primary_Color_One = input('Name a Primary Color: ')
primary_Color_Two = input('Name a Primary Color: ')

#Get value of primary colors
#And their reverse

if primary_Color_One == 'red' and primary_Color_Two == 'yellow' or primary_Color_One == 'yellow' and primary_Color_Two == 'red':
    print('The Color is Orange')

if primary_Color_One == 'Red' and primary_Color_Two == 'Yellow' or primary_Color_One == 'Yellow' and primary_Color_Two == 'Red':
    print('The Color is Orange')

if primary_Color_One == 'blue' and primary_Color_Two == 'red' or  primary_Color_One == 'red' and primary_Color_Two == 'blue':
    print('The Color is Purple')

if primary_Color_One == 'Blue' and primary_Color_Two == 'Red'or  primary_Color_One == 'Red' and primary_Color_Two == 'Blue':
    print('The Color is Purple')

if primary_Color_One == 'yellow' and primary_Color_Two == 'blue'or primary_Color_One == 'blue' and primary_Color_Two == 'yellow':
    print('The Color is Green')

if primary_Color_One == 'Yellow' and primary_Color_Two == 'Blue'or primary_Color_One == 'Blue' and primary_Color_Two == 'Yellow':
    print('The Color is Green')

#If user enter Incorrect Color
#Error message will display

elif():
    print('You picked a wrong Color')
