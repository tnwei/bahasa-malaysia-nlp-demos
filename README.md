# bahasa-malaysia-nlp-demos

Demos and code samples for BM NLP models from [malay-huggingface](https://huggingface.co/malay-huggingface), also hosted [on github](https://github.com/malaysia-ai/malay-huggingface).

##  BERT models

The BERT models have the `fill-mask` inference API ready to use, making it possible to host a light-weight demo without requiring significant compute.  Simple Gradio demo implemented in`bert-X-bahasa-cased.py`. 

BERT models have their own readme at [bert-readme.md](bert-readme.md). Demo hosted at [https://huggingface.co/malay-huggingface/bert-base-bahasa-cased](https://huggingface.co/malay-huggingface/bert-base-bahasa-cased) (previously [https://bert-x-bahasa-cased.herokuapp.com/](https://bert-x-bahasa-cased.herokuapp.com/))
<!--
Open items moving ahead:
+ What other tasks available
-->

| Model name              | Use via `transformers` | Inference API         | Demo status | Link to hosted model
| ----------------------- | ---------------------- | --------------------- | ----------- | ----
| bert-tiny-bahasa-cased  | Available              | Available (fill-mask) | Available   | https://huggingface.co/malay-huggingface/bert-tiny-bahasa-cased
| bert-base-bahasa-cased  | Available              | Available (fill-mask) | Available   | https://huggingface.co/malay-huggingface/bert-base-bahasa-cased     
| bert-large-bahasa-cased | Available              | Available (fill-mask) | Available   | https://huggingface.co/malay-huggingface/bert-large-bahasa-cased
    
