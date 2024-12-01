def get_example_input(day, year=2024):
    import AdvancedHTMLParser
    import re
    import requests
    page = requests.get(f"https://adventofcode.com/{year}/day/{day}").text
    if page.startswith("Please don't"):
        return False
    parser = AdvancedHTMLParser.IndexedAdvancedHTMLParser()
    parser.parseStr(page)
    for i in parser.getElementsByClassName("day-desc")[0].getAllChildNodes():
        if i.getEndTag() == "</p>" and re.match("[^\n]*example[^\n]*:", i.text):
            return i.nextElementSibling.firstChild.text.strip()