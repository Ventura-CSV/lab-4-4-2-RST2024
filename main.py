def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    while True:
        try:
            number = float(input('Enter a number '))
        except ValueError:
            print ('Enter only a number')
        else:
            print (number)

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
