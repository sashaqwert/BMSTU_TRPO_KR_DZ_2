"""
Скрипт для демонстрации паттерна "Наблюдатель".
Команда для запуска: python manage.py shell < AnswerMonitor.py
"""
from surdo.Observer import Observer, Subject
from surdo.models import Answer


class AnswerObserver(Observer):
    def update(self, subject: Subject) -> None:
        count = Answer.objects.filter(answer_mark__isnull=True).count()
        print(f'Непроверенных ответов: {count}')


def main():
    ob = AnswerObserver()
    pass


if (__name__ == '__main__') or (__name__ == 'django.core.management.commands.shell'):
    main()
else:
    print(__name__)
