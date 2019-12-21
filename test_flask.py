
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.json
    print content['mytext']
    return jsonify({"uuid":uuid})

if __name__ == '__main__':
    app.run(debug=True)

