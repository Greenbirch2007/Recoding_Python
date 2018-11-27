
def clip(text,max_len= 80):
    '''在max_len前面或后面的第一个空格处截断文本
    '''
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ',0,max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rind(' ',max_len)
            if space_after >= 0 :
                end = space_after
        if end is None : # 没有找到空格
            end = len(text)

    return text[:end].rstrip()



def tag(name,*content,cls=None,**attrs):
    '''生成一个或多个HTML标签'''
    if cls is not None:
        attrs['class']  = cls

    if attrs:
        attrs_str = ''.join(' %s=%s' %(attr,value)
                            for attr,value
                            in sorted(attrs.items()))

    else:
        attrs_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>'%(name,attrs_str,c,name) for c in content)

    else:
        return '<%s%s/ > ' %(name,attrs_str)
