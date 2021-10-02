# bert-X-bahasa-cased 

<!-- 
Prerender until https://github.com/gradio-app/gradio/pull/277 is merged. Use `markdown2 -x fenced-code-blocks bert-readme.md > bert-readme-rendered.html`
-->

Demo for the `tiny`, `base` and `large` variant of BERT models trained to understand Bahasa Malaysia. Type a sentence in BM, and ask BERT to guess a word masked with '[MASK]'. Inputs are case sensitive. 

Models are made available by [Malaysia AI](https://github.com/malaysia-ai/) on HuggingFace:

+ [bert-tiny-bahasa-cased](https://huggingface.co/malay-huggingface/bert-tiny-bahasa-cased)
+ [bert-base-bahasa-cased](https://huggingface.co/malay-huggingface/bert-base-bahasa-cased)
+ [bert-large-bahasa-cased](https://huggingface.co/malay-huggingface/bert-large-bahasa-cased)

Code for more BM NLP demos [hosted on github.](https://github.com/tnwei/bahasa-malaysia-nlp-demos)

## Usage through Gradio

Gradio supports directly creating an interface for models hosted on HuggingFace. In fact, this is how this application is put together!

``` python
import gradio as gr

iface = gr.Interface.load(
    # replace w/ the intended model variant
    name="malay-huggingface/bert-base-bahasa-cased", src="huggingface"
)
iface.launch()
```

## Usage through Inference API

Alternatively, these models are also accessible directly through HuggingFace's Inference API, allowing easy integration w/ your own applications. Note that if the API wasn't called recently, HuggingFace will need about half a minute to load the models for a cold start.

``` python
import requests

# Sign up w/ HuggingFace to get a API token
# ref: https://api-inference.huggingface.co/docs/python/html/quicktour.html
API_TOKEN = ... 

# Replace URL string w/ the intended model variant
API_URL = "https://api-inference.huggingface.co/models/malay-huggingface/bert-base-bahasa-cased"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Text input to model
prompt = "Cuaca terlalu panas untuk bermain [MASK] di padang bersama kawan-kawan."

# Post API request
response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
output = response.json()

# Output format is a List[Dict]:
# [
#   {
#     "sequence": "Cuaca terlalu panas untuk bermain permainan di padang bersama kawan - kawan.",
#     "score": 0.24029025435447693,
#     "token": 5699,
#     "token_str": "permainan"
#   },
#   ...
# ]

```

## Usage through local inferencing

If your use case requires local inferencing, usage via HuggingFace is quite straightforward:

``` python
# Code adapted from model card at
# https://huggingface.co/malay-huggingface/bert-tiny-bahasa-cased
from transformers import pipeline

# Model-specific and task-specific imports
# In this example we are importing the LM model class
# for BERT to perform mask filling
from transformers import BertTokenizer, BertForMaskedLM  

# Inference pipeline setup
# Will download models when run for the first time
# On Linux, models are stored in ~/.cache/huggingface/transformers
model_name = "malay-huggingface/bert-base-bahasa-cased"
model = BertForMaskedLM.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(
    model_name, do_lower_case = False,
)
fill_mask = pipeline('fill-mask', model=model, tokenizer=tokenizer)

# Inferencing
prompt = "Cuaca terlalu panas untuk bermain [MASK] di padang bersama kawan-kawan."
output = fill_mask(prompt)

# Output format is a List[Dict]:
# [
#   {
#     "sequence": "Cuaca terlalu panas untuk bermain permainan di padang bersama kawan - kawan.",
#     "score": 0.24029025435447693,
#     "token": 5699,
#     "token_str": "p e r m a i n a n"
#   },
#   ...
# ]

```
Refer to [`transformers` docs](https://huggingface.co/transformers/) and the hosted model repos linked above for more info.