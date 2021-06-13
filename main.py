from csv_manager import CSV_Manager
from manipulator import Manipulator
import json

def filter_CSV(filter_field, value):
    reader = CSV_Manager("./articles.csv")#CSV_Manager class
    articles = reader.get_csv_as_dicts()#whats returned from this method
    manipulator = Manipulator(articles)

    filtered = manipulator.filter_by(filter_field, value)
    return list(filtered)

def count_articles(filter_field, value):
    lis = filter_CSV(filter_field, value)
    return len(lis)

def is_article(filter_field, value):
    len = count_articles(filter_field, value)
    if(len > 0): return True
    return False

def longest_article(filter_field, value):
    articles = filter_CSV(filter_field, value)
    max = 0
    article = {}

    for i in articles:
        if(int(i['pages']) > max):
            max = int(i['pages'])
            article = i
    return article

# print("Articles with a title of t4:")
# print(filter_CSV("title", "t4"))
# print('')
# print("Articles of a1 author:")
# print(filter_CSV("author", "a1"))
# print(count_articles("author", "a1"))
# print(is_article("author", "a7"))
# print(longest_articale("author", "a1"))
# print(longest_article('author', 'a2'))
reader = CSV_Manager("./articles.csv")
print(reader.mappedArticales())