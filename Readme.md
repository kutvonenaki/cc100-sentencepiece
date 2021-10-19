# en-jp common crawl trained sentencepiece tokenizers

- This repo contains pretrained sentencepiece tokenizers for both English and Japanese. Available vocabulary sizes are 8000, 16000, 32000 and 48000. Tokenizers were trained using common crawl, not the full set but around 70M sampled sentences per tokenizer. See the attached blog post for more information.



## Just use the tokenizers
```
import sentencepiece as spm
import cfg
import os
​
modelpath = os.path.join(cfg.MODELS_DIR, "cc100_en_vocab_32000.model")
tokenizer = spm.SentencePieceProcessor(model_file=modelpath)
tokenizer.encode("This is an example sentence", out_type=str)

['▁This', '▁is', '▁an', '▁example', '▁sentence']
```

The default inddices for unknown, beginning of sentence and end of sentence are 0, 1 and 3, respectively. Pad token is not in the model, but one can set for example it as the last token.
```
# special symbols, put the padding as the last symbol
UNK_IDX = tokenizer.piece_to_id('<unk>')
BOS_IDX = tokenizer.piece_to_id('<s>')
EOS_IDX = tokenizer.piece_to_id('</s>')
PAD_IDX = len(tokenizer)

print(UNK_IDX, PAD_IDX, BOS_IDX, EOS_IDX)

0 32000 1 2
```

Check more from the sentencepiece github: https://github.com/google/sentencepiece



## Use the dev environment for retraining (possibly orher languages)

### To start the dev environment

- Make sure you have docker installed
- Clone this repo ``` git clone https://github.com/kutvonenaki/cc100-sentencepiece```
- build container by bin/build_dev.sh, run the container by bin/start_dev_container.sh and start jupyter inside the container by bin/run_jupyter.sh
- by default the container is started in detached mode for long calculations, so killing your terminal won't affect the docker container running possibly at remote host. Thus after starting the container type 
```docker ps``` to see the container name. You can enter the bash at the container by ```docker exec -it container_name /bin/bash ```. Once inside the container run ```bin/run_jupyter``` to start the notebook server

### The actual training

- See the blog post and the jupyter notebook file for details