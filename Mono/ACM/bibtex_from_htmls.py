
import urllib2
import time
import pdb

def bibtex_from_urls(urls):
    data = []
    for u in urls:
        safe_url = urllib2.quote(u, safe='')
        safe_url = "http://scraper.bibsonomy.org/service?format=bibtex&selection=&url=" + safe_url
        #print safe_url
        result = urllib2.urlopen("http://scraper.bibsonomy.org/service?format=bibtex&selection=&url=" + safe_url)
        bibtex = result.read()
        data.append(bibtex)
        pdb.set_trace()
        print bibtex
        time.sleep(10)
    return data
    
if __name__ == "__main__":
    urls = [
        "http://dl.acm.org/citation.cfm?id=1833315&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2428782&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2597728&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2808685&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=604253&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2632447&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2379674&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2557845&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2048186&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1134503&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2695789&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2431926&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1145641&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2724930&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1358649&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1137631&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2857225&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1753212&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2480560&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2894793&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2797469&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2814105&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1062480&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=940094&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2237803&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1822341&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1024344&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2816884&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1151436&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1119678&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2732155&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2639503&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=966239&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2381790&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2638409&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2804373&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=361653&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1047494&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2896948&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1176750&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1181927&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2000291&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1985784&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1852806&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=769966&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1869624&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1083300&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2732157&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1028720&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=3011096&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1121387&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1985901&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2593718&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1985816&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2788628&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2686956&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2856655&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1062473&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2838764&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2593820&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2508075&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1987900&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=564106&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1852805&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2693983&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2973850&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2829919&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=584992&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=2090129&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=581426&amp;CFID=721852404&amp;CFTOKEN=37499090",
        "http://dl.acm.org/citation.cfm?id=1984732&amp;CFID=721852404&amp;CFTOKEN=37499090"
    ]
    bibtex = bibtex_from_urls(urls)
    print "="*100
    print "\r\n".join(bibtex)
