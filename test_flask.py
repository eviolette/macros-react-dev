
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api/add_message', methods=['GET', 'POST'])
def add_message():
    content = request.json
    print(content)
    return(content)

if __name__ == '__main__':
    app.run(debug=True)

