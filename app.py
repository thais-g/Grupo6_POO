import Model
from flask import Flask, request, render_template, render_template_string

app = Flask(__name__, template_folder="view")
app = Flask(__name__, static_url_path="/card")

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/paciente")
def Pagpaciente():
    return render_template("index2.html")


@app.route("/profissional")
def Pagprofissional():
    return render_template("index3.html")


@app.route("/loginpaciente")
def LoginPaciente():
    return render_template("loginpaciente.html")

@app.route("/loginprofissional")
def LoginProfissional():
    return render_template("loginprofissional.html")

@app.route("/autentica", methods=['POST'])
def autentica():
    cpf = request.form['cpf']
    senha = request.form['senha']
    tipo = request.form['tipo']
    
    if tipo == "paciente":
        for each in lista_pac:
            if lista_pac[each].cpf == cpf:
                if lista_pac[each].senha == senha:
                    return render_template("usuario.html", cpf=cpf, senha=senha)
                    break
                else:
                    return render_template_string("<!doctype html><html><title>Senha inválida!</title><h1>Senha inválida!</h1></html>")
                    break
        return render_template_string("<!doctype html><html><title>Usuário não encontrado!</title><h1>Usuário não encontrado!</h1></html>")
    elif tipo == "profissional":
        for each in lista_prof:
            if lista_prof[each].cpf == cpf:
                if lista_prof[each].senha == senha:
                    return render_template("usuario.html", cpf=cpf, senha=senha)
                    break
                else:
                    return render_template_string("<!doctype html><html><title>Senha inválida!</title><h1>Senha inválida!</h1></html>")
                    break
        return render_template_string("<!doctype html><html><title>Usuário não encontrado!</title><h1>Usuário não encontrado!</h1></html>")

@app.route("/cadastropaciente")
def cadastropaciente():
    return render_template('cadastropaciente.html')

@app.route("/cadastroprofissional")
def cadastroprofissional():
    return render_template("cadastroprofissional.html")

@app.route("/cadastrar", methods=['POST'])
def cadastrar():
    cpf = request.form['cpf']
    nome = cpf = request.form['nome']
    data_nasc = request.form['data_nasc']
    email = request.form['email']
    senha = request.form['senha']
    diag = request.form['diag']
    nivel_ativ = request.form['nivel_ativ']
    registro_profissional = request.form['registroprofissional']
    especialidade = request.form['especialidade']
    tempo_experiencia = request.form['tempodeexperiencia']
    tipo = request.form['tipo']

    if tipo == "paciente":
        lista_pac.append(Model.Paciente(cpf, nome, data_nasc, email, senha, diag, nivel_ativ))

    elif tipo == "profissional":
        lista_prof.append(Model.Profissional(cpf, nome, data_nasc, email, senha, registro_profissional, especialidade, tempo_experiencia))

    return render_template("usuario.html", nome=nome, cpf=cpf, email=email)


@app.route("/menupaciente")
def menupaciente():
    return render_template("menupaciente.html")


@app.route("/menuprofissional")
def menuprofissional():
    return render_template("menuprofissional.html")


@app.route("/definiratividades")
def definiratividades():
    return render_template("definiratividades.html")


@app.route("/atividades")
def atividades():
    return render_template("atividades.html")

@app.route("/registroatividades")
def registroatividades():

    tipo = request.form['tipo']
    select = request.form['select']

    if tipo == "definir":
        reg_ativ.append(Model.RegistroAtividade(select, "111.111.111-11", "222.222.222-22", "", "", 0))

    elif tipo == "jogar":
        reg_ativ.append(Model.RegistroAtividade(54,  "111.111.111-11", "222.222.222-22", "10/04/2022 10:00", "02:00", select))

@app.route("/diagnostico")
def diagnostico():
    nome = lista_pac[0].nome
    diag = lista_pac[0].diag
    return render_template("diagnostico.html", nome, diag)

@app.route("/cards")
def cards():
    return render_template("cards.html")


if __name__ == "__main__":

  lista_pac = Model.Paciente.CriaLista()
  lista_prof = Model.Profissional.CriaLista()
  lista_card = Model.Cards.CriaLista()
  lista_ativ = Model.Atividades.CriaLista()
  reg_ativ = []
  
  app.run()