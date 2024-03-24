"""
Скрипт для демонстрации паттерна "Наблюдатель".
Команда для запуска: python manage.py shell < AnswerMonitor.py
"""


def main():
    pass


if (__name__ == '__main__') or (__name__ == 'django.core.management.commands.shell'):
    main()
else:
    print(__name__)
