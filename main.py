from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def find_word():
    if request.method=="POST":
        file = request.files['file']
        if file:
            filename=file.filename
            # C:\Users\Danil\PycharmProjects\flask\upload\1.txt
            file_path=os.path.join(app.root_path,'upload',filename)
            file.save(file_path)

            with open(file_path,'r') as f:
                data = f.read().replace('\n',' ')
            words=data.split(' ')

            word_count ={}
            for word in words:
                if word in word_count:
                    word_count[word]+=1
                else:
                    word_count[word] = 1
            max_word=max(word_count,key=word_count.get)

            result = (max_word,word_count[max_word])
            print(result)
            return render_template('index.html',result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()