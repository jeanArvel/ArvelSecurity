import dropbox

f = open ('newimage.png')

dbx = dropbox.Dropbox('fqUmwCjiUNAAAAAAAAAAV56QlsM-Nw8iVOzBbRky4329ODcT0dYPrJUQG7Ywn4vo')
dbx.files_upload(f,'/uploaded.png')

f.close()
