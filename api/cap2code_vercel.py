# webio整合flask需要
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
# 脚本需要
from pywebio.input import *
from pywebio.output import *
from pywebio.session import set_env

# 自己程序
def cap_namer(value_str):
    value_str = value_str.lower()
    if 'u' in value_str:
        base = 1000000
    elif 'nc' in value_str:
        return 'NC'
    elif 'n' in value_str:
        base = 1000
    elif 'p' in value_str:
        base = 1
    else:
        raise('erro value')
    value_flt = float(value_str[:-2])
    inner_flt = value_flt * base
    if inner_flt < 10:
        code = str(inner_flt).replace('.','R')
    else:
        code = str(inner_flt)[:2] + str(len(str(inner_flt)) - 4)
    return code
# 自己程序
def task_func():
    set_env(title="CAP Code Calculation")

    put_markdown('本页面可以将电容值批量转换为订购时的三位代码。')
    
    values = textarea('输入电容值：', rows=15, placeholder='一行一个')

    codes = ''
    for value in values.split():
        codes = codes +  cap_namer(value) + '\n'

    put_markdown('电容代码为：')
    put_markdown(codes)

# Flask+WebIO框架
app = Flask(__name__)

# `task_func` is PyWebIO task function
app.add_url_rule('/', 'webio_view', webio_view(task_func),
            methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS methods