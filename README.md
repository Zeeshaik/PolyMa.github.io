# PolyMa.github.io
It is a prototype of Alexa or Google assistant. It is a Desktop Application coded in Python, created for official SBTET portal website, Where the application takes voice command and check with its constraints if match then open corresponding site of SBTET in browser. Technologies : Python(Backend), QtDesigner and PyQt5 (UI).

Note: One Small Error in Polyma.py File...
- In Line No 60: query = r.recognize_google(audio, language='en-in')
- Replace it with self.query = r.recognize_google(audio, language='en-in')
