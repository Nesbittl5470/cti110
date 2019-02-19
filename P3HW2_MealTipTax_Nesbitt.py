print('This program will Calculate Tips and final meal price')
print('Feb 17 2019')
print('CTI-110 Tutorial 1 - Meal Tip Tax ')
print('Legrantt Nesbitt')


# Get Total meal cost from user without tip
totalMeal = int(input('How much was the total meal?: '))


# Get amount User would like to tip
tip_Amount = float(input('What percent would you like to tip'
                        '.15, .18, or .20?" ')) * totalMeal 

# Calculates Sales Tax
sales_Tax = totalMeal * 0.07

# Calculate Meal Average
meal_Avg = totalMeal + sales_Tax + tip_Amount

# Create If statement in regards to tip amount
if tip_Amount <= .15 or .18 or .20:
    print('Good tip')

else:
    print('Incorrect Tip amount')
    
    
# Output Tip amount, sales tax, and meal average
print('You Tipped $', \
      format(tip_Amount, '.2f'), \
      sep='')

print('Sales Tax $', \
      format(sales_Tax, '.2f'), \
      sep='')

print('Cost of Meal with, Tax and Tip: $', \
      format(meal_Avg, '.2f'), \
      sep='')




      




                 
      
            
