from bookstoscrape.utils import get_soup_from_url


def get_book_info(soup):
    """
    Documentation
    """
    return "salut"


def save_book_into_csv(csvfile, book_info):
    """
    Documentation
    """
    pass


def main():
    """
    Documentation
    """
    soup = get_soup_from_url(
        "https://books.toscrape.com/catalogue/the-mysterious-affair-at-styles-hercule-poirot-1_452/index.html"
    )
    book_info = get_book_info(soup)
    with open('une_categorie.csv') as csvfile:
        save_book_into_csv(csvfile, book_info)


if __name__ == "__main__":
    main()