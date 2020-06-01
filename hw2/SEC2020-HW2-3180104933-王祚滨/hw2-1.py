def big_add(s1, s2):
    num1 = [int(i) for i in s1]
    num2 = [int(i) for i in s2]
    tmp = []
    if len(num1) <= len(num2):
        tmp = [0] * (len(num2) + 1)
        num1 = [0] * (len(num2) - len(num1)) + num1
    else:
        tmp = [0] * (len(num1) + 1)
        num2 = [0] * (len(num1) - len(num2)) + num2
    for i in range(len(tmp) - 2, -1, -1):
        if num1[i] + num2[i] + tmp[i + 1] < 10:
            tmp[i + 1] += num1[i] + num2[i]
        else:
            tmp[i + 1] += num1[i] + num2[i] - 10
            tmp[i] += 1
    # zero
    res = ""
    flag = 0
    for i in tmp:
        if i != 0:
            flag = 1
        if flag:
            res += str(i)
    return res


def big_sub(s1, s2):
    num1 = [int(i) for i in s1]
    num2 = [int(i) for i in s2]
    flag = 0
    res = ""
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
        res = "-"
        tmp = num1
        num1 = num2
        num2 = tmp

    tmp = [0] * len(num1)
    num2 = [0] * (len(num1) - len(num2)) + num2
    for i in range(len(num1) - 1, -1, -1):
        if num1[i] - num2[i] + tmp[i] < 0:
            tmp[i] += num1[i] - num2[i] + 10
            tmp[i - 1] += -1
        else:
            tmp[i] += num1[i] - num2[i]

    flag = 0
    for i in tmp:
        if i != 0:
            flag = 1
        if flag:
            res += str(i)
    if flag == 0:
        res = '0'
    return res


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
def big_division(s1, s2, fg):
    num1 = [int(i) for i in s1]
    num2 = [int(i) for i in s2]
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
                res = s1
        else:
            tmp = [0] * (len(num1) - len(num2) + 1)
            now = 0
            len1 = len(num1)
            len2 = len(num2)
            num2 = num2 + [0] * (len(num1) - len(num2))
            while now < len1 - len2 + 1:
                count = 0
                while cmp(num1, num2) > 0:
                    ss1 = ""
                    ss2 = ""
                    for i in num1:
                        ss1 += str(i)
                    for i in num2:
                        ss2 += str(i)
                    num1 = [int(i) for i in big_sub(ss1, ss2)]
                    # 去掉头部0
                    for i in num1:
                        if i == 0:
                            num1 = num1[1:]
                        else:
                            break
                    count = count + 1
                num2 = num2[:-1]
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
    return res
    # return res


# def big_mod(s1, s2):
#     num1 = [int(i) for i in s1]
#     num2 = [int(i) for i in s2]
#     res = ""
#     if len(num2)==1 and num2[0] == 0:
#         print('error!')
#     else:
#         if cmp(num1, num2) < 0:
#             res = s1
#         else:
#             s3 = big_division(s1, s2)
#             s4 = big_mul(s2, s3)
#             res = big_sub(s1, s4)
#     return res


def main():
    s1 = input()
    s2 = input()
    res = big_add(s1, s2)
    print(res)
    res = big_sub(s1, s2)
    print(res)
    res = big_mul(s1, s2)
    print(res)
    res = big_division(s1, s2, 1)
    print(res)
    res = big_division(s1, s2, 0)
    print(res)


if __name__ == '__main__':
    main()
