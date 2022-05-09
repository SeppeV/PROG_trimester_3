# This file should be used to show the implementation of finance.py 
# For instructions read the README.md
from finance import *

hobby = Grouping("Hobby")
travel_expenses = Grouping("Travel Expenses")
animals = Grouping("Animals")

hobby.deposit(500, "Maandgeld")
travel_expenses.deposit(1000, "Loon")
animals.deposit(1500, "Zwart werk")

print(hobby)
print(travel_expenses)
print(animals)
