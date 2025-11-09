def main():
    pricePerHour = 35
    
    sqfeet = float(input("Enter the square feet of wall space: "))
    pricePaint = float(input("Enter the price of pain per gallon: "))

    gallonPaint = GallonOfPaint(sqfeet)
    totalLaborHours = TotalLaborHours(sqfeet)
    totalLaborPrice = TotalLaborPrice(totalLaborHours, pricePerHour)
    totalCostOfPaint = TotalCostOfPaint(pricePaint, gallonPaint)

    print()
    print(f"The number of gallons of paint required: {gallonPaint:,.2f} gal")
    print(f"The hours of labor required: {totalLaborHours:,.0f} hours")
    print(f"The cost of the paint: RM {totalCostOfPaint:,.2f}")
    print(f"The labor charges: RM {totalLaborPrice:,.2f}")
    print(f"The total cost of the paint job: RM {(totalCostOfPaint + totalLaborPrice):,.2f}")

def GallonOfPaint(sqfeet: float):
    wallSpace_paint = 1 / 112
    paintGallon = wallSpace_paint * sqfeet
    return paintGallon

def TotalLaborHours(sqfeet: float):
    wallSpace_labor = 8 / 112
    laborHours = wallSpace_labor * sqfeet
    return laborHours

def TotalLaborPrice(laborHours: float, pricePerHour: int):
    totalPrice = laborHours * pricePerHour
    return totalPrice

def TotalCostOfPaint(pricePaint: float, gallonPaint: float):
    return pricePaint * gallonPaint

main()
