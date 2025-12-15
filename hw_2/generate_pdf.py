from latex_generator import generate_table, generate_image
import subprocess


def main():
    table_data = [
        ["Title", "Author", "Year"],
        ["War and Peace", "Leo Tolstoy", "1869"],
        ["Crime and Punishment", "Fyodor Dostoevsky", "1866"],
        ["The Master and Margarita", "Mikhail Bulgakov", "1967"],
        ["Anna Karenina", "Leo Tolstoy", "1877"],
    ]

    table_tex = generate_table(table_data)

    image_tex = generate_image(
        "artefacts/itmo.png"
    )

    full_tex = f"""
\\documentclass{{article}}
\\usepackage{{graphicx}}

\\begin{{document}}

\\section*{{Books table}}

{table_tex}

\\section*{{Image}}

{image_tex}

\\end{{document}}
"""

    output_file = "/tmp/document.tex"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(full_tex)

    subprocess.run(
            ["pdflatex", "--output-directory=artefacts", "-interaction=nonstopmode", output_file],
            capture_output=True,
            text=True,
            cwd="."
        )


if __name__ == "__main__":
    main()

