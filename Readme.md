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

### Пример задачи: [Merge Two Sorted Lists](https://github.com/makwerik/LeetCode-Algo-Journey/blob/master/merge_two_sorted_lists.py)
Долго меня не было на литкоде, сегодня появилось время и решил сразу же зайти порешать задачки.
Тут пришлось обратиться за помощью, так как я не понимал, что именно тут нужно сделать.
Оказывается ListNode не является итерируемым, а вместо этого он содержит значение (val) и ссылку на следующий узел (next).
Мне это объяснили на примере поездов с вагончиками, что-то вроде отложилось в голове, но всё равно с нуля без помощи я так быстро это не решу
![Valid Parentheses](result/Merge%20Two%20Sorted%20Lists.png)

### Пример задачи: [Remove Duplicates from Sorted Array](https://github.com/makwerik/LeetCode-Algo-Journey/blob/master/remove_duplicates_from_sorted_array.py)
Сначала долго не мог понять, что не так в моём решении, когда я просто убрал дубликаты из списка.
Оказывается нужно убирать дубликаты изменяя сразу имеющийся список, не создавая новый. Буду честен с идеей возможной реализации мне дали совет: "Использовать курсоры, чтобы работать с индексами".
Поэтому суть моего решения оказалась таковой: 
- Я создал курсор 'j', который отвечает за последний уникальный элемент в списке, изначально его значение равно 0, так как первый элемент в списке всегда уникален.
- Дальше в цикле через 'range' я проходился по списку 'nums', начало цикла было с первого индекса, так как нулевой уже определён.
- В теле цикла реализована проверка, если значение <code>'nums[j] == nums[j]'</code>, то делать ничего не нужно и мы пропускаем эту итерацию при помощи 'continue'
- Если значения не равны, значит мы поймали уникальное число (в данном случае). Мы инкрементируем значение 'j'
- После инкрементации мы выполняем замену чисел по индеку <code> nums[j] = nums[i]</code>.
- Тем самым если наше значение <code>j=1</code> мы обращаемся по этому индексу к nums и присваиваем ему значение <code>nums[i]</code>
![Valid Parentheses](result/Remove%20Duplicates%20from%20Sorted%20Array.png)


### Пример задачи: [Remove Element](https://github.com/makwerik/LeetCode-Algo-Journey/blob/master/remove_element.py)
В общем эта задача похожа на предыдущую, используется только другой подход немного.
- Создал курсор k - указывающий кол-во так же уникальных элементов, так же в будущем он нам пригодится, чтобы уникальные значения сохранять в начале списка.
- В цикле проходимся по длине массива по индексам, если значение уникально, то записываем его в начало списка, благодаря нашему курсору и инкрементируем его.
- Потом можно сделать вывод по срезу, чтобы получить все значения, кроме таргета <code>nums = nums[:k]</code> ( но я решил это опустить, так как все тесты прошли на литкоде)
![Remove Element](result/Remove%20Element.png)

### Пример задачи: [Find the Index of the First Occurrence in a String](https://github.com/makwerik/LeetCode-Algo-Journey/blob/master/find_the_index_of_the_first_occurrence_in_a_string.py)
Туу объяснения не нужны, я так думаю))
![Find the Index of the First Occurrence in a String](result/Find%20the%20Index%20of%20the%20First%20Occurrence%20in%20a%20String.png)


### Пример задачи: [Search Insert Position](https://github.com/makwerik/LeetCode-Algo-Journey/blob/master/search_insert_position.py)
![Search Insert Position](result/Search%20Insert%20Position.png)

### Пример задачи: [Length of Last Word](https://github.com/makwerik/LeetCode-Algo-Journey/blob/master/length_of_last_word.py)
В этой задаче я использовал два подхода:
Первый:
- Убрал лишние пробелы 
- Засплитил строку по пробелам, чтобы сформировать список 
- Нашел длину последнего индекса в списке

- Второй:
- Так же убрал лишние пробелы
- Отказался от сплита, чтобы разгрузить код
- Т.к мы знаем, что работаем только с последним словом, запускаем цикл по перевёрнутой строке, с помощью метода reversed
- Если встречаем пробел - цикл останавливается
- Иначе через счётчик count считаем какая длинна строки

![Length of Last Word](result/Length%20of%20Last%20Word.png)

### Пример задачи: [Add Binary](https://github.com/makwerik/LeetCode-Algo-Journey/blob/master/add_binary.py)
Пажалуста не задавайте вопросов по этой задаче, мне пришлось обращаться за помощью)
Потому что по в двоичном коде я слаб, но я примерно понял суть, что сначала складываются числа малого разряда
Например a="11", b="01"
1 + 1 = 10 - единицу переносим, сохраняем ноль
1 + 0 + 1(который ушел в перенос) = 10 - единицу переносим, сохраняем ноль
В итоге у нас есть два нуля и остался перенос в виде единички, добавляем его в конец строки, т.к шли с конца строки и
разворачиваем её, получая 100

![Length of Last Word](result/Add%20Binary.png)


### Пример задачи: [Plus One](https://github.com/makwerik/LeetCode-Algo-Journey/blob/master/plus_one.py)
![Plus One](result/Plus%20One.png)

### Пример задачи: [Sqrt(x)](https://github.com/makwerik/LeetCode-Algo-Journey/blob/master/sqrt(x).py)
В математике я не силён, поэтому пришлось сначала обратиться к гуглу, яндексу, чтобы понять как вычислить корень, без 
встроенных методов python.
Затем пришлось просить уважаемый ИИ объяснить мне формулу для поиска корня.
В итоге я понял, что:
1. Сначала мы определяем число, для которого нужно вычислить корень
2. Выбираем наше предположение, какой может быть ответ (проще взять это же число)
3. Указываем точность, при достижении которой нужно закончить цикл
4. Запускаем цикл
5. В цикле создаём переменную для хранения старого предположения (обновляем его из пункта 2)
6. Потом высчитываем по формуле новое предположение и сохраняем в (пункт 2)
7. Отнимаем от старого предположения (пункт 5) - (пункт 2)
8. Если (пункт 3) не достигнут продолжаем цикл
![Sqrt(x)](result/SqrtX.png)

### Пример задачи: [Climbing Stairs](https://github.com/makwerik/LeetCode-Algo-Journey/blob/master/climbing_stairs.py)
_Закрепляю материал, так как вероятность встретить подобную задачу в будущем невысока._

## Условие
У нас есть **лестница (N ступенек)**, и мы можем подниматься либо **на 1 ступеньку**, либо **сразу на 2**.

## Логика решения
Количество способов дойти до `n`-й ступеньки можно найти, **сложив два предыдущих результата**.

### Примеры:
- **Для `n = 3`**: складываем `n = 1` и `n = 2` .  
  **Результат: `3` комбинации.**
- **Для `n = 4`**: складываем `n = 2` и `n = 3`, получая **`5` комбинаций**.

## Как это работает в коде?
1. **Определяем две переменные** `prev_1` и `prev_2`, которые хранят количество способов для лестницы с 1 и 2 ступеньками `prev_1 = 1` и `prev_2 = 2`.
2. **Запускаем цикл** от `3` до `N+1`, вычисляя количество способов для каждой новой ступеньки.
3. В каждой итерации **находим новый результат**, складывая `prev_1 + prev_2`.
4. **Обновляем переменные**:
   - `prev_1 ← prev_2`
   - `prev_2 ← result`
5. **После выхода из цикла `prev_2` содержит итоговый ответ**.

Но я возвращаю переменную `result` :D
![Climbing Stairs](result/Climbing%20Stairs.png)






