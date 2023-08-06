# 문자열 비교 과정 코드
def compare_str(str1, str2):
    flag = True
    if len(str1) == len(str2):
        for i, j in zip(str1, str2):
            if i != j:
                flag = False
                break
    else:
        flag = False
    return flag

print(compare_str("바나나", "바나나"))      # True
print(compare_str("애플망고", "바나나"))    # False