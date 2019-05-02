import pytest
from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model

from meal_app.models import Meal

pytestmark = pytest.mark.django_db(transaction=True)


def create_meal():
    get_user_model().objects.create_user('temporary', 'temporary@example.com', 'temporary')
    a_meal = Meal
    return a_meal.objects.create(name="asha", detail="Z maslom")


class MealModelTests(TestCase):

    def test_meal_get_absolute_url(self):
        meal = create_meal()
        self.assertIs(meal.get_absolute_url() == f"/meals/{meal.name}/", True)


class MealViewTests(TestCase):
    def test_get_detail_url(self):
        self.client.login(username="temporary", password="temporary")
        meal = create_meal()
        response = self.client.get(reverse('meals:detail', kwargs={"name": meal.name}), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_get_list_url(self):
        self.client.login(username="temporary", password="temporary")
        response = self.client.get(reverse('meals:list'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_get_create_url(self):
        self.client.login(username="temporary", password="temporary")
        response = self.client.get(reverse('meals:create'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_get_delete_url(self):
        self.client.login(username="temporary", password="temporary")
        meal = create_meal()
        response = self.client.get(reverse('meals:delete', kwargs={"pk": meal.pk}), follow=True)
        self.assertEqual(response.status_code, 200)
