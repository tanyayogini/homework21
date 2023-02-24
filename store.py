from storage import Storage
from exceptions import StoreException


class Store(Storage):
    def __init__(self, items, capacity=100):
        self._items = items
        self._capacity = capacity

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def __repr__(self):
        result = "На складе хранится:\n"
        for item, key in self._items.items():
            result += f'{item} {key}\n'
        return result

    def add(self, title, quantity):
        if self.get_free_space() < quantity:
            print("Недостаточно места на складе")
            raise StoreException
        elif title in self._items:
            self._items[title] = self._items.get(title) + quantity
        else:
            self._items[title] = quantity

    def remove(self, title, quantity):
        if title not in self._items:
            print("Такого товара нет")
            raise StoreException
        elif self._items[title] < quantity:
            print("Товара не хватает, попробуйте заказать меньше")
            raise StoreException
        else:
            self._items[title] = self._items.get(title) - quantity
            if self._items[title] == 0:
                self._items.pop(title)

    def get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_unique_items_count(self):
        return len(self._items)
