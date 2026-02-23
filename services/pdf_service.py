import base64
import time
import config


def gerar_pdf(driver, url):
    driver.get(url)
    time.sleep(5)

    result = driver.execute_cdp_cmd(
        "Page.printToPDF",
        {"printBackground": True}
    )

    with open(config.PDF_OUTPUT_PATH, "wb") as f:
        f.write(base64.b64decode(result["data"]))

    return config.PDF_OUTPUT_PATH