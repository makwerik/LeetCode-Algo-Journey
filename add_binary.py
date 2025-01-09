class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Находим длину самой длиной строки
        max_len = max(len(a), len(b))
        # Добавляем нули в строки, чтобы привести их к одной длине
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        # Переменная для переноса
        transfer = 0
        # Массив для хранения результата сложения
        result = []

        # Иду с конца строки к началу
        for s in range(max_len - 1, -1, -1):
            # Суммирую текущие цифры и перенос
            total = int(a[s]) + int(b[s]) + transfer
            # Остаток от деления на 2 помещаю в результат
            result.append(str(total % 2))
            # Перенос (целая часть от деления на 2)
            transfer = total // 2

        # Если после всех разрядов остался перенос, добавляем его
        if transfer:
            result.append('1')

        # Собираем результат, т.к цифры добавлялись в обратном порядке
        return ''.join(reversed(result))