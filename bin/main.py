import os
import Implementation


def main():
    print(Implementation.calculate_fine((9, 6, 2015), (6, 6, 2015)))


    # fp = open(os.path.dirname(__file__) + "/../assets/text/answers.txt", "r")
    #
    # with open(os.path.dirname(__file__) + "/../assets/text/input.txt", "r") as input_file:
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