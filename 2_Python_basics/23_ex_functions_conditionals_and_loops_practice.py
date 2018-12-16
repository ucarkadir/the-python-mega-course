def cel_to_fahr(celsius):
    fahreneit = celsius * 9/5 + 32
    return fahreneit

temperatures = [10 , -20, 100]

for t in temperatures:
    print(float(cel_to_fahr(t)))