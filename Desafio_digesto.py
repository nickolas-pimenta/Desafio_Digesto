import requests
import pandas as pd 
from lxml import html
import os 
import sys
import json
script_dir = os.path.abspath(os.path.dirname(sys.argv[0]) or '.')

class Crawler_Tabela():  
    def Extracao_Pagina_Alvo_1(self):
        df = pd.DataFrame(columns=['Storage','CPU', 'Memory','Bandwidth', 'Price'])
        resposta = requests.get('https://www.vultr.com/products/cloud-compute/#pricing')
        conteudo_site = html.fromstring(resposta.content)
        
        if resposta.status_code == 200:
            div_tabela = '//div[@class = "pt__body js-body"]'
            tabela = conteudo_site.xpath(div_tabela)[0]
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
        return df    
    
    def Extracao_Pagina_Alvo_2(self):

        df = pd.DataFrame(columns=['Memory','vCPUs', 'Transfer','SSD Disk', '$/MO'])
        resposta = requests.get('https://www.digitalocean.com/pricing/')
        conteudo_site = html.fromstring(resposta.content)
        
        if resposta.status_code == 200:
            selecionar_tabela = '//table[@class = "table is-scrollable css-1map1ow is-fullwidth is-striped"]'
            tabela = conteudo_site.xpath(selecionar_tabela)[0]
            linhas_tabela = tabela.xpath('.//tr')
            for interacao in range(1,len(linhas_tabela)):
                conteudo_tabela = linhas_tabela[interacao].xpath('.//td')
                informacoes = []
                informacoes.append(conteudo_tabela[0].text_content())
                informacoes.append(conteudo_tabela[1].text_content())
                informacoes.append(conteudo_tabela[2].text_content())
                informacoes.append(conteudo_tabela[3].text_content())
                informacoes.append(conteudo_tabela[5].text_content())
                
                df.loc[interacao-1] = informacoes
        return df

    def Salva_Json(self,df):
        print("Insera o nome do arquivo, mas não coloque .json")
        nome = input()
        dic = df.to_dict()
        with open(script_dir+'\\'+nome+'.json', 'w') as data:
            json.dump(dic, data,indent=4)

    def Salva_CSV(self,df):
        print("Insera o nome do arquivo, mas não coloque .csv")
        nome = input()
        df.to_csv(script_dir+'\\'+nome+'.csv',index=False)

    def Print_informacoes(self,df):
        print(df)
          

    def Acoes(self):
        df_pagina1 = self.Extracao_Pagina_Alvo_1()
        df_pagina2 = self.Extracao_Pagina_Alvo_2()
        if not df_pagina1.empty and not df_pagina2.empty:
            acao = -1
            while acao != 0: 
                print("Selecione a ações que deseja realizar")
                acao = input("Digite 1 para imprimir os dados, 2 para salvar em CSV, 3 para salvar em json ou 0 para 

encerrar: ")
                if acao != "0":
                    pagina = input("Sobre os dados de qual página deseja realizar a operação? 1 para a página alvo 1 

ou 2 para a página alvo 2: ")
                
                if acao == "1" and pagina == "1":
                    self.Print_informacoes(df_pagina1)
                elif acao == "2" and pagina == "1":
                    self.Salva_CSV(df_pagina1)
                elif acao == "3" and pagina == "1":
                    self.Salva_Json(df_pagina1)
                elif acao == "1" and pagina == "2":
                    self.Print_informacoes(df_pagina2)
                elif acao == "2" and pagina == "2":
                    self.Salva_CSV(df_pagina2)
                elif acao == "3" and pagina == "2":
                    self.Salva_Json(df_pagina2)                 
                elif acao == "0":
                    return None
                else:
                    print("input inválido\n")
        else:
            print("Não foi possível extrair os dados")
        

if __name__ == "__main__":
    Extrator_de_Dados = Crawler_Tabela()
    Extrator_de_Dados.Acoes()
