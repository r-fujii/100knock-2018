#!/usr/bin/env python


from flask import Flask, render_template, request
from pymongo import MongoClient
import pandas as pd


app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.artists_db
col = db.artists_col


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        query = {key:val for key, val in request.form.items() if key != 'andor' if val}
        
        if len(query) > 0:
            andor = request.form['andor']
            result = col.find({ '${}'.format(andor) : [{k: v} for k, v in query.items()]})
            n_entry = result.count()
            if n_entry:
                # エントリが存在した場合の処理 (一度メモリに持ってしまう...)
                entries = []
                
                # 整形
                for res in result:
                    name = res.get('name')
                    aliases = ', '.join(x['name'] for x in res.get('aliases', [{'name':'NULL'}]))
                    area = res.get('area', 'NULL')
                    tags = ', '.join(x['value'] for x in res.get('tags', [{'value':'NULL'}]))
                    rating = res.get('rating', {'value':0})['value']
                    entries.append({'name':name, 'aliases':aliases, 'area':area, 'tags':tags, 'rating':rating})
                
                entries = sorted(entries, key=lambda x: x['rating'], reverse=True)[:50]
                if n_entry >= 50:
                    msg = '{}件のエントリがヒットしました。レーティングの高い50件を表示しています。'.format(n_entry)
                else:
                    msg = '{}件のエントリがヒットしました。検索結果を表示しています。'.format(n_entry)

                df = pd.DataFrame(entries, columns=['name', 'aliases', 'area', 'tags', 'rating'])
                df.index += 1
                
                result = df.to_html(classes=["table", "table-bordered", "table-hover"], escape=False)
                
                return render_template('table.html', n_entry=n_entry, msg=msg, result=result)
            
            else:
                msg = '該当するエントリはありませんでした。'
                return render_template('result.html', msg=msg)
                
        else:
            msg = '検索条件を指定してください。'
            return render_template('result.html', msg=msg)
        

if __name__ == '__main__':
    app.run(debug=True)
