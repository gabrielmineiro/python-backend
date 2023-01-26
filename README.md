# BACK-END

<h3>Passos para rodar a aplicação em ambiente de desenvolvimento:</h3>

1. Crie um banco de dados POSTGRES em sua máquina.</br>

2. Crie um ambiente virtual na sua máquina com o comando <code> python -m venv venv </code> e ative esse mesmo ambiente com o comando <code> source venv/scripts/activate </code>

3. Rode o comando <code> pip install -r requirements.txt</code> para instalar todas as depêndencias necessárias da aplicação.</br>

4. Agora é hora de configurar o seu <code>.env</code>, para isso clone o arquivo <code>.env.example</code> e o renomeie apenas para <code>.env</code>, feito isso você vai encontrar 4 chaves nesse arquivo, a primeira é <b>POSTGRES_DB</b> que deve ser preenchida com o nome do banco de dados criado no passo 1. A segunda chave é <b>POSTGRES_USER</b> que é onde você colocará o nome do seu usuário do POSTGRES. A penúltima chave é a <b>POSTGRES_PASSWORD</b>, onde você colocará a senha do seu usuário. E finalmente tem a chave <b>SECRET_KEY</b> onde você colocará uma string aleatória. Com isso feito, o seu <code>.env</code> já estará configurado.</br>

5. Para criar todas as migrations presentes na aplicação, rode <code> python manage.py makemigrations</code>

6. Para persistir as migrations no banco de dados, rode <code> python manage.py migrate</code>

7. Feito isso, rode <code> python manage.py runserver</code> para iniciar o servidor.</br>

8. No seu navegador acesse <code>http://127.0.0.1:8000</code></br>
