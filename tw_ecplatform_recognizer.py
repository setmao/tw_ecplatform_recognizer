import click
import json
import requests
import validators


@click.command()
@click.argument('ecplatform_url')
def recognize_ecplatform(ecplatform_url: str):

    # check url format
    if not validators.url(ecplatform_url):
        print('Invalid url.')
        return False

    # get ecplatform keyword
    with open('ecplatform_keyword.json') as json_file:
        ecplatform_keyword = json.load(json_file)

    try:
        resp = requests.get(ecplatform_url, timeout=3)
    except:
        print('Not found.')
        return False

    answer_list = []
    for keyword in ecplatform_keyword:
        if keyword in resp.text:
            answer_list.append(ecplatform_keyword[keyword])

    if answer_list:
        print(max(answer_list, key=answer_list.count))
    else:
        print('Not found.')


if __name__ == '__main__':
    recognize_ecplatform()
