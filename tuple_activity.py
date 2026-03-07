#PACKING

address = (227, "Brickfield Shelters", "Bangalore", "Karnataka", "562107")

for x in address:
    print(x, end = ' ')

#UNPACKING

houseno, apartName, city, state, pincode = address

print('\nHNO', houseno)   #house number
print('APT NO ', apartName)   #apartment name
print(city)   #city
print(state)   #state
print(pincode)   #pincode
