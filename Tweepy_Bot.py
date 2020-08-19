import funcstorage

loop = True
while loop == True :
    funcselect = (input("What would you like to do? Create tweet (ct), show home feed(shf), find user(fu), or list followers(lf)?\n"))

    if funcselect == "ct" :
        funcstorage.createtweet()



    if funcselect == "shf" :
        funcstorage.homefeed()

    if funcselect == "fu" :
        funcstorage.finduser()

    if funcselect == "lf" :
        funcstorage.listfollowers()






    again = (input("Would you like to continue? y/n\n"))

    if again == "y" :
        loop = True

    if again == "n" :
        loop = False

