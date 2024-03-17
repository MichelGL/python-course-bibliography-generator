"""
Фикстуры для моделей объектов (типов источников).
"""
import pytest

from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, ThesisAbstractModel, NewspaperArticleModel


@pytest.fixture
def book_model_fixture() -> BookModel:
    """
    Фикстура модели книги.

    :return: BookModel
    """

    return BookModel(
        authors="Иванов И.М., Петров С.Н.",
        title="Наука как искусство",
        edition="3-е",
        city="СПб.",
        publishing_house="Просвещение",
        year=2020,
        pages=999,
    )


@pytest.fixture
def internet_resource_model_fixture() -> InternetResourceModel:
    """
    Фикстура модели интернет-ресурса.

    :return: InternetResourceModel
    """

    return InternetResourceModel(
        article="Наука как искусство",
        website="Ведомости",
        link="https://www.vedomosti.ru",
        access_date="01.01.2021",
    )


@pytest.fixture
def articles_collection_model_fixture() -> ArticlesCollectionModel:
    """
    Фикстура модели сборника статей.

    :return: ArticlesCollectionModel
    """

    return ArticlesCollectionModel(
        authors="Иванов И.М., Петров С.Н.",
        article_title="Наука как искусство",
        collection_title="Сборник научных трудов",
        city="СПб.",
        publishing_house="АСТ",
        year=2020,
        pages="25-30",
    )

@pytest.fixture
def thesis_abstract_model_fixture() -> ThesisAbstractModel:
    """
    Фикстура модели автореферата.

    :return: ThesisAbstractModel
    """

    return ThesisAbstractModel(
        author="Иванов И.М.",
        thesis_title="Наука как искусство",
        degree="д-р. / канд.",
        field_of_science="экон.",
        specialty_code="01.01.01",
        city="СПб.",
        year=2020,
        pages=199,
    )

@pytest.fixture
def newspaper_article_model_fixture() -> NewspaperArticleModel:
    """
    Фикстура модели статьи из газеты.

    :return: NewspaperArticleModel
    """

    return NewspaperArticleModel(
        authors="Иванов И.М., Петров С.Н.",
        article_title="Наука как искусство",
        newspaper="Южный Урал",
        year=1980,
        publication_date="01.10",
        article_number=5,
    )
