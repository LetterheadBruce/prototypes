import openai

# Replace YOUR_API_KEY with your actual API key
openai.api_key = "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"

# Set the prompt for GPT-3
prompt = "Generate a subject line and preview text for an email newsletter with the following content: 'In this week's newsletter, we cover the latest trends in technology and how they are shaping the future of business. We also have an exclusive interview with a leading industry expert and a round-up of the top news stories of the week.' "

# Use the GPT-3 API to generate a subject line and preview text
completions = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024)

# Print the generated subject line and preview text
subject_line = completions.choices[0].text.strip()
print(subject_line)
preview_text = completions.choices[1].text.strip()
print(preview_text)
