# Module 3
#   Programming Assignment 4
#     Prob-1.py

# Rachel Watson

def shippingCost(orderSubTotal):
    shippingCost = 2.99

    # enter code here to test for free
    if orderSubTotal >= 10.00:
        shippingCost = 0.0
   
    return shippingCost

    shippingCost()

def unitTest():

    print("Shipping cost if subtotal < 10.00:\t", shippingCost(9.99))
    # enter additional test code here
    print("Shipping cost if subtotal = 10.00:\t", shippingCost(10.00))
    print("Shipping cost if subtotal > 10.00:\t", shippingCost(10.01))
if __name__ == "__main__":
    unitTest()