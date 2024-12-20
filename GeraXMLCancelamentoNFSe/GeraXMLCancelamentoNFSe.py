import csv
import os
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta


def criar_xml(diretorio_csv, diretorio_xml):
    # Lê o arquivo CSV
    with open(diretorio_csv, 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv, delimiter=';')

        # Verifica se o diretório de destino existe, senão cria
        if not os.path.exists(diretorio_xml):
            os.makedirs(diretorio_xml)

        for linha in leitor_csv:
            # Cria o elemento raiz do XML
            envio_evento = ET.Element("EnvioEvento")

            # Adiciona ModeloDocumento e Versao
            modelo_documento = ET.SubElement(envio_evento, "ModeloDocumento")
            modelo_documento.text = "NFSe"
            versao = ET.SubElement(envio_evento, "Versao")
            versao.text = "1.00"

            # Adiciona ChaveParceiro e ChaveAcesso
            chave_parceiro = ET.SubElement(envio_evento, "ChaveParceiro")
            chave_parceiro.text = linha['ChaveParceiro']
            chave_acesso = ET.SubElement(envio_evento, "ChaveAcesso")
            chave_acesso.text = linha['ChaveAcesso']

            # Adiciona o elemento Evento
            evento = ET.SubElement(envio_evento, "Evento")

            # Adiciona informações da NFSe
            cnpj_emissor = ET.SubElement(evento, "CNPJ")
            cnpj_emissor.text = linha['CNPJ']
            nfse_numero = ET.SubElement(evento, "NFSeNumero")
            nfse_numero.text = linha['NFSeNumero']
            rps_numero = ET.SubElement(evento, "RPSNumero")
            rps_numero.text = linha['RPSNumero']
            rps_serie = ET.SubElement(evento, "RPSSerie")
            rps_serie.text = linha['RPSSerie']

            # Define o codigo do evento de cancelamento
            eve_tp = ET.SubElement(evento, "EveTp")
            eve_tp.text = "110111"

            # Verifica se a chave 'tpAmb' existe no dicionário
            tp_amb = ET.SubElement(evento, "tpAmb")
            # Obtém o valor se existir, caso contrário, usa uma string vazia
            tp_amb.text = linha.get('tpAmb', '')

            # Difine o codigo do evento e descrição para a prefeitura
            eve_codigo = ET.SubElement(evento, "EveCodigo")
            eve_codigo.text = "2"
            eve_motivo = ET.SubElement(evento, "EveMotivo")
            eve_motivo.text = "Serviço não prestado"

            # Cria o arquivo XML
            xml_string = ET.tostring(
                envio_evento, encoding='utf-8').decode('utf-8')

            # Salva o arquivo XML
            nome_arquivo_xml = f"evento_{linha['RPSNumero']}.xml"
            caminho_arquivo_xml = os.path.join(diretorio_xml, nome_arquivo_xml)

            with open(caminho_arquivo_xml, 'w') as arquivo_xml:
                arquivo_xml.write(xml_string)

                print("XMLs criados com sucesso!")


# Diretório onde o arquivo CSV está localizado
diretorio_csv = input("Informe o diretório do arquivo CSV: ")

# Diretório onde os XMLs serão armazenados
diretorio_xml = input("Informe o diretório para salvar os XMLs: ")

# Criar XMLs a partir dos arquivos CSV no diretório especificado
criar_xml(diretorio_csv, diretorio_xml)

print("XMLs criados com sucesso!")