#Health Management System

def getdate():
    import datetime
    return datetime.datetime.now()


def logger(c, choice):
    if choice == 1:
        if c == 1:
            f = open("HarryDiet.txt", "a")
            food = input("What did you eat?\n")
            f.write("["+ str(getdate())+ "]" +" : "+ str(food) + "\n")
            f.close()
            print("Diet successfully logged")

        elif c == 2:
            f = open("RohanDiet.txt", "a")
            food = input("What did you eat?\n")
            f.write("["+ str(getdate())+ "]" +" : "+ str(food) + "\n")
            f.close()
            print("Diet successfully logged")

        else:
            f = open("HammadDiet.txt", "a")
            food = input("What did you eat?\n")
            f.write("["+ str(getdate())+ "]" +" : "+ str(food) + "\n")
            f.close()
            print("Diet successfully logged")

    else:
        if c == 1:
            f = open("HarryEx.txt", "a")
            food = input("Which exercise did you do?\n")
            f.write("["+ str(getdate())+ "]" +" : "+ str(food) + "\n")
            f.close()
            print("Exercise successfully logged")

        elif c == 2:
            f = open("RohanEx.txt", "a")
            food = input("Which exercise did you do?\n")
            f.write(getdate() +":" + food)
            f.close()
            print("Exercise successfully logged")

        else:
            f = open("HammadEx.txt", "a")
            food = input("Which exercise did you do?\n")
            f.write("["+ str(getdate())+ "]" +" : "+ str(food) + "\n")
            f.close()
            print("Exercise successfully logged")
    return


def retriever(c, choice):
    if choice == 1:
        if c == 1:
            f = open("HarryDiet.txt")
            print(f.read())
            f.close()

        elif c == 2:
            f = open("RohanDiet.txt")
            print(f.read())
            f.close()

        else:
            f = open("HammadDiet.txt")
            print(f.read())
            f.close()

    else:
        if c == 1:
            f = open("HarryEx.txt")
            print(f.read())
            f.close()

        elif c == 2:
            f = open("RohanEx.txt")
            print(f.read())
            f.close()

        else:
            f = open("HammadEx.txt")
            print(f.read())
            f.close()

    return

print("**********HEALTH MANAGEMENT SYSTEM**********\n")
client = int(input("Choose client:\n1.Harry\n2.Rohan\n3.Hammad\n"))
opn = int(input("Choose operation:\n1.Logging\n2.Retrieval\n"))
ch = int(input("1.Diet\n2.Exercise\n"))

if opn == 1:
    logger(client, ch)
else:
    retriever(client, ch)
