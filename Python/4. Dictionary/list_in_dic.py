students={
    "ronish":{"gender":"male","marks":[1,2,3,4,5]},
    "pr":{"gender":"male","marks":[15,62,73,94,5]},
    "re":{"gender":"male","marks":[1,25,35,46,6759]},
    "ro":{"gender":"male","marks":[1,256,3,4,5]},
    "ash":{"gender":"male","marks":[1,2,763,4,5]},
    "kush":{"gender":"male","marks":[13,32,3356,4,5]},
}

for name,another in students.items():
    print(f"{name} = {sum(another["marks"])}")