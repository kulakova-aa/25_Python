money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов



months = 0
budget = money_capital
monthly_spend = spend

while budget >= monthly_spend:
    budget += salary - monthly_spend
    months += 1
    monthly_spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", months)