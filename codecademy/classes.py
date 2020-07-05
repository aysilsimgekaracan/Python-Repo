#Basta Fazoolin'

# Class Menu
class Menu():

	def __init__(self, name, items, start_time, end_time):
		self.name = name
		self.items = items
		self.start_time = start_time
		self.end_time = end_time

	def __repr__(self):
		return "{name} menu available form {start_time} to {end_time}".format(name=self.name, start_time=self.start_time, end_time=self.end_time)

	def calculate_bill(self, purchased_items):
		sum_of_items = 0
		for item in purchased_items:
			if item in self.items:
				sum_of_items += self.items.get(item)
		return sum_of_items
		
# Class Franchise
class Franchise:
	def __init__(self, address, menus):
		self.address = address
		self.menus = menus

	def __repr__(self):
		return "The Address of the Franchise: {}".format(self.address)

	def available_menus(self, time):
		available_menu = []
		for menu in self.menus:
			if time >= menu.start_time and time <= menu.end_time:
				available_menu.append(menu)
		return available_menu

# Class Business
class Business:
	def __init__(self, name, franchises):
		self.name = name
		self.franchises = franchises


# Brunch
brunch_menu = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
  }
brunch = Menu("Brunch", brunch_menu, 11, 16)

# Early Bird

early_bird_menu = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu("Early Bird", early_bird_menu, 15, 18)

# Dinner Menu
dinner_menu = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner = Menu("Dinner", dinner_menu, 17, 23)

# Kids
kids_menu = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu("Kids", kids_menu, 11, 21)



print(brunch)

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
)

print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


# Creating the Franchises
menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

print(flagship_store.available_menus(17))

# Creating Business
franchises = [flagship_store, new_installment]
franchise_business = Business("Basto Fazoolin' with my Heart", franchises)

# Arepas
arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas = Menu("Take a' Arepa", arepas_menu, 10, 20)
arepas_place = ["189 Fitzgerald Avenue", arepas]

franchise_arepas = Business("Take a' Arepa", arepas_place)

