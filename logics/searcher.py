import torch
import requests
import sys
from bs4 import BeautifulSoup
from transformers import AutoTokenizer, AutoModelWithLMHead

class Search:
    def result(request, url):
        tokenizer = AutoTokenizer.from_pretrained('t5-base')
        model = AutoModelWithLMHead.from_pretrained('t5-base', return_dict=True)

        URL = url
        r = requests.get(URL)
        r.text
        soup = BeautifulSoup(r.text,'html.parser')
        results = soup.find_all(['h1', 'p'])
        text = [result.text for result in results]
        ARTICLE = ' '.join(text)
        inputs = tokenizer.encode("summarize: " + ARTICLE,
                                    return_tensors='pt',
                                    max_length=512,
                                    truncation=True)
        summary_ids = model.generate(inputs, max_length=150, min_length=80, length_penalty=5., num_beams=2)
        summary = tokenizer.decode(summary_ids[0])
        return summary