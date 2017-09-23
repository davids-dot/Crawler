# coding =UTF-8


from crawler.Crawler import Crawler

class HistoryCrawler(Crawler):
    
    def parse_menu(self):
        lis=self.soup.select(".leftList > li")
        for li in lis:
            a=li.a
            if not a==None and not a.string==None: 
                self.urls.append(a)
            
    def parse_body(self,soup):
        html=soup.select("#f_article")[0]
        return str(html)
    
    def changeFileStruct(self, soup, title):
        article=soup.select("#f_article")[0]
        center=soup.new_tag("center")
        h1=soup.new_tag("h1")
        h1.string=title
        center.insert(0,h1)
        article.insert(0,center)
        html = self.verifyUrl(str(soup))
        html=Crawler.HTML_TEMPLATE.format(content=html)
        return html
    
    
      
        
       
 
    
def test():
    crawler = HistoryCrawler("http://www.sbkk88.com/mingzhu/zhonghuashangxiawuqiannian/","上下五千年-曹余章著",pageencoding="gbk"
                             ,cssFilePath="G:\\css\\history.css")
    crawler.parse_menu() 
    crawler.crawl_file()
    crawler.changeFiles()    #changeFiles 和addCssFiles 都对文档进行了遍历，理应合并到一处提高效率
    crawler.addCssFiles()
    crawler.saveAsPdf()

def main():
    test()
#     crawler.crawl_file()
#     crawler.changeFiles()
#
    

if __name__ =="__main__":
    main()
        
