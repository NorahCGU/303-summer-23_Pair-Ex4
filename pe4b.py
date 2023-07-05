import wikipedia
import concurrent.futures
import time

def download_wiki_page(topic):
    try:
        # Create a file with the title of the topic and a .txt extension
        filename = f"{topic}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            # Retrieve the Wikipedia page content
            page = wikipedia.page(topic, auto_suggest=False)
            content = page.content
            # Write the contents of the Wikipedia page to the file
            file.write(content)
    except wikipedia.exceptions.PageError:
        print(f"Page not found: {topic}")
    except Exception as e:
        print(f"Error occurred while downloading {topic}: {str(e)}")

def main():
    # Define the topic for generative artificial intelligence
    topic = "generative artificial intelligence"

    # Get the list of related topics
    related_topics = wikipedia.search(topic)

    # Create a ThreadPoolExecutor with a maximum of 5 threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Submit tasks for each related topic
        futures = [executor.submit(download_wiki_page, topic) for topic in related_topics]

        # Wait for all tasks to complete
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
