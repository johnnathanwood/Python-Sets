# 1. Create an empty set named showroom.
showroom = set()
# 2. Add four of your favorite car model names to the set.
showroom.add("bmw")
showroom.add("honda")
showroom.add("toyota")
showroom.add("jeep")
showroom.add("kia")
showroom.add("mazda")
print(showroom)
# 3. Print the length of your set.
print("length", len(showroom))
# 4. Pick one of the items in your show room and add it to the set again.
showroom.add("bmw")
# 5.Print your showroom. Notice how there's still only one instance of that model in there.
print(showroom)
mygarage = []
for car in showroom:
    print(f"{car} is my favorite car. I have {len(showroom)} total cars.") 
print("Total Cars", len(showroom))
# 6. Using update(), add two more car models to your showroom with another set.
trucks = {"ford","dodge"}
showroom.update(trucks)
print("Updated",showroom)
print("Total Cars", len(showroom))
# 7. You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("kia")
print("Discard",showroom)
print("Total Cars", len(showroom))

# Acquiring more cars////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 1. Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = {"ford","dodge","kia","vw"}
print("junkyard cars", junkyard)
# 2. Use the intersection method to see which cars exist in both the showroom and that junkyard.
common = showroom.intersection(junkyard)
print("Common Cars", common)
print("Total common cars", len(common))
# 3. Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
showroom = showroom.union(junkyard)
print("Merged cars from junkyard to showroom", showroom)
print("Total bought", len(junkyard))
print("Total cars after merge", len(showroom))
# 4. Use the discard() method to remove any cars that you acquired from the junkyard that you want in your showroom.
junkyard.discard("kia")
junkyard.discard("vw")
print("Final types of cars in junkyard", junkyard)
print("Total cars in junkyard", len(junkyard))
print("Final types of cars in showroom", showroom)
print("Total cars in showroom", len(showroom))
