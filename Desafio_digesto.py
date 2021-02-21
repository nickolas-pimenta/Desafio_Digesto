import requests
import pandas as pd 
from lxml import html
import os 
import sys
script_dir = os.path.abspath(os.path.dirname(sys.argv[0]) or '.')

class Crawler_Tabela:  
    

    df = pd.DataFrame(columns=['Storage','CPU', 'Memory','Bandwidth', 'Price'])
    resposta = requests.get('https://www.vultr.com/products/cloud-compute/#pricing')
    text = html.fromstring(resposta.content)
    
    if resposta.status_code == 200:
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
    else:
        print("não foi possível extrair as informações")

    def Salva_Json(self,df):
        

    def Salva_CSV(self,df):
        print("Insera o nome do arquivo, mas não coloque .csv")
        nome = input()
        df.to_csv(script_dir+'\\'+nome+'.csv',index=False)

    def Acoes(self):
        if not self.df.empty:
            acao = -1
            while acao != 0: 
                print("Selecione a ações que deseja realizar")
                acao = input("Digite 1 para imprimir os dados, 2 para salvar em CSV, 3 para salvar em json ou 0 para encerrar: ")
                
                if acao == "1":
                    print(self.df)
                elif acao == "2":
                    self.Salva_CSV(self.df)
                elif acao == "3":
                    self.Salva_Json(self.df)
                elif acao == "0":
                    return None
                else:
                    print("input inválido\n")

 
        

if __name__ == "__main__":
    Extrator_de_Dados = Crawler_Tabela()
    Extrator_de_Dados.Acoes()
