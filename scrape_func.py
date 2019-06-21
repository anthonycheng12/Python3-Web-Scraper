from bs4 import BeautifulSoup as BS
import requests

mapper = {
    'table': 'table.forumline',
    # all valid posts css_selector
    'valid_posts': ['td.row1', 'td.row2'],
    'details': [
        {
            'name': 'span.name',
            'post_id': 'span.name a',
        },
        {
            'post_date': 'span.postdetails',
            'post_body': 'span.postbody',
        }
    ]
}

def get_all_posts(docs):
    table_posts = docs.select_one(mapper['table'])
    _valid_posts = []
    for _post in mapper['valid_posts']:
        _valid_posts += table_posts.select(_post)

    return _valid_posts


def parse_posts(posts):
    if len(posts) != len(mapper['details']):
        return
    dat = {}
    # idx is index and post is the valid posts
    for idx, post in enumerate(posts):
        # k is the name of the key in the details array object
        # v is the value of the key
        for k, v in mapper['details'][idx].items():
            elem = post.select_one(v)
            if not elem:
                continue
            if k in ['post_id']:
                dat[k] = elem.get('name')
            else:
                dat[k] = elem.text
    return dat

def scrape(start_num, writer, target_url):
    for var in list(range(8)):
        target_url = target_url + "&postdays=0&postorder=asc&start=" + str(start_num)
        raw = requests.get(target_url).text
        docs = BS(raw, 'html.parser')
        valid_posts = get_all_posts(docs)
        posts = []
        for i in range(len(valid_posts) // 2):
            dat = parse_posts(valid_posts[i * 2: (i + 1) * 2]) # gets the valid range of td tags we need to check 
            if dat:
                # if data returns then append it
                posts.append(dat)
        for post in posts:
            writer.writerow([post["post_id"], post["name"], post["post_date"], post["post_body"]])
        start_num += 15


def getRow(word1, word2, word3, word4):
    csv_header = []
    csv_header.extend([word1, word2, word3, word4]) 
    return csv_header