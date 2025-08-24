import os # Importa o modúlo os pra abrir as pastas do pc.
import sys # Importa o modúlo sys pra verificar se é executável.
from time import sleep # Importa a função sleep pra esperar segundos.

Pasta = None

# Define a pasta atual
if getattr(sys, "frozen", False):
    Pasta = os.path.dirname(sys.executable)
else:
    Pasta = os.path.dirname (__file__)

# Cria diretorios chave se eles não existirem.
PastaA = os.path.join(Pasta, "apps")
PastaD = os.path.join(Pasta, "docs")

# Criar pastas se não existirem
os.makedirs(PastaA, exist_ok=True)
os.makedirs(PastaD, exist_ok=True)

# Define os comandos
def Comandos(Comando, Pasta):
    if Comando == "pasta":
        Pasta_Selecionada = input("Qual? ")
        Novo_Caminho = os.path.join(Pasta, Pasta_Selecionada)
        if os.path.exists(Novo_Caminho):
            return Novo_Caminho
        else:
            print ("Pasta não encontrada.")
            print ()
            return Pasta
    elif Comando == "voltarP":
        return os.path.dirname(Pasta)
    elif Comando == "sair":
        print ()
        print ("Saindo...")
        sleep (2)
        exit()
    elif Comando == "cont":
        print ()
        for Cont in os.listdir(Pasta):
            print (Cont)
        print ()
        return Pasta
    elif Comando == "creditos":
        print ()
        print ("           Python-OS")
        print ("Feito por Pedro Knabach andrade")
        print ("Também pode ser visto na interface grafica.")
        print ()
        return Pasta
    elif Comando == "ajuda":
        print ()
        print ("        Lista de comandos:")
        print ("cont: visualiza o conteudo da pasta;")
        print ("pasta: entra em uma pasta solicitada que está na sua pasta atual;")
        print ("voltarP: volta a pasta (não volte até o C:, dá erro);")
        print ("creditos: créditos")
        print ("limpar: limpa a tela;")
        print ("ExeAPP: executa um .poa;")
        print ("mostreA: mostra o conteúdo de um arquivo.")
        print ()
        return Pasta
    elif Comando == "limpar":
        try:
            # tenta limpar pelo sistema
            os.system("cls" if os.name == "nt" else "clear")
        except:
            # se não funcionar (ex: IDE), "empurra" o conteúdo
            print("\n" * 100)
        return Pasta
    elif Comando == "ExeAPP":
        APP = input ("APP? ")
        if not APP.endswith(".poa"):
            APP += ".poa"
        cAPP = os.path.join(Pasta, APP)
        if os.path.exists(cAPP):
            os.system("cls" if os.name == "nt" else "clear")
            with open(cAPP, "r", encoding="utf-8") as f:
                Codigo = f.read()
                try:
                    exec(Codigo, {"__name__": "__main__"})
                    return Pasta
                except Exception as e:
                    print(f"Erro no app: {e}")
                    return Pasta
        else:
            print ("APP não encontrado.")
            print ()
            return Pasta
    elif Comando == "mostreA":
        Nome_A = input ("Arquivo? ")
        cARQ = os.path.join (PastaD, Nome_A)
        if os.path.exists (cARQ):
            try:
                with open(cARQ, "r", encoding="utf-8") as f:
                    print ()
                    print (f.read())
                    print ()
                    return Pasta
            except Exception as e:
                print (f"Ocorreu um erro ao tentar mostrar o arquivo: {e}.")
    else:
        print ("Comando invalido.")
        print ()
        return Pasta

# Inicio
print ("Olá, bem-vindo(a) ao...")
print ("...Python-OS!")
print ("Digite ""creditos"" pra ver sobre o Python-OS e ""ajuda"" pra saber os comandos básicos.")
print ()
# loop do comando
while True:
    Comando = input(f"{os.getlogin()}, Pasta: {Pasta}>>> ")
    Pasta = Comandos(Comando, Pasta)
