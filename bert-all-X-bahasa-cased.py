"""
"""
import gradio as gr
from gradio.mix import Parallel
import argparse
from transformers import BertTokenizer, BertForMaskedLM, pipeline
from typing import List, Dict


iface_tiny = gr.Interface.load(
    name="malay-huggingface/bert-tiny-bahasa-cased", src="huggingface"
)
iface_base = gr.Interface.load(
    name="malay-huggingface/bert-base-bahasa-cased", src="huggingface"
)
iface_large = gr.Interface.load(
    name="malay-huggingface/bert-large-bahasa-cased", src="huggingface"
)

# Prerender until https://github.com/gradio-app/gradio/pull/277 is merged
with open("bert-readme-rendered.html", "r") as f:
    long_description = f.read()

combo_iface = Parallel(
    iface_tiny,
    iface_base,
    iface_large,
    inputs=["text"],
    description="Type a sentence in BM, and ask BERT to guess a word masked with '[MASK]'",
    outputs=[gr.outputs.Label(num_top_classes=3)] * 3,  # too crowded!
    title="Demo for malay-huggingface/bert-X-bahasa-cased",
    article=long_description,
    examples=[
        ["Permohonan Najib, anak untuk dengar isu perlembagaan [MASK]."],
        ["Cuaca terlalu panas untuk bermain [MASK] di padang bersama kawan-kawan."],
    ],
)
combo_iface.launch()
