import pdfplumber
import re

def extrair_produtos(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        texto = ""
        for page in pdf.pages:
            texto += page.extract_text() + "\n"

    padrao = re.compile(
        r"(.+?)\s*\(Código:\s*(\d+)\s*\).*?\n"
        r"Qtde\.:\s*([\d,\.]+)\s*UN:\s*(\w+)\s*"
        r"Vl\. Unit\.:\s*([\d,\.]+)\s*([\d,\.]+)",
        re.MULTILINE
    )

    produtos = []

    for match in padrao.finditer(texto):
        produtos.append({
            "nome": match.group(1).strip(),
            "codigo": match.group(2),
            "quantidade": match.group(3),
            "unidade": match.group(4),
            "valor_unitario": match.group(5),
            "valor_total": match.group(6)
        })

    return produtos