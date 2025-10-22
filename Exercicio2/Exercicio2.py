# Primeiro comecamos com os imports de jason e os(systema operativo)
import json
import os

ARQUIVO = "tarefas.json"

# Função para carregar tarefas do arquivo JSON
def carregar_tarefas():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

# Função para salvar tarefas no arquivo JSON
def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

# Função para listar tarefas
def listar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.\n")
        return
    print("\nLista de Tarefas:")
    for i, t in enumerate(tarefas):
        status = "✅" if t["concluida"] else "❌"
        print(f"{i+1}. {t['titulo']} - {status}")
    print()

# Função para adicionar nova tarefa
def adicionar_tarefa(tarefas):
    titulo = input("Digite o título da tarefa: ").strip()
    if titulo:
        tarefas.append({"titulo": titulo, "concluida": False})
        salvar_tarefas(tarefas)
        print("Tarefa adicionada com sucesso!\n")
    else:
        print("Título não pode ser vazio.\n")

# Função para marcar tarefa como concluída
def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        i = int(input("Número da tarefa para marcar como concluída: ")) - 1
        tarefas[i]["concluida"] = True
        salvar_tarefas(tarefas)
        print("Tarefa marcada como concluída!\n")
    except (ValueError, IndexError):
        print("Número inválido.\n")

# Função para remover tarefa
def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        i = int(input("Número da tarefa para remover: ")) - 1
        removida = tarefas.pop(i)
        salvar_tarefas(tarefas)
        print(f"Tarefa '{removida['titulo']}' removida.\n")
    except (ValueError, IndexError):
        print("Número inválido.\n")

# Função principal
def menu():
    tarefas = carregar_tarefas()
    while True:
        print("==== MENU ====")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Marcar como concluída")
        print("4. Remover tarefa")
        print("0. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "0":
            print(" Saindo do programa...")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    menu()
