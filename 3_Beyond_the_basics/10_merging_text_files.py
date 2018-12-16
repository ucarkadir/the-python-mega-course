import glob
from datetime import datetime

filenames = glob.glob("files/*.txt")
print(filenames)

with open("./"+datetime.now().strftime("%d-%m-%Y-%H-%S-%f")+".txt", 'w') as myfile:
    for fn in filenames:
        with open(fn, "r") as f:
            myfile.write(f.read() + "\n")


