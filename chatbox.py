def chat():
    print("Hello!how may i help you")
    
    while True:
        user=(input("\nSPEAKKKKKKKKKK\n"))

        if user=="hello":
            print("Dont you have anything else to say:")
        elif user=="i need help to solve world theories":
            print("You cant figure your life out and world theories haha")
        elif user=="i want to know good resturants":
            print("You dont have any money .........")
        elif user=="how are you":
            print("tell ur motive i dont have time for this shit")
        elif user=="i am bored":
            print("then why are u eating my time go and do something")
        else:
            print(" i am going bye i dont want to waste more time here")
        break

def again():
    while True:
        want=input("do you want to try this thing again?").strip().lower()

        if want=="yes":
            chat()
        elif want=="no":
            print("Great i can rest now ")
            break
        else:
            print("what language is this u illiterate rat")
chat()
again()






