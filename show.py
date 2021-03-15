import cgi, os

form = cgi.FieldStorage()
name = str(form.getvalue("name"))
email = str(form.getvalue("email"))
tel = str(form.getvalue("tel"))
msg = str(form.getvalue("msg"))
fle = form['filename']

fn = os.path.basename(fle.filename)
open("/Users/bhagya/Desktop/my_blog/blog/messages"+fn, "wb").write(fle.file.read())
