
# ## Language - Python, Ruby or Nodejs preferred.
 
# Question1 : Write API: 
# Using Python Flask or ExpressJS, Write a REST API that reads the body and  returns JSON.
 
# # API Method POST
# # URL : /find_symbols_in_names
 
# # Input JSON Body of the API:
# {
#     "chemicals": ['Amazon', 'Microsoft', 'Google'],
#     "symbols": ['I', 'Am', 'cro', 'Na', 'le', 'abc']
# }
 
# # Output: display the chemical names with their symbol surrounded by square brackets:
# {
#     "result": "[Am]azon, Mi[cro]soft, Goog[le]"
# }

# Answer:
#   Language Used is: PYTHON
#   Library Used is: Python flask 
#   POSTMAN is used to showcase


from flask import Flask,request,jsonify
  
app = Flask(__name__)
  
@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'
@app.route('/getjson', methods = ['GET'])
def getJsonHandler():
    print (request.is_json)
    content = request.get_json()
    name=content
    name = {
    "chemicals": ['Amazon', 'Microsoft', 'Google'],
    "symbols": ['I', 'Am', 'cro', 'Na', 'le', 'abc']
           }
    s = name["symbols"]
    t=name["chemicals"]
    a=[]
    for i in s:
        for j in t:
            if(i in j):
                q=j.replace(i,"[" +i+"]")
                a.append(q)
        
    return jsonify(a)    

if __name__ == '__main__':
    app.debug = True
    app.run()
