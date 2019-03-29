import sys
loggedin = False
while loggedin == False:
    file = open("names11.txt")
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')
    details= username+","+password+"\n"
    score1=username
    for line in file:
        if line==details:
            loggedin= True
    if loggedin==False:
        print("your entered incorrect")
print("correct")
sum=0
f = open("questions1.txt", "r")
print("question")
q1=input(f.read(20)).lower()
if q1=="baby":
    print ("correct")
    sum=sum+3
elif q1 !="baby":
    p1=input("try again what is the answer").lower()
    if p1=="baby":
        print ("correct")
        sum=sum+1
    else:
        print("wrong")
        print("your score is ")
        print(sum)
        text_file = open("question64.txt", "a")
        text_file.write("\n" + username+ ' has a score of ' + str(sum) + "\n")
        with open("question64.txt") as f1:
            lines = f1.readlines()
            lines = [x.strip() for x in lines]
            print ("\n".join(lines))
            text_file.close()
            sys.exit()
print("question 2:")
q2=input(f.read(32)).lower()
if q2=="smooth criminal":
    print ("correct")
    sum=sum+3
elif q2 !="smooth criminal":
    p2=input("try again what is the answer").lower()
    if p2=="smooth criminal":
        print ("correct")
        sum=sum+1
    else:
        print("wrong")
        print("your score is ")
        print(sum)
        text_file = open("question64.txt", "a")
        text_file.write("\n" + username+ ' has a score of ' + str(sum) + "\n")
        with open("question64.txt") as f1:
            lines = f1.readlines()
            lines = [x.strip() for x in lines]
            print ("\n".join(lines))
            text_file.close()
            sys.exit()
print("question 3:")
q3=input(f.read(32)).lower()
if q3=="happier":
    print ("correct")
    sum=sum+3
elif q3 !="happier":
    print("wrong")
    p3=input("try again what is the answer").lower()
    if p3=="happier":
        print ("correct")
        sum=sum+1
    else:
        print("wrong")
        print("your score is ")
        print(sum)
        text_file = open("question64.txt", "a")
        text_file.write("\n" + username+ ' has a score of ' + str(sum) + "\n")
        with open("question64.txt") as f1:
            lines = f1.readlines()
            lines = [x.strip() for x in lines]
            print ("\n".join(lines))
            text_file.close()
            sys.exit()
print("question 4:")
q4=input(f.read(21)).lower()
if q4=="rockstar":
    print ("correct")
    sum=sum+3
elif q4 !="rockstar":
    print("wrong")
    p4=input("try again what is the answer").lower()
    if p4=="rockstar":
        print ("correct")
        sum=sum+1
    else:
        print("wrong")
        print("your score is ")
        print(sum)
        text_file = open("question64.txt", "a")
        text_file.write("\n" + username+ ' has a score of ' + str(sum) + "\n")
        with open("question64.txt") as f1:
            lines = f1.readlines()
            lines = [x.strip() for x in lines]
            print ("\n".join(lines))
            text_file.close()
            sys.exit()
print("question 5:")
q5=input(f.read(28)).lower()
if q5=="imagine":
    print ("correct")
    sum=sum+3
elif q5 !="imagine":
    print("wrong")
    p5=input("try again what is the answer").lower()
    if p5=="imagine":
        print ("correct")
        sum=sum+1
    else:
        print("wrong")
        print("your score is ")
        print(sum)
        text_file = open("question64.txt", "a")
        text_file.write("\n" + username+ ' has a score of ' + str(sum) + "\n")
        with open("question64.txt") as f1:
            lines = f1.readlines()
            lines = [x.strip() for x in lines]
            print ("\n".join(lines))
            text_file.close()
            sys.exit()
print("questin")
q6=input(f.read(14)).lower()
if q6=="money":
    print ("correct")
    sum=sum+3
elif q6!="money":
    print("wrong")
    p6=input("try again what is the answer").lower()
    if p6=="money":
        print ("correct")
        sum=sum+1
    else:
        print("wrong")
        print("your score is ")
        print(sum)
        text_file = open("question64.txt", "a")
        text_file.write("\n" + username+ ' has a score of ' + str(sum) + "\n")
        with open("question64.txt") as f1:
            lines = f1.readlines()
            lines = [x.strip() for x in lines]
            print ("\n".join(lines))
            text_file.close()
            sys.exit()
print("question")
q7=input(f.read(34)).lower()
if q7=="sicko mode":
    print ("correct")
    sum=sum+3
elif q7 !="sicko mode":
    print("wrong")
    p7=input("try again what is the answer").lower()
    if p7=="sicko mode":
        print ("correct")
        sum=sum+1
    else:
        print("wrong and the quiz has ended")
        print("your score is ")
        print(sum)
        text_file = open("question.txt", "a")
        text_file.write("\n" + username+ ' has a score of ' + str(sum) + "\n")
        with open("question64.txt") as f1:
            lines = f1.readlines()
            lines = [x.strip() for x in lines]
            print ("\n".join(lines))
            text_file.close()
            sys.exit()
print("question")
q8=input(f.read(36)).lower()
if q8=="girls like you":
    print ("correct")
    sum=sum+3
elif q8 !="girls like you":
    print("wrong")
    p8=input("try again what is the answer").lower()
    if p8=="girls like you":
        print ("correct")
        sum=sum+1
    else:
        print("wrong")
        print("your score is ")
        print(sum)
        text_file = open("question64.txt", "a")
        text_file.write("\n" + username+ ' has a score of ' + str(sum) + "\n")
        with open("question64.txt") as f1:
            lines = f1.readlines()
            lines = [x.strip() for x in lines]
            print ("\n".join(lines))
            text_file.close()
            sys.exit()
print("question")
q9=input(f.read(19)).lower()
if q9=="dna":
    print ("correct")
    sum=sum+3
elif q9 !="dna":
    print("wrong")
    p9=input("try again what is the answer").lower()
    if p9=="dna":
        print ("correct")
        sum=sum+1
    else:
        print("wrong")
        print("your score is ")
        print(sum)
        text_file = open("question64.txt", "a")
        text_file.write("\n" + username+ ' has a score of ' + str(sum) + "\n")
        with open("question64.txt") as f1:
            lines = f1.readlines()
            lines = [x.strip() for x in lines]
            print ("\n".join(lines))
            text_file.close()
            sys.exit()
print("question")
q10=input(f.read(20)).lower()
if q10=="diamonds":
    print ("correct")
    sum=sum+3
elif q10 !="diamonds":
    print("wrong")
    p10=input("try again what is the answer").lower()
    if p10=="diamonds":
        print ("correct")
        sum=sum+1
    else:
        print("wrong")
        print("your score is ")
        print(sum)
        text_file = open("question64.txt", "a")
        text_file.write("\n" + username+ ' has a score of ' + str(sum) + "\n")
        with open("question64.txt") as f1:
            lines = f1.readlines()
            lines = [x.strip() for x in lines]
            print ("\n".join(lines))
            text_file.close()
            sys.exit()
print("your score is")
print(sum)
text_file = open("question64.txt", "a")
text_file.write("\n" + username+ ' has a score of ' + str(sum) + "\n")
with open("question64.txt") as f1:
    lines = f1.readlines()
    lines = [x.strip() for x in lines]
    print ("\n".join(lines))
    text_file.close()
    sys.exit()
