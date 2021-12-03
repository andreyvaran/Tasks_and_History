import sys
import datetime
def get_errpr_time(input_path : str):
    result = -1
    with open('input.txt') as f:
        maxtime, n = map(int, f.readline().split())
        err_list_time = []
        for line in f:
            if 'ERROR' in line[22:28]:
                dtm_time_line = datetime.datetime.fromisoformat(line[1:20])
                i = 0
                while i != len(err_list_time):
                    if (dtm_time_line- err_list_time[i]).total_seconds() >= maxtime:
                        err_list_time.pop(i)
                    else:
                        break
                # add new time
                err_list_time.append(dtm_time_line)
                # result
                if (len(err_list_time) >= n ):
                    result = dtm_time_line
                    break
        return result

if __name__ == '__main__':
    print(get_errpr_time('input.txt'))
'''
В команде разработки бэкенда одной известной компании задумались об автоматическом информировании об ошибках в системе.
 Для этого необходимо реализовать программу, анализирующую логи выбранной машины и определяющую первый момент времени, ставший критическим.
Критическим называется такой момент времени K, что на промежутке [K−t+1;K] приизошло суммарно ошибок больше либо равно e.

Ошибками являются все сообщения, имеющие статус ERROR.'''