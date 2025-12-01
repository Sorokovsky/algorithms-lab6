from typing import TypeVar, Generic, Callable

TKey = TypeVar('TKey')
TValue = TypeVar('TValue')


class Database(Generic[TKey, TValue]):
    items: dict[TKey, TValue]

    def __init__(self):
        self.items = {}

    def has_by_key(self, key: TKey) -> bool:
        return key in self.items.keys()

    def add_item(self: "Database[TKey, TValue]", key: TKey, value: TValue) -> None:
        if self.has_by_key(key):
            print(f"Елемент вже існує за ключем {key}, тому не доданий.")
        else:
            self.items[key] = value

    def remove_item(self: "Database[TKey, TValue]", key: TKey) -> None:
        if self.has_by_key(key):
            del self.items[key]
        else:
            print(f"Елемента за ключем {key} не існує.")

    def loop(self: "Database[TKey, TValue]", callback: Callable[[TKey, TValue, int], None],
             is_sorted: bool = False) -> None:
        i = 0
        keys = self.items.keys()
        if is_sorted:
            keys = sorted(keys)

        for key in keys:
            callback(key, self.items[key], i)
            i += 1
