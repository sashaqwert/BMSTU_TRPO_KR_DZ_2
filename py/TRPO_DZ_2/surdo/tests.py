"""
Код для ЛР №8 (в ДЗ-2 не используется)
"""

from django.test import TestCase
import surdo.models as models
import surdo.gateways as gateways
import surdo.table_module as table_module

# Create your tests here.


class TestUserCreate(TestCase):
    def setUp(self):
        pass  # Пустая БД

    def test_create(self):
        table_module.AppUserModule.insert(1, 'admin', 'Александр', 'Евгеньевич', 'Чиварзин')
        self.assertTrue(table_module.AppUserModule.check_exists(username='admin'))
        obj = models.AppUser.objects.get(id_user=1)
        self.assertEqual(obj.username, 'admin')
        self.assertEqual(obj.id_user, 1)

    def test_checkExists(self):
        self.assertFalse(table_module.AppUserModule.check_exists(1))

    def test_wrong_user(self):
        with self.assertRaises(ValueError):
            gateways.AppUserGateway.find_user(-5)  # Отрицательных ID не бывает


class TestUserModel(TestCase):
    def setUp(self):
        models.AppUser.objects.create(username='test', first_name='testF', middle_name='testM', last_name='testL')

    def test_str(self):
        self.assertContains(str(str(models.AppUser.objects.get(username='test'))), 'test')  # Подстрока в строке
