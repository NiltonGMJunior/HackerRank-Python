if __name__ == '__main__':
    students_by_score = {}
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score not in scores:
            scores.append(score)
            students_by_score[score] = [name]
        else:
            students_by_score[score].append(name)
    scores.sort()
    students_by_score[scores[1]].sort()
    for name in students_by_score[scores[1]]:
        print(name)