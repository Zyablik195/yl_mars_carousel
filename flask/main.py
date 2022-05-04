from flask import Flask, render_template, request
import io
import PIL.Image as Image

app = Flask(__name__)
list1 = ["/static/images/mars1.png", "/static/images/mars2.png"]

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='')

@app.route('/galery', methods=['POST', 'GET'])
def log():
    global list1
    if request.method == 'GET':
        args = {}
        args['title'] = ''
        args['item1'] = list1[0]
        args['items'] = list1[1:]
        return render_template('login.html', **args)
    elif request.method == 'POST':
        f = request.files['file'].read()
        image = Image.open(io.BytesIO(f))
        savepath = f'static/images/mars{len(list1) + 1}.png'
        image.save(savepath)
        list1.append(savepath)
        return "Форма отправлена"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')