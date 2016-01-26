import os
import Implementation


def main():
    fp = open(os.path.dirname(__file__) + "/../assets/text/input.txt", "r")

    t = int(fp.readline().strip())
    for a0 in range(t):
        R,C = fp.readline().strip().split(' ')
        R,C = [int(R),int(C)]
        G = []
        G_i = 0
        for G_i in range(R):
           G_t = str(fp.readline().strip())
           G.append(G_t)
        r,c = fp.readline().strip().split(' ')
        r,c = [int(r),int(c)]
        P = []
        P_i = 0
        for P_i in range(r):
           P_t = str(fp.readline().strip())
           P.append(P_t)

        print("YES" if Implementation.grid_search(G, P) else "NO")





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