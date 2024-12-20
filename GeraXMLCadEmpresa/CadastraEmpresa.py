import csv
import os
from xml.etree.ElementTree import Element, SubElement, tostring


def create_xml_from_csv(csv_path, output_dir):
    # Verifica se o diretório de saída existe e cria se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Verificar se o caminho fornecido é um diretório ou arquivo
    if os.path.isdir(csv_path):
        # Listar todos os arquivos no diretório fornecido
        for file_name in os.listdir(csv_path):
            file_path = os.path.join(csv_path, file_name)
            # Verificar se é um arquivo CSV
            if os.path.isfile(file_path) and file_name.endswith('.csv'):
                process_csv_file(file_path, output_dir)
    elif os.path.isfile(csv_path) and csv_path.endswith('.csv'):
        # Se for um arquivo CSV, processar apenas este arquivo
        process_csv_file(csv_path, output_dir)
    else:
        print("O caminho fornecido não é um diretório válido ou um arquivo CSV válido.")


def process_csv_file(csv_file, output_dir):
    # Abrir o arquivo CSV e ler os dados
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        # Para cada linha no arquivo CSV
        for idx, row in enumerate(reader, start=1):
            # Criar o elemento raiz do XML
            root = Element('CadastroEmpresa')

            # Para cada coluna no CSV, exceto a última
            for key, value in row.items():
                if value:  # Verifica se o valor não está em branco
                    # Criar elemento XML e adicionar ao elemento raiz
                    SubElement(root, key).text = value

            # Converter o elemento XML em uma string XML formatada
            xml_string = tostring(root, encoding='unicode')

            # Caminho do arquivo XML de saída
            xml_file_path = os.path.join(output_dir, f'Cad_{idx}.xml')

            # Escrever a string XML em um arquivo
            with open(xml_file_path, 'w') as xmlfile:
                xmlfile.write(xml_string)


# Diretório onde o arquivo CSV está localizado
csv_path = input("Informe o caminho do diretório ou arquivo CSV: ")

# Diretório onde os XMLs serão armazenados
output_dir = input("Informe o diretório onde deseja armazenar os XMLs: ")

# Criar XMLs a partir dos arquivos CSV no diretório especificado
create_xml_from_csv(csv_path, output_dir)

print("XMLs criados com sucesso!")
