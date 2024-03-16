from string import Template
from pydantic import BaseModel
from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, ThesisAbstractModel, NewspaperArticleModel
from formatters.styles.base import BaseCitationStyle
from logger import get_logger

logger = get_logger(__name__)

class APABook(BaseCitationStyle):
    """
    Форматирование для книг по стандартам APA.
    """

    data: BookModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors ($year) $title ($edition) $city: $publishing_house, $pages с."
        )

    def substitute(self) -> str:

        logger.info('Форматирование книги "%s" ...', self.data.title)

        return self.template.substitute(
            authors=self.data.authors,
            title=self.data.title,
            edition=self.get_edition(),
            city=self.data.city,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
            pages=self.data.pages,
        )

    def get_edition(self) -> str:
        """
        Получение отформатированной информации об издательстве.

        :return: Информация об издательстве.
        """

        return f"{self.data.edition} изд. – " if self.data.edition else ""

class APAInternetResource(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов по стандартам APA.
    """

    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template(
            "$website ($access_date) $article $link)"
        )

    def substitute(self) -> str:

        logger.info('Форматирование интернет-ресурса "%s" ...', self.data.article)

        return self.template.substitute(
            article=self.data.article,
            website=self.data.website,
            link=self.data.link,
            access_date = self.data.access_date,
        )

class APAArticlesCollection(BaseCitationStyle):
    """
    Форматирование для статей из сборника по стандартам APA.
    """

    data: ArticlesCollectionModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors ($year) $article_title, $collection_title $city: $publishing_house, $pages с."
        )

    def substitute(self) -> str:

        logger.info('Форматирование сборника статей "%s" ...', self.data.article_title)

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            collection_title=self.data.collection_title,
            city=self.data.city,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
            pages=self.data.pages,
        )

class APAThesisAbstract(BaseCitationStyle):
    """
    Форматирование для авторефератов по стандартам APA.
    """

    data: ThesisAbstractModel

    @property
    def template(self) -> Template:
        return Template(
            "$author ($year). $thesis_title. $degree. $field_of_science. $city, $year. $pages."
        )

    def substitute(self) -> str:

        logger.info('Форматирование автореферата "%s" ...', self.data.thesis_title)

        return self.template.substitute(
            author=self.data.author,
            thesis_title=self.data.thesis_title,
            degree=self.data.degree,
            field_of_science=self.data.field_of_science,
            city=self.data.city,
            year=self.data.year,
            pages=self.data.pages,
        )

class APANewspaperArticle(BaseCitationStyle):
    """
    Форматирование для статей из газеты по стандартам APA.
    """

    data: NewspaperArticleModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors ($year). $article_title. $newspaper, $publication_date, $article_number."
        )

    def substitute(self) -> str:

        logger.info('Форматирование статьи из газеты "%s" ...', self.data.article_title)

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            newspaper=self.data.newspaper,
            year=self.data.year,
            publication_date=self.data.publication_date,
            article_number=self.data.article_number,
        )

class APACitationFormatter:
    """
    Базовый класс для форматирования списка источников по стандартам APA.
    """

    formatters_map = {
        BookModel.__name__: APABook,
        InternetResourceModel.__name__: APAInternetResource,
        ArticlesCollectionModel.__name__: APAArticlesCollection,
        ThesisAbstractModel.__name__: APAThesisAbstract,
        NewspaperArticleModel.__name__: APANewspaperArticle
    }

    def __init__(self, models: list[BaseModel]) -> None:
        """
        Конструктор.

        :param models: Список объектов для форматирования
        """

        formatted_items = []
        for model in models:
            formatted_items.append(self.formatters_map.get(type(model).__name__)(model))  # type: ignore

        self.formatted_items = formatted_items

    def format(self) -> list[BaseCitationStyle]:
        """
        Форматирование списка источников.

        :return:
        """

        return sorted(self.formatted_items, key=lambda item: item.formatted)
