### Описание проекта:
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

### Установка и запуск:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Elijah-iSO/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Инициализация БД и создание миграций:
```
flask db init
```

```
flask db migrate
```

Запустить проект:

```
flask run
```

### .env:
```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=q1w2e3r4
```

### Author:
ILYA OLEYNIKOV
GitHub:	https://github.com/Elijah-iSO
E-mail: oleynikovis@yandex.ru
