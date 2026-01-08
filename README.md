# 📊 Inteligência Financeira: Análise de Risco e Inadimplência (ERP)

Este projeto apresenta uma solução de ponta a ponta para gestão de risco financeiro, utilizando **Python** para engenharia de dados e **Power BI** para visualização estratégica. O objetivo é identificar quais canais de aquisição de clientes estão gerando maior faturamento vs. maior risco de inadimplência.

---

## 🖼️ Visualização do Dashboard
![Dashboard de Risco Financeiro](dashboard_final.png)


---

## 🛠️ Tecnologias e Metodologias
- **Tratamento de Dados (ETL):** Utilização de Python (Pandas) para limpeza e normalização de +100 mil registros.
- **Cálculo Estatístico (Z-Score):** Implementação de Z-Score para identificar canais com inadimplência estatisticamente acima da média.
- **Data Viz:** Dashboard em Power BI com design focado em UX para tomada de decisão rápida.

## 📉 Principais Insights Gerados
1. **Identificação de Gargalos:** O canal **LinkedIn Ads** foi identificado como um ponto crítico de risco (Z-Score alto), necessitando de revisão na qualificação de leads.

Na Prática: Isso significa que o custo de aquisição do LinkedIn pode até ser bom, mas a "qualidade" do cliente é baixa. O insight aqui é sugerir ao time de vendas que implemente uma camada de filtragem (como pedir o faturamento da empresa no formulário) para evitar que clientes sem fôlego financeiro entrem na base.

2. **Eficiência por Canal:** O **E-mail Marketing** demonstrou ser o canal mais saudável, com alto faturamento absoluto e baixo valor em atraso.
   
Na Prática: O insight é de investimento. Como o risco é baixo, a empresa pode escalar as campanhas de e-mail sem medo de quebrar o fluxo de caixa. É o canal mais "saudável" para estratégias de retenção.
   
3. **Perfil de Cliente:** O ticket médio de **R$ 25,47 mil** confirma uma operação focada no mercado High-Ticket/B2B.

Na Prática: Cada cliente inadimplente aqui dói muito. Perder um único pagamento de 25 mil é pior do que perder 100 pagamentos de 200 reais. O insight é que o monitoramento deve ser individualizado e não apenas estatístico.

---

## 📁 Estrutura do Repositório
- `Dashboard_Risco_ERP.pbix`: Arquivo original do Power BI.
- `script_tratamento.py`: Código Python utilizado no processamento dos dados.
