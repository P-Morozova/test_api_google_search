import requests
import re

SEARCH_TEXT = "QA Automation"
EXPECTED_RESPONSE_TITLE = SEARCH_TEXT + " - Поиск в Google"
EXPECTED_RESPONSE_CODE = 200
MAIN_LINK = "https://www.google.ru/"
SEARCH_LINK = "https://www.google.ru/search?q=QA+Automation&newwindow=1&hl=ru&sxsrf" \
              "=AJOqlzXogYV2iMIF4qa5moLZAI6mcl0zcg:1675750958871&source=hp&ei=Lu7hY-ObM7mDkdUPxKOc0Ao&iflsig" \
              "=AK50M_UAAAAAY-H8PokuTeWpoPwPYeTLoEUonHqmbV-a&ved=0ahUKEwjj6ojl4oL9AhW5QaQEHcQRB6oQ4dUDCAg&uact=5&oq" \
              "=QA+Automation&gs_lcp" \
              "=Cgdnd3Mtd2l6EAMyCwgAEIAEELEDEIMBMgoIABCABBAUEIcCMgsIABCABBCxAxCDATIKCAAQgAQQFBCHAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCCMQ6gIQJzoECCMQJzoOCC4QgAQQsQMQxwEQ0QM6CAgAEIAEELEDOhEILhCABBCxAxCDARDHARDRAzoICC4QgAQQsQM6CwguEIAEEMcBENEDOgoILhCxAxDUAhBDOggIABCxAxCDAToLCC4QgAQQxwEQrwFQzQ9YlSNgnFJoA3AAeACAAesBiAGKFpIBBDItMTOYAQCgAQGwAQo&sclient=gws-wiz "


def test_main_page_status_code():

    main_page_response = requests.get(MAIN_LINK)
    response_code = main_page_response.status_code
    assert response_code == EXPECTED_RESPONSE_CODE, "ERROR! Expected response code: " + str(
        EXPECTED_RESPONSE_CODE) + ", got " + str(response_code) + " instead"


def test_result_page_title():

    result_page_response = requests.get(SEARCH_LINK)
    title = re.split(r'<[/]?title>', result_page_response.text)[1]
    assert title == EXPECTED_RESPONSE_TITLE, "ERROR! The title of the page doesn't match what is expected: expected " \
                                             + EXPECTED_RESPONSE_TITLE + "got " + title + " instead"