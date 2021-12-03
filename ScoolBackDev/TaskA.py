import json


def get_result():
    lines = []
    while True:
        line = input()
        lines.append(line)
        if line[-1] == "]":
            break
    text = '\n'.join(lines)
    if len(text) < 22:
        result = []
    else:
        input_data = json.loads(text)
        input_data = sorted(input_data, key=lambda inp: (inp["order_id"], inp["item_id"], inp["event_id"]))

        index = 0
        size = len(input_data)

        while index != size - 1:
            if input_data[index]['order_id'] == input_data[index + 1]['order_id'] and \
                    input_data[index]['item_id'] == input_data[index + 1]['item_id']:
                input_data.pop(index)
                size -= 1
            else:
                index += 1

        result = []

        if len(input_data) > 1:
            items_temp = []
            order = input_data[0]['order_id']
            for i in range(len(input_data) - 1):
                if input_data[i + 1]['order_id'] == order:
                    if input_data[i]['status'] == "CANCEL":
                        continue
                    if input_data[i]['count'] - input_data[i]['return_count'] > 0:
                        items_temp.append({"count": input_data[i]['count'] - input_data[i]['return_count'],
                                           "id": input_data[i]["item_id"]})
                else:
                    if input_data[i]['status'] != "CANCEL" and input_data[i]['count'] - input_data[i][
                        'return_count'] > 0:
                        items_temp.append({"count": input_data[i]['count'] - input_data[i]['return_count'],
                                           "id": input_data[i]["item_id"]})
                    if items_temp:
                        result.append({"id": input_data[i]["order_id"], "items": items_temp})
                    items_temp = []
                    order = input_data[i + 1]['order_id']

            if input_data[-1]['status'] != "CANCEL" and input_data[-1]['count'] - input_data[-1]['return_count'] > 0:
                items_temp.append({"count": input_data[-1]['count'] - input_data[-1]['return_count'],
                                   "id": input_data[-1]["item_id"]})
            if items_temp:
                result.append({"id": input_data[-1]["order_id"], "items": items_temp})

        elif len(input_data) == 1:
            if input_data[0]['status'] != "CANCEL" and input_data[0]['count'] - input_data[0]['return_count'] > 0:
                result.append({"id": input_data[0]["order_id"],
                               "items": [{"count": input_data[0]['count'] - input_data[0]['return_count'],
                                          "id": input_data[0]["item_id"]}]})

    return json.dumps(result)


if __name__ == '__main__':
    print(get_result())

'''Одной из важных частей онлайн-магазинов является обработка заказов. Заказ содержит в себе несколько товаров, каждый из которых приобретается в определенном количестве.

Но состав заказа не является строго фиксированным с момента оформления до момента фактической отправки заказчику.
Пользователь может передумать покупать какой-либо товар (весь или частично) или, наоборот, решить увеличить количество какого-либо товара в заказе перед отправкой. В итоге может получиться даже так, что заказ в итоге нет смысла отправлять, так как в нём не осталось товаров.

Всё, что происходит с заказами в системе, фиксируется в формате событий "после изменения event_id в заказе order_id итоговое заказанное количество товара item_id равно count, а итоговое отмененное количество равно return_count". В итоге реальное количество товаров для отправки может быть вычислено как разница между count и return_count. Разница может получиться отрицательной - в рамках данной задачи это равносильно разнице, равной нулю (в причинах расхождения количеств в событии будет заниматься другой отдел).

Также у товара в заказе есть статус - OK или CANCEL.
Это независимая от количества товара информация, обозначающая возможность отправки товара в данном заказе - если товар находится в статусе CANCEL,
 то его не надо отправлять, сколько бы штук товара не требовалось. Важно отметить, что статус CANCEL может сменить на OK в дальнейшем - к примеру, 
 на складе появилась новая партия товара.
 
Вам требуется обработать список событий и вывести для каждого заказа итоговый список товаров для отправки. 
Для каждого товара необходимо учитывать только последнее событие (событие с максимальным значением event_id) среди событий, содержащих информацию о данном товаре.
 Если итоговый статус товара - CANCEL, то он не должен попасть в заказ.
 В заказ должны попасть только товары с ненулевым итоговым количеством для отправки.
 Выводить необходимо только заказы, в которых содержится хотя бы один товар для отправки.'''
