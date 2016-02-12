def main():
    test = [
        {"a": 100, "b": 129},
        {"a": 100, "b": 67},
        {"a": 100, "b": 16},
        {"a": 100, "b": 576},
        {"a": 345, "b": 234}
        ]

    test.sort(key=lambda x: (x["a"], x["b"]))

    print("Nothing to do.")

    # fp = open(os.path.dirname(__file__) + "/../assets/text/answers.txt", "r")
    #
    # with open(os.path.dirname(__file__) + "/../assets/text/sherlock_and_anagrams_input.txt", "r") as input_file:
    #     n = int(input_file.readline().strip())
    #     print(n)
    #     for line in input_file:
    #         n, c, m = line.strip().split(" ")
    #         n, c, m = int(n), int(c), int(m)
    #         result = format("%i" % Implementation.calculate_chocolates(n, c, m))
    #         answer = fp.readline().strip()
    #         if result != answer:
    #             print("%s %s %s" % (line, result, answer))
    #
    # fp.close()


if __name__ == '__main__':
    main()
