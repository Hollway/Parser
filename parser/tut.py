import re



class  TutBy(object):
    __url = ""



    def __init__(self, date:str):
        self.__news = []
        pass

    def  get_page(self):
        return None

    def parse_bs(self):
        pass

    def parse_re(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        for news in self.__news:
            yield news
        raise StopIteration