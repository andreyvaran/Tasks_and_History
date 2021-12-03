import heapq
from functools import total_ordering


@total_ordering
class Cash_Data:

    def __init__(self, id='name', time=0):
        self.id = id
        self.time = time

    def __gt__(self, other):
        return self.time > other.time

    def __eq__(self, other):
        return self.time == other.time

    def __lt__(self, other):
        return self.time < other.time

    def get_time(self):
        return self.time

    def get_id(self):
        return self.id

    def __repr__(self):
        return " id:%s - time:%s" % (self.id, self.time)


def print_cash(n: int, size_cash: int):
    tmp_heap = []
    heapq.heapify(tmp_heap)
    glob_iter = 1
    temp_name = []
    for i in range(n):
        tmp = input().split()
        cur_data = Cash_Data(tmp[0], int(tmp[1]))
        # UPDATE
        try:
            index = temp_name.index(cur_data.id)
        except Exception as e:
            index = -1

        if index != -1:
            if tmp_heap[index].time < cur_data.time:
                tmp_heap[index].time = cur_data.time
                print(str(glob_iter) + " UPDATE " + cur_data.id)
                heapq.heapify(tmp_heap)
                temp_name = list(map(lambda data: data.id, tmp_heap))
        else:
            # PUT
            if len(tmp_heap) < size_cash:
                heapq.heappush(tmp_heap, cur_data)
                temp_name = list(map(lambda data: data.id, tmp_heap))
                print(str(glob_iter) + " PUT " + cur_data.id)
            # DELETE
            else:
                if tmp_heap[0].time < cur_data.time:
                    tmp = heapq.heappop(tmp_heap)
                    heapq.heappush(tmp_heap, cur_data)
                    print(str(glob_iter) + " DELETE " + tmp.id)
                    print(str(glob_iter) + " PUT " + cur_data.id)
                    temp_name = list(map(lambda data: data.id, tmp_heap))

        glob_iter += 1


if __name__ == '__main__':
    n, size_cash = map(int, input().split())
    print_cash(n, size_cash)

'''
Get time limit error

Вам предлагается смоделировать алгоритм кэширования, при котором в памяти хранится информация о m наиболее поздних по времени вызова запросах. 
Важной деталью является тот факт, что порядок получения кэшом информации о запросах необязательно совпадает с порядком их вызова.
Для работы с кэшем есть 3 типа операций:

PUT  — положить информацию о запросе в кэш (если запроса нет в кэше).
UPDATE  — обновить информацию о запросе (если запрос уже есть в кэше).
DELETE  — удалить информацию о запросе из кэша, если необходимо освободить место.
Необходимо обработать список запросов и вывести список совершенных с кэшом операций, чтобы в любой момент соблюдались следующие условия:

Хранимые в кэше запросы являются наиболее поздними по времени вызова среди уже обработанных.
Количество запросов в кэше не превосходит m.
Для каждого идентификатора запроса в кэше хранится самая поздняя по времени вызова информация.
Операция PUT применяется только к запросам, которых нет в кэше на момент совершения операции, а UPDATE - только к уже находящимся в кэше
'''
