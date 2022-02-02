'''
budget class
app.py - utilising budget class
withdraw method
deposit method
balance attr
'''

from myclasses import Budget

food = Budget(200)

bills = Budget(150)

entertainment = Budget(100)

print(food)
print(bills)
print(entertainment)

entertainment.deposit(food.withdraw(50))
