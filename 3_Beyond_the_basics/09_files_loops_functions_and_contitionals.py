temp = [10,-20,-289,100]
def writer(temp, filepath):
    with open(filepath, "w") as myfile:
        for c in temp:
            if c > -273.15:
                f = c* 9/5 + 32
                myfile.write(str(f) + "\n")

writer(temp,"temp.txt")