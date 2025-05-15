# Fake Job Detection System

An advanced NLP-based system designed to identify fraudulent job postings using state-of-the-art machine learning techniques. This project leverages Natural Language Processing (NLP) to analyze job descriptions and detect potential scams or fake job listings.

## NLP Features

- Advanced text preprocessing pipeline
- TF-IDF vectorization for feature extraction
- N-gram analysis for capturing context
- Stopword removal and text normalization
- Part-of-speech tagging for semantic analysis

## Machine Learning Components

- XGBoost classifier for high accuracy predictions
- Feature engineering for text data
- Hyperparameter optimization
- Cross-validation for model robustness

## Technical Features

- Web interface for job description input
- Real-time prediction of job posting authenticity
- Built with Flask framework
- Uses XGBoost for classification
- TF-IDF vectorization for text processing

![image](https://github.com/user-attachments/assets/5e4f3833-d274-4e10-9346-263c587c48bd)

![image](https://github.com/user-attachments/assets/5b5f9c61-5e34-4a93-a086-fb399e79d9dd)


## Project Structure

```
fake_job_detection/
├── flask_app/
│   ├── app.py           
│   └── templates/
│       └── index.html   
├── models/
│   ├── xgboost_model.pkl  # Trained XGBoost model
│   └── tfidf_vectorizer.pkl  # TF-IDF vectorizer
├── notebooks/           # Jupyter notebooks for model training
└── requirements.txt     
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Kundhave/Fake-Job-Posting-Detection-.git
   cd Fake-Job-Posting-Detection-
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   cd flask_app
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Enter a job description in the text box
2. Click the submit button
3. The system will predict whether the job posting is real or fake

## Model Details

- **Algorithm**: XGBoost
- **Features**: TF-IDF vectorized job descriptions
- **Training Data**: Dataset of labeled job postings
- **Accuracy**: 97% 

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

