def main():
    print("This program illustrates a chaotic functions")
    x = float(input("Enter a number between 0 and 1: "))
    for i in range (100):
        x = 2.0 * x * (1 - x)
        print(x)

main()
