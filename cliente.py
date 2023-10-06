class Cliente:

    def __init__(self, primeiro_nome, ultimo_nome, endereco, celular, email, genero):
       self.primeiro_nome = primeiro_nome
       self.ultimo_nome = ultimo_nome
       self.endereco = endereco
       self.celular = celular
       self.email = email
       self.genero = genero

    def validar_email(self, email):
        if self.email == email:
            print ("Email já cadastrado anteriormente.")
        else:
            print("Email disponivel para cadastro.")