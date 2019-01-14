import wikipedia

def main():
    search_phrase = False

    while search_phrase != '':
        search_phrase = input('Enter page title or search phrase: ')
        try:
            print(wikipedia.summary(search_phrase))
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)

main()