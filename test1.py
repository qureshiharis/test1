# Defining a main() function
def main():
    print("main runs fine")
    print("sum is: ", sum(3,2))

# Sum function
def sum(x, y):
    return x+y

# Safety check, as to if we import functions from this file, it doesn't end up running 
if __name__ == "__main__":
    main()
