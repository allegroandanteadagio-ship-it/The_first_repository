from typing import Any


class Stack:
    """Класс, реализующий структуру данных - stack."""

    def __init__(self):
        self._items: list[Any] = []

    def push(self, item):
        """Добавить в stack."""
        self._items.append(item)
        
    def pop(self):
        """Удалить последний элемент из stack."""
        return self._items.pop()
    
    def see_last_el(self):
        """Просмотр последнего элемента."""
        return self._items[-1]

    def len_stack(self):
        """Просмотр длины stack."""
        return len(self._items)
    

stack = Stack()
stack.push('Hi, Git')
stack.push('False')
stack.push('12500')
stack.push({
    "user": "helga"
})

print(stack.len_stack())
print(stack.pop())
print(f'{stack.see_last_el()}, длина стека - {stack.len_stack()}')
print(stack.len_stack())
stack.push('Последний элемент')
print(stack.len_stack())
