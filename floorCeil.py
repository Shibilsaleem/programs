def floorCeil(f,c):
    if f==c:
        number=2*f
    if f<c:
        number=(2*f)+1
    return number
floor=float(input('Enter the floor of the number when divided by 2 : '))
ceil=float(input('Enter the ceil of the number when divide by 2 : '))
print(floorCeil(floor,ceil))