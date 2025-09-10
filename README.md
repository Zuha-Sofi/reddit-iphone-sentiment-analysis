# iPhone Sentiment & Topic Modelling (Reddit)

This project analyzes Reddit discussions about **iPhones** using **sentiment analysis** and **topic modelling**. By leveraging Natural Language Processing (NLP) techniques, we classify user sentiment (positive, negative, neutral) and uncover hidden discussion themes around Apple’s flagship product.  

The project was completed as part of the *COSC2671 – Social Media and Network Analytics* course at RMIT University.  

---

## 📌 Objectives
- Collect Reddit data from the **r/iPhone** subreddit using the Reddit API.  
- Preprocess and clean text (tokenization, stopword removal, lemmatization).  
- Perform sentiment analysis using:  
  - Opinion word counting.  
  - VADER Sentiment Analysis.  
- Apply **Latent Dirichlet Allocation (LDA)** for topic modelling.  
- Visualize trends in sentiment and identify dominant topics in user discussions.  

---

## ⚙️ Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/iphone-sentiment-analysis.git
   cd iphone-sentiment-analysis
   Install dependencies

2. **pip install -r requirements.txt**


3. **Set up Reddit API credentials**

Create an app at Reddit Developer Apps

Store credentials securely as environment variables (or in a .env file you don’t commit):

export REDDIT_CLIENT_ID=your_client_id
export REDDIT_CLIENT_SECRET=your_client_secret
export REDDIT_USERNAME=your_username
export REDDIT_PASSWORD=your_password

The notebook will:

Collect Reddit posts & comments from r/iPhone.

Clean and preprocess the text corpus.

Apply Count-based and VADER sentiment analysis.

Perform topic modelling with LDA.

Generate visualizations (word frequency, sentiment timelines, intertopic distance map).

## 📊 Key Insights

- Sentiment

    -Count-based method shows greater swings in sentiment (positive/negative extremes).

    -VADER provides a smoother, largely positive trend.

- Topics Identified (10 clusters)
  
  -iPhone models & upgrades.
  
  -Hardware features (camera, battery, screen).

- App usage & updates.

  -Support, bug fixes, and user issues.
  
  -Purchase decisions and user experiences.

These findings highlight consumer interests, common frustrations, and areas where Apple can focus improvements.
