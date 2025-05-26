from sumy.parsers.plaintext import PlaintextParser #Parses plain text input
from sumy.nlp.tokenizers import Tokenizer #Tokenizes text into sentences and words.
from sumy.summarizers.lsa import LsaSummarizer #Implements the Latent Semantic Analysis (LSA) algorithm for summarizing text.

def summarize_text(text, sentence_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)

# Takes the full article text, summarizes it using summarize_text, and returns the result.
def main(article_text):
    summary = summarize_text(article_text)
    return summary

# Input Article that Needs to be Summarized.
article = """
Regular exercise is one of the most important things you can do for your health. It has many benefits, including improving your overall health and fitness, and reducing your risk for many chronic diseases. There are many different types of exercise, including aerobic, strength training, balance, and flexibility exercises.
Aerobic exercise, such as walking, running, or cycling, increases your breathing and heart rate and is good for your heart and lungs. Strength training, like lifting weights, improves muscle strength and bone health. Flexibility exercises, such as stretching and yoga, enhance the range of motion of your joints and prevent injuries. Balance exercises help prevent falls, which is especially important for older adults.
Regular physical activity can also help you manage your weight, reduce stress and anxiety, and improve your mood. It can lead to better sleep and increased energy levels. In addition, exercise plays a significant role in preventing diseases such as heart disease, diabetes, cancer, and depression.
Experts recommend that adults get at least 150 minutes of moderate-intensity aerobic activity or 75 minutes of vigorous-intensity activity each week, along with muscle-strengthening activities on two or more days a week. Even small amounts of physical activity are better than none and provide health benefits.
Incorporating exercise into your daily routine can be simple and enjoyable. Whether it's taking the stairs instead of the elevator, going for a walk during your lunch break, or joining a fitness class, every bit of movement counts.
"""
summary = main(article)

print(f'Given Article: {article}') #Shows the Input Article
print(f'Concise Summary: {summary}') #Shows the Concised Summary.