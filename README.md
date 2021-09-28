# bahasa-malaysia-nlp-demos

Demos and code samples for BM NLP models from [malay-huggingface](https://huggingface.co/malay-huggingface).

Status of all available model repos and demos documented in [STATUS.md](STATUS.md), tracked as issues in the related [github repo](https://github.com/malaysia-ai/malay-huggingface). Completed demos are shown below.

##  BERT models

The BERT models have the `fill-mask` inference API ready to use, making it possible to host a light-weight demo without requiring significant compute.  Simple Gradio demo implemented in`bert-X-bahasa-cased.py`. 

BERT models have their own readme at [bert-readme.md](bert-readme.md). Demo hosted at [https://huggingface.co/malay-huggingface/bert-base-bahasa-cased](https://huggingface.co/malay-huggingface/bert-base-bahasa-cased) (previously [https://bert-x-bahasa-cased.herokuapp.com/](https://bert-x-bahasa-cased.herokuapp.com/))
<!--
Open items moving ahead:
+ What other tasks available
-->

    
| Model name              | Repo status | Inference API     | Demo status | Link to model repo
| ----------------------- | --------- | ----------------- | ----------- | ----
| bert-tiny-bahasa-cased  | Ready     | Ready (fill-mask) | Ready, [https://huggingface.co/spaces/malay-huggingface/bert-x-bahasa-cased](https://huggingface.co/spaces/malay-huggingface/bert-x-bahasa-cased)       | [https://huggingface.co/malay-huggingface/bert-tiny-bahasa-cased](https://huggingface.co/malay-huggingface/bert-tiny-bahasa-cased)
| bert-base-bahasa-cased  | Ready     | Ready (fill-mask) | Ready, [https://huggingface.co/spaces/malay-huggingface/bert-x-bahasa-cased](https://huggingface.co/spaces/malay-huggingface/bert-x-bahasa-cased)       | [https://huggingface.co/malay-huggingface/bert-base-bahasa-cased](https://huggingface.co/malay-huggingface/bert-base-bahasa-cased)     
| bert-large-bahasa-cased | Ready     | Ready (fill-mask) | Ready, [https://huggingface.co/spaces/malay-huggingface/bert-x-bahasa-cased](https://huggingface.co/spaces/malay-huggingface/bert-x-bahasa-cased)       | [https://huggingface.co/malay-huggingface/bert-large-bahasa-cased](https://huggingface.co/malay-huggingface/bert-large-bahasa-cased)
