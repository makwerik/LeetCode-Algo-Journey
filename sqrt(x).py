class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0

        # Число из которого извлекаем корень
        number = x

        # Начальное предположение какой корень у числа (может быть любым, например, само число)
        initial_approximation = number

        # Точность (когда разница между итерациями станет меньше этого значения, остановимся)
        accuracy = 0.01

        # Цикл для улучшения предположения
        while True:
            # Здесь у нас сохраняется старое предположение корня, чтобы потом его сравнить с новым предположением и
            # вычесть точность
            initial_approximation_old = initial_approximation

            # Формула Ньютона, вычисляющая предположение корня
            initial_approximation = 0.5 * (initial_approximation + number / initial_approximation)

            # Проверяем, отнимая от начального предположения "initial_approximation" старое
            if abs(initial_approximation - initial_approximation_old) < accuracy:
                return int(initial_approximation)


if __name__ == '__main__':
    sqrt = Solution()

    assert sqrt.mySqrt(8) == 2
    assert sqrt.mySqrt(9) == 3
