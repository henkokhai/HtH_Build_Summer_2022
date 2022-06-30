full_name = "Khai Phan"
nickname = "Ponzu"
age = 20
python_experience = False

hobbies = [
    "sleeping", "playing guitar", "videography", "photography", "playing videogames"
]

favorites = {
    "movie": "Sing 2",
    "number": 15,
    "food": "KBBQ",
    "hobby": hobbies[2],
    "videogame": "Valorant",
}

print(full_name, nickname, age, python_experience)
print() #this prints a new line when no arguments are provided
print(hobbies)
print()
print(favorites)

all_varss = dict(vars())
