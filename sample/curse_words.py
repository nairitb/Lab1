from urllib.request import urlopen

def read_file():
    contents = open(r"F:\NAIRIT\PyCharm\EICT\Lab1\movie_quotes.txt")
    quotes = contents.read()
    #print(quotes)
    check_badwords(quotes)



def check_badwords(word_tocheck):
    connection = urlopen("www.wdylike.appspot.com/?q=", +word_tocheck)
    output = connection.read()

read_file()