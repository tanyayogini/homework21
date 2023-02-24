from exceptions import UserInputException


class Request:
    def __init__(self, req_str):
        req_list = req_str.lower().split(" ")
        self._deliver_from = req_list[4]
        self._deliver_to = req_list[6]
        self._amount = int(req_list[1])
        self._product = req_list[2]
        if self._deliver_to not in ("склад", "магазин") or self._deliver_from not in ("склад", "магазин"):
            raise UserInputException

    @property
    def deliver_from(self):
        return self._deliver_from

    @property
    def deliver_to(self):
        return self._deliver_to

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product
