from random import choice

from ..personal.names import fake_name, fake_surname
from ..strings import fake_string

domains = ["google", "youtube", "facebook", "baidu", "wikipedia", "qq", "tmall", "yahoo", "taobao", "amazon", "sohu", "twitter",
           "jd", "live", "vk", "instagram", "weibo", "sina", "login", "360", "reddit", "linkedin", "blogspot", "netflix",
           "microsoftonline", "pages", "yahoo", "yandex", "mail", "pornhub", "twitch", "porn555", "csdn", "alipay", "google",
           "microsoft", "aliexpress", "t", "google", "ebay", "bing", "naver", "github", "stackoverflow", "amazon", "livejasmin",
           "office", "msn", "imdb", "google", "xvideos", "whatsapp", "tribunnews", "wordpress", "googleusercontent", "paypal",
           "bilibili", "apple", "xhamster", "imgur", "google", "google", "xinhuanet", "google", "adobe", "fandom", "google",
           "babytree", "pinterest", "fbcdn", "amazon", "dropbox", "tumblr", "exosrv", "hao123", "amazon", "amazon", "amazonaws",
           "google", "instructure", "speakol", "booking", "zhihu", "tianya", "soso", "google", "thestartmagazine", "detail",
           "bbc", "salesforce", "pixnet", "aparat", "cnn", "onlinesbi", "force", "rakuten", "bbc", "google", "bodelen",
           "1cnblogs"]

tlds = ["com", "co.uk", "org", "net", "ru", "eu", "de", "fr", "tv", "cn", "es", "com.tr"]


def fake_email(addr=None, domain=None, tld=None):
    addr = addr or f"{fake_string(min_length=1)}"
    domain = domain or f"{fake_string(min_length=1)}"
    tld = tld or f"{fake_string(min_length=2, max_length=7)}"
    return f"{addr}@{domain}.{tld}"


def fake_enough_email(addr=None, domain=None, tld=None):
    addr = addr or f"{fake_name()}.{fake_surname()}"
    domain = domain or f"{choice(domains)}"
    tld = tld or f"{choice(tlds)}"
    return f"{addr}@{domain}.{tld}"
