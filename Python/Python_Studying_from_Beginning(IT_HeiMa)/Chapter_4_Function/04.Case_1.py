# Case 1
def triangle_are(b, h):
    """

    """
    area = b * h / 2
    return area

print("三角形的面积为：", triangle_are(30, 10))


# Case 2
def count_vowel(sentence):
    """
    
    """
    total = 0
    for character in sentence:
        if character in "aeiouAEIOU":
            total += 1
    return total

print(count_vowel("Hello Python! Hello World!"))


# Case 3
def cal_score(score_list):
    """
        
    """
    max_score = max(score_list)
    min_score = min(score_list)
    avg_score = round(sum(score_list) / len(score_list), 1)

    return max_score, min_score, avg_score

