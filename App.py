from openai import OpenAI
client = OpenAI()

response = client.responses.create(
  prompt={
    "id": "pmpt_6abc048384ac81939a7b9afc6e8511de028f575f0683ece3",
    "version": "2"
  }
)
