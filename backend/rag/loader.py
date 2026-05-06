import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

from backend.rag.ocr import (
    extract_text_from_image,
    extract_text_from_scanned_pdf
)


def load_all_files(folder_path):
    documents = []

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        # NORMAL PDF
        if file.endswith(".pdf"):

            try:
                loader = PyPDFLoader(file_path)
                docs = loader.load()

                # if text exists
                if docs and len(docs[0].page_content.strip()) > 50:

                    for d in docs:
                        d.metadata["source"] = file

                    documents.extend(docs)

                else:
                    # scanned pdf → OCR
                    text = extract_text_from_scanned_pdf(file_path)

                    documents.append(
                        Document(
                            page_content=text,
                            metadata={"source": file}
                        )
                    )

            except:
                # fallback OCR
                text = extract_text_from_scanned_pdf(file_path)

                documents.append(
                    Document(
                        page_content=text,
                        metadata={"source": file}
                    )
                )

        # IMAGE OCR
        elif file.endswith((".png", ".jpg", ".jpeg")):

            text, confidence = extract_text_from_image(file_path)

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": file,
                        "type": "image",
                        "ocr_confidence": confidence
                    }
                )
            )

    return documents
