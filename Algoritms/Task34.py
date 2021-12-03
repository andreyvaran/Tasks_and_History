# Каждый из N школьников некоторой школы знает Mi языков. Определите,
# какие языки знают все школьники и языки, которые знает хотя бы один из школьников.





if __name__ == '__main__':
    n = int(input())
    all_know = None
    some_know = None
    for i in range(n):
        langs = int(input())
        temp = []
        for _ in range(langs):
            temp.append(input())
        if all_know :
            temp = set(temp)
            all_know = all_know.intersection(temp)
            some_know = some_know.union(temp)

        else :
            all_know = set(temp)
            some_know = set(temp)

    print(len(all_know))
    for i in all_know:
        print(i)
    print(len(some_know))
    for i in some_know:
        print(i)