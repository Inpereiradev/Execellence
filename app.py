from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



#https://youtu.be/Xz9hlTHj4Bw?si=S3xvL-wAc-bEuylA
#https://youtu.be/OrUcM94ltRE?si=B6shefX7KghazjjA
#https://youtu.be/YADhI8jlYsk?si=XXBdtIR4ZpXyuLor