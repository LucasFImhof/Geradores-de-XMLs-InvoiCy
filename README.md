# README - Projetos de geração de XML com base em arquivos CSV

Este repositório contém projetos desenvolvidos para facilitar processos específicos na plataforma InvoiCy. Todos os projetos seguem uma estrutura padrão, e as instruções apresentadas neste README se aplicam a todos eles. Vale destacar que os dados e a estrutura dos arquivos CSV variam conforme o caso, mas cada projeto inclui um exemplo de CSV para preenchimento.

O objetivo dos projetos é utilizar uma base de dados em formato CSV para gerar arquivos XML. Estes arquivos podem ser utilizados para diferentes finalidades, como cadastro de empresas, consulta de documentos, geração de inutilizações de números, entre outros. Embora cada projeto tenha suas particularidades, o funcionamento geral segue o mesmo princípio.

A plataforma InvoiCy é um software de gestão fiscal que oferece captura e emissão de diversos modelos de documentos fiscais. Para saber mais sobre a plataforma, [clique aqui.](https://migrate.info/)

---

## Funcionalidades

- Processa arquivos CSV com delimitador `;` e converte cada linha em um arquivo XML individual.
- Cria automaticamente o diretório de saída se ele não existir.
- Ignora campos vazios no CSV durante a conversão.

---

## Requisitos

- Python 3.6 ou superior
- Biblioteca padrão do Python:
  - `csv`
  - `os`
  - `xml.etree.ElementTree`

---

## Como usar

### 1. Clone ou baixe este repositório

Execute o comando abaixo no terminal para obter o projeto:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_DIRETORIO>
```
## 2. Execute o Script

Certifique-se de que o Python está instalado no ambiente. Em seguida, execute o script com o comando:

```bash
python script.py
```
## 3. Insira os Caminhos Solicitados no Terminal

Durante a execução, o script solicitará dois caminhos:

1. **Caminho do diretório ou arquivo CSV**:
   - Para processar vários arquivos CSV, informe o caminho para o diretório que os contém.
   - Para processar apenas um arquivo CSV, informe o caminho completo do arquivo.

2. **Caminho do diretório onde deseja armazenar os XMLs**:
   - Informe o caminho para o diretório de saída onde os arquivos XML serão salvos.
   - Caso o diretório não exista, ele será criado automaticamente.

### Exemplo de entrada no terminal:

```plaintext
Informe o caminho do diretório ou arquivo CSV: ./entrada
Informe o diretório onde deseja armazenar os XMLs: ./saida
```

## 4. Verifique os Arquivos Gerados no Diretório de Saída

Após a execução, os arquivos XML gerados estarão no diretório informado.  
Cada arquivo XML será nomeado no formato `Cad_1.xml`, `Cad_2.xml`, etc., com base na ordem das linhas do CSV.

---

## Estrutura de Arquivos

### Entrada: CSV

O arquivo CSV deve estar no formato delimitado por ponto-e-vírgula (`;`).  
As colunas do CSV serão usadas como elementos XML.

**Exemplo de entrada**:

```csv
ChaveParceiro;EmpNomFantasia;EmpApelido;EmpRazSocial;
Chave de parceiro InvoiCy; Nome fantasia da empresa; Apelido da empresa; Razão social da empresa;
Chave de parceiro InvoiCy; Nome fantasia da empresa; Apelido da empresa; Razão social da empresa;
Chave de parceiro InvoiCy; Nome fantasia da empresa; Apelido da empresa; Razão social da empresa;
```
## Saída: XML

Cada linha do CSV será convertida em um arquivo XML independente.

**Exemplo de saída para a linha `Chave de parceiro InvoiCy; Nome fantasia; Apelido; Razão social;`**:

```xml
<CadastroEmpresa>
	<ChaveParceiro>Chave de parceiro InvoiC</ChaveParceiro>
	<EmpNomFantasia>Nome Fantasia</EmpNomFantasia>
	<EmpApelido>Apelido</EmpApelido>
	<EmpRazSocial>Razão Social</EmpRazSocial>
</CadastroEmpresa>
```

## Exemplo de Estrutura de Diretórios

### Antes da Execução

```bash
./entrada
  ├── empresas1.csv
  ├── empresas2.csv

./saida
  (vazio)
```
### Após a Execução

```bash
./saida
  ├── Cad_1.xml
  ├── Cad_2.xml
  ├── Cad_3.xml
  ├── ...
```
## Customização

- **Alterar delimitador**: Modifique o parâmetro `delimiter` na função `csv.DictReader` para outro delimitador, como vírgula (`,`).
- **Adicionar validações ou filtros**: Personalize a lógica dentro da função `process_csv_file` para manipular os dados antes de gerar os arquivos XML.

O código é modular e fácil de ajustar para outras funcionalidades.

---

## Avisos

1. **Arquivos Existentes**: O script não substitui arquivos XML com o mesmo nome. Certifique-se de que os arquivos existentes no diretório de saída não entrem em conflito com os gerados.
2. **Formato do CSV**: Verifique se o arquivo CSV está corretamente formatado antes de processar, para evitar erros na conversão.
3. **Caminho Correto**: Certifique-se de que os caminhos informados no terminal sejam válidos.

---

## Autor

Desenvolvido por [Lucas Frank Imhof](https://github.com/LucasFImhof). Para contribuições ou dúvidas, entre em contato.
