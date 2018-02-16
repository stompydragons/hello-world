student_names = ["James", "Katarina", "Jessica", "Mark", "Bort", "Frank Grimes", "Max Power"]

for name in student_names:
    if name == "Bort":
        continue
    elif name == "Mark":
        print("Found him! " + name)
        break
    print ("Currently testing " + name)
