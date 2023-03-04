# Simpt backend

## установка
* `git clone https://github.com/G0-G4/simpt.git`
* `cd simpt`
* `python -m venv env`
* `source env/bin/activate` на linux и mac или  `env\Scripts\activate` на windows
* `pip install -r requirements.txt`
* `cd simpt`
* создать .env файл с содержимым: 
    ```
    SECRET_KEY=secret_key_example
    DEBUG=True
    ```
* `python manage.py migrate`

## Запуск
`python manage.py runserver`