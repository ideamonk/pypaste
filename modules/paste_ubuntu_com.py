## paste.pocoo.org module
# Sun Aug  2 02:51:56 IST 2009            Abhishek Misha <ideamonk at gmail.com>

# Wanna __hack__ and add more support, look at source of http://paste.pocoo.org
# find this portion - 
# ... 
#      <option value="apache">Apache Config (.htaccess)</option>
#      <option value="bash">Bash</option>
#      <option value="bat">Batch (.bat)</option>
#      <option value="boo">Boo</option>
#      <option value="c">C</option>
# ...
# know your extension, find corresponding return value from the html

def get_syntax(ext):
    if ext=='c':
        return 'c'
    elif ext=='cpp':
        return 'cpp'
    elif ext=='sh':
        return 'bash'
    elif ext=='lisp':
        return 'common-lisp'
    elif ext=='csharp':
        return 'csharp'
    elif ext=='css':
        return 'css'
    elif ext=='html':
        return 'html'
    elif ext=='java':
        return 'java'
    elif ext=='jsp':
        return 'jsp'
    elif ext=='js':
        return 'js'
    elif ext=='lua':
        return 'lua'
    elif ext=='llvm':
        return 'llvm'
    elif ext=='sql':
        return 'mysql'
    elif ext=='pl':
        return 'perl'
    elif ext=='php':
        return 'php'
    elif ext=='rb':
        return 'ruby'
    elif ext=='py':
        return 'python'
    elif ext=='tex':
        return 'tex'
    elif ext=='vim':
        return 'vim'
    elif ext=='xml':
        return 'xml'
    elif ext=='yaml':
        return 'yaml'
    else:
        return 'text'

def prepare(file_ext,user,chunk):
    url = "http://paste.ubuntu.com/"
    values = {'syntax':get_syntax(file_ext),'poster':user,'content':chunk}
    
    return url,values

