# ５．９　　函数注解
# python3提供了一种句法，用于为函数声明中的参数和返回值附加元数据。示例５．１９是５．１５添加注解后的版本，唯一的确保是第一行

# def clip(text,max_len= 80):
def clip(text:str,max_len:'int > 0'=80) -> str:
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


# 1.有注解的函数声明　　　函数省中的各个参数可以在：
# 之后增加注解表达式。如果参数有默认值，注解放在参数名和＝之间
# 如果想注解返回值，在)和函数声明末尾的:之间添加-> 和一个表达式。
# 那个表达式可以是任何类型。注解中最常用的类型是类(如，str,init)和字符串(如'int>0') 在示例5.19中，max_len参数的注解用的是字符串

# 注解不会做任何处理，只是存储在函数的__annotations__属性(一个字典)中：
