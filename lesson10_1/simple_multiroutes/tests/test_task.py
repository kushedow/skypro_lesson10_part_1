from task import app
import unittest

class TestCase(unittest.TestCase):
    def test_sort(self):
        with app.test_client() as client:

            #  проверка статуса

            path = '/'
            resp = client.get(path)
            self.assertEqual(200, resp.status_code, msg=f'Приложение не обрабатывает запрос к {path}')

            path = '/employees/'
            resp = client.get(path)
            self.assertEqual(200, resp.status_code, msg=f'Приложение не обрабатывает запрос к {path}')

            path = '/employees/3/'
            resp = client.get(path)
            self.assertEqual(200, resp.status_code, msg=f'Приложение не обрабатывает запрос к {path}')


            # ожидание и реальность

            path = '/'
            expected = 'Тут будет главная'
            resp = client.get(path)
            self.assertEqual(expected, resp.get_data(True),
                             msg=f'Неверный ответ при запросе к {path} должно быть {expected}')

