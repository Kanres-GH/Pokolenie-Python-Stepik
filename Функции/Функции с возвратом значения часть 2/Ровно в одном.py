def is_one_away(word1, word2):
    if len(word1) == len(word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i]==word2[i]:
                cnt += 1
        if len(word1)-cnt==1:
            return True
    return False

txt1 = input()
txt2 = input()
print(is_one_away(txt1, txt2))