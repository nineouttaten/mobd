import pandas as pd
import datetime
from PyQt5.QtWidgets import QMessageBox, QLabel
from dateutil.relativedelta import relativedelta

# Создание матрицы платежей
def payment_matrix(credit, payment, I, months):
    matrix = []
    S = credit
    new_date = datetime.datetime.today().date()
    for i in range(months - 1):
        new_date = new_date + relativedelta(months=+1)
        pc = int(S * I)
        main = payment - pc
        result_S = S - main
        matrix.append([new_date, S, payment, pc, main, result_S])
        S -= (payment - pc)
    new_date = new_date + relativedelta(months=+1)
    matrix.append([new_date, S, S, 0, S, 0])
    matrix = pd.DataFrame(matrix, index=[list(range(1, months + 1))], columns=["Date", "Sum", 'payment', "percent", "body", "Sum_after"])
    return matrix


matrix = payment_matrix(200000, 9415, 0.01, 24)
print("--------")
print(matrix.iloc[0, :])
