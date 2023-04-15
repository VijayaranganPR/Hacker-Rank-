if __name__ == '__main__':
    nested_list = []
    score_set = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name, score])
        score_set.add(score)
        
    score_set.remove(min(score_set))
    for i in sorted(filter(lambda x: x[1] == min(score_set), nested_list)):
        print(i[0])
    