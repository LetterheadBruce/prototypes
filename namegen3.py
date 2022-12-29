import openai

# Replace YOUR_API_KEY with your actual API key
openai.api_key = "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"

def generate_subject_lines_and_preview_text(text):
    # Set the prompt for GPT-3
    prompt = f"Generate a list of potential email subject lines and preview text for the following text: '{text}'"
    
    # Use the GPT-3 API to generate subject lines and preview text
    completions = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024)
    
    subject_lines_and_preview_text = []
    
    # Get the generated subject lines and preview text
    for choice in completions.choices:
        subject_line = choice.text.strip()
        preview_text = choice.text.strip()
        subject_lines_and_preview_text.append((subject_line, preview_text))
    
    return subject_lines_and_preview_text

# Example usage
text = "In this week's newsletter, we cover the latest trends in technology and how they are shaping the future of business. We also have an exclusive interview with a leading industry expert and a round-up of the top news stories of the week."
subject_lines_and_preview_text = generate_subject_lines_and_preview_text(text)
print(subject_lines_and_preview_text)
