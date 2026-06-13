iimport pandas as pd
import google.generativeai as genai
import time
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-3-flash-preview')

def generate_questions(paragraph):
    # The specific prompt defined in your requirements
    prompt = f"""المهمة: اقرأ الفقرة المعطاة، ثم ولّد ثلاثة أسئلة عربية لكل فقرة يمكن الإجابة عنها مباشرة من المعلومات الموجودة فيها فقط
الشروط:
اكتب 3 أسئلة فقط بدون اجابات.
كل الأسئلة باللغة العربية.
يجب أن تكون الإجابة على كل سؤال موجودة في الفقرة فقط.
لا تستخدم أي معلومات من خارج الفقرة.
تجنب أسئلة الرأي مثل: ما رأيك؟ هل تعتقد؟
حافظ على نفس مستوى اللغة في الفقرة قدر الإمكان؛ إذا كانت فصحى فاستخدم الفصحى، وإذا كانت باللهجة فاستخدم لهجة قريبة.
حاول استخدام نفس الفاظ الفقرة.
الفقرة:
{paragraph}"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error processing paragraph: {e}")
        return "Error"
    
# Load the Excel sheet
input_file = 'input_paragraphs.xlsx'
df = pd.read_excel(input_file)
# process first 20 rows
df = df.head(20)
# Identify the column name
column_name = df.columns[0]

print(f"Starting Question Generation for {len(df)} paragraphs...")
results = []
for index, row in df.iterrows():
    paragraph_text = row[column_name]
    print(f"Processing Row {index + 1}...")
    
    questions = generate_questions(paragraph_text)
    results.append(questions)
    # Adding a small delay to respect rate limits
    time.sleep(12)

# Save the output
df['Gemini'] = results
output_file = 'Task16_Gemini.xlsx'
df.to_excel(output_file, index=False)
print(f"Finished! Results saved to {output_file}")
