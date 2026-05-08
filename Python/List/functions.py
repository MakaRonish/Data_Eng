def func(lst: list[int],name:str):
    print(f"Inside func={lst}")
    lst.append(100)
    name="new"
    print(f"after append func={lst}\n{name}")

list1=[10,20,30,55]
name="ronish"
func(list1,name)
print(f"outside list {list1}\n{name}")