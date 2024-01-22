from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

output = generator("Hello, I'm a language model,", max_length=50, num_return_sequences=2)

print(output)