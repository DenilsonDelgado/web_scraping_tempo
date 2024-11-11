# Previsão do Tempo - Web Scraping e Envio de E-mail

Este é um script Python da minha atividade da aula de coding, que realiza web scraping para buscar a previsão do tempo de uma cidade específica, 
utilizando a API do Climatempo. Após coletar as informações de temperatura máxima e mínima,
o script envia essas informações para o e-mail fornecido pelo usuário.

## Funcionalidades

- **Busca de cidade e previsão do tempo**: O script permite que o usuário informe o nome de uma cidade e, por meio de web scraping, coleta a previsão do tempo da cidade, incluindo as temperaturas mínima e máxima.
- **Envio de e-mail**: As informações de previsão de temperatura são enviadas para o e-mail informado pelo usuário.

## Dependências

O script utiliza as seguintes bibliotecas:
- `requests`: Para realizar a requisição HTTP e obter os dados da página.
- `beautifulsoup4`: Para realizar o parsing do HTML e extrair as informações da previsão do tempo.
- `smtplib`: Para o envio de e-mails.
- `email.mime`: Para a formatação e envio de e-mails.
- `dotenv`: Para carregar variáveis de ambiente, como as credenciais de e-mail de forma segura.

Instale as dependências necessárias utilizando o seguinte comando:

```bash
pip install requests beautifulsoup4 python-dotenv
