# 循环字符串查找目标字符串是否在循环字符串中
def pos2time1(s1, s2):
    s = s1 * 2
    rule = re.compile(s2)
    reuslt = re.findall(rule, s)
    return reuslt != []


def pos2time2(s1, s2):
    rule = re.compile(s2)
    for i in range(len(s1)):
        s1 = s1[1:] + s1[0]
        if re.findall(rule, s1) != []:
            return True
        else:
            continue
    return False


if __name__ == '__main__':
    s1 = 'ABCDE'
    s2 = 'EAB'
    s3 = 'AEB'
    import re
    print(pos2time2(s1, s3))
