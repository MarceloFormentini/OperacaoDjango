# Estrutura base do projeto Django
```
OperacaoDjango/            ← Pasta do projeto (raiz)
├── manage.py              ← Script para comandos administrativos
├── OperationDjango/        ← Configurações principais do projeto
│   ├── __init__.py
│   ├── settings.py        ← Configurações do projeto (apps, banco, idioma etc.)
│   ├── urls.py            ← Arquivo de rotas principais
│   ├── asgi.py            ← Entrada para servidores ASGI (Ex: WebSockets)
│   └── wsgi.py            ← Entrada para servidores WSGI (Ex: Gunicorn)
├── tarefas/               ← Sua app personalizada
│   ├── __init__.py
│   ├── admin.py           ← Admin (painel de gestão)
│   ├── apps.py            ← Configurações da app
│   ├── models.py          ← Modelos do banco de dados (ORM)
│   ├── views.py           ← Funções que respondem às requisições (controllers)
│   ├── urls.py            ← Rotas específicas da app
│   ├── tests.py           ← Testes automatizados
│   └── migrations/        ← Arquivos de migração do banco
│       └── __init__.py
```

## Explicação dos Arquivos
✅ manage.py
- Arquivo que você usa para rodar comandos do Django (como runserver, migrate, startapp, etc.)
```
python manege.py runserver
```

✅ settings.py
- Contém todas as configurações do projeto.
- Principais itens configuráveis:
  - INSTALLED_APPS: apps que fazem parte do projeto (ex: 'tarefas')
  - DATABASES: qual banco está usando
  - LANGUAGE_CODE: idioma (ex: pt-br)
  - TIME_ZONE: fuso horário
  - STATIC_URL: arquivos estáticos (CSS, JS)

✅ urls.py (na pasta do projeto)
- Roteador principal do seu site. Direciona URLs para cada app.

✅ wsgi.py e asgi.py
- Entradas para servidores web.
  - wsgi.py é usado em servidores "tradicionais" (Gunicorn, uWSGI)
  - asgi.py é usado para aplicações assíncronas (WebSocket, etc.)

✅ tarefas/views.py
- Onde ficam as funções que recebem a requisição e retornam uma resposta (HTML, JSON, texto, etc.)

✅ tarefas/urls.py
- Define as rotas específicas da app tarefas.

✅ models.py
- Onde define as tabelas do banco de dados (ORM = Object Relational Mapping).

✅ tarefas/admin.py
- Onde você registra modelos para aparecerem no painel administrativo.

✅ tarefas/apps.py
- Arquivo de configuração da app, usado internamente pelo Django.

✅ migrations/
- Armazena os scripts gerados automaticamente para criar ou alterar as tabelas no banco.
```
python manage.py makemigrations
python manage.py migrate
```
✅ tarefas/tests.py
- Onde você escreve testes automatizados para garantir que seu código funciona como esperado.

## Fluxo de requisição no DJango
```
[ Navegador (ex: /tarefas/) ]
            |
            v
[ urls.py do projeto (OperationDjango/urls.py) ]
            |
            v
[ include('tarefas.urls') → urls.py da app ]
            |
            v
[ views.py → função 'home' ou outra view ]
            |
            v
[ Lógica da view (pode acessar banco com models.py) ]
            |
            v
[ Resposta (HttpResponse, render de template, JSON...) ]
            |
            v
[ De volta ao navegador ]
```

Exemplo referente ao código
- Navegador acessa: http://localhost:8000/
- OperationDjango/urls.py:
```
path('', include('tarefas.urls'))
```
- tarefas/urls.py
```
path('', views.home)
```
- tarefas/views.py
```
def home(request):
	return HttpResponse("Olá, Django!")
```

## 🧪 Testes
Realizados testes automáticos para validar o CRUD.

Para verificar a cobertura de teste com o **coverage**.

Para instalar
```
pip install coverage
```

Executar os testes com o **coverage**
```
coverage run manage.py test
```

Relatório no terminal
```
../OperacaoDjango> coverage report
Name                                 Stmts   Miss  Cover
--------------------------------------------------------
OperationDjango\__init__.py              0      0   100%
OperationDjango\settings.py             18      0   100%
OperationDjango\urls.py                  3      0   100%
manage.py                               11      2    82%
tarefas\__init__.py                      0      0   100%
tarefas\admin.py                         3      0   100%
tarefas\apps.py                          4      0   100%
tarefas\migrations\0001_initial.py       5      0   100%
tarefas\migrations\__init__.py           0      0   100%
tarefas\models.py                        7      1    86%
tarefas\tests.py                        24      0   100%
tarefas\urls.py                          3      0   100%
tarefas\views.py                        25      2    92%
--------------------------------------------------------
TOTAL                                  103      5    95%
```

## 🧬 GitHub Actions
🚀 CI/CD significa:
- CI = Continuous Integration (Integração Contínua)
- CD = Continuous Delivery ou Continuous Deployment (Entrega/Implantação Contínua)

🧪 CI – Continuous Integration (Integração Contínua)
É o processo de testar automaticamente o código toda vez que alguém faz uma alteração (commit ou pull request).

🔧 Com CI, normalmente acontece:
- Rodar testes automatizados
- Verificar estilo/cobertura de código (linters, coverage)
- Garantir que nada quebrou

🚚 CD – Continuous Delivery / Deployment
Depois do código testado com CI, entra o CD:
- Continuous Delivery: o código é preparado para produção, mas precisa de alguém apertar um botão pra ir pro ar.
- Continuous Deployment: vai automaticamente pra produção se tudo der certo nos testes.

