import geocoder

# Gather Data
t = input("Enter Your Location :")

# Location Research
g = geocoder.arcgis(t)

# Output
print(g.latlng)
