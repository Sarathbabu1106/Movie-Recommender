🎬 Movie Recommender (Streamlit)
A simple Movie Recommendation System built with Streamlit, using both Collaborative Filtering (SVD) and Content-Based Filtering (TF-IDF + Cosine Similarity).

This app allows users to get movie recommendations either by genre or by movie title.

📂 Project Structure

movie-recommender/
│
├── streamlit_app.py       # Main Streamlit app

├── ml-latest-small/       # Dataset folder
│   ├── ratings.csv
│   ├── movies.csv
│   └── tags.csv

├── requirements.txt       # Dependencies
└── README.md              # Project description
⚙️ Features
By Genre: Get random recommendations from a selected genre.

By Movie Title: Get similar movies based on content features (genres + tags).

Interactive UI: Built with Streamlit for easy deployment and usage.

Datasets: Uses the MovieLens dataset.

🛠 Installation & Setup
Clone the repository:

bash
git clone https://github.com/Sarathbabu1106/movie-recommender.git
cd movie-recommender
Install dependencies:

bash
pip install -r requirements.txt
Run the app locally:

bash
streamlit run streamlit_app.py

Open in browser:

Code
http://localhost:8501

📋 Requirements
Dependencies are listed in requirements.txt:

streamlit
pandas
numpy
scikit-surprise
scikit-learn

🚀 Deployment on Streamlit Cloud

Push your project to GitHub.

Go to Streamlit Cloud.

Connect your GitHub account.

Select your repo and branch.

Set entry point as streamlit_app.py.

Deploy — you’ll get a live URL instantly.

📸 Demo Screenshot (Optional)
Add a screenshot of your app running locally or deployed.

📜 License
This project is for educational purposes. Dataset provided by MovieLens.
