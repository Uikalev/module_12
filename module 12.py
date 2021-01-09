print("Добрый день! Наша программа поможет вам определиться с банком для размещения депозита на год.")
print('На выбор представлены банки: "ТКБ", "СКБ", "ВТБ", "СБЕР" ')
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
percent = list(per_cent.values())
print("Ставка в каждом банке соотвественно: ")
print(percent)
money = int(input("Пожалуйста, введите сумму, которую вы планируете положить на счёт: "))
deposit=[]
deposit.append(int(money/100*float(percent[0])))
deposit.append(int(money/100*float(percent[1])))
deposit.append(int(money/100*float(percent[2])))
deposit.append(int(money/100*float(percent[3])))
print("Сумма депозита в каждом банке соответственно, составит:")
print(deposit)
print("Максимальная сумма, которую вы можете заработать — " + str(max(deposit)))

print("Таким образом мы рекомендуем вам ТКБ банк")



