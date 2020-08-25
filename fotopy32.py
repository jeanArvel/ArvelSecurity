import dropbox

cliente = dropbox.client.DropboxClient('fqUmwCjiUNAAAAAAAAAAV56QlsM-Nw8iVOzBbRky4329ODcT0dYPrJUQG7Ywn4vo')
nombreArchivo = 'prueba.txt'

archivo = open(nombreArchivo,'rb')
respuesta = Cliente.put_file('/DropboxAPI/'+nombreArchivo,archivo)

print (respuesta)
