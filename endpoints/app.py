from flask import Flask, jsonify, request
from validacao import valida_funcao_prod, valida_nome_usuario, valida_senha, valida_uso_prod, valida_nome_prod, valida_cpf, valida_data, valida_email, valida_lote, valida_quant
from inserir import adicionar_usuario
from consultar import consultar_usuario
from atualizar import atualizar_usuario
from deletar import deletar_usuario_bd

app = Flask(__name__)

token = "22453|iIY9kltE4ObDytgOSmIAOKmlic2hmGDh"

# Listas
compra = []
uso = []
sensor = []
login = []
cont_saida = []
itens = []
alerta = []
cont_ent = []
produtos = []
usuarios = []
estoque = {}

estoque['compra'] = compra
estoque['uso'] = uso
estoque['sensor'] = sensor
estoque['login'] = login
estoque['itens'] = itens
estoque['alerta'] = alerta
estoque['cont_ent'] = cont_ent
estoque['produtos'] = produtos

# Rota Principal


@app.route("/")
def home():
    return "Bem-vindo à Vetalis"


# -------------------- Motivo de uso do medicamento --------------------#

# Listar motivos de uso do remedios

@app.route("/estoque/motivos_uso", methods=["GET"])
def listar_uso():
    return jsonify(uso)


# Buscar por motivo uso do medicamento
@app.route("/estoque/motivos_uso/<int:indice>", methods=["GET"])
def busca_uso(indice):
    if indice < len(uso):
        return jsonify(uso[indice])
    return jsonify({"erro": "Remédio não encontrado"}), 404


# Adicionar motivo do uso do remedio
@app.route("/estoque/uso", methods=["POST"])
def add_remedio():
    novo_remedio = request.get_json()
    uso.append(novo_remedio)
    resp_motivo = valida_uso_prod(novo_remedio)
    resp_nome = valida_nome_prod(novo_remedio)
    resp_qtd = valida_quant(novo_remedio)
    if resp_motivo and resp_nome and resp_qtd:
        return jsonify({"mensagem": "Remédio usados com sucesso!"}), 201
    else:
        return jsonify({"Valido": False, "Mensagem": "Erro ao tirar medicamento do estoque"})

# Atualizar motivos de uso do medicamento
@app.route("/estoque/motivos_uso/<int:indice>", methods=["PUT"])
def up_uso(indice):
    if indice < len(uso):
        dados = request.get_json()
        uso[indice].update(dados)
        resp_motivo = valida_uso_prod(dados)
        resp_nome = valida_nome_prod(dados)
        resp_qtd = valida_quant(dados)
        if resp_nome and resp_motivo and resp_qtd:
            return jsonify({"mensagem": "Remédio atualizado"})
        else:
            return jsonify({"Valido": False, "Mensagem": "Erro na validação"})
    return jsonify({"erro": "Remédio não encontrado"}), 404

# Deletar motivos de uso do medicamento
@app.route("/estoque/motivos_uso/<int:indice>", methods=["DELETE"])
def deletar_lista_uso(indice):
    if indice < len(uso):
        uso.pop(indice)
        return jsonify({"mensagem": "Lista removida com sucesso!"})
    return jsonify({"erro": "Lista não encontrada"}), 404



# -------------------- Usuarios--------------------#

# Buscar usuario por usuario
@app.route("/estoque/usuarios/<int:indice>", methods=["GET"])
def busca_usuario(indice):
    if indice < len(usuarios):
        return jsonify(usuarios[indice])
    return jsonify({"erro": "Usuario não encontrado"}), 404

# Buscar todos os usuarios
@app.route("/estoque/usuarios", methods=["GET"])
def busca_usuarios():
    resp = consultar_usuario()
    return resp

# Adicionar usuario
@app.route("/estoque/usuarios", methods=["POST"])
def add_usuario():
    novo_usuario = request.get_json()
    usuarios.append(novo_usuario)
    resp_nome = valida_nome_usuario(novo_usuario)
    resp_senha = valida_senha(novo_usuario)
    resp_cpf = valida_cpf(novo_usuario['cpf'], token)
    resp_email = valida_email(novo_usuario['email'], token)
    if resp_nome and resp_senha and resp_cpf and resp_email:
        resp_db = adicionar_usuario(novo_usuario)
        if resp_db:
            return jsonify({"valido": True, "msg1": "dados válidos", "Resultado": resp_db})
        else:
            return jsonify({"valido": False})
    else:
        return jsonify({"valido": False, "msg1": "algum ou ambos os dados estão errados"})

# Atualizar Usuario
@app.route("/estoque/usuarios/<int:usuario_id>", methods=["PUT"])
def up_usuario(usuario_id):
    dados = request.get_json()
    resp_nome = valida_nome_usuario(dados)
    dados['usuario_id'] = usuario_id
    if resp_nome:
        resp_db = atualizar_usuario(dados)
        if resp_db:
            return jsonify( {"valido":True , "msg1": "dados Atualizados", "resultado": resp_db})
        else: 
            return False
    else:
        return jsonify({"valido": False, "msg1": "algum ou ambos os dados estão errados"})

# Deletaer usuario
@app.route("/estoque/usuario/<int:usuario_id>", methods=["DELETE"])
def deletar_usuario(usuario_id):
    resp = deletar_usuario_bd(usuario_id)
    if resp:
        return jsonify({"Mensagem": "Usuario removido com sucesso", "resultado": resp}), 200
    else:
        return False
    

#--------------------Login--------------------#

# Buscar usuarios para login
@app.route("/estoque/login/<int:indice>", methods=["GET"])
def busca_login(indice):
    if indice < len(usuarios):
        return jsonify(usuarios[indice])
    return jsonify({"erro": " erro no login"}), 404

# Listar usuarios logados
@app.route("/estoque/login/", methods=["GET"])
def busca_logins():
    return jsonify(usuarios)

# Enviar os dados para o login
@app.route("/login", methods=["POST"])
def add_login():
    ent_login = request.get_json()
    login.append(ent_login)
    resp_nome = valida_nome_usuario(ent_login)
    resp_senha = valida_senha(ent_login)
    if resp_nome and resp_senha:

        return jsonify({"Valido": True, "mensagem": "login feito com sucesso"}), 201
    else:
        return jsonify({"Valido": False, "mensagem": "Erro no Login"})
    

#--------------------Lista de compra--------------------#

# Buscar itens para a compra
@app.route("/estoque/compra/<int:indice>", methods=["GET"])
def buscar_compra(indice):
    if indice < len(compra):
        return jsonify(compra[indice])
    return jsonify({"erro": "Compra não encontrado"}), 404

# Listar produtos para a compra
@app.route("/estoque/compra", methods=["GET"])
def lista_compra():
    return jsonify(compra)

# Adicionar produto
@app.route("/estoque/compra", methods=["POST"])
def add_compra():
    nova_compra = request.get_json()
    compra.append(nova_compra)
    resp_nome = valida_nome_prod(nova_compra)
    resp_data = valida_data(nova_compra)
    if resp_nome and resp_data:
        return jsonify({"mensagem": "Compra adicionado com sucesso!"}), 201
    else:
        return jsonify({"Valido": False, "Mensagem": "Erro na validação"})

# Atualizar lista de compra
@app.route("/estoque/compra/<int:indice>", methods=["PUT"])
def up_compra(indice):
    if indice < len(compra):
        dados = request.get_json()
        compra[indice].update(dados)
        resp_nome = valida_nome_prod(dados)
        resp_data = valida_data(dados)
        if resp_nome and resp_data:
            return jsonify({"mensagem": "Compra atualizada com sucesso!"}), 201
        else: 
            return jsonify({"Validação": False, "Mensagem": "Erro na validação"})
    return jsonify({"erro": "Compra não encontrada"}), 404

# Deletaer compra
@app.route("/estoque/compra/<int:indice>", methods=["DELETE"])
def deleta_compra(indice):
    if indice < len(compra):
        compra.pop(indice)
        return jsonify({"mensagem": "Compra removida com sucesso!"}), 201
    return jsonify({"erro": "Compra não encontrada"}), 404


#--------------------Sensores--------------------#

# Buscar sensores
@app.route("/estoque/sensor/<int:indice>", methods=["GET"])
def busca_sensor(indice):
    if indice < len(sensor):
        return jsonify(sensor[indice])
    return jsonify({"erro": "Sensor não encontrado"}), 404

# Listar sensores cadastrados
@app.route("/estoque/sensor", methods=["GET"])
def lista_sensor():
    return jsonify(sensor)

# Adicionar sensores
@app.route("/estoque/sensor", methods=["POST"])
def add_sensor():
    novo_sensor = request.get_json()
    sensor.append(novo_sensor)
    resp_nome = valida_nome_usuario(novo_sensor)
    if resp_nome:
        return jsonify({"mensagem": "Sensor adicionado com sucesso!"}), 201
    else:
        return jsonify({"Validação": False, "Mensagem":"Erro na validação"})

# Atualizar sensores
@app.route("/estoque/sensor/<int:indice>", methods=["PUT"])
def up_sensor(indice):
    if indice < len(sensor):
        dados = request.get_json()
        sensor[indice].update(dados)
        resp_nome = valida_nome_usuario(dados)
        if resp_nome:
            return jsonify({"mensagem": "Sensor atualizado"})
        else:
            return jsonify({"Mensagem": "Erro na validação"})
    else:
        return jsonify({"erro": "Sensor não encontrado"}), 404
    

#--------------------Itens--------------------#

# Buscar intens
@app.route("/estoque/itens", methods=["GET"])
def busca_itens():
    return jsonify(itens)

# Buscar intem por item
@app.route("/estoque/itens/<int:indice>", methods=["GET"])
def listar_itens(indice):
    if indice < len(itens):
        return jsonify(itens[indice])
    return jsonify({"mensagem": "Iten não encontrasdo"}), 404

# Adicionar itens
@app.route("/estoque/itens", methods=["POST"])
def add_item():
    novo_item = request.get_json()
    itens.append(novo_item)
    resp_func = valida_funcao_prod(novo_item)
    resp_nome = valida_nome_prod(novo_item)
    if resp_func and resp_nome:
        return jsonify({"mensagem": "Item adicionado com sucesso!"})
    else:
        return jsonify({"Valido": False, "Mensagem": "Erro ao adiconar item"})

# Atualizar itens
@app.route("/estoque/itens/<int:indice>", methods=["PUT"])
def up_item(indice):
    if indice < len(itens):
        dados = request.get_json()
        itens[indice].update(dados)
        resp_func = valida_funcao_prod(dados)
        resp_nome = valida_nome_prod(dados)
        if resp_func and resp_nome:
            return jsonify({"mensagem": " Item atualizado com sucesso!"}), 201
        else:
            return jsonify({"Valido": False, "Mensagem": "Erro na validação"})
    return jsonify({"mensagem": " Item não atualizado!"}), 404

# Deletar itens
@app.route("/estoque/itens/<int:indice>", methods=["DELETE"])
def deletar_item(indice):
    if indice < len(itens):
        itens.pop(indice)
        return jsonify({"mensagem": "Item apagado com sucesso!"}), 201
    return jsonify({"erro": "Item não encontrado"}), 404


#--------------------Pesquisa--------------------#

# Bucar pesquisa
@app.route("/estoque/pesquisa/<int:indice>", methods=["GET"])
def buscar_pesquisa(indice):
    if indice < len(compra):
        return jsonify(compra[indice])
    return jsonify({"erro": "item não encontrado"}), 404


#--------------------Controle de saida--------------------#

# Busacar saida por saide de medicamentos
@app.route("/estoque/cont_sai/<int:indice>", methods=["GET"])
def listar_controle_saida(indice):
    if indice < len(cont_saida):
        return jsonify(cont_saida[indice])
    return jsonify({"erro": "produto nao encontrado"}), 404


# Buscar todas as saidas
@app.route("/estoque/cont_saida", methods=["GET"])
def buscar_cont_saida():
    return jsonify(cont_saida)

# Adicionar itens de saida
@app.route("/estoque/cont_sai", methods=["POST"])
def add_controle_saida():
    saida = request.get_json()
    cont_saida.append(saida)
    resp_motivo = valida_uso_prod(saida)
    resp_nome = valida_nome_prod(saida)
    if resp_motivo and resp_nome:
        return jsonify({"mensagem": "item adicionado com sucesso"}), 201
    else: 
        return jsonify({"Valido": False, "Menssagem": "Erro na validação"})

# Deletar saida de medicamento
@app.route("/estoque/cont_sai/<int:indice>", methods=["DELETE"])
def deleta_saida(indice):
    if indice < len(cont_saida):
        cont_saida.pop(indice)
        return jsonify({"mensagem": "item removido com sucesso!"})
    return jsonify({"erro": "item não encontrado"}), 404


#--------------------Controle de entrada--------------------#

# Adicionar novos produtos
@app.route("/estoque/cont_ent", methods=["POST"])
def add_controle_entrada():
    entrada = request.get_json()
    cont_ent.append(entrada)
    resp_nome = valida_nome_prod(entrada)
    resp_qtd = valida_quant(entrada)
    resp_lote = valida_lote(entrada)
    if resp_nome and resp_qtd and resp_lote:
        return jsonify({"mensagem": "item adicionado com sucesso"}), 201
    else: 
        return jsonify({"Valido": False, "Mensagem": "Erro na validação"})

# Deletar entrada de novos medicamentos
@app.route("/estoque/cont_ent/<int:indice>", methods=["DELETE"])
def deletar_cont_entrada(indice):
    if indice < len(cont_ent):
        cont_ent.pop(indice)
        return jsonify({"mensagem": "item removido com sucesso!"})
    return jsonify({"erro": "item não encontrado"}), 404

# Buscar a entrada por entrada de medicamentos
@app.route("/cont_ent/<int:indice>", methods=["GET"])
def listar_controle_entrada(indice):
    if indice < len(cont_ent):
        return jsonify(cont_ent[indice])
    return jsonify({"erro": "produto nao encontrado"}), 404

# Buscar todas as entradas de medicamentos
@app.route("/estoque/cont_ent", methods=["GET"])
def buscar_cont_ent():
    return jsonify(cont_ent)


#--------------------Relatorio--------------------#

# Relatorio de usuarios
@app.route("/estoque/relatorio_usuario", methods=["GET"])
def relatorio_user():
    return (usuarios)

# Relatorio de produtos
@app.route("/estoque/relatorio_produtos", methods=["GET"])
def relatorio_prod():
    return (produtos)

# Relatorio de saida de medicamentos
@app.route("/estoque/relatorio_cont_saida", methods=["GET"])
def relatorio_saida():
    return (cont_saida)

# Relatorio de entrada de medicamentos
@app.route("/estoque/relatorio_cont_ent", methods=["GET"])
def relatorio_ent():
    return (cont_ent)

# Relatorio da lista de compra
@app.route("/estoque/relatorio_lista_compra", methods=["GET"])
def relatori_compra():
    return (compra)

# Relatorio do uso dos medicamentos
@app.route("/estoque/relatorio_uso", methods=["GET"])
def relatorio_uso():
    return (uso)

# Relatorio dos sensores
@app.route("/estoque/relatorio_sensor", methods=["GET"])
def relatorio_sensor():
    return (sensor)

# Relatorio de alertas
@app.route("/estoque/relatori_alertas", methods=["GET"])
def relatorio_alertas():
    return (alerta)

#--------------------Alerta--------------------#


@app.route("/alerta", methods=["GET"])
def listar_alerta():
    return jsonify(alerta)


#--------------------Produto--------------------#

# Adicionar produtos
@app.route("/produtos", methods=["POST"])
def add_produto():
    novo_produto = request.get_json()
    produtos.append(novo_produto)
    resp_fun = valida_funcao_prod(novo_produto)
    resp_nome = valida_nome_prod(novo_produto)
    resp_qtd = valida_quant(novo_produto)
    resp_lote = valida_lote(novo_produto)
    if resp_fun and resp_nome and resp_qtd and resp_lote:
        return jsonify({"mensagem": "Produto adicionado com sucesso!"}), 201
    else: return jsonify({"Valido": False, "Mensagem": "Erro na validação do produto"})

# Buscar produto por produto
@app.route("/produtos/<int:indice>", methods=["GET"])
def buscar_produto(indice):
    if indice < len(produtos):
        return jsonify(produtos[indice])
    return jsonify({"erro": "Produto não encontrado"}), 404

# Atualizar produtos
@app.route("/produtos/<int:indice>", methods=["PUT"])
def up_produto(indice):
    if indice < len(produtos):
        dados = request.get_json()
        produtos[indice].update(dados)
        resp_func = valida_funcao_prod(dados)
        resp_nome = valida_nome_prod(dados)
        resp_qtd = valida_quant(dados)
        resp_lote = valida_lote(dados)
        if resp_func and resp_nome and resp_qtd and resp_lote:
            return jsonify({"mensagem": " Produto atualizado com sucesso!"}), 404
        else: 
            return jsonify({"Valido": False, "Mensagem": "Erro na atualização do produto"})
    else:
        return jsonify({"Mensagem": "Produto não encontrado"})

# Deletar produtos
@app.route("/produtos/<int:indice>", methods=["DELETE"])
def deletar_produto(indice):
    if indice < len(produtos):
        produtos.pop(indice)
        return jsonify({"mensagem": "Produto apagado com sucesso!"}), 201
    return jsonify({"erro": "Produto não encontrado"}), 404


#-----------------------------------------------#

if __name__ == "__main__":
    app.run(debug=True)