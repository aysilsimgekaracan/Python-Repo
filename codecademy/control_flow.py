# 3. Sal's Shipping
def ground_shipping(weight):
  if weight <= 2:
    return weight*1.5 + 20
  elif weight > 2 and weight <= 6:
    return weight*3 + 20
  elif weight > 6 and weight <= 10:
    return weight*4 + 20
  else:
    return weight*4.75 + 20

premium_ground_shipping = 125

def drone_shipping(weight):
  if weight <= 2:
    return weight*4.5
  elif weight > 2 and weight <= 6:
    return weight*9
  elif weight > 6 and weight <= 10:
    return weight*12
  else:
    return weight*14.25

def cheapest_shipping(weight):
  if ground_shipping(weight) <= drone_shipping(weight) and ground_shipping(weight) <=  premium_ground_shipping:
    print("Ground Shipping is the cheapest way with the cost of: " + str(ground_shipping(weight)))
  elif drone_shipping(weight) <= ground_shipping(weight) and drone_shipping(weight) <= premium_ground_shipping:
    print("Drone Shipping is the cheapest way with the cost of: " + str(drone_shipping(weight)))
  else:
    print("Premium Ground Shipping is the cheapest way with the cost of: " + str(premium_ground_shipping))

print(ground_shipping(8.4))
print(drone_shipping(1.5))
cheapest_shipping(4.8)
cheapest_shipping(41.5)

