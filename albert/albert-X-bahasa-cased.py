import gradio as gr
from gradio.mix import Parallel
import argparse
from pathlib import Path

wd = Path(__file__).parent.resolve()

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=7860)
args = parser.parse_args()


iface_tiny = gr.Interface.load(
    name="malay-huggingface/albert-tiny-bahasa-cased", src="huggingface"
)
iface_base = gr.Interface.load(
    name="malay-huggingface/albert-base-bahasa-cased", src="huggingface"
)
iface_large = gr.Interface.load(
    name="malay-huggingface/albert-large-bahasa-cased", src="huggingface"
)

with open(wd / "albert-readme.md", "r") as f:
    long_description = f.read()

combo_iface = Parallel(
    iface_tiny,
    iface_base,
    iface_large,
    inputs=["text"],
    description="Type a sentence in BM, and ask BERT to guess a word masked with '[MASK]'",
    outputs=[gr.outputs.Label(num_top_classes=3)] * 3,  # too crowded!
    title="Demo for malay-huggingface/albert-X-bahasa-cased",
    article=long_description,
    examples=[
        ["Permohonan Najib, anak untuk dengar isu perlembagaan [MASK]."],
        ["Cuaca terlalu panas untuk bermain [MASK] di padang bersama kawan-kawan."],
    ],
    # Serving on Heroku
    server_port=args.port,
    server_name="0.0.0.0",
)
combo_iface.launch()
