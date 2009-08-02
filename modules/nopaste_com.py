## nopaste.com module
# Sun Aug  2 18:09:54 IST 2009            Abhishek Misha <ideamonk at gmail.com>

# Wanna __hack__ and add more support, look at source of http://nopaste.com/
# find this portion - 
# ... 
#   <option value="html">HTML</option>
#   <option value="pascal">Pascal / Delphi</option>
#   <option value="plain" selected>Plain</option>
#   <option value="rhtml">RHTML</option>
# ...
# know your file extension, find corresponding return value from the html

def get_syntax(ext):
    ''' nopaste.com supports very less number of syntax highlights :( '''
    if ext=='html':
        return 'html'
    elif ext=='p':
        return 'pascal'
    elif ext=='rhtml':
        return 'rhtml'
    elif ext=='rb':
        return 'ruby'
    elif ext=='xml':
        return 'xml'
    else:
        return 'plain'
    
def prepare(filename,file_ext,user,chunk):
    url = "http://nopaste.com/add"
    values= {
                'language':get_syntax(file_ext),
                'nick':user,
                'content':chunk,
                'description':filename,
                'hold':'1'
            }
    
    return url,values
