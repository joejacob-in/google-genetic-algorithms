#!/usr/bin/env python
"""
"""
import mechanize 
import html2text


url = "http://python.meetup.com/185/calendar/past_list/"

br = mechanize.Browser()
br.open(url)


# loop over all the 'Read more' links in the page
for link in br.links(text="Read more"): 

    br.click_link(link)
    html = br.response().read()
    html = html2text.codecs.decode(html, 'iso-8859-1')

    print html2text.html2text(html)




#br.find_link(url_regex=re.compile("http://python.meetup.com/185/calendar/\d+"))


if __name__ == '__main__':
    pass

