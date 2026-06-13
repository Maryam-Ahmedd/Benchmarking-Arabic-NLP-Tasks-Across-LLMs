import pandas as pd
import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip 

def main():
    # Setup Undetected Chromedriver
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)

    # Load Excel File
    input_file = 'input_paragraphs.xlsx'
    try:
        df = pd.read_excel(input_file)
        column_name = df.columns[0]
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    df = df.head(40)

    # Open ChatGPT
    driver.get("https://chatgpt.com")
    print("ACTION REQUIRED: Log in and solve any verification.")
    print("Once you see the prompt box, press Enter here...")
    input() 

    results = []

    prompt_prefix = """المهمة: اقرأ الفقرة المعطاة، ثم ولّد ثلاثة أسئلة باللغة العربية يمكن الإجابة عنها مباشرة من المعلومات الموجودة فيها فقط
الشروط:
اكتب 3 أسئلة فقط بدون اجابات.
كل الأسئلة باللغة العربية.
يجب أن تكون الإجابة على كل سؤال موجودة في الفقرة فقط بدون استخدام أي معلومات من خارج الفقرة.
تجنب أسئلة الرأي مثل: ما رأيك؟ هل تعتقد؟
حافظ على نفس مستوى اللغة في الفقرة قدر الإمكان؛ إذا كانت فصحى فاستخدم الفصحى، وإذا كانت باللهجة فاستخدم لهجة قريبة.
حاول استخدام نفس الفاظ الفقرة.
الفقرة: """

    for index, row in df.iterrows():
        paragraph = row[column_name]
        # Combine everything into one single string
        full_prompt = f"{prompt_prefix}\n{paragraph}"

        print(f"Processing row {index + 1}...")

        try:
            # Copy the entire prompt to clipboard
            pyperclip.copy(full_prompt)

            # Locate the text area
            text_area = driver.find_element(By.ID, "prompt-textarea")
            text_area.click()
            time.sleep(1)

            # Paste the text using CTRL+V (or CMD+V for Mac)
            # This ensures the prompt is sent as ONE block
            text_area.send_keys(Keys.CONTROL, 'v')
            
            time.sleep(1)
            # Press Enter once to send the pasted block
            text_area.send_keys(Keys.ENTER)

            # Wait for generation
            print("Waiting for response...")
            time.sleep(25) 

            # Capture latest response
            responses = driver.find_elements(By.CSS_SELECTOR, ".markdown.prose")
            if responses:
                last_response = responses[-1].text
                results.append(last_response)
                print("Captured.")
            else:
                results.append("Error: No response found")

        except Exception as e:
            print(f"Error at row {index + 1}: {e}")
            results.append("Automation Error")

        # Buffer between rows
        time.sleep(random.uniform(8, 12)) 

    # 4. Save results
    df['ChatGPT_Results'] = results
    df.to_excel('Task16_ChatGPT.xlsx', index=False)
    
    print("Done! Check Task16_ChatGPT.xlsx")
    driver.quit()

if __name__ == "__main__":
    main()