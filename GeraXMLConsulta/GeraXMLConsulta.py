import csv
import os
from xml.etree.ElementTree import Element, SubElement, tostring

def map_modelo_documento(value):
    if value == '55':
        return 'NFe'
    elif value == '57':
        return 'CTe'
    elif value == '99':
        return 'NFSe'
    else:
        return 'Outro'

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
            root = Element('Consultar')

            # Adicionar ChaveParceiro e ChaveAcesso
            SubElement(root, 'ChaveParceiro').text = row['ChaveParceiro']
            SubElement(root, 'ChaveAcesso').text = row['ChaveAcesso']

            # Criar o elemento de Consulta
            consulta_elem = SubElement(root, 'Consulta')
            SubElement(consulta_elem, 'ModeloDocumento').text = map_modelo_documento(row['ModeloDocumento'])
            SubElement(consulta_elem, 'Versao').text = row['Versao']
            SubElement(consulta_elem, 'tpAmb').text = row['tpAmb']
            SubElement(consulta_elem, 'CnpjEmpresa').text = row['CnpjEmpresa']
            SubElement(consulta_elem, 'NumeroInicial').text = row['NumeroInicial']
            SubElement(consulta_elem, 'NumeroFinal').text = row['NumeroFinal']
            SubElement(consulta_elem, 'Serie').text = row['Serie']
            SubElement(consulta_elem, 'EmitidoRecebido').text = row['EmitidoRecebido']

            # Criar o elemento de ParametrosConsulta
            parametros_elem = SubElement(root, 'ParametrosConsulta')
            SubElement(parametros_elem, 'Situacao').text = 'S'
            SubElement(parametros_elem, 'XMLCompleto').text = 'S'
            SubElement(parametros_elem, 'XMLLink').text = 'S'
            SubElement(parametros_elem, 'PDFBase64').text = 'S'
            SubElement(parametros_elem, 'PDFLink').text = 'S'
            SubElement(parametros_elem, 'Eventos').text = 'S'

            # Converter o elemento XML em uma string XML formatada
            xml_string = tostring(root, encoding='unicode')

            # Caminho do arquivo XML de saída
            xml_file_path = os.path.join(output_dir, f'consulta_{idx}.xml')

            # Escrever a string XML em um arquivo
            with open(xml_file_path, 'w') as xmlfile:
                xmlfile.write(xml_string)

# Diretório onde o arquivo CSV está localizado
csv_path = input("Informe o caminho do diretório ou arquivo CSV: ")

# Diretório onde os XMLs serão armazenados
output_dir = input("Informe o diretório onde deseja armazenar os XMLs de consulta: ")

# Criar XMLs de consulta a partir dos arquivos CSV no diretório especificado
create_xml_from_csv(csv_path, output_dir)

print("XMLs de consulta criados com sucesso!")
