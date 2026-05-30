# 🌐 Rakhine – Myanmar Parallel Corpus

This repository contains a parallel dataset for **Rakhine ↔ Myanmar machine translation** and Natural Language Processing (NLP) research.

## 🎯 Purpose

This dataset is designed for:

* Machine Translation (MT)
* Language Modeling
* NLP Research
* Dialect Analysis (Rakhine and Standard Burmese)
* Language Preservation

---

# 📌 Project Overview

The Rakhine language is a major language variety spoken in Rakhine State, Myanmar. However, digital language resources for Rakhine remain limited.

This project aims to build:

* 📚 A parallel sentence corpus (Rakhine ↔ Myanmar)
* 🧠 Training data for AI translation models
* 🔊 Future speech and text datasets
* 🌍 Open resources for Rakhine language technology

---

# 📁 Dataset Structure

```text
rakhine-myanmar-parallel-corpus/
│
├── data/
│   ├── train.csv
│   ├── dev.csv
│   └── test.csv
│
├── raw_data/
│   ├── rakhine_text.txt
│   └── myanmar_text.txt
│
├── scripts/
│   ├── align_sentences.py
│   └── clean_data.py
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# 📊 Data Format

## CSV Format (Parallel Sentences)

| rakhine       | myanmar       |
| ------------- | ------------- |
| ငါ စားပြီးပြီ | ငါ စားပြီးပြီ |
| နင် ဇာလဲ      | သင် ဘယ်မှာလဲ  |

---

# ⚙️ How to Build the Dataset

## 1. Prepare Raw Text Files

Place the following files in the `raw_data/` directory:

* `raw_data/rakhine_text.txt`
* `raw_data/myanmar_text.txt`

## 2. Run the Alignment Script

```bash
python scripts/align_sentences.py
```

## 3. Generated Output

```text
data/train.csv
```

---

# 🧠 Use Cases

* Neural Machine Translation (NMT)
* Chatbot Training
* Rakhine–Myanmar Language Research
* Dialect Comparison
* Language Preservation
* NLP Benchmark Development

---

# 🚀 Future Improvements

* Add an English translation layer (Rakhine ↔ Myanmar ↔ English)
* Add speech datasets (audio + transcription)
* Improve alignment using semantic similarity models
* Expand the dataset to 10,000+ sentence pairs
* Publish on Hugging Face Datasets
* Create benchmark evaluation datasets

---

# ⚠️ Limitations

* The initial dataset uses rule-based sentence alignment (line-by-line).
* Translation quality depends on manual curation.
* Semantic alignment methods are recommended for large-scale datasets.
* The dataset is currently limited in size and coverage.

---

# 📜 License

This dataset is intended for research, education, and open-source NLP development.

Recommended license:

**Creative Commons Attribution 4.0 International (CC BY 4.0)**

---

# 🤝 Contribution

Contributions are welcome.

You can help by:

* Adding new sentence pairs
* Improving translations
* Fixing alignment issues
* Adding dialect variations
* Reporting errors
* Expanding vocabulary coverage

---

# 🌍 Goal

To support the digital preservation, research, and AI development of the Rakhine language and its dialects.

---

# 📬 Contact

Researchers, developers, linguists, and community contributors interested in Rakhine NLP and language technology are welcome to collaborate.

