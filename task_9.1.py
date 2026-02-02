import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books (1).csv", encoding="utf-8")

data_2023 = df[df["Год"] == 2023]
data_2024 = df[df["Год"] == 2024]

def plot_books_2023(data):
    plt.plot(
        data["Месяц"],
        data["Книги"],
        marker='o',
        color='red',
        label='Прочитано книг'
    )
    plt.title("Прочитанные книги 2023")
    plt.xlabel("Месяцы")
    plt.ylabel("Количество книг")
    plt.grid(True)
    plt.legend()

def plot_pages_2024(data):
    plt.bar(
        data["Месяц"],
        data["Страницы"],
        color='green',
        label='Прочитано страниц'
    )
    plt.title("Прочитанные страницы 2024")
    plt.xlabel("Месяцы")
    plt.ylabel("Количество страниц")
    plt.grid(True)
    plt.legend()

plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
plot_books_2023(data_2023)

plt.subplot(1, 2, 2)
plot_pages_2024(data_2024)

plt.tight_layout()
plt.show()