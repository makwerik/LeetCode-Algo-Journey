class Solution:
    def romanToInt(self, s: str) -> int:

        integer_first = {
            "IV": 4,
            "VI": 6,
            "VII": 7,
            "VIII": 8,
            "IX": 9,
            "XII": 12,
            "XIII": 13,
            "XIV": 14,
            "XV": 15,
            "XVI": 16,
            "XVII": 17,
            "XVIII": 18,
            "XIX": 19,
            "XX": 20,
            "XXX": 30,
            "XL": 40,
            "LX": 60,
            "LXX": 70,
            "LXXX": 80,
            "XC": 90,
            "CM": 900,
            "CD": 400,
            "I": 1,
            "II": 2,
            "III": 3,
            "V": 5,
            "XI": 11,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        # Сразу ищем подходящие ключи, чтобы оптимизировать процесс
        keys_in_s_first = [k for k in integer_first if k in s]

        for k in keys_in_s_first:
            s = s.replace(k, f"{str(integer_first[k])},")

        integer = list(map(int, s.split(',')[:-1]))
        return sum(integer)