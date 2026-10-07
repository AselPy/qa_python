import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book(self):
        collector = BooksCollector()
        n = 'Гарри Поттер'

        collector.add_new_book(n)

        assert n in collector.books_genre

    def test_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_get_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин колец')

        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Властелин колец', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == [
            'Гарри Поттер',
            'Властелин колец'
        ]

    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')

        assert collector.get_books_genre() == {
            'Гарри Поттер': ''
        }

    @pytest.mark.parametrize(
        'book_genre, expected',
        [
            ('Фантастика', True),
            ('Мультфильмы', True),
            ('Комедии', True),
            ('Ужасы', False),
            ('Детективы', False)
        ]
    )
    def test_get_books_for_children(self, book_genre, expected):
        collector = BooksCollector()

        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', book_genre)

        result = 'Книга' in collector.get_books_for_children()

        assert result == expected

    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == [
            'Гарри Поттер'
        ]

    def test_add_book_in_favorites_twice(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == [
            'Гарри Поттер'
        ]

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == [
            'Гарри Поттер'
        ]