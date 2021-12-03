import json
import requests
from operator import itemgetter


def write_json(new_dict, file_name):  # write_json(new_result, 'product.json')
    try:
        data = json.load(open(file_name))
    except:
        data = []

    data.append(new_dict)
    with open(file_name, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def sort_curricula(a):
    new_curricula = []
    j = {}

    for dic in a["curricula"]:  # lessonid, subjectname, teachername, roomname
        for les in a['lessons']:
            if dic['lessonid'] == les['id']:
                j['timeslot'] = list(
                    item for item in les['timeslot'][1:-1].split(','))  # какой-то петух сделал кортеж - строкой
        j['subjectname'] = dic['subjectname']
        j['teachername'] = dic['teachername']
        j['roomname'] = dic['roomname']
        new_curricula.append(j)
        j = {}

    new_curricula.sort(key=itemgetter('timeslot'))

    return new_curricula


def shedule_base():
    degree = 'https://schedule.sfedu.ru/APIv1/grade/list/'
    group = 'https://schedule.sfedu.ru/APIv1/group/forGrade/'
    shedule = 'https://schedule.sfedu.ru/APIv1/schedule/group/'

    result = requests.get(degree)
    course_list = json.loads(result.text)
    bachelor = {}
    master = {}
    postgraduate = {}

    for i in course_list:
        if 'bachelor' in i.values():
            bachelor[i['num']] = (i['id'])
        elif 'master' in i.values():
            master[i['num']] = (i['id'])
        else:
            postgraduate[i['num']] = (i['id'])
    for key, values in bachelor.items():
        result = requests.get(group + str(values))
        course_list = json.loads(result.text)
        c = []
        for i in course_list:
            result = requests.get(shedule + str(i['id']))
            curricula_list = json.loads(result.text)
            c.append({i['num']: sort_curricula(curricula_list)})
        bachelor[key] = c
    for key, values in master.items():
        result = requests.get(group + str(values))
        course_list = json.loads(result.text)
        c = []
        for i in course_list:
            result = requests.get(shedule + str(i['id']))
            curricula_list = json.loads(result.text)
            c.append({i['num']: sort_curricula(curricula_list)})
        master[key] = c
    for key, values in postgraduate.items():
        result = requests.get(group + str(values))
        course_list = json.loads(result.text)
        c = []
        for i in course_list:
            result = requests.get(shedule + str(i['id']))
            curricula_list = json.loads(result.text)
            c.append({i['num']: sort_curricula(curricula_list)})
        postgraduate[key] = c

    base = {'bachelor': bachelor,
            'master': master,
            'postgraduate': postgraduate}
    return base  # degree:course:group:shedule


base = shedule_base()
write_json(base, 'sfedu_base.json')
