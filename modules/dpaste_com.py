## dpaste.com module
# Sun Aug  2 03:16:49 IST 2009            Abhishek Misha <ideamonk at gmail.com>

# Wanna __hack__ and add more support, look at source of http://dpaste.com
# find this portion - 
# ... 
#    <option value="Python">Python</option>
#    <option value="PythonConsole">Python Interactive/Traceback</option>
#    <option value="Sql">SQL</option>
#    <option value="DjangoTemplate">Django Template/HTML</option>
# ...
# know your extension, find corresponding return value from the html

def get_syntax(ext):
    if ext=='css':
        return 'Css'
    elif ext=='html':
        return 'Rhtml'
    elif ext=='js':
        return 'JScript'
    elif ext=='sql':
        return 'Sql'
    elif ext=='py':
        return 'Python'
    elif ext=='xml':
        return 'Xml'
    elif ext=='rb':
        return 'Ruby'
    elif ext=='conf':
        return 'Apache'
    elif ext=='sh':
        return 'Bash'
        # that's all on dpaste folks
    else:
        return ''

def prepare(filename,file_ext,user,chunk):
    url = "http://dpaste.com"
    values = {
                'language':get_syntax(file_ext),
                'poster':user,
                'content':chunk,
                'title':filename,
                'hold':'1'
          }
    return url,values

