## Extração de Dados de Vendas da SteamDB com Selenium e Armazenamento em Parquet

Este projeto utiliza o Selenium para automatizar a extração de dados de vendas em andamento no site SteamDB, formatá-los em um DataFrame Pandas e, em seguida, armazená-los em um arquivo Parquet de alta performance para futuras análises.
Estrutura do Projeto

    README.md: Este arquivo de documentação.
    steam_sales_scraper.py: Script Python contendo o código para extração e armazenamento dos dados.

## Dependências

Certifique-se de ter as seguintes bibliotecas Python instaladas:

    pandas
    pyarrow
    selenium
    webdriver-manager

## Funcionamento

    Configuração do WebDriver:
        O script instala automaticamente o ChromeDriver necessário.
        Um driver do Chrome é inicializado.

    Navegação e Interação com a Página:
        O driver acessa a página de vendas da SteamDB.
        Espera-se que a página carregue completamente e o menu dropdown de exibição de itens por página seja exibido.
        O menu dropdown é clicado, e a opção de exibir todos os itens é selecionada.
        É adicionado um pequeno atraso para garantir que todos os dados sejam carregados.

    Extração dos Dados:
        A tabela de vendas é localizada na página.
        O script percorre as linhas da tabela, extraindo o texto de cada célula (coluna) e armazenando em uma lista.

    Formatação e Armazenamento em Parquet:
        A lista de dados extraídos é transformada em um DataFrame Pandas.
        O DataFrame é salvo em um arquivo Parquet chamado dados.parquet, utilizando o motor PyArrow para otimizar o desempenho.

    Encerramento do WebDriver:
        O driver do Chrome é encerrado para liberar recursos.

## Utilização

    Certifique-se de ter as dependências instaladas (veja a seção "Dependências").
    Execute o script steam_sales_scraper.py.
    O arquivo dados.parquet será criado na mesma pasta do script, contendo os dados das vendas extraídos.

## Observações

    Este script é sensível a mudanças na estrutura da página da SteamDB. Caso o site seja atualizado, o código pode precisar de ajustes para funcionar corretamente.
    A extração de dados em grande escala pode ser limitada por mecanismos de proteção contra bots do site.
    O uso de um arquivo Parquet permite um armazenamento eficiente e uma leitura rápida dos dados para futuras análises com Pandas ou outras ferramentas compatíveis.
