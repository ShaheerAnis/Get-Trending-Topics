from pytrends.request import TrendReq

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Get the top trending topics
def get_trending_topics():
    try:
        # Fetch the top trending topics on Google
        trending_data = pytrends.trending_searches(pn='united_states')

        if trending_data.empty:
            return ["No trending topics found."]

        # Extract trending topics from the DataFrame
        trending_topics = list(trending_data[0])

        return trending_topics

    except Exception as e:
        return [f"An error occurred: {str(e)}"]

if __name__ == "__main__":
    trending_topics = get_trending_topics()
    
    print("Top Trending Topics:")
    for i, topic in enumerate(trending_topics, start=1):
        print(f"{i}. {topic}")
