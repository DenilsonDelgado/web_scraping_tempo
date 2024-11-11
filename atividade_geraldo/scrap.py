import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Função para enviar o e-mail
def send_email(subject, body, to_email):
    from_email = getenv("EMAIL_ADDRESS", '')# Seu e-mail
    from_password = getenv("EMAIL_PASSWORD","")  # Sua senha de e-mail (considere usar OAuth2 ou senhas de app, se possível)
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Configurar servidor SMTP do Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Começar criptografia
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()  # Fechar conexão
        print(f"[-] E-mail enviado para {to_email} com sucesso!")
    except Exception as e:
        print(f"[-] Erro ao enviar e-mail: {e}")

def get_temperature(cidade_id, to_email):
    url = f"https://www.climatempo.com.br/previsao-do-tempo/cidade/{cidade_id}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    min_temp = soup.find("span", id="min-temp-1")
    max_temp = soup.find("span", id="max-temp-1")

    temperature_info = f"[-] A TEMPERATURA MÁXIMA EM {nome_cidade.upper()} - {estado} É DE {max_temp.text}, COM MÍNIMA DE {min_temp.text}"
    print(temperature_info)
    
    # Enviar e-mail com as informações
    send_email("Previsão do Tempo", temperature_info, to_email)

def get_city_id(city_name, to_email):
    global cidade_id, nome_cidade, estado
    url = "https://www.climatempo.com.br/json/busca-por-nome"
    payload = {"name": city_name}
    response = requests.post(url, data=payload)
    data = response.json()
    if data[0]["response"]["success"]:
        cidade_id = data[0]["response"]["data"][0]["idcity"]
        nome_cidade = data[0]["response"]["data"][0]["city"]
        estado = data[0]["response"]["data"][0]["uf"]
        get_temperature(cidade_id, to_email)
    else:
        print("[-] CIDADE NÃO ENCONTRADA!")

# Entrada de dados
city_name = input("[-] NOME DA CIDADE: ").strip()
to_email = input("[-] EMAIL: ").strip()
get_city_id(city_name, to_email)
