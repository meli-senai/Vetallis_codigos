import urllib.parse
import requests

def valida_funcao_prod(dados_func):
    if dados_func['funcao'] == '':
            return False
        
    if len(dados_func['funcao']) <= 3:
        return False

    for caractere in dados_func['funcao']:
        if caractere.isdigit():
            return False  
    
    return True

def valida_nome_usuario(dado_login):
    if dado_login["nome"] !='':
        if len(dado_login["nome"]) >= 5:
            return True
        else:
            return False
    else:
        return False

def valida_senha(dados):
    if dados["senha"] != '':
        if len (dados["senha"]) >= 5:
            return True
    else:
        return False
    
def valida_uso_prod (dados_atualizar):
    if len(dados_atualizar["motivo"]) >= 10:
        return True
    return False

def valida_nome_prod (dados_produto):
    if len (dados_produto ["nome"]) >= 5:
        return True
    return False

def valida_quant(dados_produto):
    if int(dados_produto['quantidade']) >= 5:
        return True
    return False

def valida_lote(dados_lote):
    if len(dados_lote['lote']) > 2:
        for caracter in dados_lote['lote']:
            if caracter.isdigit():
                return True
    return False

def valida_data(dados_compra):
    meses = ['01', '02', '03', '04', '05', '06',
             '07', '08', '09', '10', '11', '12',]
    if len(dados_compra["nome"]) > 3:
        print("data", dados_compra["data"])
        if len(dados_compra["data"]) == 10:
            for data in dados_compra["data"]:
                if not(data.isdigit() or data == "/"):
                    data_correta = False
                    break
                else:
                    data_correta = True
            if data_correta == True:
                print("dia", dados_compra["data"][0:1])
                if int(dados_compra["data"][6:]) >= 2025:
                    if dados_compra["data"][3:5] in meses:
                        if dados_compra["data"][3:5] in ['01', '03', '05', '07', '08', '10', '12']:
                            if 0 < int(dados_compra["data"][0:2]) <= 31:
                                return True
                            else:
                                return False
                        elif dados_compra["data"][3:5] in ['04', '06', '09', '11']:
                            if 0 < int(dados_compra["data"][0:2]) <= 30:
                                return True
                            else:
                                return False
                        else:
                            if int(dados_compra["data"][0:2]) == 28:
                                return True
                            else:
                                return False
                    else:
                        return ("mes incorreto")
                else:
                    return ("ano incorreto")
            else:
                return ("data incorreta")
        else:
            return ("erro quantidade de caracteres")
    else:
        return ("erro no nome")
    return False

def valida_cpf (cpf,token):
    #URL basica da API
    url = "https://api.invertexto.com/v1/validator"

    #parâmetros que serão enviados via query string
    params={
        "token":token,
        "value":cpf # no exemplo, 'value' representa o cpf
    }
    try:
        #envia a requisição GET com os parâmetros
        response = requests.get(url, params=params)
        response.raise_for_status()#levanta exceçãopara statu HTTP de erro

        #converte a resposta para JSON
        data= response.json()
        if data["valid"] == True:
            return True
        return False

    except requests.exceptions.HTTPError as errh:
        print("Erro HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Erro de conexão:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout:",errt)
    except requests.exceptions.RequestException as err:
        print ("Erro:", err)

    return False

def valida_email(email, token):
    #URL base da API de validação de e-mail
    base_url= "https://api.invertexto.com/v1/email-validator"

    #codifica o email para garantir que a URL fique correta
    email_encoded = urllib.parse.quote (email)

    #Monta a URL com o e-mail na rota
    url= f"{base_url}/{email_encoded}"

    #parâmetros da query string (nesse caso, apenas o token)
    params = {"token": token}

    try:
        #realiza a requisição GET passado os parâmetro na URL
        response = requests.get (url, params=params)
        response.raise_for_status()#Levanta exceção para status HTTP de erro

        #Converte a resposta para JSON
        data = response.json()
        if data["valid_format"] == True and data["valid_mx"] == True and  data["disposable"] == False:
            return True
        return False

    except requests.exceptions.HTTPError as errh:
        print("Erro HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Erro de conexão:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout:",errt)
    except requests.exceptions.RequestException as err:
        print ("Erro:", err)

        return False