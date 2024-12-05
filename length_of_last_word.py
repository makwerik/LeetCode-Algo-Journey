class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Убиваю лишние пробелы в начале и в конце строки
        s = s.strip()
        # Запускаю цикл по перевёрнутой строке
        count = 0
        for char in reversed(s):
            # Если встречаем пробел, выходим из цикла
            if char == " ":
                break
            # Иначе считаем длину строки
            count += 1
        return count
