# Simple Flask App

## Zawartość repozytorium
* **main.py** / **hello_world**
* **Makefile**
* **Dockerfile**
* **.circleci/config.yml**
* **requirements.txt** / **test_requirements.txt**

## Uruchamianie Lokalne
1. Tworzenie srodowiska: `python -m venv .venv`
2. Aktywacja: `source .venv/bin/activate`
3. Instalacja: `pip install -r requirements.txt -r test_requirements.txt`
4. Uruchomienie aplikacji: `python main.py`
5. Uruchomienie testów: `PYTHONPATH=. py.test`
