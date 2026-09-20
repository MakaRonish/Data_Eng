def elgible(age):
    if age < 0:
        raise ValueError("age cannot be neg")

    if age >= 0 and age <18:
        raise ValueError("Not eligible")

    print("you can vote")


try:
    elgible(-1)

except ValueError as e:
    print("some error occured")
    print(e)
    print(type(e))
    