# lint-amnesty, pylint: disable=missing-module-docstring

from lxml import etree
import lxml.etree


def check_html(html):
    '''
    Check whether the passed in html string can be parsed by lxml.
    Return bool success.
    '''
    parser = etree.HTMLParser()
    try:
        etree.fromstring(html, parser, parser=lxml.etree.XMLParser(resolve_entities=False))
        return True
    except Exception:   # pylint: disable=broad-except
        pass
    return False
