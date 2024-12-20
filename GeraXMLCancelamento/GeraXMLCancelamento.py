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
            modelo_documento.text = "NFe" if linha['ModeloDocumento'] == '55' else "NFCe"

            versao = ET.SubElement(envio_evento, "Versao")
            versao.text = "4.00"

            # Adiciona ChaveParceiro e ChaveAcesso
            chave_parceiro = ET.SubElement(envio_evento, "ChaveParceiro")
            chave_parceiro.text = linha['ChaveParceiro']

            chave_acesso = ET.SubElement(envio_evento, "ChaveAcesso")
            # Agora, 'ChaveAcesso' está antes de 'ChaAcesso'
            chave_acesso.text = linha['ChaveAcesso']

            # Adiciona o elemento Evento
            evento = ET.SubElement(envio_evento, "Evento")

            # Adiciona informações da NTF
            ntf_cnpj_emissor = ET.SubElement(evento, "NtfCnpjEmissor")
            ntf_cnpj_emissor.text = linha['CNPJ']

            ntf_numero = ET.SubElement(evento, "NtfNumero")
            ntf_numero.text = linha['NtfNumero']

            ntf_serie = ET.SubElement(evento, "NtfSerie")
            ntf_serie.text = linha['NtfSerie']

            # Verifica se a chave 'tpAmb' existe no dicionário
            tp_amb = ET.SubElement(evento, "tpAmb")
            # Obtém o valor se existir, caso contrário, usa uma string vazia
            tp_amb.text = linha.get('tpAmb', '')

            cha_acesso = ET.SubElement(evento, "ChaAcesso")
            cha_acesso.text = linha['ChaAcesso']

            # Adiciona elemento EveInf
            eve_inf = ET.SubElement(evento, "EveInf")

            # Adiciona informações de data e hora
            data_hora_atual = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

            eve_dh = ET.SubElement(eve_inf, "EveDh")
            eve_dh.text = data_hora_atual

            eve_fuso_horario = ET.SubElement(eve_inf, "EveFusoHorario")
            eve_fuso_horario.text = "-03:00"  # Exemplo, ajuste conforme necessário

            eve_tp = ET.SubElement(eve_inf, "EveTp")
            eve_tp.text = "110111"  # Exemplo, ajuste conforme necessário

            even_seq = ET.SubElement(eve_inf, "EvenSeq")
            even_seq.text = "1"  # Exemplo, ajuste conforme necessário

            # Adiciona elemento Evedet
            evedet = ET.SubElement(eve_inf, "Evedet")

            eve_desc = ET.SubElement(evedet, "EveDesc")
            eve_desc.text = "Cancelamento"

            evex_just = ET.SubElement(evedet, "EvexJust")
            evex_just.text = "Cancelado pois haviam erros no documento."

            # Cria o arquivo XML
            xml_string = ET.tostring(
                envio_evento, encoding='utf-8').decode('utf-8')

            # Salva o arquivo XML
            nome_arquivo_xml = f"evento_{linha['NtfNumero']}.xml"
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
