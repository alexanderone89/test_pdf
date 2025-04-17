import fitz


def get_text_percentage(file_name: str) -> float:
    doc = fitz.open(file_name)
    print(f'[++++] {doc}')
    for page_num, page in enumerate(doc):
        text_blocks = page.get_text_blocks()
        if not text_blocks:
            print(f'   [+] СТРАНИЦА [{page_num + 1}] - БЫЛА ОТСКАНИРОВАНА')
        else:
            print(f'   [+] СТРАНИЦА [{page_num + 1}] - ТЕКСТ')
    doc.close()


if __name__ == "__main__":
    text_perc = get_text_percentage("expdf.pdf")
