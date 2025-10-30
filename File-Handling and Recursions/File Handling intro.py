#with open(r"C:\Users\aliay\Desktop\Text Files\Intro.txt", "r") as f:
#    text = "" #we start with an empty string
#    for line in f:
#        text += line.strip() #removes new line then adds to the string
#print(text)
#ans = eval(text)
#print(ans)

with open(r"C:\Users\aliay\Desktop\Text Files\Intro.txt", "r") as f:
    lines = f.readlines()
    print(eval("".join(line.strip() for line in lines)))

with open(r"C:\Users\aliay\Desktop\Text Files\Intro.txt", "r") as f:
    lines = f.read(10)
    print(lines)

with open(r"C:\Users\aliay\Desktop\Text Files\Intro.txt", "r") as f:
    for i in range(10):
        line = f.readline()
        print(line, end="")

#Creating a new File:
with open(r"C:\Users\aliay\Desktop\Text Files\CreatingANewFile.txt", "w") as f:
    f.write("ez bro I made this!\n")
    f.write("ah ah ah ah\n")

try:
    with open(r"C:\Users\aliay\Desktop\Text Files\Nigga.txt", "r") as f:
        for i in range(10):
            linessss = f.readline()
            print(linessss, end="")
except FileNotFoundError:
    print("File not found")
except IOError:
    print("lora khale")