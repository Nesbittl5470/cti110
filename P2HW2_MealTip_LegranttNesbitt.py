print('This program will Calculate Tips and final meal price')
print('Feb 10 2019')
print('CTI-110 Tutorial 1 - Meal Tip Calculator ')
print('Legrantt Nesbitt')

# Get Total meal cost from user without tip

totalMeal = int(input('How much was the total meal?: '))

# Calculates Tip

tipOne = totalMeal * 0.15 
tipTwo = totalMeal * 0.18
tipThree = totalMeal * 0.20

# Calculates Tip + Total Meal cost

totMealAvgOne = totalMeal * 0.15 + totalMeal
totMealAvgTwo = totalMeal * 0.18 + totalMeal
totMealAvgThree = totalMeal * 0.20 + totalMeal
                
print ('This is Tip One', \
       format(tipOne, '.2f'))

print ('This is Tip Two', \
       format(tipTwo, '.2f'))
print ('This is Tip Three', \
       format(tipThree, '.2f'))


print ('Cost of Meal with Tip One:', \
       format(totMealAvgOne, '.2f'))
                                            
print ('Cost of Meal with Tip Two:', \
       format(totMealAvgTwo, '.2f'))

print ('Cost of Meal with Tip Three:', \
       format(totMealAvgThree, '.2f'))  
