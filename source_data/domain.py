"""清点已提供的描述符和导出文件。"""
from .io import asset,unique,integer

def summarize(v,root):
    raw,digest=asset(root,v['source']);d=v['descriptor'];names=unique(d['messages'],'name')
    if v['root_message'] not in names:raise ValueError('根消息未定义')
    for m in d['messages']:
        nums=[integer(f['number'],1) for f in m['fields']]
        if len(nums)!=len(set(nums)):raise ValueError('字段号重复')
    return {'raw_bytes':len(raw),'sha256':digest,'message_types':len(names),'root_message':v['root_message']}
