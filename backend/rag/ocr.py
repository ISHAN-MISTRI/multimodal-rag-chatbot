import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# OCR from image
def extract_text_from_image(image_path):

    image = Image.open(image_path)

    # resize
    image = image.resize((image.width * 5, image.height * 5))

    # grayscale
    image = image.convert("L")

    # thresholding
    image = image.point(lambda x: 0 if x < 140 else 255)

    custom_config = r'--oem 3 --psm 11'

    # OCR text
    text = pytesseract.image_to_string(
        image,
        config=custom_config
    )

    # OCR confidence data
    data = pytesseract.image_to_data(
        image,
        output_type=Output.DICT
    )

    confidences = []

    for conf in data["conf"]:
        try:
            conf = float(conf)

            if conf > 0:
                confidences.append(conf)

        except:
            pass

    avg_confidence = 0

    if confidences:
        avg_confidence = sum(confidences) / len(confidences)

    print("\n--- IMAGE OCR TEXT ---\n")
    print(text)

    print(f"\nOCR Confidence: {avg_confidence:.2f}%")

    return text, avg_confidence

# OCR from scanned PDF


def extract_text_from_scanned_pdf(pdf_path):
    pages = convert_from_path(
        pdf_path,
        poppler_path=r"C:\poppler-26.02.0\Library\bin"
    )

    full_text = ""

    for page in pages:
        text = pytesseract.image_to_string(page)
        full_text += text + "\n"

    print("\n--- OCR EXTRACTED TEXT ---\n")
    print(full_text)

    return full_text
