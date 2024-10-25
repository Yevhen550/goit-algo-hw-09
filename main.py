from typing import Dict, List
import time
import matplotlib.pyplot as plt


def find_coins_greedy(amount: int, coins: List[int]) -> Dict[int, int]:

    # Сортуємо монети за спаданням
    coins.sort(reverse=True)
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count

    return result


def find_min_coins(amount: int, coins: List[int]) -> Dict[int, int]:

    # Ініціалізація списку для зберігання
    # мінімальної кількості монет для кожної суми
    max_value = amount + 1
    min_coins = [max_value] * (amount + 1)
    min_coins[0] = 0

    # Відстежуємо, які монети використовуються
    # для досягнення мінімальної кількості
    coin_count = [{} for _ in range(amount + 1)]

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                if min_coins[a - coin] + 1 < min_coins[a]:
                    min_coins[a] = min_coins[a - coin] + 1
                    coin_count[a] = coin_count[a - coin].copy()
                    coin_count[a][coin] = coin_count[a].get(coin, 0) + 1

    # Якщо неможливо скласти суму, повертаємо порожній словник
    if min_coins[amount] == max_value:
        return {}

    return coin_count[amount]


def compare_algorithms(coins: List[int], max_amount: int):

    greedy_times = []
    dp_times = []
    amounts = range(1, max_amount + 1)

    for amount in amounts:
        # Вимірювання часу для жадібного алгоритму
        start_time = time.time()
        find_coins_greedy(amount, coins)
        greedy_times.append(time.time() - start_time)

        # Вимірювання часу для алгоритму динамічного програмування
        start_time = time.time()
        find_min_coins(amount, coins)
        dp_times.append(time.time() - start_time)

    # Побудова графіків для порівняння ефективності
    plt.figure(figsize=(12, 6))
    plt.plot(amounts, greedy_times, label="Жадібний алгоритм", linewidth=2)
    plt.plot(amounts, dp_times, label="Динамічне програмування", linewidth=2)
    plt.title("Порівняння часу виконання: жадібне та динамічне програмування")
    plt.xlabel("Сума до зміни")
    plt.ylabel("Час виконання (секунди)")
    plt.legend()
    plt.grid(True)
    plt.show()


# Приклади використання
coins = [50, 25, 10, 5, 2, 1]
test_amount = 113

# Використання жадібного алгоритму
greedy_result = find_coins_greedy(test_amount, coins)
print("Жадібний алгоритм Результат для 113:", greedy_result)

# Використання динамічного програмування
dp_result = find_min_coins(test_amount, coins)
print("Результат динамічного програмування для 113:", dp_result)

# Порівняння ефективності алгоритмів для сум від 1 до 1000
compare_algorithms(coins, 1000)
