"""
Тестирование функций оформления списка источников по APA.
"""

from formatters.base import BaseCitationFormatter
from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    ThesisAbstractModel,
    NewspaperArticleModel,
)
from formatters.styles.apa import (
    APABook,
    APAInternetResource,
    APAArticlesCollection,
    APAThesisAbstract,
    APANewspaperArticle,
)


class TestAPA:
    """
    Тестирование оформления списка источников по стандарту APA.
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книги.

        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = APABook(book_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (2020) Наука как искусство (3-е изд. – ) СПб.: Просвещение, 999 с."
        )

    def test_internet_resource(
        self, internet_resource_model_fixture: InternetResourceModel
    ) -> None:
        """
        Тестирование форматирования интернет-ресурса.

        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        model = APAInternetResource(internet_resource_model_fixture)

        assert (
            model.formatted
            == "Ведомости (01.01.2021) Наука как искусство https://www.vedomosti.ru"
        )

    def test_articles_collection(
        self, articles_collection_model_fixture: ArticlesCollectionModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :return:
        """

        model = APAArticlesCollection(articles_collection_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (2020) Наука как искусство, Сборник научных трудов СПб.: АСТ, 25-30 с."
        )

    def test_thesis_abstract(
        self, thesis_abstract_model_fixture: ThesisAbstractModel
    ) -> None:
        """
        Тестирование форматирования автореферата.

        :param ThesisAbstractModel thesis_abstract_model_fixture: Фикстура модели автореферата
        :return:
        """

        model = APAThesisAbstract(thesis_abstract_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М. (2020). Наука как искусство (д-р. / канд.). экон., 01.01.01. СПб., 2020. 199."
        )

    def test_newspaper_article(
        self, newspaper_article_model_fixture: NewspaperArticleModel
    ) -> None:
        """
        Тестирование форматирования статьи из газеты.

        :param NewspaperArticleModel newspaper_article_model_fixture: Фикстура модели статьи из газеты
        :return:
        """

        model = APANewspaperArticle(newspaper_article_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (1980). Наука как искусство. Южный Урал, 01.10, 5."
        )

    def test_citation_formatter(
        self,
        book_model_fixture: BookModel,
        internet_resource_model_fixture: InternetResourceModel,
        articles_collection_model_fixture: ArticlesCollectionModel,
        thesis_abstract_model_fixture: ThesisAbstractModel,
        newspaper_article_model_fixture: NewspaperArticleModel,
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :return:
        """

        models = [
            APABook(book_model_fixture),
            APAInternetResource(internet_resource_model_fixture),
            APAArticlesCollection(articles_collection_model_fixture),
            APAThesisAbstract(thesis_abstract_model_fixture),
            APANewspaperArticle(newspaper_article_model_fixture),
        ]
        result = BaseCitationFormatter(models).format()

        # Тестирование сортировки списка источников
        assert result[0] == models[1]
        assert result[1] == models[3]
        assert result[2] == models[4]
        assert result[3] == models[0]
        assert result[4] == models[2]
