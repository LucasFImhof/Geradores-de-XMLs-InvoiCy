import re
import os
import xml.etree.ElementTree as ET

diretorio = 'C:\\Users\\li21260\\Downloads\\DocPendentes\\DocPendentes\\Erro'

for nome_arquivo in os.listdir(diretorio):
    if nome_arquivo.endswith('.xml'):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)

        # Ler o conteúdo do arquivo XML
        with open(caminho_arquivo, 'r') as file:
            xml_content = file.read()

        # Remover o grupo <Resultado> usando uma expressão regular
        xml_content = re.sub(r'<Resultado>.*?</Resultado>',
                             '', xml_content, flags=re.DOTALL)

        # Escrever o conteúdo modificado de volta no arquivo
        with open(caminho_arquivo, 'w') as file:
            file.write(xml_content)
