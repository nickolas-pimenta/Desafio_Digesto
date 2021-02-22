# Desafio digesto

## Sobre o desafio

O desafio consistiu em criar robôs que conseguissem entrar nos links, https://www.vultr.com/products/cloud-compute/#pricing e https://www.digitalocean.com/pricing, para extrair informações de tabelas contidas em seus html’s e disponibilizar ao usuário do programa opções para imprimir os dados, salvar em CSV ou salvar em JSON.<br> 											
<br>A primeira URL foi chamada de página alvo 1 e a segunda de página alvo 2, dessa forma, seguirei me referindo a ambas de acordo.<br> 	
<br>Para a página alvo 1 o desafio era extrair informações da tabela abaixo:

![tabela alvo 1](https://user-images.githubusercontent.com/79375722/108646370-5ed60c00-7494-11eb-8803-3c5b43335e32.JPG)
**Tabela página alvo 1**

Nas instruções do desafio constava  que apenas as informações das colunas Storage, CPU, Memory, Bandwidth e Price deveriam ser extraídas e portanto o projeto seguiu com esse padrão.

Para a página alvo 2 o desafio era extrair informações da tabela abaixo:
![tabela alvo 2](https://user-images.githubusercontent.com/79375722/108646622-4c100700-7495-11eb-898a-60b5f94f5242.JPG)

**Tabela página alvo 2**

Como na página alvo 1 apenas parte da tabela era necessária, para este caso as colunas são Memory, vCPUs, Transfer, SSD Disk e $/MO.


## Requisitos do sistema

O programa foi construído em cima da versão 3.7.4 do python e utilizou as seguintes bibliotecas:

+ **os** - biblioteca padrão da linguagem
+ **sys** - biblioteca padrão da linguagem
+ **json** - biblioteca padrão da linguagem
+ **requests==2.25.0**
+ **pandas==1.1.4**
+ **lxml==4.6.2**

## O porque da escolha dessas bibliotecas 

O desafio exigiu diversas etapas de resolução, para cada uma delas foi necessário utilizar ferramentas diferentes, seguem abaixo seus objetivos:

+ **requests** - possibilita se conectar com as páginas e extrair o html delas
+ **html da biblioteca lxml** - permite selecionar os elementos desejados pelo xpath e extrair os textos dentros deles
+ **pandas** - permite estruturar os textos extraídos e conservar no formato de tabela, além disso consegue facilmente exportar os dados no formato csv
+ **json + pandas** - a biblioteca pandas permite converter o data frame em dicionário, dessa forma, a biblioteca json recebendo isso consegue gerar um arquivo json já identado e de fácil visualização
+ **os e sys** - para facilitar a exportação dos arquivos e não se preocupar para qual diretório eles vão, as bibliotecas os e sys permitiram identificar o mesmo diretório que o código fonte está hospedado e exportar os arquivos para o mesmo local

## Como utilizar

Depois de instalar o python e as bibliotecas, basta executar o programa. Com isso um menu irá estar disponível para o usuário decidir qual função executar e sobre os dados de qual página.

![menu inicial](https://user-images.githubusercontent.com/79375722/108646838-ea03d180-7495-11eb-9caa-c48d8c75ab61.JPG)<br>
**Menu inicial**


![menu de seleção](https://user-images.githubusercontent.com/79375722/108646846-ed975880-7495-11eb-982b-2bfe4c06b4ed.JPG)<br>
**Após selecionar uma função**

![realizado](https://user-images.githubusercontent.com/79375722/108646853-f2f4a300-7495-11eb-90d7-5c2774852107.JPG)<br>
**Depois de selecionar a função e os dados de uma das páginas**

Depois de executar a função, o menu volta para o estado inicial e aguarda o próximo comando do usuário, sendo ele para selecionar outra função ou encerrar.

**Obs:** Além da interação do usuário com o menu, caso ele deseje salvar o arquivo tanto em CSV ou JSON o programa pedirá um nome para o arquivo, após a inserção, um arquivo do tipo selecionado irá ser criado dentro do diretório em que o arquivo próprio programa está hospedado  

## Problemas conhecidos

O programa funciona bem para as páginas alvo, porém caso haja algum tipo de mudança nos códigos html das páginas, o robô pode vir a precisar de manutenção para se readequar ao novo padrão. 


