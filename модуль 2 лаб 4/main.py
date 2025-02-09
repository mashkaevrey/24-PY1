if __name__ == "__main__":
    class Draft_article:
        '''Базовый класс Черновиковая статья, который будет использоваться для печати газетной статьи.'''
        pages: int = 3
        def __init__(self, author: str, article: str):
            self.author = author
            self.article = article
            self.increase_draft_papers()
        @property
        def papers(self) -> int:
            '''Вернет количество черновиковых страниц.'''
            return self.pages

        @papers.setter
        def papers(self, fresh_papers: int) -> None:
            '''Устанавливает количество черновиковых страниц для будущей газеты.'''
            if not isinstance(fresh_papers, int):
                raise TypeError("Количество черновиковых страниц должно быть типа int")
            if fresh_papers <= 0:
                raise ValueError("Количество черновиковых страниц должно быть положительным числом")
            self.pages = fresh_papers

        @classmethod
        def increase_draft_papers(cls) -> int:
            '''Увеличивает количество черновиковых страниц для статьи.'''
            cls.pages += 1

        def check_grammar(self) -> bool:
            '''Проверят текст черновиков на грамматические ошибки.'''
            ...

        def __str__(self) -> str:
            return f'Черновик статьи "{self.article}"'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({self.article!r})'

    class Newspaper(Draft_article):
        pages = 3
        def __init__(self, author: str, article: str):
            super().__init__(author, article)
            super().increase_draft_papers()
            self.format: str = "HTML"
        def check_grammar(self) -> bool:
            '''Проверяет текст черновика ещё раз во избежание грамматических ошибок перед печатью.'''
            ...

        def __str__(self):
            return f'Физическая газета "{self.article}"'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({self.article!r})'
    # pass
