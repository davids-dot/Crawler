# -*- coding=UTF-8 -*-

from crawler.Crawler import Crawler
#一个文件是一个modul而不是类



class LiaoCrawler(Crawler):
    #在这里要初始化url 和文件名的对应
    def parse_menu(self):
        lis = self.soup.select(".x-sidebar-left ul.uk-nav.uk-nav-side li[id]")
        for li in lis:
            a=li.findChild("a")
            self.urls.append(a)

    def parse_body(self,soup):
        body =soup.find_all(class_="x-wiki-content")[0]
        return str(body)

    
    def changeFileStruct(self,soup,title):
        center_tag = soup.new_tag("center")
        title_tag = soup.new_tag('h1')
        title_tag.string = title
        center_tag.insert(0, title_tag)
        soup.find("p").insert_before(center_tag)
        html = self.verifyUrl(str(soup))
        html = Crawler.HTML_TEMPLATE.format(content=html)
        return html
    
def main():
    pass
    
if __name__ == '__main__':
    main()
        