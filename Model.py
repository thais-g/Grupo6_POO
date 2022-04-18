class Usuario: #classe mãe
  def __init__(self, cpf, nome, data_nasc, email, senha):
    self._cpf = cpf #id único
    self._nome = nome
    self._data_nasc = data_nasc
    self._email = email
    self._senha = senha


  @property
  def cpf(self):
        #Este código é executado quando alguém for ler o valor de self.cpf
        return self._cpf
  @cpf.setter
  def cpf(self, cpf):
        #Este código é executado sempre que alguém fizer self.cpf = cpf
        self._cpf = cpf

  @property
  def nome(self):
        return self._nome
  @nome.setter
  def nome(self, nome):
        self._nome = nome

  @property
  def data_nasc(self):
        return self._data_nasc
  @nome.setter
  def data_nasc(self, data_nasc):
        self._data_nasc = data_nasc

  @property
  def email(self):
        return self._email
  @nome.setter
  def email(self, email):
        self._email = email

  @property
  def senha(self):
        return self._senha
  @nome.setter
  def senha(self, senha):
        self._senha = senha


class Paciente(Usuario):
  def __init__(self, cpf, nome, data_nasc, email, senha, diag, nivel_ativ):
    super().__init__(cpf, data_nasc, nome, email, senha)
    self._diag = diag
    self._nivel_ativ = nivel_ativ

  @property
  def diagnostico(self):
        return self._diag
  @diagnostico.setter
  def diagnostico(self, diag):
        self._diag = diag

  @property
  def nivel_ativ(self):
        return self._nivel_ativ
  @nivel_ativ.setter
  def nivel_ativ(self, nivel_ativ):
        self._nivel_ativ = nivel_ativ

  def CriaLista():
      lista_paciente = []
      lista_paciente.append(Paciente("111.111.111-11", "Fulano", "10/10/2010", "fulano@server.com", "1234", "Apraxia", 1))
      lista_paciente.append(Paciente("1222.222.222-22", "Fulano", "10/10/2010", "fulano@server.com", "1234", "Apraxia", 1))
      lista_paciente.append(Paciente("333.333.333-33", "Fulano", "10/10/2010", "fulano@server.com", "1234", "Apraxia", 1))


class Profissional(Usuario):
  def __init__(self, cpf, nome, data_nasc, email, senha, registro_profissional, especialidade, tempo_experiencia):
    super().__init__(cpf, nome, data_nasc, email, senha)
    self._registro_profissional = registro_profissional
    self._especialidade = especialidade
    self._tempo_experiencia = tempo_experiencia
  

  @property
  def registro_profissional(self):
        return self._registro_profissional
  @registro_profissional.setter
  def registro_profissional(self, registro_profissional):
        self.registro_profissional = registro_profissional

  @property
  def especialidade(self):
        return self._especialidade
  @especialidade.setter
  def especialidade(self, especialidade):
        self._especialidade = especialidade

  @property
  def tempo_experiencia(self):
        return self._tempo_experiencia
  @tempo_experiencia.setter
  def tempo_experiencia(self, tempo_experiencia):
        self._tempo_experiencia = tempo_experiencia
  

  def CriaLista():
      lista_profissional = []
      lista_profissional.append(Profissional("111.111.111-11", "Fulano", "10/10/2010", "fulano@server.com", "1234", "crm1548", "fonoaudiologia", 10))
      lista_profissional.append(Profissional("1222.222.222-22", "Fulano", "10/10/2010", "fulano@server.com", "1234", "crm1548", "fonoaudiologia", 10))
      lista_profissional.append(Profissional("333.333.333-33", "Fulano", "10/10/2010", "fulano@server.com", "1234", "crm1548", "fonoaudiologia", 10))


#Sem getters e setters pois cards constantes para prova de conceito (seria interessante só se fóssemos tornar alteráveis)
#Instanciamento fixo no app
class Cards:
  def __init__(self, id, imagem, nome, som, categoria):  
    self.id_card = id
    self.imagem = imagem  #Caminho do arquivo
    self.nome = nome
    self.som = som    #Caminho do arquivo
    self.categoria = categoria
  
  def CriaLista():
    listaCards = []
    listaCards.append(Cards(1,"C:\\Users\\lecex\\Downloads\\mapa-de-lideranca-situacional.png","Olá","C:\\Users\\lecex\\Downloads\\mapa-de-lideranca-situacional.png","Saudacoes"))
    listaCards.append(Cards(2,"C:\\Users\\lecex\\Downloads\\mapa-de-lideranca-situacional.png","Tchau","C:\\Users\\lecex\\Downloads\\mapa-de-lideranca-situacional.png","Saudacoes"))
    listaCards.append(Cards(3,"C:\\Users\\lecex\\Downloads\\mapa-de-lideranca-situacional.png","Não","C:\\Users\\lecex\\Downloads\\mapa-de-lideranca-situacional.png","Saudacoes"))


#Apenas para registro. Projeto de escalabilidade, ainda sem função implementada.
class CardAcessado:  #relação entre paciente e card

  registro = []

  def __init__(self, id_card, cpf_pac, data_hora): 
    self.id_card = id_card 
    self.cpf_pac = cpf_pac
    self.data_hora = data_hora

  def registra(self, id_card, cpf_pac, data_hora):

    self.registro.append(id_card, cpf_pac, data_hora)


#As interações do paciente com as atividades não são registradas aqui, essas são as atividades em si
class Atividades:
  def __init__(self, id_ativ, nivel, enunciado, opcoes, resposta): 
    self.id_ativ = id_ativ
    self.nivel = nivel
    self.enunciado = enunciado
    self.opcoes = opcoes #lista de opções disponíveis
    self.resposta = resposta #resposta desejada pela pessoa idealizadora

  def CriaLista():
    lista_ativ = []
    lista_ativ.append(Atividades(1, 1, 'Qual o sigficado de "está chovendo canivetes"?', ['1 - Está chovendo muito', '2 - Está caindo facas', '3 - Não está chovendo'], 0))


#Na seleção de atividades pelo profissional é instanciado um objeto com data_hora, tempo_duracao e escolha zerados
#Não há interesse em registro de performance, e sim qual resposta foi selecionada. O erro aqui é tão significativo quanto o acerto
class RegistroAtividade:  #relação entre paciente, atividade e profissional
  def __init__(self, id_ativ, cpf_prof, cpf_pac, data_hora, tempo_duracao, escolha): 
    self.id_ativ = id_ativ
    self.cpf_prof = cpf_prof
    self.cpf_pac = cpf_pac
    self.data_hora = data_hora
    self.tempo_duracao = tempo_duracao
    self.escolha = escolha #opção escolhida pelo paciente

  def DefinirAtividades(lista_ativ, reg_ativ, nivel, cpf_pac, cpf_prof): #Registrar paciente e profissional
   #for para exibir as atividades de mesmo nivel do paciente
    for each in (lista_ativ):
      if lista_ativ[each].nivel == nivel:
        reg_ativ.append(RegistroAtividade(lista_ativ[each].id, cpf_prof, cpf_pac, "", "", 0))








  
