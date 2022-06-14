# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request



class AgriSpider(scrapy.Spider):
    name = 'agri'
    allowed_domains = ['www.agrios.it']
    start_urls = ['http://www.agrios.it/fuer-obstbauern/pflanzenschutzmittel-seite/']
  
    def parse(self, response):
        
        cat = response.xpath('//a[@class="fancybox"]/@href').getall()
        for catone in cat:
            link = catone.strip('#')
            
            #links = response.urljoin(catone)
           # print(link)
            
            #yield Request(url=links, callback=self.parse_list)
        
            title = response.xpath(f'//div[@id="{link}"]/p/text()').getall()
            keys = response.xpath(f'//div[@id="{link}"]/div/div[1]/text()').getall()
            values = response.xpath(f'//div[@id="{link}"]/div/div[2]/text()').getall()
            for ti in title:
                ti
            dictionary = {}
            for key in keys:
                for value in values:
                    dictionary[key.strip('\t\n  ')]= value.strip('\t\n  ')
            
            dec = []
            dec.append(dictionary)
            for de in dec:
                Wirkstoff = de.get('Wirkstoff:')

                WirkstoffGruppe = de.get('Wirkstoff-Gruppe:')
                MaxEinsätzeproJahr = de.get('Max. Einsätze pro Jahr:')
                DosisproHL = de.get('Dosis pro HL:')
                DosisproHA = de.get('Dosis pro HA:')
                Karenzzeit = de.get('Karenzzeit:')
                bienengefährlich = de.get('bienengefährlich:')
                Einschränkung = de.get('Einschränkung:')
                '''if not Wirkstoff:
                    Wirkstoff = ''
                    
                
                if not WirkstoffGruppe:
                    WirkstoffGruppe = ''
                    

                if not MaxEinsätzeproJahr:
                    MaxEinsätzeproJahr = ''
                    
                if not DosisproHL:
                    DosisproHL = ''
                    

                if not DosisproHA:
                    DosisproHA = ''
                    
                if not Karenzzeit:
                    Karenzzeit = ''
                   

                if not bienengefährlich:
                    bienengefährlich = ''
                    
                if not Einschränkung:
                    Einschränkung = ''
                '''   

    
        
            yield{
                'Title' : ti,
                'Wirkstoff' : Wirkstoff,
                'Wirkstoff-Gruppe' : WirkstoffGruppe,
                'Max. Einsätze pro Jahr' : MaxEinsätzeproJahr,
                'Dosis pro HL' : DosisproHL,
                'Dosis pro HA' : DosisproHA,
                'Karenzzeit' : Karenzzeit,
                'bienengefährlich' : bienengefährlich,
                'Einschränkung' : Einschränkung
                
             }


        pass
