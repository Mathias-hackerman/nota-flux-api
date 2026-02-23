
# 🚀 NotaFlux

Automação inteligente para extração estruturada de dados de NFC-e (Nota Fiscal de Consumidor Eletrônica) a partir de QR Code da SEFAZ RJ.

O projeto utiliza Selenium + Microsoft Edge (CDP) para gerar o PDF da nota diretamente da página oficial e realiza parsing automatizado para transformar os itens da compra em JSON estruturado.

---

## 📌 Objetivo

Criar um backend capaz de:

- Acessar uma NFC-e via URL de QR Code
- Gerar o PDF da nota fiscal
- Extrair os produtos automaticamente
- Retornar os dados estruturados em JSON
- Funcionar tanto como script standalone quanto como API Flask

---

## 🧠 Arquitetura

```

NotaFlux/
│
├── app.py                 # API Flask
├── run.py                 # Execução standalone (CLI)
├── config.py              # Configurações do projeto
│
├── services/
│   ├── browser_service.py # Inicialização do Edge (headless)
│   ├── pdf_service.py     # Geração do PDF via CDP
│   └── parser_service.py  # Extração estruturada via regex

````

### 🔹 Separação de responsabilidades

- **browser_service** → Gerencia o driver do navegador
- **pdf_service** → Converte página em PDF
- **parser_service** → Extrai produtos e converte em JSON
- **run.py** → Execução manual
- **app.py** → API REST

---

## ⚙️ Tecnologias Utilizadas

- Python 3.10+
- Selenium
- Microsoft Edge WebDriver
- Chrome DevTools Protocol (printToPDF)
- pdfplumber
- Flask

---

## 🚀 Como Executar

### 🔹 Modo Standalone (CLI)

```bash
python run.py
````

Digite a URL da NFC-e quando solicitado.

---

### 🔹 Modo API (Flask)

```bash
python app.py
```

Endpoint:

```
POST /extrair
{
  "url": "URL_DA_NFCE"
}
```

Retorno:

```json
[
  {
    "nome": "BATATA MONALISA KG",
    "codigo": "134427",
    "quantidade": "1,19",
    "unidade": "KG",
    "valor_unitario": "5,99",
    "valor_total": "7,12"
  }
]
```

---

## 🧩 Como Funciona

1. Selenium abre a página da NFC-e
2. CDP gera PDF da página renderizada
3. pdfplumber extrai texto do PDF
4. Regex estruturada identifica:

   * Nome do produto
   * Código
   * Quantidade
   * Unidade
   * Valor unitário
   * Valor total
5. Retorno estruturado em JSON

---

## 🔥 Diferenciais Técnicos

* Uso direto do `Page.printToPDF` via Chrome DevTools Protocol
* Parser resiliente baseado no padrão real da SEFAZ RJ
* Arquitetura modular
* Possibilidade de rodar 100% headless
* Pode ser adaptado para processamento em memória (stateless)

---

## 📈 Possíveis Evoluções

* Processamento assíncrono com Celery
* Suporte a múltiplos estados
* Conversão automática para banco de dados
* Deploy via Docker
* Versionamento de layouts fiscais

---

## 💡 Caso de Uso

* Controle automático de compras
* Organização financeira
* Sistemas ERP pessoais
* Integração com dashboards

---

## 🏗️ Status do Projeto

✔ Funcional
✔ Modular
✔ Pronto para deploy leve
🔄 Em evolução

---

## 👨‍💻 Autor

Projeto desenvolvido como estudo avançado de:

* Automação Web
* Engenharia reversa de documentos fiscais
* Arquitetura backend modular
* Parsing estruturado de PDF

---

## 📄 Licença

Uso educacional e experimental.


