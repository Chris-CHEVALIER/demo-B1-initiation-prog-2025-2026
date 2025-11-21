print("Hello World!")

# first_name = input("Quel est votre prénom ? ")
# print("Bienvenue " + first_name + " !")

students = [
    {"first_name": "Thomas", "last_name": "Penot"},
    {"first_name": "Rim", "last_name": "BOULMAAROUF"},
    {"first_name": "Timothé", "last_name": "Hamel"},
]
students.append({"first_name": "Charif", "last_name": "El Bakkali"})


# students.sort()


cosmo = {
    "first_name": "Cosmo",
    "last_name": "Chevalier",
    "age": 2.5,
    "color": "sable",
    "breed": "Golden Retriever",
    "weight": 35,
}

cosmo["weight"] = 32

print(
    "Bienvenue "
    + cosmo["first_name"]
    + " "
    + cosmo["last_name"]
    + " le "
    + cosmo["breed"]
    + " à l'École Hexagone !"
)


def welcome_message(first_name, last_name):
    return "Bienvenue " + first_name + " " + last_name + " à l'École Hexagone ! ✨"

for student in students:
    print(welcome_message(student["first_name"], student["last_name"]))

print("Dans ma classe, j'ai " + str(len(students)) + " étudiants")

count = 0
while count < 5:
    print("Mon compteur " + str(count))
    count += 1
