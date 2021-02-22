import requests
import pandas as pd 
from lxml import html
import os 
import sys
import json
# Este comando identifica o repositório em que o arquivo do programa esta guardado e usa o mesmo endereco para salvar os arquivos CSV e JSON
script_dir = os.path.abspath(os.path.dirname(sys.argv[0]) or '.')


# Classe do Crawler que contém todos os metodos utilizados
class Crawler_Tabela(): 


# Este metodo extrai as informacoes da pagina alvo 1 e retorna elas no formato de data frame      
    def Extracao_Pagina_Alvo_1(self):

        df = pd.DataFrame(columns=['Storage','CPU', 'Memory','Bandwidth', 'Price'])
        resposta = requests.get('https://www.vultr.com/products/cloud-compute/#pricing')
        conteudo_site = html.fromstring(resposta.content)
        
        if resposta.status_code == 200:
# Aqui o comando seleciona a tabela desejada via xpath
            div_tabela = '//div[@class = "pt__body js-body"]'
            tabela = conteudo_site.xpath(div_tabela)[0]
# Aqui o comando seleciona as linhas da tabela via xpath
            div_linhas = tabela.xpath('./div')
                
            for interacao in range(0,len(div_linhas)):
# A partir daqui os textos da tabela estao sendo selecionados e tratados para serem convertidos em data frame
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
    
# Este metodo extrai as informacoes da pagina alvo 2 e retorna elas no formato de data frame     
    def Extracao_Pagina_Alvo_2(self):

        df = pd.DataFrame(columns=['Memory','vCPUs', 'Transfer','SSD Disk', '$/MO'])
        resposta = requests.get('https://www.digitalocean.com/pricing/')
        conteudo_site = html.fromstring(resposta.content)
        
        if resposta.status_code == 200:
# Aqui o comando seleciona a tabela desejada via xpath
            selecionar_tabela = '//table[@class = "table is-scrollable css-1map1ow is-fullwidth is-striped"]'
            tabela = conteudo_site.xpath(selecionar_tabela)[0]
# Aqui o comando seleciona as linhas da tabela via xpath
            linhas_tabela = tabela.xpath('.//tr')

            for interacao in range(1,len(linhas_tabela)):
# A partir daqui os textos da tabela estao sendo selecionados e tratados para serem convertidos em data frame             
                conteudo_tabela = linhas_tabela[interacao].xpath('.//td')
                informacoes = []
                informacoes.append(conteudo_tabela[0].text_content())
                informacoes.append(conteudo_tabela[1].text_content())
                informacoes.append(conteudo_tabela[2].text_content())
                informacoes.append(conteudo_tabela[3].text_content())
                informacoes.append(conteudo_tabela[5].text_content())
                
                df.loc[interacao-1] = informacoes
        else:
            print("não foi possível extrair as informações")
        return df


# Este metodo salva as informacoes no formato JSON. Ele recebe um data frame, pede para o usuario inserir o nome que dejesa para o arquivo e o salva no mesmo diretorio que o programa esta salvo
    def Salva_Json(self,df):
        print("Insera o nome do arquivo, mas não coloque .json")
        nome = input()
        dic = df.to_dict()
        with open(script_dir+'/'+nome+'.json', 'w') as data:
            json.dump(dic, data,indent=4)
        print("arquivo salvo com sucesso\n")

# Este metodo salva as informacoes no formato CSV. Ele recebe um data frame, pede para o usuario inserir o nome que dejesa para o arquivo e o salva no mesmo diretorio que o programa esta salvo
    def Salva_CSV(self,df):
        print("Insera o nome do arquivo, mas não coloque .csv")
        nome = input()
        df.to_csv(script_dir+'/'+nome+'.csv',index=False)
        print("arquivo salvo com sucesso\n")


# Este metodo recebe um data frame e printa suas informaçoes.
    def Print_informacoes(self,df):
        print(df)
        print("")
          

# Este metodo executa o menu que o usuario interage e controla quando um determinado metodo deve ser chamado
    def Menu(self):
        df_pagina1 = self.Extracao_Pagina_Alvo_1()
        df_pagina2 = self.Extracao_Pagina_Alvo_2()
        if not df_pagina1.empty and not df_pagina2.empty:
            acao = -1
            while acao != 0: 
                print("Selecione qual função deseja executar")
                acao = input("Digite 1 para imprimir os dados, 2 para salvar em CSV, 3 para salvar em json ou 0 para encerrar: ")
                if acao != "0":
                    pagina = input("Sobre os dados de qual página deseja realizar a operação? 1 para a página alvo 1 ou 2 para a página alvo 2: ")
                
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
# Aqui cria-se uma instancia da classe e executa o metodo Acoes
    Extrator_de_Dados = Crawler_Tabela()
    Extrator_de_Dados.Menu()
