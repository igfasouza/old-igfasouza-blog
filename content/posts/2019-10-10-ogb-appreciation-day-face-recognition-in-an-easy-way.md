---
layout: post
title: OGB Appreciation Day – Face Recognition in an easy way
date: '2019-10-10'
slug: ogb-appreciation-day-face-recognition-in-an-easy-way
tags:
- Python
description: 'How’s it going horse? It’s Oracle Groundbreaker’s Appreciation Day!
  Today it’s #ThanksOGB day and I decided to join the idea with a post about Face
  Recognition in an easy way using Oracle OCI Marketpl'
image: wp/2019/10/1-fpDngO6lM5pDeIPOOezK1g.jpeg
---

![](/old-igfasouza-blog/images/wp/2019/10/1-fpDngO6lM5pDeIPOOezK1g-1024x682.jpeg)

**How’s it going horse?**

## It’s Oracle Groundbreaker’s Appreciation Day!

Today it’s #ThanksOGB day and I decided to join the idea with a post about Face Recognition in an easy way using Oracle OCI Marketplace Nvidia image.

**What is OGB Appreciation day?**  
[OGB Appreciation day](https://oracle-base.com/blog/2019/09/30/ogb-appreciation-day-2019-thanksogb/)

Don’t forget to search for tweets with #ThanksOGB.

Oracle blog post my [article](https://blogs.oracle.com/datascience/how-to-build-a-face-recognition-application-with-4-lines-of-code) about Face Recognition in 4 lines of code.

Today I want to show how you can create an Oracle OCI instance using the Marketplace and configure the environment to run this example easily with the Nvidia image.

[Oracle OCI Marketplace](https://cloudmarketplace.oracle.com/marketplace/oci)

You can follow this [link](https://blogs.oracle.com/solaris/oracle-solaris-now-available-in-the-oci-marketplace) on how to create an image using the marketplace. Just change to use Nvidia image!

Once you have the instance running just ssh the image and run:

```bash
sudo apt install python3-pip
sudo apt-get install python3-setuptools
wget http://dlib.net/files/dlib-19.17.tar.bz2
tar jxvf dlib-19.17.tar.bz2
cd dlib-19.17
sudo python3 setup.py install
sudo pip3 install face_recognition
```

Now you are ready to play with Face Recognition.

![](/old-igfasouza-blog/images/wp/2019/10/face_recognition01.jpg)

You can use my Python code to Streaming your Raspberry Pi camera feeds.

```html
import io
import picamera
import logging
import socketserver
from threading import Condition
from http import server
PAGE="""\
<html>
<head>
<title>Raspberry Pi - Surveillance Camera</title>
</head>
<body>
<center><h1>Raspberry Pi - Surveillance Camera</h1></center>
<center><img src="stream.mjpg" width="640" height="480"></center>
</body>
</html>
"""
class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()
    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)
class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()
class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True
with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    output = StreamingOutput()
    #Uncomment the next line to change your Pi's Camera rotation (in degrees)
    #camera.rotation = 90
    camera.start_recording(output, format='mjpeg')
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()
```

Just change the code for instead of 0 use the streaming url, in the example here: http://ipaddress:8000/stream

```
video_capture = cv2.VideoCapture(0)
```

Happy face recognition.  
![](/old-igfasouza-blog/images/wp/2019/10/giphy.gif)

## Link

[pyimagesearch](https://www.pyimagesearch.com/start-here)
