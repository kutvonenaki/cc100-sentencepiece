import unicodedata
import os    
import cfg
import nltk
from tqdm import tqdm


def chunks(sentences, n, tot_len):
    """Yield successive n-sized chunks from sentences."""
    for i in range(0, tot_len, n):
        end_i = min(len(sentences),i + n)
        yield sentences[i:end_i]["text"]
        
        

def make_sentence_files(dataset, chunksize = 10000000, data_dir = cfg.JP_SENTENCES_DIR):
    """
    Make a sentence per line files, chuncsize sentences per file"""
    
    # make sure data dir exists
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        
    # use simple regex for sentence tokenizing
    sent_detector = nltk.RegexpTokenizer(u'[^　！？。]*[！？。.\n]')
    
    # loop over the chunks
    for chunk_ind, sentence_chunk in enumerate(chunks(dataset, chunksize, len(dataset))):
        
        # new file for each chunk
        filename = "sent_{}.txt".format(chunk_ind)
        filepath = os.path.join(data_dir, filename)
        
        print("writing to ", filepath)
                                                
        with open(filepath, "w") as f:

            for sentence in tqdm(sentence_chunk):
                
                # remove newlines
                line = sentence.strip()

                # unicode normalize japanese spaces etc
                unicodedata.normalize('NFKC', line)

                # tokenize into sentences
                sentences = sent_detector.tokenize(line)

                # do not save empty items such as
                if sentences != []:

                    f.writelines(s + '\n' for s in sentences)