# Instruções para Configurar e Executar o Projeto

Este projeto requer a configuração das credenciais de acesso ao banco de dados oracle e a criação de tabelas com dados de mercado para funcionar corretamente.

## Configuração das Credenciais do Banco de Dados Oracle

As credenciais de acesso ao banco de dados estão localizadas no código, no seguinte diretório: `src/conexion/passphrase/authentication.oracle`. O usuário é 'sys' e a senha é '123mudar'. Certifique-se de ajustar essas credenciais de acordo com suas configurações.

## Criação de Tabelas e Inserção de Dados

Para criar as tabelas necessárias e inserir os dados do mercado, siga estas etapas:

1. Abra o arquivo `sql/create_tables.sql` e verifique se o usuário especificado corresponde ao seu usuário do banco de dados.

2. Abra o arquivo `sql/inserting_samples_records.sql` e faça a mesma verificação.

3. Abra o arquivo `utils/config.py` e faça a mesma verificação.

## Execução dos Scripts

Após configurar as credenciais e verificar os arquivos SQL, você pode iniciar a execução dos scripts. Certifique-se de que o Python 3.9 esteja instalado em sua máquina com o seguinte comando:

```bash
python --version
````

Abra um terminal no diretório do projeto.
Crie um ambiente virtual com o seguinte comando:

```bash
python3 -m venv venv
````

Ative o ambiente virtual com o comando:

```bash
source venv/bin/activate
````

Instale as dependências com o seguinte comando:

```bash
pip install -r requirements.txt
````

Após a instalação das dependências, execute o seguinte comando para criar as tabelas e inserir dados:

```bash
python3.9 create_tables_and_records.py
````

Por fim, execute o programa principal com o seguinte comando:

```bash
python3.9 principal.py
````

Lembre-se de que é necessário ter o Python 3.9 instalado em sua máquina para executar o projeto com sucesso.

## Vídeo de execução

CLique [aqui](https://www.youtube.com/watch?v=oa_AFW3yi-M) para assistir o vídeo de execução do código.



