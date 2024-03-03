print("Counting to 10")
for num in range(1,10):
    print(num)
    
favorite_foods = ['pizza', 'mac n cheese', 'ice cream', 'chocolate', 'i eat other healthy stuff :D']
print("Here are all your favorite foods")
for favorite_food in favorite_foods :
    print(f"{favorite_food}")
    
num_letters = 5
print("Here are the favorite foods that are longer than 5 letters.")
for favorite_food in favorite_foods:
    if len(favorite_food) > num_letters:
        print(favorite_food)
        
plural_foods = []
for favorite_food in favorite_foods:
    plural_food = favorite_food + "s"
    plural_foods.append(plural_food)
print("Here are the plural forms of your foods")
for plural_food in plural_foods :
    print(plural_foods)
