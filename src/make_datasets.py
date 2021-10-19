import unicodedata
import os    
import cfg
import nltk
from tqdm import tqdm
import glob
from random import sample

def sample_and_make_tempfile(sentences_dir, num_files):
    """ Use the set of files containing a sentence per line,
    sample num_files out of those and save as a temp file """

    sentence_files = glob.glob(sentences_dir + "/*.txt")

    # sample num_files
    sampled_files=sample(sentence_files, num_files)

    print("sampled files:")
    print(sampled_files)

    #read all the lines from sampled files and save to a list
    all_lines = []
    for filename in sampled_files:
        with open(filename) as f:
            lines = f.read().splitlines()
            
        all_lines.extend(lines)

    print("number of lines sampled:", len(all_lines))

    #combine into a single file and save
    tempfile_path = os.path.join(cfg.DATA_DIR, "temp.txt")
    with open(tempfile_path, "w") as f:

                for sentence in tqdm(all_lines):
                    
                    # remove newlines
                    line = sentence.strip()

                    # do not save empty items such as
                    if sentence != []:

                        f.writelines(sentence + '\n')

    print("Wrote to ", tempfile_path)
    return tempfile_path


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