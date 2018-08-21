# GetPos program in Python

cood = "48.8041101,2.321208899999988"

# Function definition is here
def GetPos (cood) : 
    "This Extract latitude and longitude from coodinate type DD"
    latitude, longitude = [float (index) for index in cood.split(',')]
    return latitude, longitude

latitude, longitude = GetPos (cood) 
print "latitude  = ", latitude 
print "longitude = ", longitude

