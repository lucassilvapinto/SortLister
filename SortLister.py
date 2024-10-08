while True:
    lista = []
    
    try:
    
        n = int(input("Enter the number of elements\n"))
        for n in range(0,n):
            lst = input("Please, insert the numbers: ")
            lista.append(lst) 

        options = ['asc', 'desc'] 

        while True:
            order = input("Enter the order of elements\n Asc or Desc\n").lower()

            if order in options:
                if order == "desc":
                    lista.sort(reverse=True)
                    break
                elif order == "asc":
                    lista
                    break
            else:
                print("\nChoose a option")


        print("\n\nAccording with your choice, here is the list: ", lista)
        

        while True:

            try:
                    num = int(input("Press 1 and enter to exit the program or 2 and enter to reset the program..."))
                    if num == 1:
                        break
                    elif num == 2:
                        continue    
                    else:
                        print("Choose an option, 1 or 2\n\n\n\n")
            except ValueError:
                    print("Oops!  That was no valid number.  Try again...")    
    except ValueError:
        print("Please insert a valid number")