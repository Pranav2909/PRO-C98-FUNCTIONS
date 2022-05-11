def swapFileData():
    A = input("Enter file 1 name")
    B = input("Enter file 2 name")
    with open(A,"r") as F:
        data_a = F.read()
    with open(B,"r") as E:
        data_b = E.read()
    with open(A,"w") as F:
        F.write(data_b)
    with open(B,"w") as E:
        E.write(data_a)
swapFileData()