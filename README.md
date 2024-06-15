Тесты для класса BooksCollector
1. проверяем, что добавилось две книги (test_add_new_book_add_two_books);
2. добавляем одну книгу дважды (test_add_new_book_twice_falce);
3. устанавливаем жанр книге (test_set_book_genre_true); 
4. устанавливаем несуществующий жанр книге (test_set_book_genre_not_from_genre_list_shows_empty);
5. получаем жанр книги по её имени (test_get_book_genre_horror_true);
6. выводим список книг (test_get_books_with_specific_genre_three_genres_true);
7. получаем словарь books_genre (test_get_books_genre_three_books_true);
8. возвращаем книги, подходящие детям (test_get_books_for_children_three_genres_true);
9. добавляем книгу в Избранное (test_add_book_in_favorites_true);
10. удаляем книгу из Избранного (test_delete_book_from_favorites_true);
11. получаем список избранных книг (test_get_list_of_favorites_books_true)