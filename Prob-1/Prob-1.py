# Module 3
#   Programming Assignment 4
#     Prob-1.py

# Rachel Watson

def shippingCost(subtotal):

    shippingCost = 2.99

    # enter code here to test for free
    if subtotal >= 10.00:
        total= subtotal + shippingCost
   
    return shippingCost

    shippingCost()

def unitTest():

    print("Shipping cost if subtotal < 10.00:\t", shippingCost(5.99))
    # enter additional test code here


if __name__ == "__main__":
    unitTest()