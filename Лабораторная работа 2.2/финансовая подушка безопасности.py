money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count_month = 0
while True:
    expend_ = spend - salary
    if expend_ > money_capital:
        break
    count_month += 1
    money_capital -= expend_
    spend += spend * increase


print("Количество месяцев, которое можно протянуть без долгов:", count_month)

