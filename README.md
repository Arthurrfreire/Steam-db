# Web Scraping com Selenium

Este projeto utiliza o Selenium para raspar dados de um site. Neste caso, estou raspando dados do site SteamDB.

## Dependências

Este projeto depende das seguintes bibliotecas Python:

- Selenium
- pandas
- pyarrow
- webdriver_manager

## Instalação

Você pode instalar todas as dependências com o seguinte comando:

pip install selenium pandas pyarrow webdriver_manager

## Como usar
Para usar este script, siga os passos abaixo:

Clone este repositório para o seu computador.
Navegue até a pasta do projeto.
Execute o script Python com o comando python extrair_dados.py.
O script irá abrir uma janela do navegador, navegar até o site SteamDB, selecionar a opção para exibir todos os resultados na página, e então raspar os dados da tabela de vendas. Os dados raspados serão salvos em um arquivo Parquet chamado dados.parquet.

## Notas
Este script foi testado no Windows com o Google Chrome. Se você estiver usando um sistema operacional ou navegador diferente, pode ser necessário ajustar o código para funcionar corretamente.
