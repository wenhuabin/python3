
def inputErr():
    while True:
        try: 
            x = int(input("Please enter a number:"))
            break
        except ValueError:
            print("Oops! invalid!")

if __name__ == "__main__":
    inputErr()
