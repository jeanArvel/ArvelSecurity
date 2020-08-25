import dropbox

f = open ('prueba.txt')

dbx = dropbox.Dropbox('fqUmwCjiUNAAAAAAAAAAV56QlsM-Nw8iVOzBbRky4329ODcT0dYPrJUQG7Ywn4vo')
dbx.files_upload(f, '/prueba.txt')

f.close()
