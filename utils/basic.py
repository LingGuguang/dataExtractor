import json

def read_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        ret = json.load(f)
    return ret


def save_json(path, dic):
    with open(path,"w", encoding='utf-8') as f: 
        f.write(json.dumps(dic,ensure_ascii=False, indent=2)) 

def save_txt(path, dic):
    with open(path, 'w+', encoding='utf-8') as f:
        f.write(dic)