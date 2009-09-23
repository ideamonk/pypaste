## paste.ubuntu.com module
# Sun Aug  2 02:51:56 IST 2009            Abhishek Misha <ideamonk at gmail.com>

# If I missed your favourite file extension/syntact, you can simply view the
# source of http://paste.ubuntu.com an look for 
'''
<option value="text">Plain Text</option>
<option value="apacheconf">ApacheConf</option>
<option value="as">ActionScript</option>
<option value="bash">Bash</option>
'''
# add a line
# if (ext=='you extension in lowercase'):
#    return corresponding value from <option> tags in source of page

def get_syntax(ext):
    if ext=='c':
        return 'c'
    elif ext=='cpp':
        return 'cpp'
    elif ext=='sh':
        return 'bash'
    elif ext=='lisp':
        return 'common-lisp'
    elif ext=='charp':
        return 'csharp'
    elif ext=='css':
        return 'css'
    elif ext=='diff':
        return 'diff'
    elif ext=='html':
        return 'html'
    elif ext=='java':
        return 'java'
    elif ext=='js':
        return 'js'
    elif ext=='lua':
        return 'lua'
    elif ext=='llvm':
        return 'llvm'
    elif ext=='am':
        return 'make'
    elif ext=='in':
        return 'make'
    elif ext=='makefile':
        return 'make'
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
    else:
        return 'text'

def prepare(file_ext,user,chunk):
    url = "http://paste.pocoo.org/"
    values= {
                'language':get_syntax(file_ext),
                'nick':user,
                'code':chunk
            }
    
    return url,values
