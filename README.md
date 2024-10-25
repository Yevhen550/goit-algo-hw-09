# goit-algo-hw-09

# ВИСНОВКИ :

-- Жадібний алгоритм (Greedy Algorithm) працює дуже швидко та показує стабільно
низький час виконання для різних сум. Це очікувано, оскільки алгоритм просто
обирає найбільший доступний номінал поки не завершить обчислення,
що робить його O(n), де n — кількість номіналів монет.

-- Алгоритм динамічного програмування (Dynamic Programming) трохи повільніший
і має коливання у часі виконання залежно від суми. Це пов'язано з тим,
що алгоритм обчислює оптимальну кількість монет для кожної суми від 1 до заданої,
що вимагає більше обчислень. Його складність O(n \* m),
де n — кількість номіналів, а m — сума, яку потрібно скласти.

# Загальний Висновок :

Жадібний алгоритм дуже ефективний для реальних ситуацій, коли номінали монет
дозволяють отримати оптимальне рішення (як у нашому випадку з монетами 50, 25, 10, 5, 2, 1).
Алгоритм динамічного програмування буде кращим, якщо набір номіналів
не дозволяє отримати мінімальну кількість монет за допомогою жадібного підходу.
Це важливо для більш специфічних ситуацій з нестандартними номіналами.
