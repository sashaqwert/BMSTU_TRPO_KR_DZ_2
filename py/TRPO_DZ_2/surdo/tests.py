"""
Код для ЛР №8 (в ДЗ-2 не используется)
"""

from django.test import TestCase
import surdo.models as models
import surdo.gateways as gateways
import surdo.table_module as table_module

# Create your tests here.
class TestUser(TestCase):
    def setUp(self):
        pass  # Пустая БД

    def test_create(self):
        table_module.AppUserModule.insert(1, 'admin', 'Александр', 'Евгеньевич', 'Чиварзин')
        obj = models.AppUser.objects.get(id_user=1)
        self.assertEqual(obj.username, 'admin')
        self.assertEqual(obj.id_user, 1)
