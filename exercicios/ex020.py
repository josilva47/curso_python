from time import sleep

lista = []
apagados = []

def listar(tarefa):
    if not tarefa:
        print(f'\033[31mNada para listar\033[m')
    else: 
        print('\033[32m~~~~TAREFAS~~~~\033[m')
        for i in tarefa:
            print(f'- {str(i).capitalize()}')
        print(f'\033[32m~\033[m' *15)
        sleep(2)

def desfazer(tarefa, tarefas_apagadas):
    if tarefa:
        tarefas_apagadas.append(tarefa.pop())
        print(f'\033[32mSucesso! Utilize o comando "Listar" para verificar a nova lista\033[m')
    else:
        print(f'\033[33mNada para desfazer\033[m')

def refazer(tarefas_apagadas, tarefas_refazer):
    if tarefas_apagadas:
        tarefas_refazer.append(tarefas_apagadas.pop())
        print(f'\033[32mSucesso! Utilize o comando "Listar" para verificar a nova lista\033[m')
    else:
        print(f'\033[33mNada para refazer\033[m')
        

while True:
    print(f'\033[1;34mComandos: Listar, Desfazer, Refazer\033[m')
    usuario = str(input('Digite uma tarefa ou comando: ')).strip().lower()

    if not usuario:
        print(f'\033[33mVoce nao digitou nenhuma tarefa!\033[m')
        continue

    if usuario not in ('listar', 'desfazer', 'refazer'):
        if usuario in lista:
            print(f'\033[33mTarefa ja esta na lista\033[m')
        else:
            lista.append(usuario)
            print(f'\033[33mTarefa adicionada!\033[m')

    elif usuario == 'listar':
         listar(lista)
    
    elif usuario == 'desfazer':
        desfazer(lista, apagados)

    else:
        refazer(apagados, lista)
        




