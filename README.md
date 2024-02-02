# SmartInvest AI

## Visão Geral

O SmartInvest AI é um painel de análise de investimentos para o mercado de ações, projetado para ajudar investidores a monitorar e analisar o desempenho dos ativos em suas carteiras em tempo real. Com funcionalidades que incluem o registro de transações, visualizações gráficas detalhadas e a comparação com o índice IBOV, o SmartInvest AI auxilia na tomada de decisões de investimento mais informadas. A integração com a API do ChatGPT oferece um consultor financeiro inteligente, proporcionando análises aprofundadas e recomendações personalizadas.

## Estrutura do Código

O aplicativo é composto por diversos componentes principais, organizados da seguinte forma:

- `app.py`: Inicializa o aplicativo, configura estilos, gerencia exceções de callback e define configurações do servidor.
- `index.py`: Responsável por rodar o aplicativo e gerenciar as rotas ou páginas do aplicativo.
- `utils/functions.py`: Funções utilitárias para manipulação de dados e interação com a API do TradingView.
- `components/`: Diretório contendo os componentes do Dash, como a carteira (`wallet.py`), modal de cadastro de ativos (`modal.py`), página inicial (`home.py`), cabeçalho (`header.py`), integração ChatGPT (`chatgpt.py`), e outros.
- `tvdatafeed/`: Módulos para interação com a API do TradingView, incluindo `consumer.py`, `datafeed.py`, `main.py` e `seis.py`.

## Funcionalidades

- Monitoramento em tempo real dos ativos
- Registro e acompanhamento de transações de compra e venda
- Visualizações gráficas para análise dos ativos
- Comparação do desempenho da carteira com o IBOV
- Consultoria financeira através da integração com o ChatGPT

## Instalação

Clone o repositório para obter a última versão do SmartInvest AI:

```
git clone https://github.com/takeonepilot/Smart_Invest_AI.git
```

## Docker

Instalção via Docker, execute os seguintes comandos:

```
docker build -t smart_invest_ai .
```

```
docker run -d --name mart_invest_ai -p 8080:8080 smart_invest_ai
```

## Local

Instale as dependências necessárias para executar o aplicativo:

```
pip install -r requirements.txt
```

## Execução

Para iniciar o aplicativo, execute:

```
python index.py
```

## Contribuição

Contribuições são sempre bem-vindas! Se você tem alguma sugestão para melhorar o aplicativo, sinta-se à vontade para criar uma issue ou enviar um pull request.

## Contato

Para dúvidas, sugestões ou contribuições, sinta-se à vontade para abrir uma [Issue](https://github.com/takeonepilot/Smart_Invest_AI/issues) aqui no GitHub ou me seguir e entrar em contato através do [meu perfil no GitHub](https://github.com/takeonepilot).

## Licença

SmartInvest AI é distribuído sob a licença MIT.
