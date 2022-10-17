fake_db = {

    '/company/history': {
        'page_title': 'Company History',
        'page_details': 'Details about my company'
    },
    '/company/employees': {
        'page_title': 'Our team',
        'page_details': 'Details about my team'
    }

}


def get_page(url: str) -> dict:
    if not url:
        return {}

    url = url.strip().lower()
    url = '/' + url.lstrip('/')
    page = fake_db.get(url, {})
    return page
