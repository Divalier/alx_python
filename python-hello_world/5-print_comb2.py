for i in range(0,100):
    if i<10:
        print(f"0{i}, ", end=" ")
    elif i==99:
        print("99", end="\n")
    else:
        print(f"{i}, ", end=" ")