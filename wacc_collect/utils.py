import PyPDF2
import re
import pandas as pd

def find_wacc_ltgr(pdf_path, company_name):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        results = []

        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()

            if company_name.lower() in text.lower():
                broker_match = re.search(
                    r'\b(?:Banco Santander|UBS Equities|Morgan Stanley|JPMorgan|Warburg Research GmbH|Societe Generale|RBC Capital Markets|Jefferies|BNP Paribas Exane|Deutsche Bank|Barclays)\b',
                    text)
                broker = broker_match.group(0) if broker_match else 'Others'

                # Updated regex to capture various formats of WACC mention
                wacc_match = re.search(r'(?:(?:WACC|discount back at|WACC of)\s*[:=]?\s*(\d+\.?\d*)%|(\d+\.?\d*)%\s*WACC)',
                                       text, re.IGNORECASE)
                ltgr_match = re.search(r'(?:(?:LTGR|terminal growth rate)\s*[:=]?\s*(\d+\.?\d*)%|(\d+\.?\d*)%\s*LTGR)',
                                       text, re.IGNORECASE)
                wacc = None
                if wacc_match:
                    wacc = wacc_match.group(1) or wacc_match.group(2)
                    wacc = float(wacc) if wacc else None

                ltgr = None
                if ltgr_match:
                    ltgr = ltgr_match.group(1) or ltgr_match.group(2)
                    ltgr = float(ltgr) if ltgr else None

                if wacc is not None or ltgr is not None:
                    result = {
                        'broker': broker,
                        'page_num': page_num + 1,
                        'wacc': wacc,
                        'ltgr': ltgr
                    }
                    results.append(result)

            # Calculate mean and median while limiting to 2 decimal places
            mean_wacc = round(pd.Series([res['wacc'] for res in results if res['wacc'] is not None]).mean(), 2)
            median_wacc = round(pd.Series([res['wacc'] for res in results if res['wacc'] is not None]).median(), 2)
            mean_ltgr = round(pd.Series([res['ltgr'] for res in results if res['ltgr'] is not None]).mean(), 2)
            median_ltgr = round(pd.Series([res['ltgr'] for res in results if res['ltgr'] is not None]).median(), 2)

            summary = {
                'mean_wacc': mean_wacc,
                'median_wacc': median_wacc,
                'mean_ltgr': mean_ltgr,
                'median_ltgr': median_ltgr
            }

        return results, summary
