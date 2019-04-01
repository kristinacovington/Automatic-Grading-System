#!/usr/bin/env python

from flask import Flask, render_template, request
from werkzeug import secure_filename

import os
import subprocess

app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      #filename = secure_filename(f.filename)
      #f.save("/usr/bin/g++ uploads/" + f.filename)
      f.save("/usr/bin/uploads/" + f.filename)

      subprocess.call("rm -f ./a.out", shell=True)
      retcode = subprocess.call("/usr/bin/g++ /usr/bin/uploads/" + f.filename, s                                                                                        hell=True)
      error = ""
      score = ""
      title = ""
      orig = ""
      if retcode:
         error += "failed to compile " + f.filename + "\r\n"
         return s

      subprocess.call("rm -f ./output", shell=True)
      retcode = subprocess.call("./test.sh", shell=True)

      score += "Score: " + str(retcode) + " out of 2 correct.\r\n"

      title += "*************Original submission*************\r\n"
      with open('/usr/bin/uploads/' + f.filename,'r') as fs:
         orig += fs.read()

      return render_template('uploader.html', error = error, score = score, titl                                                                                        e = title, orig = orig)

if __name__ == '__main__':
   app.run(host="0.0.0.0")
