from services.browser_service import iniciar_driver
from services.pdf_service import gerar_pdf
from services.parser_service import extrair_produtos
import json
import os


def main():
    url = input("Digite a URL da NFCe: ").strip()

    if not url.startswith("http"):
        print("URL inválida.")
        return

    driver = iniciar_driver()

    try:
        print("Gerando PDF...")
        pdf_path = gerar_pdf(driver, url)

        print("Extraindo produtos...")
        produtos = extrair_produtos(pdf_path)

        print("\nResultado:\n")
        print(json.dumps(produtos, indent=4, ensure_ascii=False))

    except Exception as e:
        print("Erro:", e)

    finally:
        driver.quit()

        if os.path.exists(pdf_path):
            os.remove(pdf_path)


if __name__ == "__main__":
    main()