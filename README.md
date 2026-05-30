# 🌐 Rakhine – Myanmar Parallel Corpus

This repository contains a parallel dataset for **Rakhine ↔ Myanmar language machine translation** and NLP research.

It is designed for:
- Machine Translation (MT)
- Language modeling
- NLP research
- Dialect analysis (Rakhine Burmese)

---

# 📌 Project Overview

Rakhine language is a major dialect/language variety in Myanmar, but digital language resources are still limited.

This project aims to build:
- 📚 Parallel sentence corpus (Rakhine ↔ Myanmar)
- 🧠 Training data for AI translation models
- 🔊 Future speech + text datasets

---

# 📁 Dataset Structure

rakhine-myanmar-parallel-corpus/
│
├── data/
│ ├── train.csv
│ ├── dev.csv
│ ├── test.csv
│
├── raw_data/
│ ├── rakhine_text.txt
│ ├── myanmar_text.txt
│
├── scripts/
│ ├── align_sentences.py
│ ├── clean_data.py
│
├── README.md
├── LICENSE


---

# 📊 Data Format

## CSV format (parallel sentences)

| rakhine | myanmar |
|---------|---------|
| ငါ စားပြီးပြီ | ငါ စားပြီးပြီ |
| နင် ဇာလဲ | သင် ဘယ်မှာလဲ |

---

# ⚙️ How to Build Dataset

### 1. Prepare raw text files
- `raw_data/rakhine_text.txt`
- `raw_data/myanmar_text.txt`

### 2. Run alignment script
```bash
python scripts/align_sentences.py

---

### 3. Output generated:
data/train.csv

---

# 🧠 Use Cases
Neural Machine Translation (NMT)
Chatbot training
Dialect comparison (Rakhine vs Standard Burmese)
Language preservation

---

# 🚀 Future Improvements
Add English translation layer (Rakhine ↔ Myanmar ↔ English)
Add speech dataset (audio + transcription)
Improve alignment using semantic similarity models
Expand dataset to 10,000+ sentence pairs

---

# ⚠️ Limitations
Initial dataset is rule-based aligned (line-by-line)
Sentence quality depends on manual curation
Advanced semantic alignment is recommended for large-scale training

---

# 📜 License

This dataset is intended for research and open-source NLP development.

Suggested license:

Creative Commons Attribution 4.0 (CC BY 4.0)

---

# 🤝 Contribution

Contributions are welcome:

Add new sentence pairs
Improve translations
Fix alignment issues
Add dialect variations

---

# 🌍 Goal

To support digital preservation and AI development for the Rakhine language and its dialects.

---

# 📬 Contact

If you are contributing to Rakhine NLP or language technology projects, collaboration is welcome.
