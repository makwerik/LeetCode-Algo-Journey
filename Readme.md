# Решение алгоритмов с LeetCode

Всем привет! 

Этот репозиторий создан для того, чтобы решать задачи с LeetCode самостоятельно и более глубоко прокачать свои навыки работы с алгоритмами. Это мой второй репозиторий, где я планирую решить задачи своими силами. 

Первый репозиторий я также вел сам, но иногда обращался за помощью. В этот раз решил более основательно работать над задачами, применяя исключительно свои знания и навыки. 

Здесь я буду делиться своими решениями: скриншотами выполненных задач и самим кодом. Надеюсь, это поможет мне лучше разобраться в алгоритмах и поделиться опытом с другими.

### Возможные обновления

Возможно, обновления в репозитории будут появляться не очень часто. Это связано с тем, что мои текущие навыки в решении алгоритмов ещё требуют улучшения. Также основная работа и занятость отнимают значительную часть времени, поэтому прогресс может идти медленнее, чем хотелось бы. Но я буду стараться регулярно решать задачи и делиться ими здесь.

### Как использовать
- Откройте файлы с кодом, чтобы увидеть мои решения задач с LeetCode.
- В директории `result/` также находятся скриншоты успешных решений.

Оставайтесь на связи и следите за обновлениями!

### Пример задачи: [Two Sum](https://github.com/makwerik/LeetCode-Algo-Journey/blob/master/two_sum.py)

![Two Sum](result/Two%20Sum.png)

### Пример задачи: [Palindrome Number](https://github.com/makwerik/LeetCode-Algo-Journey/blob/master/palindrome_number.py)
Задача может быть сложно читаемая, так как я пытался оптимизировать скорость выполнения с 60ms до 46ms хотя бы<br>
Изначально решение было более читаемым
![Palindrome Number](result/Palindrome%20Number.png)


### Пример задачи: [Roman to Integer](https://github.com/makwerik/LeetCode-Algo-Journey/blob/master/roman_to_integer.py)
Решение задачи пришло ночью, в момент когда я засыпал. А так два дня велась безуспешная борьба, не на жизнь, а на смерть
![Roman to Integer](result/Roman%20to%20Integer.png)

### Пример задачи: [Longest Common Prefix](https://github.com/makwerik/LeetCode-Algo-Journey/blob/master/longest_common_prefix.py)
Я особенно горжусь решением этой задачи, потому что оно выполняется за минимальное время, хотя по памяти не выигрывает. Однажды, поздно ночью, лежа в кровати, я задумался о том, чем руководствуюсь, когда мысленно решаю задачу без использования кода. Я проанализировал свои логические шаги и понял, как именно нахожу решение, просто глядя на данные.
Сначала я мысленно определяю количество строк в списке. Затем беру символ из первой строки и поочередно сравниваю его с символами на тех же позициях в остальных строках. Если символ совпадает во всех строках, я запоминаю его и перехожу к следующему символу. Если хотя бы в одной строке символ не совпадает, то нет смысла продолжать проверку, и я отбрасываю его.
После этого остается лишь вывести те символы, которые я запомнил. В данном случае счётчиком выступает переменная count, которая соответствует длине списка.
Этот процесс можно назвать ментальной моделью решения задачи, где я сознательно выстраиваю в голове последовательность шагов, основанных на логике и наблюдениях, чтобы прийти к правильному решению.
![Longest Common Prefix](result/Longest%20Common%20Prefix.png)

### Пример задачи: [Valid Parentheses](https://github.com/makwerik/LeetCode-Algo-Journey/blob/master/valid_parentheses.py)
Данная задача мне далась достаточно сложно, т.к я не понимал примерной хотя бы логики решения.
Но я помнил, что раньше в этой задаче я использовал стек, но всё равно мне это не помогло сейчас, в итоге я решил просто
почитать статьи (без готового кода) и после прочтения первых пары строк я понял принцип, сейчас я его опишу:
Я создал словарь где ключами были закрывающие скобки, а значения открывающие. Дальше создал стек. После этого в цикле начал
проходить и если данный символ находился в значениях моего словаря, значит скобка открывающая и я помещал её в стек и через
continue шел дальше по строке, как только я встречал скобку которой нет в значениях словаря - значит она закрывающая, и если 
стек не пустой я проверял совпадает ли значение ключа закрывающей скобки со значением которое я возвращал через метод "pop",
если да, то снова через continue я шел дальше по строке, если не совпадали - значит нарушена структура скобок и возвращаем False.
Ну и в самом конце, после цикла я проверял стек, если он пустой return True else False
![Valid Parentheses](result/Valid%20Parentheses.png)
