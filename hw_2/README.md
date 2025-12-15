# 2.1

- была создана директория (модуль) `hw_2/latex_generator` в которой реализован файл `hw_2/latex_generator/latex_generator.py` с функциями для генерации таблицы
- в корне был реализован `hw_2/generate_table.py` с генерацией таблицы, используя созданный модуль
- результат генерации таблицы был записан в `hw_2/artefacts/table.tex`
- полученная таблица была вставлена в тестовый документ overleaf и отрендерена
- скриншот с резуальтатом предоставлен в `hw_2/artefacts/overleaf_demo.png`


# 2.2

- в корне репозитория была создана дополнительная директория `latex-generator`, куда переехал модуль `hw_2/latex_generator`
- файл `latex-generator/latex_generator/latex_generator.py` был расширен функцией для генерации картинки
- проинициализован файл `latex-generator/pyproject.toml`
- библиотека была собрана и опубликована в pypi под названием `latex-generator-dazaii` (что именно происходило находится в `hw_2/artefacts/package_uploading.txt`)
- в корне был проинициализирован poetry пакет с помощью `poetry init`
- была установлена наша библиотека `latex-generator-dazaii`
- создан скрипт `hw_2/generate_pdf.py`, который использует установленную библиотеку для генерации PDF с таблицей и картинкой - в нем генерируется .tex файл, сохраняется во временную директорию, а затем он используется утилитой `pdflatex` для генерации самого pdf
- для генерации PDF запускаем `poetry run generate_pdf.py`
- результат - `hw_2/artefacts/document.pdf`


# 2.3

- создан `hw_2/Dockerfile` для автоматизации процесса генерации PDF
- Dockerfile устанавливает все необходимые зависимости: Python, LaTeX дистрибутив (TeX Live), библиотеку `latex-generator-dazaii` из PyPI
- создан `hw_2/docker-compose.yml` для более удобного запуска контейнера
- запускаем сборку с помощью `docker compose up --build`
- получаем такой же, как и в прошлом задании, файл `hw_2/artefacts/document.py`
