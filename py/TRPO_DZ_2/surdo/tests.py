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
        # AppUser.__str__()
        self.assertEqual(str(str(models.AppUser.objects.get(username='test'))), 'AppUser{id_user=1, username=test}')

    def test_attrs(self):
        u = models.AppUser.objects.get(username='test')
        self.assertEqual(u.first_name, 'testF')
        self.assertEqual(u.middle_name, 'testM')
        self.assertEqual(u.last_name, 'testL')
        self.assertEqual(u.username, 'test')
        self.assertEqual(u.id_user, 1)


class TestAppUserGateway(TestCase):
    def setUp(self):
        models.AppUser.objects.create(username='test', first_name='testF', middle_name='testM', last_name='testL')

    def test_get_attrs(self):
        ug = gateways.AppUserGateway.find_user(1)
        self.assertEqual(ug.get_id(), 1)
        self.assertEqual(ug.get_first_name(), 'testF')
        self.assertEqual(ug.get_middle_name(), 'testM')
        self.assertEqual(ug.get_last_name(), 'testL')
        self.assertEqual(ug.get_username(), 'test')

    def test_set_first_name(self):
        ug = gateways.AppUserGateway.find_user(1)
        ug.set_first_name('changedF')
        self.assertEqual(ug.first_name, 'changedF')

    def test_set_middle_name(self):
        ug = gateways.AppUserGateway.find_user(1)
        ug.set_middle_name('changedM')
        self.assertEqual(ug.middle_name, 'changedM')

    def test_set_last_name(self):
        ug = gateways.AppUserGateway.find_user(1)
        ug.set_last_name('changedL')
        self.assertEqual(ug.last_name, 'changedL')

    def test_set_username(self):
        ug = gateways.AppUserGateway.find_user(1)
        ug.set_username('changedU')
        self.assertEqual(ug.username, 'changedU')

    def test_str(self):
        ug = gateways.AppUserGateway.find_user(1)
        self.assertEqual(str(ug), 'test')

    def test_update(self):
        ug = gateways.AppUserGateway.find_user(1)
        ug.first_name = 'changedF'
        ug.middle_name = 'changedM'
        ug.last_name = 'changedL'
        ug.username = 'changedU'
        ug.update()
        obj = models.AppUser.objects.get(id_user=ug.id)
        self.assertEqual(obj.first_name, 'changedF')
        self.assertEqual(obj.middle_name, 'changedM')
        self.assertEqual(obj.last_name, 'changedL')
        self.assertEqual(obj.username, 'changedU')

    def test_delete(self):
        ug = gateways.AppUserGateway.find_user(1)
        ug.delete()
        self.assertIsNone(gateways.AppUserGateway.find_user(1))


class TestAppUserModule(TestCase):
    def setUp(self):
        models.AppUser.objects.create(
            username='user', first_name='Александр', middle_name='Евгеньевич', last_name='Чиварзин')

    def test_wrong_insert(self):
        with self.assertRaises(ValueError):
            # Здесь важен только ID
            table_module.AppUserModule.insert(1, 'any', 'any', 'any', 'any')

    def test_get_id_username(self):
        self.assertEqual(table_module.AppUserModule.get_id_by_username('user'), 1)
        self.assertEqual(table_module.AppUserModule.get_username_by_id(1), 'user')

    def test_get(self):
        self.assertEqual(table_module.AppUserModule.get_fio(1), 'Александр Евгеньевич Чиварзин')
        self.assertEqual(table_module.AppUserModule.get_first_name(1), 'Александр')
        self.assertEqual(table_module.AppUserModule.get_middle_name(1), 'Евгеньевич')
        self.assertEqual(table_module.AppUserModule.get_last_name(1), 'Чиварзин')

    def test_delete(self):
        self.assertTrue(table_module.AppUserModule.check_exists(1))
        table_module.AppUserModule.delete(1)
        self.assertFalse(table_module.AppUserModule.check_exists(1))


class TestTaskModel(TestCase):
    def setUp(self):
        models.AppUser.objects.create(
            username='user', first_name='Александр', middle_name='Евгеньевич', last_name='Чиварзин')

    def test_str(self):
        t = models.Task.objects.create(task_author_id=1, task_title='Test', task_text='SuperTest')
        self.assertEqual(str(t),
                         'Task{id_task=1, task_title=Test, task_authorAppUser{id_user=1, username=user}}')
