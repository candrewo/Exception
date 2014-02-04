import sys
 
def calculate_rate(base, percentage):
    return base * percentage
 
def calculate_meal_costs(meal_base, tax_rate, tip_rate):
    """
    Calculates dollar amounts for tax, tip, and total meal cost
    """
    tax_value = calculate_rate(meal_base, tax_rate)
    meal_with_tax = tax_value + meal_base
    tip_value = calculate_rate(meal_with_tax, tip_rate)
    total = meal_with_tax + tip_value
    meal_info = dict(meal_base=meal_base,
                    tax_rate=tax_rate,
                    tip_rate=tip_rate,
                    tax_value=tax_value,
                    total = total)
    return meal_info

def calcmeal(meal_base):
    if meal_base > 0:
        return meal_base
    else:
        while meal_base == 0:
            print "The meal must be a number. Try again."
            meal_base = float(raw_input("Please enter the cost of the meal: "))
            break
        return meal_base
 
def calctax(tax_rate):
    if tax_rate > 0:
        return tax_rate
    else:
        while tax_rate == 0:
            print "The tax rate must be a greater than 0 (eg. .10, .09)"
            tax_rate = float(raw_input("Please enter the tax: "))
            break
        return tax_rate

def calctip (tip_rate):
    if tip_rate > 0:
        return tip_rate
    else:
        while tip_rate == 0:
            print "Don't be stingy. Tip greater than 0 as a percent (eg. .15, .20)"
            tip_rate = float(raw_input("Please enter the tip: "))
            break
        return tip_rate
	

def main():
    meal = float(sys.argv[1])
    tax = float(sys.argv[2])
    tip = float(sys.argv[3])
    meal_base = calcmeal(meal)
    tax_rate = calctax(tax)
    tip_rate = calctip(tip)
    meal_info = calculate_meal_costs(meal_base,tax_rate,tip_rate)

    print "The base cost of your meal was ${0:.2f}.".format(meal_info['meal_base'])
    print "You need to pay ${0:.2f} for tax.".format(meal_info['tax_value'])
    print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(
                                        float(100*meal_info['tip_rate']), 
                                        meal_info['tax_value'])
    print "The grand total of your meal is ${0:.2f}.".format(meal_info['total'])


if __name__ == '__main__':
    main()