# created by me on december 12 2023
# function definitions
def fahrenheit():
    try:
        tc = float(input("please enter a number:"))
        print("")
        # calculations for converting
        tf = 9 / 5 * tc + 32
        print("the temperature is {} degrees f ".format(tf))
    except ValueError:
        print("invalid input, enter valid number")


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
