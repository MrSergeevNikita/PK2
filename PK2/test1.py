import unittest
from rk2 import library, CDs, CD_and_Library, number1, number2, number3

one_to_many_test = [(k.name_cd, k.cost, m.name)
                    for m in library
                    for k in CDs
                    if k.cd_lib_id == m.id]

many_to_many_temp = [(m.name, km.cd_id, km.library_id)
                     for m in library
                     for km in CD_and_Library
                     if m.id == km.cd_id]

many_to_many_test = [(k.name_cd, k.cost, CD_Library_name)
                     for CD_Library_name, library_id, cd_id in many_to_many_temp
                     for k in CDs if k.id == cd_id]


class Tests(unittest.TestCase):

    def test1(self):
        self.assertEqual(number1(one_to_many_test), [('Видео с аквапарка', 'Аквапарк')])

    def test2(self):
        self.assertEqual(number2(one_to_many_test), [('Музыкальные клипы', 3000),
                                                     ('Мультфильмы', 2500), ('Фильмы', 2000), ('Музыка', 500),
                                                     ('Игры', 200), ('Аквапарк', 0)])

    def test3(self):
        self.assertEqual(number3(many_to_many_test), [('Видео с аквапарка', 'Аквапарк'),
                                                      ('Соник', 'Игры'), ('Том и Джерри', 'Игры'),
                                                      ('Альбом группы Кино', 'Музыка'),
                                                      ('Музыкальные клипы 90-х', 'Музыка'),
                                                      ('Музыкальные клипы 90-х', 'Музыкальные клипы'),
                                                      ('Альбом группы Кино', 'Музыкальные клипы'),
                                                      ('Том и Джерри', 'Мультфильмы'),
                                                      ('Соник', 'Мультфильмы'), ('Аватар', 'Фильмы')])


if __name__ == '__main__':
    unittest.main()