# 🍦 Gelato Mágico - Prevendo Vendas de Sorvete

## 📌 Cenário
Imagine que você é proprietário de uma sorveteria chamada **Gelato Mágico**, localizada em uma cidade litorânea.  
Você percebe que a quantidade de sorvetes vendidos diariamente tem uma forte correlação com a **temperatura ambiente**.  

Sem planejamento, você pode:
- Produzir **mais do que o necessário** → gerando desperdício.
- Produzir **menos que a demanda** → perdendo vendas.

Para resolver isso, aplicamos **Machine Learning** para prever quantos sorvetes serão vendidos com base na temperatura do dia.

---

## 🎯 Objetivo do Projeto
- ✅ Treinar um modelo de **regressão preditiva** para prever vendas de sorvete com base na temperatura.  
- ✅ Registrar e gerenciar o modelo com **MLflow**.  
- ✅ Criar uma API simples com **Flask** para realizar previsões em tempo real.  
- ✅ Estruturar o projeto para garantir **reprodutibilidade**.  

---

## 🛠️ Estrutura do Projeto
gelato-magico/
│-- data/ # Scripts e dados
│ └── generate_data.py
│-- inputs/ # Arquivos de entrada (texto)
│ └── sentences.txt
│-- models/ # Modelos treinados (joblib)
│-- src/ # Código principal
│ ├── train.py # Treino e logging do modelo
│ └── serve.py # API para servir previsões
│-- requirements.txt # Dependências do projeto
│-- README.md # Documentação

---

## 📊 Resultados do Modelo
Após treinar o modelo de **Regressão Linear**, obtivemos os seguintes resultados:

- **R² (Coeficiente de Determinação):** `0.97` (indica boa explicação da variação das vendas)
- **RMSE (Raiz do Erro Quadrático Médio):** `19.85` (erro médio em torno de 20 unidades de sorvete)

<img width="440" height="91" alt="image" src="https://github.com/user-attachments/assets/0f83d9c5-f40b-4d6c-a4a9-fc7eb2fd6c85" />


---

## 🚀 API de Previsão
O modelo pode ser usado via **Flask API**.  

1. Execute a API:
```bash
python src/serve.py

---

<img width="425" height="245" alt="image" src="https://github.com/user-attachments/assets/2ba3fb9f-e604-412d-92ea-7e4674247d1c" />
