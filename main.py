from store import Store
from shop import Shop
from request import Request
from exceptions import StoreException, ShopException, UserInputException

store = Store({"печеньки": 3, "собачки": 3, "котики": 5, "книги": 10, "булки": 15, "пирожки": 10}, 50)
shop = Shop({"печеньки": 5}, 10)
storage_list = {'склад': store, 'магазин': shop}


def main():
    print(store)
    print(shop)
    while True:
        req = input('Введите запрос в формате "Доставить 3 печеньки из склад в магазин". '
                    'Для выходы введите стоп\n')
        if req.lower() == 'стоп':
            break

        """ Формируем экземпляр класса Request на основе запроса пользователя. 
        Для проверки запроса использованы исключения: 
        ValueError - в случае если в нужном месте не указано количество (int).
        IndexError - если в строке меньше слов, чем требуется для запроса.
        UserInputException - исключение на случай, если в нужных местах строки 
        не оказалось слов "склад", "магазин"""

        try:
            request = Request(req)
        except (ValueError, IndexError, UserInputException):
            print("Неправильно введенный запрос")
            continue

        """Выполняем запрос пользователя. Если что-то из условий задачи не выполняется - 
        выбрасывается исключение. Смотрим, на каком этапе возникло исключение. 
        Если это второй этап (доставки) - возвращаем товар назад"""

        try:
            storage_list[request.deliver_from].remove(request.product, request.amount)
            storage_list[request.deliver_to].add(request.product, request.amount)
            print(f"Нужное количество есть в {request.deliver_from}\n"
                  f"Курьер забрал {request.amount} {request.product} со {request.deliver_from}\n"
                  f"Курьер везет {request.amount} {request.product} со {request.deliver_from} "
                  f"в {request.deliver_to}\nКурьер доставил {request.amount} {request.product} "
                  f"в {request.deliver_to}.\n")
            print(store)
            print(shop)

        except StoreException:
            if request.deliver_from == 'магазин':
                storage_list[request.deliver_from].add(request.product, request.amount)
                continue

        except ShopException:
            if request.deliver_from == 'склад':
                storage_list[request.deliver_from].add(request.product, request.amount)
                continue


if __name__ == "__main__":
    main()
