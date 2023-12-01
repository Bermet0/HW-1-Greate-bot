import asyncio
from parsel import Selector
import httpx
from db.queries import save_ad_to_db

MAIN_URL = "https://www.house.kg/snyat"
parse_ads = MAIN_URL


def get_html(url):
    response = httpx.get(url)
    # print(response.status_code)
    # print(response.text[:250])
    return response.text


def get_title(selector: Selector):
    title = selector.css("title::text").get()
    print(title)


def get_all_catalog_items(selector: Selector):
    items = selector.css(".listings-wrapper")
    return items


def clean_text(text):
    if text is None:
        return ''

    result = text.strip().replace("\n", "").replace("\t", "")
    result = ' '.join(result.split())
    if result[-1] == " ,":
        result.replace(" ,", "")
    return result


def main():
    for page in range(1, 10):
        html = get_html(MAIN_URL + f"/offers/{page}")
        selector = Selector(text=html)
        # get_title(selector)
        items = get_all_catalog_items(selector)
        for item in items:
            title = clean_text(item.css(".title::text").get())
            descr = clean_text(item.css(".top-info::text").get())
            url = item.css("::attr(href)").get()
            print(f"{MAIN_URL}{url}")
            # # image_url = item.css(".catalog-item-cover img::attr(src)").get()
            # # print(image_url)
            # save_ad_to_db(title, descr, url)



if __name__ == "__main__":
    main()
