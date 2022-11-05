class UrlStartPage:
    prefix = 'https://'  # 'https://preprod.', 'https://master.', 'https://'
    if prefix == 'https://':
        suffix = ''
    else:
        suffix = '.preprod.pw'
    suffix_page = ''
    url_start_page = f"{prefix}logincasino.work{suffix}{suffix_page}"


class UrlStartPageAdmin:
    if UrlStartPage.suffix == '.preprod.pw':
        url_page_admin = "http://admin-work.pw.preprod.pw/x" # 'https://fixvacancy.admin-work.pw.preprod.pw/x', 'http://admin-work.pw.preprod.pw/x'
    else:
        url_page_admin = "https://admin-work.work/x"
