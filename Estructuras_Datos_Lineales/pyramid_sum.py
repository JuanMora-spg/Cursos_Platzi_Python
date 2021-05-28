def pyramid_sum(lower, upper, margin=0):
    blanks = " " * margin
    print(blanks, lower, upper)

    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + pyramid_sum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result


def main():
    print("\nGenerador de suma piramidal\n")
    pyramid_sum(1, 2)


if __name__ == '__main__':
    main()
