import openai
import os
os.environ['OpenAI_API_Key'] = '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'
# key = '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'
openai.api_key = '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'

response = openai.Completion.create(model='text-davinci-003',
                                    prompt='Give me two reasons to learn OpenAI API with Python',
                                    max_tokens=300)

print(response['choices'][0]['text'])