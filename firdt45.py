from flask import Flask, render_template, request, jsonify
import mysql.connector as con
import pandas as pd
import json

app = Flask(__name__)

# '/' means it is home route
@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template("index.html")

@app.route('/adding',methods=['GET','POST'])
def start():
    if request.method == 'GET':
        obj= con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur=obj.cursor()
        cur.execute("use practice2")
        query="select * from genes"
        result=pd.read_sql(query,obj)
        lis1=[]
        lis2=[]
        lis3=[]
        lis4=[]
        lis5=[]
        lis6=[]
        lis7=[]
        lis8=[]
        for i in result['DISEASE']:
            lis1.append(i)
        for i in result['TYPE_OF_INHERITANCE']:
            lis2.append(i)
        for i in result['GENE_RESPONSIBLE']:
            lis3.append(i)
        for i in result['GENE_LOCATION']:
            lis4.append(i)
        for i in result['SYMPTOMS']:
            lis5.append(i)
        for i in result['PATHWAY']:
            lis6.append(i)
        for i in result['Pathway_links']:
            lis7.append(i)
        for i in result['Histopathology_links']:
            lis8.append(i)
        result1=[]
        for i in range(len(result)):
            dict1={}
            dict1['DISEASE']=lis1[i]
            dict1['TYPE_OF_INHERITANCE']=lis2[i]
            dict1['GENE_RESPONSIBLE']=lis3[i]
            dict1['GENE_LOCATION']=lis4[i]
            dict1['SYMPTOMS']=lis5[i]
            dict1['PATHWAY']=lis6[i]
            dict1['Pathway_links']=lis7[i]
            dict1['Histopathology_links']=lis8[i]
            result1.append(dict1)
        return jsonify(result1)


@app.route('/senddata',methods=["POST"])
def recieve_data():
    name_ = request.form.get("User_Name")
    email_ = request.form.get("User_Email")
    Reason_for_Download = request.form.get("Reason_For_Download" )
    Organization_Belonging_To= request.form.get("Organization_Belonging_To")
    obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
    cur = obj.cursor()
    cur.execute("use practice2")
    query = "INSERT INTO info (name,email,Reason_for_Download,organization_Belonging_To) VALUES (%s, %s, %s, %s)"
    values = (name_,email_,Reason_for_Download,Organization_Belonging_To)
    cur.execute(query,values)
    obj.commit()
    return 'Data Recieved'
@app.route('/senddata1',methods=["GET"])
def recieve_data_s2():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from bioinfotools"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["TOOL_NAME"]:
            list1.append(i)
        for i in result["DESCRIPTION"]:
            list2.append(i)
        for i in result["LOCATION"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["TOOL_NAME"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)


@app.route('/senddata2',methods=["GET"])
def recieve_data_s4():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from drug"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["Database_Name"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Database_link"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["Database_Name"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)


@app.route('/senddata3',methods=["GET"])
def recieve_data_s3():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from tools"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["Tool_name"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["TOOL_NAME"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)


@app.route('/senddata4', methods=["GET"])
def recieve_data_s5():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from biopro"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["Tool_name"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["TOOL_NAME"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)


@app.route('/senddata5', methods=["GET"])
def recieve_data_s6():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from biotech"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["Technique"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["Technique"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)


@app.route('/senddata6', methods=["GET"])
def recieve_data_s7():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from  bioserv"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["NAME"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["NAME"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)


@app.route('/senddata7', methods=["GET"])
def recieve_data_s8():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from  prottools"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["NAME"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["NAME"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)


@app.route('/senddata8', methods=["GET"])
def recieve_data_s9():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from  transtools"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["NAME"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["NAME"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)

@app.route('/senddata9', methods=["GET"])
def recieve_data_s10():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from  protserv"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["NAME"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["NAME"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)


@app.route('/senddata10', methods=["GET"])
def recieve_data_s11():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from  omimtools"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["NAME"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["NAME"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)


@app.route('/senddata11', methods=["GET"])
def recieve_data_s12():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from  bioinfoserv3"
        result = pd.read_sql(query, obj)
        list1=[]
        list2 = []
        list3=[]
        for i in result["NAME"]:
            list1.append(i)
        for i in result["DESCRIPTION"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["NAME"]=list1[i]
            dict1["DESCRIPTION"] = list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)


@app.route('/senddata12', methods=["GET"])
def recieve_data_s13():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from  transserv"
        result = pd.read_sql(query, obj)
        list1=[]
        list2= []
        list3=[]
        for i in result["NAME"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["NAME"]=list1[i]
            dict1["DESCRIPTION"] = list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)


@app.route('/senddata13', methods=["GET"])
def recieve_data_s14():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from  geneticserv"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["NAME"]:
            list1.append(i)
        for i in result["DESCRIPTION"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["NAME"]=list1[i]
            dict1["DESCRIPTION"] = list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)

@app.route('/sentdata14',methods=['GET','POST'])
def start1():
    if request.method == 'GET':
        obj= con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur=obj.cursor()
        cur.execute("use practice2")
        query="select * from  vege"
        result=pd.read_sql(query,obj)
        lis1=[]
        lis2=[]
        lis3=[]
        lis4=[]
        lis5=[]
        lis6=[]
        lis7=[]
        lis8=[]
        for i in result['NAME']:
            lis1.append(i)
        for i in result['Scientific_Name']:
            lis2.append(i)
        for i in result['Leaf']:
            lis3.append(i)
        for i in result['Stem']:
            lis4.append(i)
        for i in result['Fruit']:
            lis5.append(i)
        for i in result['Root']:
            lis6.append(i)
        for i in result['Season']:
            lis7.append(i)
        for i in result['Region']:
            lis8.append(i)
        result1=[]
        for i in range(len(result)):
            dict1={}
            dict1['NAME']=lis1[i]
            dict1['Scientific_Name']=lis2[i]
            dict1['Leaf']=lis3[i]
            dict1['Stem']=lis4[i]
            dict1['Fruit']=lis5[i]
            dict1['Root']=lis6[i]
            dict1['Season']=lis7[i]
            dict1['Region']=lis8[i]
            result1.append(dict1)
        return jsonify(result1)


@app.route('/senddata15',methods=["GET"])
def recieve_data_s16():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from bioprocesstools"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["NAME"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["TOOL_NAME"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)


@app.route('/senddata16',methods=["GET"])
def recieve_data_s17():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from Fermentation"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["NAME"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["TOOL_NAME"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)




@app.route('/senddata17',methods=["GET"])
def recieve_data_s18():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from soil"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["NAME"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["NAME"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)


@app.route('/senddata18',methods=["GET"])
def recieve_data_s19():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from dataw"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["NAME"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["Resource"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)

@app.route('/senddata19',methods=["GET"])
def recieve_data_s20():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from appu"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        list4=[]
        for i in result["NAME"]:
            list1.append(i)
        for i in result["application"]:
            list4.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["disease"]=list1[i]
            dict1["applications"] = list4[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)

@app.route('/senddata20',methods=["GET"])
def recieve_data_s21():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from compu"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        list4=[]
        list5=[]
        for i in result["METHOD"]:
            list1.append(i)
        for i in result["INPUT_DATA_TYPE"]:
            list4.append(i)
        for i in result["CELL_AND_TISSUES_TYPE"]:
            list2.append(i)
        for i in result["OUTPUT"]:
            list3.append(i)
        for i in result["RESOURCES"]:
            list5.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["METHOD"]=list1[i]
            dict1["INPUT_DATA_TYPE"] = list4[i]
            dict1["CELL_AND_TISSUES_TYPE"]=list2[i]
            dict1["OUTPUT"] = list3[i]
            dict1["RESOURCES"] = list5[i]
            result1.append(dict1)
        return jsonify(result1)

@app.route('/senddata21', methods=["GET"])
def recieve_data_s22():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from  sequence"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["NAME"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["NAME"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)

@app.route('/senddata22', methods=["GET"])
def recieve_data_s23():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from  biodata1"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["NAME"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["NAME"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)

@app.route('/senddata23', methods=["GET"])
def recieve_data_s24():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from  crisper"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["NAME"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["NAME"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)

@app.route('/senddata24', methods=["GET"])
def recieve_data_s25():
    if request.method == 'GET':
        obj = con.connect(host='localhost', user='root', password='rajesh3341@38')
        cur = obj.cursor()
        cur.execute("use practice2")
        query = "select * from  metagenomics"
        result = pd.read_sql(query, obj)
        list1=[]
        list2=[]
        list3=[]
        for i in result["NAME"]:
            list1.append(i)
        for i in result["Description"]:
            list2.append(i)
        for i in result["Location"]:
            list3.append(i)
        result1 = []
        for i in range(len(result)):
            dict1={}
            dict1["NAME"]=list1[i]
            dict1["DESCRIPTION"]=list2[i]
            dict1["LOCATION"]=list3[i]
            result1.append(dict1)
        return jsonify(result1)



if __name__ == '__main__':
    app.run(debug=True)