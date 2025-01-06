def clean_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Remove unnecessary spaces and newlines
    cleaned_text = " ".join(text.split())
    return cleaned_text

# Clean the extracted text
cleaned_text = clean_text("data/vat_text.txt")

# Save the cleaned text
with open("cleaned_vat_text.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)
print("Cleaned text saved to 'cleaned_vat_text.txt'")
