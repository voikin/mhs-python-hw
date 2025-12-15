from latex_generator import generate_table


def main():
    table_data = [
        ["Название", "Автор", "Год"],
        ["Война и мир", "Лев Толстой", "1869"],
        ["Преступление и наказание", "Фёдор Достоевский", "1866"],
        ["Мастер и Маргарита", "Михаил Булгаков", "1967"],
        ["Анна Каренина", "Лев Толстой", "1877"],
    ]

    latex_code = generate_table(table_data)

    output_file = "artefacts/table.tex"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(latex_code)


if __name__ == "__main__":
    main()
