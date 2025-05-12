# ML Integration (Python)
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sqlalchemy import create_engine
import joblib

# Load logs
en = create_engine(conn)
df = pd.read_sql_table('batch_logs', en)
X = df[['cpu','memory_free','duration_seconds']]
y = df['failed']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
model=RandomForestClassifier()
model.fit(X_train,y_train)
print(model.score(X_test,y_test))
joblib.dump(model,'failure_predictor.joblib')
