"""
Скрипт для демонстрации паттерна "Наблюдатель".
Команда для запуска: python manage.py shell < AnswerMonitor.py
"""
from surdo.Observer import Subject, Observer


class AnswerObserver(Observer):
    def update(self, subject: Subject) -> None:
        from surdo.models import Answer
        from surdo.models import Answer
        count = Answer.objects.filter(answer_mark__isnull=True).count()
        print(f'Непроверенных ответов: {count}')


def main():
    from surdo.gateways import AnswerGateway

    ob = AnswerObserver()
    g = AnswerGateway(-1, 1, 1, "", 1)
    g.attach(ob)
    print('Нажмите CTRL + C для выхода')
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print('Наблюдение остановлено!')
    pass


def prepare():
    import os
    import django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TRPO_DZ_2.settings")
    django.setup()


if __name__ == '__main__':
    prepare()
if (__name__ == '__main__') or (__name__ == 'django.core.management.commands.shell'):
    main()
else:
    print(__name__)
