# расходы:
development_cost = 775
server_cost = 20 * 12
marketing_cost = 1000
all_expenses = development_cost + server_cost + marketing_cost

# доходы:
# среднее количество заказов в месяц
orders = 1450
# средняя цена желания
price = 55
# коммиссия системы
commission = 0.03
# отхват рынка в процентах по месяцам
market_coverage = {
    1: 2,
    2: 6,
    3: 10,
    4: 13,
    5: 20,
    6: 27,
    7: 35,
    8: 42,
    9: 50,
    10: 56,
    11: 57,
    12: 60,
}


def main():
    number_of_orders = [percent / 100 * orders for percent in market_coverage.values()]
    profit = [number * price * commission for number in number_of_orders]
    all_profit = sum(profit)

    lines = [
        '\tМесяц',
        '\t' + '\t'.join(f'{k}' for k in market_coverage.keys()),
        'Охват рынка, %\t' + '\t'.join(f'{v}' for v in market_coverage.values()),
        'Кол-во заказов\t' + '\t'.join(f'{int(i)}' for i in number_of_orders),
        'Прибыль, £\t' + '\t'.join(f'{int(p)}' for p in profit),
        'Прибыль инкр., £\t' + '\t'.join(f'{int(sum(profit[:i + 1]))}' for i in range(len(profit))),
        f'Общая прибыль, £\t{int(all_profit)}'
    ]
    print('\n'.join(lines))
    print()
    print(f'По статистике в Англии совершается {orders} заказов желаний в месяц - целевой рынок.'
          f'Медиана цены желания составляет {price} £.\n'
          f'Комиссия разрабатываемой системы от онлайн оплаты заказа составляет {commission}%, '
          f'то есть в среднем составляет {price * commission}£ с 1 заказа.')
    print()
    print(f'Итоговая прибыль за 1 год функционирования системы составит: '
          f'{int(all_profit)}-{int(all_expenses)}={int(all_profit - all_expenses)} (£).')


if __name__ == '__main__':
    main()
