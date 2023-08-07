from django.contrib.auth import get_user_model
from django.test import TestCase

UserModel = get_user_model()


class BestTestCase(TestCase):
    def creat_and_login_user(self, **credentials):
        user = UserModel.objects.create_user(**credentials)
        self.client.login(**credentials)
        return user

    def assertCollectionEmpty(self, collection, message=None):
        return self.assertEquals(0, len(collection), message)


    def assertCollectionNotEmpty(self, collection, message=None):
        return self.assertEqual(1, len(collection), message)
