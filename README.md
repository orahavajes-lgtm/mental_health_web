# mental-health-predictor

# האתר עושה שימוש בשני מודלים מאומנים – Decision Tree ורשת ניורונים (Neural Network) – 
# על מנת לחזות האם האדם העונה על טופס השאלות זקוק לטיפול פסיכולוגי או שלא.
# המשתמש יכול לבחור דרך הממשק איזה מודל להפעיל לצורך החיזוי.
# יש להתקין את הקוד ב־VS Code או כל סביבת פיתוח אחרת התומכת ב־Python.

# הוראות שימוש באתר:

# שכפול המאגר
git clone https://github.com/orahavajes-lgtm/mental_health_web.git
cd mental_health_web

# התקנת ספריות נדרשות
pip install -r requirements.txt
pip install flask numpy scikit-learn tensorflow

# דרישות מערכת
# יש לוודא שמותקנת גרסת Python 3.11 במחשב

# הרצת השרת
python app.py

# פתיחת האתר בדפדפן

# כניסה לכתובת:
http://127.0.0.1:5000

# תיאור כללי:
# האתר מציג טופס שאלות למשתמש, כולל בחירת מודל (Decision Tree או Neural Network).
# לאחר שליחת הטופס, הנתונים נשלחים לשרת, עוברים עיבוד והמרה לערכים מספריים,
# ומוזנים למודל שנבחר לצורך חיזוי.
# התוצאה מוצגת למשתמש יחד עם ציון המודל שבו נעשה שימוש.

# האתר ייראה כך: <img width="721" height="434" alt="{EC837846-D85B-4255-98B8-5EE6C86BF40E}" src="https://github.com/user-attachments/assets/a77241a6-8a17-4cc5-a1a1-0fc46492a1a1" />
