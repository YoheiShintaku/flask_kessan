import flask
import sys
import traceback    
import pandas as pd
app = flask.Flask('any name')

@app.route("/")
def index():
    return flask.render_template('index.html')  # templateディレクトリからのパス

@app.route("/kabu/kessan")
def kabu_kessan_index():
    return flask.render_template('/kabu/kessan/index.html')

@app.route('/kabu/kessan/action', methods = ['POST', 'GET'])
def kabu_kessan_action():    
    try:
#        if flask.request.method != 'POST': 
#        dct = flask.request.form
        pathIn = './static/data/kabu/kessan/df.tsv'  # pythonでは「.」ないとだめ
        df = pd.read_csv(pathIn, sep='\t')
        df = df.head(2)
        df['img_url'] = '/static/image/image.png'  # htmlでは「.」があるとだめ
        return flask.render_template("/kabu/kessan/result.html", df=df)
    except:
        a, b, c = sys.exc_info()
        with open('kabu_kessan_action_error1.txt', mode='w') as f:
            f.write(str(a) + '\n')
            f.write(str(b))
        with open('kabu_kessan_action_error2.txt', mode='w') as f:
            f.write(traceback.format_exc())
