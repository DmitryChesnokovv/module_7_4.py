team1_num = 7
team2_num = 8
score_1 = 38
score_2 = 45
team1_time = 1200.76
team2_time = 1435.89
tasks_total = 90
time_avg = 48.7

# Использование %
print("В команде Мастера кода участников: %d !" % team1_num)
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

# Использование .format()
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {:.1f} с !".format(team2_time))

# Использование f-строк
print(f"Команды решили {score_1} и {score_2} задач.")

if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!")
