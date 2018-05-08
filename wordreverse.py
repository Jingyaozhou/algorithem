# 将输入的句子反转
def sentencewordreverse(sentence):
    # 切分单词到列表
    word_token = sentence.split()
    # 列表反转
    word_token.reverse()
    # 列表转化成句子
    sentencerevesed = ' '.join(word_token)
    return sentencerevesed


if __name__ == '__main__':
    sentence = 'Today is Tuesday'
    print(sentencewordreverse(sentence))
