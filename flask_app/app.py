# Flask UI (Python)
from flask import Flask, render_template, request
from sqlalchemy import create_engine
import pandas as pd
app=Flask(__name__)
engine=create_engine(conn)

@app.route('/',methods=['GET','POST'])
def index():
    min_id=request.form.get('min_id',type=int)
    sql="SELECT * FROM etl_table"
    if min_id: sql += f" WHERE id >= {min_id}"
    df=pd.read_sql(sql,engine)
    return render_template('report.html', tables=[df.to_html()], min_id=min_id)

if __name__=='__main__':
    app.run(debug=True)
