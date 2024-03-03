# Test_streamlit
Aqui serão feitos testes com streamlit para meu projeto

- Bibliotecas utilizadas

    * [Plotly](https://plotly.com/)
    * [Pandas](https://pandas.pydata.org/)
    * [Streamlit](https://streamlit.io/)
    * [HTTPX](https://www.python-httpx.org/)


* Estrutura do Projeto

```markdown
dashboard_vendas/
│
├── app.py
├── Dashboard.py # Aplicação completa!
├── dados/
│   ├── __init__.py
│   └── carrega_dados.py
├── visualizacao/
│   ├── __init__.py
│   ├── tabelas.py
│   └── graficos.py
└── utilidades/
    ├── __init__.py
    └── formatadores.py

```

---

### Para visualizar o projeto execute os comandos abaixo

```docker
docker build -t dash .
```

```docker
docker run -p 8501:8501 dash
```

Depois de executar os comandos acima acesse `http://localhost:8501/` ou `127.0.0.1:8501`
