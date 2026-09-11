# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "通天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = { "通天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# Case 1
print(french_set.intersection(football_set))
inter_set = french_set & football_set
print(inter_set)

# Case 2
#print(football_set.intersection(basketball_set.intersection(french_set.intersection(art_set))))
all_set = football_set & basketball_set & french_set & art_set
print(all_set)

# Case 3
print(football_set.difference(basketball_set))

difference_set = football_set - basketball_set
print(difference_set)

difference_set = {s for s in football_set if s not in basketball_set}
print(difference_set)

# Case 4
number_of_football = len(football_set)
number_of_basketball = len(basketball_set)
number_of_french = len(french_set)
number_of_art = len(art_set)

print(f"足球：{number_of_football}")
print(f"篮球：{number_of_basketball}")
print(f"法语：{number_of_french}")
print(f"艺术：{number_of_art}")


# Case 5
all_students = football_set.union(basketball_set).union(french_set).union(art_set)
all_students_2 = football_set | basketball_set | french_set | art_set

all_enrol_list = [*football_set, *basketball_set, *french_set, *art_set]
print(all_enrol_list)

for std in all_students:
    print(f"{std} 选修了 {all_enrol_list.count(std)} 门课程")