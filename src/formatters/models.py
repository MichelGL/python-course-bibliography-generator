"""
Описание схем объектов (DTO).
"""

from typing import Optional

from pydantic import BaseModel, Field


class BookModel(BaseModel):
    """
    Модель книги:

    .. code-block::

        BookModel(
            authors="Иванов И.М., Петров С.Н.",
            title="Наука как искусство",
            edition="3-е",
            city="СПб.",
            publishing_house="Просвещение",
            year=2020,
            pages=999,
        )
    """

    authors: str
    title: str
    edition: Optional[str]
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)


class InternetResourceModel(BaseModel):
    """
    Модель интернет ресурса:

    .. code-block::

        InternetResourceModel(
            article="Наука как искусство",
            website="Ведомости",
            link="https://www.vedomosti.ru/",
            access_date="01.01.2021",
        )
    """

    article: str
    website: str
    link: str
    access_date: str


class ArticlesCollectionModel(BaseModel):

    """
    Модель сборника статей:

    .. code-block::

        ArticlesCollectionModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            collection_title="Сборник научных трудов",
            city="СПб.",
            publishing_house="АСТ",
            year=2020,
            pages="25-30",
        )
    """

    authors: str
    article_title: str
    collection_title: str
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: str

class ThesisAbstractModel(BaseModel):
    """
    Модель автореферата:

    .. code-block::

        ThesisAbstractModel(
            author="Иванов И.М.",
            thesis_title="Наука как искусство",
            degree="д-р. / канд.",
            field_of_science="экон.",
            specialty_code="01.01.01",
            city="СПб.",
            year=2020,
            pages=199,
        )
    """

    author: str
    thesis_title: str
    degree: str  # доктора или кандидата
    field_of_science: str  # отрасль наук (сокращённо)
    specialty_code: str  # код специальности
    city: str  # город издательства
    year: int = Field(..., gt=0)  # год
    pages: int = Field(..., gt=0)  # количество страниц

class NewspaperArticleModel(BaseModel):
    """
    Модель статьи из газеты:

    .. code-block::

        NewspaperArticleModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            newspaper="Южный Урал",
            year=1980,
            publication_date="01.10",
            article_number=5,
        )
    """

    authors: str
    article_title: str
    newspaper: str
    year: int = Field(..., gt=0)
    publication_date: str
    article_number: int = Field(..., gt=0)
