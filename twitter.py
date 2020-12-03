import os
import json
from pprint import pprint

from playwright import sync_playwright


def get_page(context, cookie_file):
    if os.path.exists(cookie_file):
        cookies = json.load(open(cookie_file, 'r'))
        context.addCookies(cookies)

    page = context.newPage()

    if len(context.cookies()):
        page.goto("https://twitter.com/home")
        page.waitForLoadState("load")

    else:
        page.goto("https://twitter.com/login")
        page.waitForLoadState("load")

        page.fill('input[type="text"]', "pino23218421")
        page.fill('input[type="password"]', "(H6Ho2Tko=]8t6=H")

        page.click('div[data-testid="LoginForm_Login_Button"]')

        json.dump(context.cookies(), open(cookie_file, 'w'), indent = 4)

        page.waitForNavigation()

    return page


with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.newContext()

    page = get_page(context, './cookies.json')

    # 追加予定のユーザ名
    add_user_name = "monst_campaign"

    page.goto("https://twitter.com/{}".format(add_user_name))

    page.click('div[aria-label="もっと見る"]')
    page.waitForSelector('div[role="menu"]')

    page.click('a[href="/i/lists/add_member"]')
    page.waitForSelector('div[aria-label="タイムライン: リストを選択"]')

    # リストのどれか一つにユーザが追加済みか確認
    is_added_user = len(page.querySelectorAll('div[aria-label="タイムライン: リストを選択"] > div > div div > a[role="link"] > div > div:last-child svg')) > 0
    if not is_added_user:
        # 追加予定のリスト名
        add_list_name = "test1"

        # 追加予定のリスト要素を抽出
        def check_element(x):
            return len(x.querySelectorAll('a[role="link"] > div > div:last-child svg')) == 0  and x.innerText() == add_list_name
        add_list_element = list(filter(check_element, page.querySelectorAll('div[aria-label="タイムライン: リストを選択"] > div > div div > a[role="link"]')))

        # リスト追加実行
        if len(add_list_element) == 1:
            add_list_element[0].click()
            page.click('div[role="dialog"] > div > div > div > div > div > div:last-child  div[role="button"]')

    page.screenshot(path=f'tswitter.png')

    browser.close()
