# Nesting 

#  lIstas de dicionarios
covenant_elite = {"name:": "elite", "color:": "blue", "points:": 10, "shield:": True}
covenant_jackal = {"name:": "jackal", "color": "gray", "points;": 6, "shield:": True}

# nesting: diccionarios en diccionarios
users = {
    "charly:": {
        "firstname": "Carlos",
        "middlename": "Antonio",
        "lastname": "Tovar garcia",
        "location": "Mexico",
        "age": 34,
    },

    "mrred": {
        "firstname": "Jose",
        "middlename": "Lizandro",
        "lastname": "Villareal Martinez",
        "location": "Mexico",
        "age": 18,
    }
}

#looping de diccionarios en diccionarios 
for user, user_info in users.items():
    fullname = f"{user_info["firstname"]}{user_info["middlename"]}{user_info["lastname"]}"
    location = user_info["location"]
    age = user_info["age"]
    print(f"\n El nombre completo de {user} es")
    print(fullname)
    print(f"\n la ubicacion de {user} es")
    print(location)
    print(f"\n la edad de {user}:")
    print(user_info["age"])