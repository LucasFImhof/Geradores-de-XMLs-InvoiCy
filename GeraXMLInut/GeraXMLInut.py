import csv
import xml.etree.ElementTree as ET
import os


def criar_xml(input_csv, output_dir):
    with open(input_csv, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')

        for row in csv_reader:
            # Criação do elemento raiz
            inutilizacao = ET.Element("Inutilizacao")

            # Mapeamento dos campos do CSV para os elementos XML
            campos_xml = {
                "ChaveParceiro": row["ChaveParceiro"],
                "ChaveAcesso": row["ChaveAcesso"],
                "CnpjEmissor": row["CnpjEmissor"],
                "NumeroInicial": row["NumeroInicial"],
                "NumeroFinal": row["NumeroFinal"],
                "Serie": row["Serie"],
                "Justificativa": row["Justificativa"],
                "ModeloDocumento": row["ModeloDocumento"],
                "tpAmb": row["tpAmb"],
            }

            # Adição dos elementos filhos ao elemento raiz
            for campo, valor in campos_xml.items():
                ET.SubElement(inutilizacao, campo).text = valor

            # Criação do objeto de árvore
            tree = ET.ElementTree(inutilizacao)

            # Criação do diretório se não existir
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            # Nome do arquivo baseado no número inicial
            nome_arquivo = f"{row['NumeroInicial']}.xml"
            caminho_arquivo = os.path.join(output_dir, nome_arquivo)

            # Salvamento do XML no arquivo
            tree.write(caminho_arquivo, encoding="utf-8",
                       xml_declaration=False)

    print("Arquivos XML gerados com sucesso!")


if __name__ == "__main__":

    # Solicitação do arquivo CSV do usuário
    input_csv = input("Informe o caminhoC: do arquivo CSV: ")

    # Solicitação do diretório de salvamento do usuário
    output_dir = input(
        "Informe o caminho do diretório para salvar os arquivos XML: ")
        
    # Criar XMLs de consulta a partir dos arquivos CSV no diretório especificado
    criar_xml(input_csv, output_dir)

print("XMLs criados com sucesso!")