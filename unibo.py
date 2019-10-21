from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

from scraper import implements, Scraper

class Unibo(implements(Scraper)):
	def __init__(self, link):
		self.link = link

		self.currentLaurea = None
		self.currentTitolo = None
		self.currentPageLink = None
		
		self.countTesi = 0

	def scrape(self):
		response = requests.get(self.link)
		assert response.status_code == 200
		soup = BeautifulSoup(response.text, 'html.parser')
		elenco_corsi = soup.find("div",{"class":"ep_toolbox_content"})
		for corso in elenco_corsi.contents[0].contents[0].findAll('ul'):
			self.currentLaurea = corso.a.text
			self.scrapeCorso( urljoin(self.link, corso.a['href']) )
		print(
			"Numero tesi trovate: {}".format(self.countTesi)
			)

	def scrapeCorso(self, linkCorso):
		responseCorso = requests.get(linkCorso)
		assert responseCorso.status_code == 200
		soup = BeautifulSoup(responseCorso.text, 'html.parser')
		year_ul_tag = soup.find("div",{"class":"ep_view_menu"}).contents[4]
		for anno in year_ul_tag.findAll("li"):
			self.scrapeCorsoAnno( urljoin(linkCorso,anno.a['href']) )


	def scrapeCorsoAnno(self, linkCorsoAnno):
		responseCorsoAnno = requests.get(linkCorsoAnno)
		assert responseCorsoAnno.status_code == 200
		soup = BeautifulSoup(responseCorsoAnno.text, 'html.parser')
		for tesiHtml in soup.findAll('p'):
			tesiSumm = tesiHtml.text.replace("\n","")
			if "ALMA MATER STUDIORUM - Università di Bologna, 2007-2019" in tesiSumm:
				continue
			if "Documento full-text non disponibile" in tesiSumm:
				continue
			if "Documento ad accesso riservato" in tesiSumm:
				continue
			#print(tesiSumm)
			#print('####################')
			self.countTesi = self.countTesi + 1

if __name__ == '__main__':
	Unibo("https://amslaurea.unibo.it/view/cds/cds/").scrape()
	