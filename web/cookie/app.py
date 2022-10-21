from server import Server

server = Server()


@server.get('/')
async def root(request):
    admin = request.cookies.get('admin', '')

    headers = {}
    if admin == '':
        headers['set-cookie'] = 'admin=false'

    if admin == 'true':
        return (200, '''
            <title>ccs ctf</title>
            <link rel="stylesheet" href="/style.css" />
            <div class="container">
                <h1>welcome to ccs club</h1>
                %s
            </div>
        ''' % "ccsCTF{w3lc0me__c55_c1ub_4351sadf23}", headers)
    else:
        return (200, '''
            <title>ccs ctf</title>
            <link rel="stylesheet" href="/style.css" />
            <div class="container">
                <h1>Secure Page</h1>
                 admin эрхийг олж авсаны дараа клубт элсэж орох нь дээ :(
            </div>
        ''', headers)


@server.get('/style.css', c_type='text/css')
async def style(request):
    del request
    return (200, '''
        * {
            font-family: 'Helvetica Neue', sans-serif;
            box-sizing: border-box;
        }

        html, body { margin: 0; }

        .container {
            padding: 2rem;
            width: 90%;
            max-width: 900px;
            margin: auto;
        }

        input:not([type="submit"]) {
            width: 100%;
            padding: 8px;
            margin: 8px 0;
        }
    ''')


server.run('0.0.0.0', 3000)
