#tax.py 
#given a parameter income, returns tax based on income bracket
#in this example, a graduate income tax code that does not tax 
#income below 1000, taxes at a 10% rate all income after the first
#$1000 up to $10000, a 20% rate up to $20000, and a 30% rate on anything else

def main():
    print tax(30000)
    print tax(5000)
    print tax(50000)

def tax(income):
    if income < 1000:
        tax = 0
    elif income < 10000:
        tax = 0.1*(income-1000)
    elif income < 30000:
        basetax = 0.1*(10000-1000)
        tax = basetax + 0.2*(income-10000)
    else:
        basetax = 0.1 * (10000-1000) + 0.2*(30000-10000)
        tax = basetax + 0.3*(income-30000)
    return tax

main()  
