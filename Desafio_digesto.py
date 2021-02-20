import requests
import pandas as pd 
from lxml import html

class Crawler_Tabela:

    df = pd.DataFrame(columns=['Storage','CPU', 'Memory','Bandwidth', 'Price'])
    resposta = requests.get('https://www.vultr.com/products/cloud-compute/#pricing')
    text = html.fromstring(resposta.content)
    
    if resposta.status_code == 200:
        try:
            div_tabela = '//div[@class = "pt__body js-body"]'
            tabela = text.xpath(div_tabela)[0]
            div_linhas = tabela.xpath('./div')
                
            for interacao in range(0,len(div_linhas)):
                informacoes = []
                div_content = div_linhas[interacao].xpath('./div[@class = "pt__row-content"]')[0]

                divs_texto = div_content.xpath('./div')
                
                informacoes.append(divs_texto[1].text_content().strip())
                informacoes.append(divs_texto[2].text_content().strip())
                informacoes.append(divs_texto[3].text_content().strip().split('Ram')[0])
                informacoes.append(divs_texto[4].text_content().strip().split('Bandwidth')[0])
                informacoes.append(divs_texto[5].text_content().strip().split('\n')[0])
                
                df.loc[interacao] = informacoes
           
        except:
            pass
        
        print(df)
        

        

if __name__ == "__main__":
    teste = Crawler_Tabela()
