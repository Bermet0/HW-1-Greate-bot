import asyncio
from db import queries
from db.queries import save_house
from parsel import Selector
import httpx


MAIN_URL = "https://www.house.kg/snyat"


def get_html(url):
    response = httpx.get(url)
    # print(response.status_code)
    # print(response.text[:250])
    return response.text


def get_title(selector: Selector):
    title = selector.css("title::text").get()
    print(title)


def get_all_catalog_items(selector: Selector):
    items = selector.css('.listings_wrapper div.listing')
    return items


def clear_text(text):
    if text is None:
        return ''

    result = text.strip().replace("\n", "").replace("\t", "")
    result = ' '.join(result.split())
    if result[-1] == ' ,':
        result.replace(' ,', '')
    return result


def main():
    html = get_html(MAIN_URL + '/offers')
    selector = Selector(text=html)
    # get_title(selector)
    items = get_all_catalog_items(selector)
    for item in items:
        title = clear_text(item.css('.title::text').get())

        descr = clear_text(item.css('.description::text').get())
        price = clear_text(item.css('.sep.main::text').get())
        url0 = item.css('::attr(href)').get()
        url = (f'{MAIN_URL}{url0}')
        img = clear_text(item.css('.tmb-wrap-table::attr(src)').get())
        # print(img)
        save_house(title, descr, price, url, img)


if __name__ == "__main__":
    queries.init_db()
    main()
