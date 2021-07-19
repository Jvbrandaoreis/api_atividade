from models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome='Joao',idade=23)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    #pessoa = Pessoas.query.filter_by(nome='Joao').first()
    #print(pessoa.idade)

def altera_pessoa():
    pessoa= Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Joao').first()
    pessoa.idade = 31
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Joao').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    consulta_pessoas()