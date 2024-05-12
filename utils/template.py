EXTRACTOR_TEMPLATE = """你是一名数据工程师。我将给你一段文字，该文字包含了6个query和5个answer，每个query里面包含1个headline和1个question。
你需要根据以下提示识别出headline、question、answer。
1.在每对query和answer后面，总是有\n\n出现
2.在每个query内，headline总是先出现，然后是question
3.有时候headline和question会被\"包围
4.answer总是在query的后面，且只有两种值:Yes和No
5.在一个query里，你必须提取出headline和question。
6.你必须严格按照文字提供的内容进行输出，不能擅自总结、提炼、修改原文。
7.headline、question和answer两侧的非文字类符号需要去除。

文字:{few_shot_text}

你需要严格按照以下的json格式输出6组headline，question和answer，：后面是对数据类型的要求，//后面是对数据内容的要求。
```json```
{
    "headline": str
    "question": str
    "answer":   bool //如果答案是Yes，则为True，否则为False。如果没有answer，则为Null。
}

"""



