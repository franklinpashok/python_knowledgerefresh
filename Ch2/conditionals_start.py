#
# Example File for working with conditional statements
#

def main():
    x, y = 100, 100

# conditional flow uses if, elif, else
    if (x < y):
        st = " x is less than y"
    elif(x == y):
        st = "x is equal to y"
    else:
        st = "x is greater than y"
    print(st)

    st = "x is less than y" if (x<y) else "x is greater or equal to y"
    print(st)


if __name__ == "__main__":
    main()