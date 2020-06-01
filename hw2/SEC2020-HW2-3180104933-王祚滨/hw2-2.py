def big_sub(num1, num2):
    flag = 0
    res = []
    tmp = [0] * len(num1)
    num2 = [0] * (len(num1) - len(num2)) + num2
    for i in range(len(num1) - 1, -1, -1):
        if num1[i] - num2[i] + tmp[i] < 0:
            tmp[i] += num1[i] - num2[i] + 10
            tmp[i - 1] += -1
        else:
            tmp[i] += num1[i] - num2[i]

    return tmp


def big_mul(s1, s2):
    num1 = [int(i) for i in s1]
    num2 = [int(i) for i in s2]
    res = ""
    tmp = [0] * (len(num1) + len(num2))
    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            qwq = i + j + 1
            tmp[qwq] += num1[i] * num2[j]
            if tmp[qwq] >= 10:
                tmp[qwq - 1] += tmp[qwq] // 10
                tmp[qwq] = tmp[qwq] % 10
    flag = 0
    for i in tmp:
        if i != 0:
            flag = 1
        if flag:
            res += str(i)
    if flag == 0:
        res = '0'

    return res


def cmp(num1, num2):
    flag = 0
    if num1 == num2:
        return 0
    if len(num1) == len(num2):
        for i in range(len(num1)):
            if num1[i] > num2[i]:
                flag = 0
                break
            if num1[i] == num2[i]:
                continue
            if num1[i] < num2[i]:
                flag = 1
                break
    if len(num1) < len(num2) or flag:
        return -1
    else:
        return 1


# fg = 1 division fg = 0 mod
def big_mod(s1, s2, fg, isStr):
    if isStr:
        num1 = [int(i) for i in s1]
        num2 = [int(i) for i in s2]
    else:
        num1 = s1
        num2 = s2
    flag = 0
    res = ""
    tmp = []
    if len(num2) == 1 and num2[0] == 0:
        print('error!')
    else:
        if len(num1) == len(num2):
            for i in range(len(num1)):
                if num1[i] > num2[i]:
                    flag = 0
                    break
                if num1[i] == num2[i]:
                    continue
                if num1[i] < num2[i]:
                    flag = 1
                    break
        if len(num1) < len(num2) or flag:
            if fg:
                res = "0"
            else:
                if isStr:
                    res = s1
                else:
                    for i in s1:
                        res = res + str(i)
        else:
            tmp = [0] * (len(num1) - len(num2) + 1)
            now = 0
            len1 = len(num1)
            len2 = len(num2)
            num2 = num2 + [0] * (len(num1) - len(num2))
            while now < len1 - len2 + 1:
                count = 0
                while cmp(num1, num2) >= 0:
                    num1 = big_sub(num1, num2)
                    count = count + 1
                num2 = [0] + num2[:-1]
                tmp[now] = count
                now += 1
            flag = 0
            if fg:
                for i in tmp:
                    if i != 0:
                        flag = 1
                    if flag:
                        res += str(i)
            else:
                for i in num1:
                    if i != 0:
                        flag = 1
                    if flag:
                        res += str(i)
            if flag == 0:
                res = "0"
    return res


def big_public(s1, s2, s3):
    s1 = big_mod(s1, s3, 0, 1)
    num2 = list(int(i) for i in s2)
    # num2 = num2[::-1]
    res = "1"
    # 不让用int
    # ss2 = int(s2)
    while cmp(num2, [0]) > 0:
        # print(ss2)
        if big_mod(num2, [2], 0, 0) == "1":
            # if ss2 & 1:
            res = big_mul(s1, res)
            res = big_mod(res, s3, 0, 1)
        s1 = big_mul(s1, s1)
        s1 = big_mod(s1, s3, 0, 1)
        num2 = list(int(i) for i in big_mod(num2, [2], 1, 0))
        # ss2 = ss2>>1
    res = big_mod(res, s3, 0, 1)
    return res


def main():
    p = input()
    g = input()
    a = input()
    b = input()
    res = "1"
    test = big_mod([1], [2], 0, 0)
    A = big_public(g, a, p)
    print(A)
    B = big_public(g, b, p)
    print(B)
    K = big_public(A, b, p)
    print(K)


if __name__ == '__main__':
    main()
