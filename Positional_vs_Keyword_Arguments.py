def greet_with(location, name):
    print(f"Hello {name}")
    print(f"Your location is {location}")


var_location = input("Please type your location: ")

var_name = input("Tell me your name: ")

greet_with(name=var_name, location=var_location)