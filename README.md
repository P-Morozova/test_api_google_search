# A simple google search api tests

## Test main google search page

Steps:

- send a GET-request to https://www.google.ru/
- get response and make sure that received response code is 200 (OK)

Expected result: response_code = 200

##  Test result page of google search

Steps:

- send a GET-request to https://www.google.ru/search?q=QA+AUtomation&newwindow=1&hl=ru&sxsrf=AJOqlzXogYV2iMIF4qa5moLZAI6mcl0zcg:1675750958871&source=hp&ei=Lu7hY-ObM7mDkdUPxKOc0Ao&iflsig=AK50M_UAAAAAY-H8PokuTeWpoPwPYeTLoEUonHqmbVa&ved=0ahUKEwjj6ojl4oL9AhW5QaQEHcQRB6oQ4dUDCAg&uact=5&oq=QA+AUtomation&gs_lcp=Cgdnd3Mtd2l6EAMyCwgAEIAEELEDEIMBMgoIABCABBAUEIcCMgsIABCABBCxAxCDATIKCAAQgAQQFBCHAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCCMQ6gIQJzoECCMQJzoOCC4QgAQQsQMQxwEQ0QM6CAgAEIAEELEDOhEILhCABBCxAxCDARDHARDRAzoICC4QgAQQsQM6CwguEIAEEMcBENEDOgoILhCxAxDUAhBDOggIABCxAxCDAToLCC4QgAQQxwEQrwFQzQ9YlSNgnFJoA3AAeACAAesBiAGKFpIBBDItMTOYAQCgAQGwAQo&sclient=gws-wiz)
- get response and make sure the title of the response matches "*YOUR SEARCH TEXT* - Поиск в Google"

Expected result: title of response is equal to "*YOUR SEARCH TEXT* - Поиск в Google"
