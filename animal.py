def meow():
    print("Meow... meow")

def bark():
    print("Hau hau....")

def unknown():
    print("Unknown animal...")

animals = {
    "cat": meow,
    "dog": bark,
}

animal_type = input("Enter animal type: ")  # cat or dog
animals.get(animal_type, unknown)()
