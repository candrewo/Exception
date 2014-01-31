from tip_calculator_as_functions import calculate_rate 
from tip_calculator_as_functions import calculate_meal_costs 
import sys


try:
	meal = float(sys.argv[1])
	tax = float(sys.argv[2])
	tip = float(sys.argv[3])
	tax_value = meal * tax
	meal_with_tax = meal + (tax_value)
	tip_value = tip * (meal_with_tax)
	total = meal_with_tax + tip_value
	calculate_meal_costs(meal,tax,tip)
	print "Meal: ${:.2f}".format(meal)
	print "Tax: ${:.2f}".format(tax_value)
	print "Tip: ${:.2f}".format(tip_value)
	print "Total: ${:.2f}".format(total)
except ValueError: 
	print """Sorry, you must supply a number for meal cost, 
	tax and tip. Please enter a number."""
except NameError:
	print """Sorry, you must supply a number for meal cost, 
	tax and tip. Please enter a number."""
	raise
