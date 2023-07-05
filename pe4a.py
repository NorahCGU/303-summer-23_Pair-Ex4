import wikipedia
import time

def download_wikipedia_pages(topic):
    search_results = wikipedia.search(topic)

    start_time = time.time()

    for result in search_results:
        page = wikipedia.page(result, auto_suggest=False)
        title = page.title
        content = page.content

        # Create a file with the topic title and write the content to it
        with open(f"{title}.txt", "w", encoding="utf-8") as file:
            file.write(content)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Execution time: {execution_time} seconds")

# Specify the topic you want to search for
topic = "generative artificial intelligence"

# Call the function to download Wikipedia pages and measure the execution time
download_wikipedia_pages(topic)
