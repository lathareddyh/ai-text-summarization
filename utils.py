from transformers import pipeline
from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM
import PyPDF2

model_name = "facebook/bart-large-cnn"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

summarizer = pipeline(
    "summarization",
    model=model,
    tokenizer=tokenizer
)

# Extract PDF Text
def extract_text_from_pdf(pdf_file):

    text = ""

    reader = PyPDF2.PdfReader(pdf_file)

    for page in reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text


# Summarize Text
def summarize_text(text, max_len=150):

    if len(text.strip()) < 50:
        return "Text is too short to summarize."

    summary = summarizer(
        text,
        max_length=max_len,
        min_length=40,
        do_sample=False
    )

    return summary[0]['summary_text']