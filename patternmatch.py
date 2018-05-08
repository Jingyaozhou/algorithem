def patternmache(s1, s2):
    # 是否匹配完整标识符
    flag = -1
    # 记录起始序列
    start_ind = []
    # 记录结束序列
    end_ind = []
    # 记录最小长度
    min_len = []
    # 初始化目标游标
    t = 0
    for i, j in enumerate(s1):
        # 第一部分判定第一次出现的字符
        # 判定是否与目标值相同
        if j == s2[t]:
            if t == 0:
                start_ind.append(i)
                t += 1
                continue
            elif t == len(s2) - 1:
                end_ind.append(i)
                t = 0
                flag = 1
                min_len.append(end_ind[-1] - start_ind[-1] + 1)
            else:
                t += 1
        # 修改第一个字符的游标
        if t == 1 and j == s2[t - 1]:
            start_ind.pop()
            start_ind.append(i)
    # 如果标识符为1则找到匹配字符串
    if flag == 1:
        p = min_len.index(min(min_len))
        return start_ind[p], end_ind[p]
    else:
        return -1, -1


if __name__ == '__main__':
    s1 = 'adhgiehigehigebjgijijijcjijijajijbjc'
    s2 = 'abc'
    print(patternmache(s1, s2))
