from geopy.distance import geodesic
from collections import defaultdict

class FoodItem:
    def __init__(self, name, price, preparation_time, restaurant_id):
        self.name = name
        self.price = price
        self.preparation_time = preparation_time
        self.restaurant_id = restaurant_id

class Restaurant:
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location
        self.orders = 0  # Initialize order count for each restaurant

def get_distance(location1, location2):
    return geodesic(location1, location2).kilometers

def find_nearest_restaurants(user_location, restaurants, radius):
    nearest_restaurants = []
    for restaurant in restaurants:
        distance = get_distance(user_location, restaurant.location)
        if distance <= radius:
            nearest_restaurants.append(restaurant)
    return nearest_restaurants

def compare_food_items(nearest_restaurants, all_food_items):
    best_menu = defaultdict(list)
    for restaurant in nearest_restaurants:
        restaurant_food = [food for food in all_food_items if food.restaurant_id == restaurant.id]
        sorted_food = sorted(restaurant_food, key=lambda x: (x.price, x.preparation_time))
        best_menu[restaurant].extend(sorted_food)
    return best_menu
#i commented the sample data out but this is were e call food items in the food table and restuarants in the restaurants table
# Sample data
# user_location = (40.7128, -74.0060)  # Example user location (latitude, longitude)
# restaurants = [
#     Restaurant(1, "Restaurant A", (40.7129, -74.0061)),
#     Restaurant(2, "Restaurant B", (40.7127, -74.0059)),
#     Restaurant(3, "Restaurant C", (40.7130, -74.0062))
# ]
# food_items = [
#     FoodItem("Pizza", 10.99, 30, 1),
#     FoodItem("Burger", 8.99, 20, 1),
#     FoodItem("Sushi", 15.99, 40, 2),
#     FoodItem("Salad", 7.99, 15, 3)
# ]

# Algorithm
radius = 5  # Initial search radius in kilometers
nearest_restaurants = find_nearest_restaurants(user_location, restaurants, radius)#these variables will work after we asign them to values in the database
while not nearest_restaurants:
    radius += 5  # Increase search radius if no restaurants are found within the initial radius
    nearest_restaurants = find_nearest_restaurants(user_location, restaurants, radius)

best_menu = compare_food_items(nearest_restaurants, food_items)
for restaurant, menu in best_menu.items():
    print(f"Restaurant: {restaurant.name}")
    for food in menu:
        print(f"Food: {food.name}, Price: ${food.price}, Preparation Time: {food.preparation_time} minutes")