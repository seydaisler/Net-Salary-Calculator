print('***Net Salary Calculator***')
def inputGross():
    gross=int(input('what is your yearly gross salary?\n'))
    if gross <=0:
        print('Please enter a valid gross salary')
        return inputGross()
    return gross


def calculateChildTaxDiscount():
    childCount=int(input('how many children do you have?\n'))
    if childCount < 0:
       print('Please enter a valid value') 
       return calculateChildTaxDiscount()
    if childCount> 4:
        childCount=4
    return childCount * 0.5

def calculateTaxCategory():
    taxCategory=int(input('What is your tax category?\n'))
    if taxCategory>5 or taxCategory<=0:
        print('print enter a valid value')
        return calculateTaxCategory()
    taxCategoryPercentages={1:2.8, 2:3.4, 3:4.8, 4:5.2, 5:6.1}
    return taxCategoryPercentages[taxCategory]

def calculateTax():
    netto=((100 - (calculateTaxCategory() - calculateChildTaxDiscount() ))/100 * inputGross())
    return netto

netto=calculateTax()
print('Your yearly net salary is', int(netto))
