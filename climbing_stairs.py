class Solution:
    def climbStairs(self, n: int) -> int:
        """Поднимаемся по ступенькам"""

        # База
        if n == 1:
            return 1  # (Одна ступенька - один шаг)
        if n == 2:
            return 2  # (Две ступеньки: 1+1, 2 - два шага)

        prev_1, prev_2 = 1, 2

        # Тут храним итоговый результат
        result: int = 0
        for _ in range(3,
                       n + 1):  # Цикл по ступенькам следующим, начинаем с лестницы в 3 ступеньки и заканчиваем на N+1
            # Считаем сумму 2 предыдущих значений, потому что закономерность такая, что результат следующей ступеньки
            # равен сложению двух предыдущих
            result = prev_1 + prev_2

            # После вычисления результата, обновляем prev_1 = prev_2
            prev_1 = prev_2

            # А prev_2 = result
            prev_2 = result

        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.climbStairs(5) == 8
