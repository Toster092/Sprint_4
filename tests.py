from main import BooksCollector

import pytest
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):  # проверяем, что добавилось две книги
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_twice_falce(self):  # добавляем одну книгу дважды
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_true(self):  # устанавливаем жанр книге
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_set_book_genre_not_from_genre_list_shows_empty(self):  # устанавливаем несуществующий жанр книге
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Неизвестный жанр')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_get_book_genre_horror_true(self):  # получаем жанр книги по её имени
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    @pytest.mark.parametrize('book_name, genre', [['Гордость и предубеждение и зомби', 'Ужасы'],
                                                  ['Мушкетер', 'Детективы'], ['Властелин колец', 'Фантастика']])
    def test_get_books_with_specific_genre_three_genres_true(self, book_name, genre):  # выводим список книг
        # с определённым жанром
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_with_specific_genre(genre) == [book_name]

    @pytest.mark.parametrize('book_name, genre', [['Гордость и предубеждение и зомби', 'Ужасы'],
                                                  ['Мушкетер', 'Детективы'], ['Властелин колец', 'Фантастика']])
    def test_get_books_genre_three_books_true(self, book_name, genre):  # получаем словарь books_genre
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_genre() == {book_name: genre}

    @pytest.mark.parametrize('book_name, genre', [['Гордость и предубеждение и зомби', 'Ужасы'],
                                                  ['Мушкетер', 'Детективы'], ['Властелин колец', 'Фантастика']])
    def test_get_books_for_children_three_genres_true(self, book_name, genre):  # возвращаем книги, подходящие детям
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_for_children() == [book_name]

    def test_add_book_in_favorites_true(self):  # добавляем книгу в Избранное
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_delete_book_from_favorites_true(self):  # удаляем книгу из Избранного
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_true(self):  # получаем список избранных книг
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']
