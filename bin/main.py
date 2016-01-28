import os
import Implementation


def main():
    with open(os.path.dirname(__file__) + "/../assets/text/input.txt", "r") as input_file:
        n,m = input_file.readline().strip().split(' ')
        n,m = [int(n),int(m)]
        topic = []
        topic_i = 0
        for topic_i in range(n):
           topic_t = str(input_file.readline().strip())
           topic.append(topic_t)
        max, teams = Implementation.max_known_topics_teams(topic)
        print(max)
        print(teams)


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