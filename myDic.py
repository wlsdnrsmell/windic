# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json
import tkinter as tk
# TODO: replace with your own app_id and app_key

#print("json \n" + json.dumps(r.json()))
def main():    
    app_id = '2eed45e2'
    app_key = 'abad96030e92a2115c7423310eb854d7'

    language = 'en'
    #frame
    root = tk.Tk()
    root.title('단어찾기')
    #root.geometry('500x400+10+10')
    word_id=root.clipboard_get()
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()+'/definitions'

    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
   
    no_row =0
    dict = r.json()
    lbl = tk.Label(root, text =dict['results'][0]['id'])
    lbl.grid(row=no_row,column=0)
    for res in dict['results'][0]['lexicalEntries']:
        word_lex=res['lexicalCategory']
        #print(word_lex)
        #print(isinstance(word_lex,str))
        txt = tk.Label(root, text=word_lex)
        txt.grid(row=no_row,column=1)
        no_row=no_row+1
        #print(res['lexicalCategory'])
        for sub in res['entries'][0]['senses']:
            word_def =str(sub['definitions'])
            #print(word_def)
            #print(isinstance(word_def,str))
            txt1 = tk.Message(root, text=word_def,)
            txt1.grid(row=no_row,column=2)
            no_row=no_row+1
            #print(sub['definitions'])
    #print("code {}\n".format(r.status_code))
    #print("text \n" + r.text)
    root.mainloop()
if __name__=='__main__':
    main()
    
    

