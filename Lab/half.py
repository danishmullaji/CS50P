def main():
    # prompt the user for the bill amount
    bill = float(input("What is the Bill Amount before Tax: "))

    # calculate the net bill after tax
    net_bill = tax(bill)

    # add tip and split the bill print
    gross_bill = tip(net_bill)

    split = int(input("Split between how many people: "))
    print(f"Total Bill Amount Rs. {gross_bill:,.2f}")
    print(f"Rs. {gross_bill / split:,.2f} each person would pay.")

# prompt for tax percentage
def tax(x):
    tax = float(input("Enter the Tax: "))
    x = x + (x * tax / 100)
    return x


# prompt for tip percentage
def tip(y):
    tip = float(input("How much you gonna Tip: "))
    y = y + (y * tip / 100)
    return y


main()