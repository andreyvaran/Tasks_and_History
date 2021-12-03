import csv


def get_table(market_path, billing_path):
    print("order_id,shop_name,shop_id,cost")
    try:
        with open(billing_path, 'r') as bt, open(market_path, 'r') as mt:
            billing_reader = csv.reader(bt)
            market_reader = csv.reader(mt)
            next(billing_reader)
            next(market_reader)
            try:
                billing = next(billing_reader)
                market = next(market_reader)
            except Exception as e:
                pass
            while market_reader and billing_reader:
                while int(billing[1]) != int(market[0]):
                    try:
                        if int(billing[1]) > int(market[0]):
                            market = next(market_reader)
                        elif int(billing[1]) < int(market[0]):
                            billing = next(billing_reader)
                    except Exception as e:
                        break
                else:
                    if market[1] is not None:
                        print(f"{billing[0]},{market[1]},{market[0]},{billing[2]}")
                try:
                    billing = next(billing_reader)
                except:
                    break
    except Exception as e:
        pass


if __name__ == '__main__':
    market_path, billing_path = input().split()
    get_table(market_path, billing_path)

'''
Во время проектирования распределенной системы планировалось использовать две различные базы данных.
 Разработчики не предусмотрели, что им может понадобится выполнять операцию сопоставления значений между таблицами этих баз данных. 
 Помогите им придумать, как выполнить операцию inner join.

База данных market и таблица market.shop представляет собой таблицу магазинов из двух колонок

shop_id - идентификатор магазина
shop_name - название магазина
База данных billing и таблица billing.order представляет собой таблицу заказов из трех колонок

order_id - идентификатор заказа
shop_id - идентификатор магазина для, который выполнил заказ
cost - общая стоимость товаров в заказе
Необходимо получить новую таблицу в которой будут следующие колонки:

order_id - номер заказа
shop_name - название магазина
shop_id - идентификатор магазина
cost - общая стоимость товаров в заказе'''
