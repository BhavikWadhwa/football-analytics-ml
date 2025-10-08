[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://football-analytics-ml-canadawest.streamlit.app)


# Canada West Soccer Match Predictor

A Python + Streamlit web app that scrapes real match data from the [Canada West Soccer League](https://canadawest.org/sports/msoc/2025-26/schedule), trains a predictive model, and lets users predict match outcomes between any two university teams.

---

## Features
- **Automated Web Scraper**: Collects the latest match results directly from the Canada West website.
- **Machine Learning Model**: Uses logistic regression to predict match results (`home_win`, `away_win`, `draw`).
- **Interactive Streamlit App**: Choose any two teams and view predicted outcomes with confidence percentages.
- **Fully Reproducible**: All data, code, and model files are included.

---

## Project Structure
soccer-project/
│
├── data/
│ └── matches_2025.csv # Scraped match data
│
├── models/
│ ├── match_predictor.pkl # Trained model
│ └── label_encoder.pkl # Team encoder
│
├── src/
│ ├── scrape_canadawest.py # Web scraper
│ └── train.py # Model training script
│
├── app.py # Streamlit prediction app
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## ⚙️ Setup & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/canadawest_predictor.git
cd canadawest_predictor
```

### 2. Create a Virtual Environment
```bash 
python -m venv .venv
.venv\Scripts\activate  # (Windows)

source .venv/bin/activate (Mac/Linux)
```
### 3. Install Dependencies
```bash 
pip install -r requirements.txt
```
### 4. Run the Scraper
```bash 
Fetch the latest match results:

python src/scrape_canadawest.py
```
### 5. Train the Model
```bash 
python src/train.py
```
### 6. Launch the Web App
```bash 
streamlit run app.py
```

## Model Details

**Algorithm**: Logistic Regression

**Features Used**: Encoded home/away teams, goal differences

**Target Classes**: home_win, away_win, draw

## Deployment

You can deploy this on Streamlit Cloud
 easily:

Push your project to GitHub

Connect your repo on Streamlit Cloud

Add the URL: app.py as the entry point

Streamlit will auto-install dependencies via requirements.txt

## Future Improvements

Include player statistics, home advantage, and form-based features

Add visualizations for standings and team trends

Expand to include women’s division and multi-season training

## Author

Bhavik Wadhwa
University of the Fraser Valley