boss="Arthur";
def walk(name,speed):
    print(f"{name} is walking at {speed} km/h speed");
    global boss;
    boss="philip";
    print(boss);
    if speed>=15:
        return "dead";
    else:
        return "alive";




# room = 213
#
# temperature = 25.53567
# print(f"I'm  staying at room {room} with temperature {temperature:.2f}")
# print("We said \"its\" ")
# ans=walk("Shihab",10);
# print(ans);
# print(boss)
# name=input("What is your name: ");

# print(name)
# students={
#     "011221017": "Shihab Uddin,23, a programmer,4",
#      11221018: "Jane Doe, an architect"
# }
# students[11221018]="Tazvir, a gamer,lnda";
# del students[11221018];
# students[8]:{"nayem,a ...,30,dsd"};
# print(students[11221018]);
# print(students[8]);
# animal_types = {"human"}
# animal_types.add("bird")
# animal_types.update(["cat", "dog"])
# animal_types.add("human") # doesn't add human again as it's there
# animal_types.discard("dog") # discard dog from the set
# print(animal_types)

pencil_box = [
    "Rubber", "Pencil", "Pen", "Scale", ("Sharpner", "Dirt"), 10000
]

print(pencil_box[5])

