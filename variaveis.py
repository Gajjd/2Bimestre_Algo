status = "maravilhoso"

def comportamento():
    global status
    status = "Cansativo"
    print("Python é " + status)

print(comportamento())

print("Python é " + status)