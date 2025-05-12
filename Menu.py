import random

food_types = ["Italian", "Chinese", "Mexican", "Indian", "Japanese"]

food_dishes = {
    "Italian": ["Spaghetti", "Pizza", "Lasagna"],
    "Chinese": ["Noodles", "Dumplings", "Fried Rice"],
    "Mexican": ["Tacos", "Burrito", "Quesadilla"],
    "Indian": ["Curry", "Naan", "Biryani"],
    "Japanese": ["Sushi", "Ramen", "Tempura"]
}

print("Available food types:")
print(", ".join(food_types))

user_input = input("Enter food types (separated by commas): ")
food_choices = user_input.split(",")

selected_dishes = []

for food_type in food_choices:
    food_type = food_type.strip().capitalize()
    if food_type in food_dishes:
        for dish in food_dishes[food_type]:
            selected_dishes.append(dish)

number_of_dishes = random.randint(1, 6)
random_dishes = []

for x in range(number_of_dishes):
    if selected_dishes:
        random_dishes.append(random.choice(selected_dishes))

print("Randomly chosen dishes:")
for dish in random_dishes:
    print("-", dish)
