# Case
student_grades = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)

for s in student_grades:
    total = sum(s[2:])
    avg = round(total / 3, 2)
    print(f"{s[1]}的总分为 {total}；平均分为 {avg:.1f}")

chinese_total_grades = 0
math_total_grades = 0
english_total_grades = 0

for i in student_grades:
    chinese_total_grades += s[2]
    math_total_grades += s[3]
    english_total_grades += s[4]


chinese_grades = [s[2] for s in student_grades]
math_grades = [s[3] for s in student_grades]
english_grades = [s[4] for s in student_grades]

print(f"语文最低分：{min(chinese_grades)}， 最高分：{max(chinese_grades)}， 平均分：{sum(chinese_grades)/len(chinese_grades)}")
print(f"数学最低分：{min(math_grades)}， 最高分：{max(math_grades)}， 平均分：{sum(math_grades)/len(math_grades)}")
print(f"英语最低分：{min(english_grades)}， 最高分：{max(english_grades)}， 平均分：{sum(english_grades)/len(english_grades)}")

for s in student_grades:
    total = sum(s[2:])
    avg = round(total / 3, 2)

    if avg > 90:
        print(f"{s[1]} 是优秀学生")



# Case_Modified
student_grades = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)

for id, name, chinese_grades, math_grades, english_grades in student_grades:
    total = chinese_grades + math_grades + english_grades
    avg = total / 3
    print(f"{id} {name}  {chinese_grades}  {math_grades}  {english_grades}  {total}  {avg : .1f}")
    