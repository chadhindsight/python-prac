# repeat everything until input says "stop copying me"
msg = input("Hey, tell me something!")


while msg != "stop copying me":
    print(msg)
    msg = input()
# outside message given when we stop copying
print("Fine! I will stop now")
    