from openai import OpenAI

## Set the API key and model name
MODEL="gpt-4o"
client = OpenAI(api_key='')

# Function to read the input text file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to summarize the text using GPT-4
def summarize_text(text):

    completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Help me with youtube transcription summarizing task."},
                {"role": "user", "content": f"Please summarize the following text, there are several subjects. list the subject and summarize the subsequent contents of that subject in bullets. every subject should have at least 5 bullets, each bullets the contents should be a sentences in detail. also write in korean:\n\n{text}"}
                ]
            )
    return completion.choices[0].message.content

# Function to write the summarized text to an output file
def write_text_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

# Main function to execute the summarization
def main(input_file_path, output_file_path):
    input_text = read_text_file(input_file_path)
    summarized_text = summarize_text(input_text)
    write_text_file(output_file_path, summarized_text)

# Example usage
input_file_path = './transcriptions/tmp.txt'
output_file_path = './transcriptions/summary.txt'
main(input_file_path, output_file_path)
