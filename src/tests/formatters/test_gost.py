"""
Тестирование функций оформления списка источников по ГОСТ Р 7.0.5-2008.
"""

from formatters.base import BaseCitationFormatter
from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    ThesisAbstractModel,
    NewspaperArticleModel,
)
from formatters.styles.gost import (
    GOSTBook,
    GOSTInternetResource,
    GOSTCollectionArticle,
    GOSTThesisAbstract,
    GOSTNewspaperArticle,
)


class TestGOST:
    """
    Тестирование оформления списка источников согласно ГОСТ Р 7.0.5-2008.
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книги.

        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = GOSTBook(book_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. Наука как искусство. – 3-е изд. – СПб.: Просвещение, 2020. – 999 с."
        )

    def test_internet_resource(
        self, internet_resource_model_fixture: InternetResourceModel
    ) -> None:
        """
        Тестирование форматирования интернет-ресурса.

        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        model = GOSTInternetResource(internet_resource_model_fixture)

        assert (
            model.formatted
            == "Наука как искусство // Ведомости URL: https://www.vedomosti.ru (дата обращения: 01.01.2021)."
        )

    def test_articles_collection(
        self, articles_collection_model_fixture: ArticlesCollectionModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :return:
        """

        model = GOSTCollectionArticle(articles_collection_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. Наука как искусство // Сборник научных трудов. – СПб.: АСТ, 2020. – С. 25-30."
        )

    def test_thesis_abstract(
        self, thesis_abstract_model_fixture: ThesisAbstractModel
    ) -> None:
        """
        Тестирование форматирования автореферата.

        :param ThesisAbstractModel thesis_abstract_model_fixture: Фикстура модели автореферата
        :return:
        """

        model = GOSTThesisAbstract(thesis_abstract_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М.. Наука как искусство [д-р. / канд.]: экон., 01.01.01 / СПб., 2020. – 199 с."
        )

    def test_newspaper_article(
        self, newspaper_article_model_fixture: NewspaperArticleModel
    ) -> None:
        """
        Тестирование форматирования статьи из газеты.

        :param NewspaperArticleModel newspaper_article_model_fixture: Фикстура модели статьи из газеты
        :return:
        """

        model = GOSTNewspaperArticle(newspaper_article_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. Наука как искусство // Южный Урал. – 1980. – 01.10. – № 5."
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
            GOSTBook(book_model_fixture),
            GOSTInternetResource(internet_resource_model_fixture),
            GOSTCollectionArticle(articles_collection_model_fixture),
            GOSTThesisAbstract(thesis_abstract_model_fixture),
            GOSTNewspaperArticle(newspaper_article_model_fixture),
        ]
        result = BaseCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0] == models[2]
        assert result[1] == models[4]
        assert result[2] == models[0]
        assert result[3] == models[3]
        assert result[4] == models[1]
