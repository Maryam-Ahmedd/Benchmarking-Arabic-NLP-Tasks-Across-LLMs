from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

import time
import pyperclip


# =====================================
# Paragraphs
# =====================================

paragraphs = [
    """أغلب الناس بتبقى فاكرة إن النية في بداية العمل الخيري هي المحرك، والحقيقة إنها مش كده خالص، بالعكس البداية بتكون محملة بالأدرينالين وحماس البداية وأحيانا مهرب من ضغوط الحياة والشغل والأزمات الشخصية. لكن الي بيحصل بعد كده هو الاختبار الحقيقي والي بيتجدد مع كل باب بيتقفل في وشنا بس هنكمل خبط ولا لا.""",

    """في حياتي قابلت مئات ويمكن آلاف ناس حابة تساعد الناس التانية بالمجهود قبل الفلوس، والقاعدة الأساسية الي تعلمتها، مستحيل تكون نيتك ورغبتك حقيقة وربنا ميفتحش باب لده. ولو الباب اتقفل هيتفتح غيره، ولو متوفقتش راجع نيتك وافتكر دايما قوله تعالى: ﴿هَا أَنتُمْ هَٰؤُلَاءِ تُدْعَوْنَ لِتُنفِقُوا فِي سَبِيلِ اللَّهِ فَمِنكُم مَّن يَبْخَلُ﴾.""",

    """من أهم الصفات التي يجب الالتفات إليها عند الزواج مدى بساطة الشخص الذي سيتم الارتباط به، ومواقف فترة الخطوبة تكشف شيئًا من ذلك. من أعظم النعم في هذه الحياة أن يرزقك الله شخصًا سهلًا في حياتك، سهل في كل شيء، سهل تحكي معاه، سهل تناقشه، سهل ترضيه، وسهل يفهمك.""",

    """منذ تأسيس المقاومة، وهناك محاولات مستمرة لنزع سلاحها. لكن الواقع بيقول إنه طالما في عدو على حدودنا بهالقدر من الإجرام وعدم الالتزام بأي قانون أو إنسانية، ما في مجال للثقة فيه. السلاح يجب أن يبقى موجهاً نحوه مهما علت الأصوات المعارضة.""",

    """لاحظت شي وما اعرف اذا عليه دراسات او لا، ان الشخص كل ما زاد تمسكه بدينه صار أقوى نفسياً. تفسيري لهذا الشي يقول إن الشخص المتدين لما تمر عليه ضائقة يتذكر ربه وتعاليم دينه التي تنهى عن أذية النفس والانتحار وأن فيه آخرة والكل بيتحاسب.""",

    """مش ملاحظين اخر فترة عن ظاهرة فتكت بنا كشباب بالاردن وهي سهولة الطلاق؟ الشب المقبل على الزواج مدخر المهر وبالنهاية بخطب وبكتب كتابه وبعد باكم شهر بتطلب البنت الطلاق وتستحق قانونا نصف الصداق كونها مطلقة قبل الدخول.""",

    """كل ماشفت عائلة يرمون قطتهم تجيني غصة، يكبرون بدون القدرة على التعامل مع الحياة خارج البيت، بدون مايمرنون غريزة الصيد، ثم يرمونهم بالشارع لحياة بائسة لاسبوع اسبوعين لين يموتون مدعوسين او من الجوع والعطش.""",

    """قبل النقاب كنت اتحجب والبس عبايات ملونه واحط فل ميكب والحجاب على حسب شعري اذا مسويته اطلع شوي منه واذا لا اتحجب كامل وبرضو ميكب. الغريب ان النظرات والمضايقات زادت كثير بعد ما تنقبت.""",

    """المقاطعة بالنسبة الي صارت نمط حياة ما بيختلف علي شي والحمدلله البدائل الوطنية موجودة. يعني المقاطعه بتدعم الاقتصاد المحلي وبتعطي فرص للشركات الاردنية ترفع كفاءتها وجودتها، يعني مش بس مبدأ وإنسانية بل كمان وطنية.""",

    """بس اتفرج عالدول اللي برا، زي الصين مثلا، بتلاقي النسبة الكبرى من الشعب بتهتم بالدراسة وتركيزها الاكبر كيف تكون متميزة بمجالها وكيف تضيف قيمة للمجتمع. بس لما اتفرج عدولنا وخاصة احنا الاردن، ياخي هالاشي يكاد يكون نسبته 1% او اقل.""",

    """أول كتاب اشتريته في التربية كان "في بيتنا طفل بريء"، وبصراحة الكتاب ده أفدني جدا وفرق معايا في تربية بناتي. الكتاب سهل ويسير جدًا وحجمه صغير ومختلف عن كتب التربية الكبيرة المفصلة.""",

    """التعفن الدماغي بقى حاجة بنشوفها كل يوم من كتر القعدة على السوشيال ميديا والمحتوى السريع اللي ملوش أي فايدة. الواحد يفضل يقلب بالساعات في فيديوهات قصيرة وتفاهات لحد ما تركيزه يضعف ومبقاش قادر يقعد خمس دقايق يقرأ أو يفكر بهدوء.""",

    """السوشيال ميديا ليها فوايد كتير زي انها خلت التواصل بين الناس أسهل بكتير وأي حد يقدر يعرف أخبار الدنيا وهو قاعد في بيته، والسوشيال ميديا كمان بقت مصدر كبير للترفيه والتعلم ومتابعة الحاجات اللي الناس بتحبها. بس في نفس الوقت في ناس بتقضي وقت طويل عليها لدرجة إنها بتأثر على مذاكرتهم وشغلهم ونومهم."""
]

# =====================================
# Prompt
# =====================================

base_prompt = """
المهمة:
اقرأ الفقرة المعطاة، ثم ولّد ثلاثة أسئلة عربية لكل فقرة يمكن الإجابة عنها مباشرة من المعلومات الموجودة فيها فقط.

الشروط:
- اكتب 3 أسئلة فقط بدون إجابات.
- كل الأسئلة باللغة العربية.
- يجب أن تكون الإجابة على كل سؤال موجودة في الفقرة فقط.
- لا تستخدم أي معلومات من خارج الفقرة.
- تجنب أسئلة الرأي مثل: ما رأيك؟ هل تعتقد؟
- حافظ على نفس مستوى اللغة في الفقرة قدر الإمكان.
- حاول استخدام نفس ألفاظ الفقرة.

الفقرة:
"""


# =====================================
# Chrome connection
# =====================================

options = Options()

# Chrome must be opened first using:
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenium_chrome"

options.debugger_address = "127.0.0.1:9222"

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 60)


# =====================================
# Open JaisChat
# =====================================

driver.get("https://www.jaischat.ai/c/476d81bf-4a8f-4a2e-807b-678c87c1e5cb")

print("JaisChat opened.")
time.sleep(10)


# =====================================
# Helper functions
# =====================================

def get_assistant_messages():
    selectors = [
        "div.markdown",
        "[class*='markdown']",
        "[class*='prose']",
        "[class*='message']",
    ]

    messages = []

    for selector in selectors:
        elements = driver.find_elements(By.CSS_SELECTOR, selector)

        for element in elements:
            text = element.text.strip()
            if len(text) > 20:
                messages.append(text)

        if messages:
            return messages

    return messages


def send_prompt(prompt):
    for attempt in range(3):
        try:
            print(f"  Attempt {attempt + 1}...")

            box = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
            time.sleep(1)
            box.click()

            # Clear old text
            box.send_keys(Keys.CONTROL, "a")
            box.send_keys(Keys.DELETE)
            time.sleep(0.5)

            # ── Inject text via JS (works with React-controlled textareas) ──
            driver.execute_script("""
                var nativeInputValueSetter = Object.getOwnPropertyDescriptor(
                    window.HTMLTextAreaElement.prototype, 'value').set;
                nativeInputValueSetter.call(arguments[0], arguments[1]);
                arguments[0].dispatchEvent(new Event('input',  { bubbles: true }));
                arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
            """, box, prompt)

            time.sleep(2)

            # Verify the value was accepted
            current_value = driver.execute_script("return arguments[0].value;", box)
            print(f"  DEBUG — pasted length: {len(current_value)}")

            if len(current_value.strip()) < 10:
                print("  Text injection failed. Retrying...")
                continue

            print("  Prompt injected successfully.")

            # Click the last visible enabled button (send button)
            buttons = driver.find_elements(By.TAG_NAME, "button")
            for btn in reversed(buttons):
                try:
                    if btn.is_displayed() and btn.is_enabled():
                        btn.click()
                        print("  Send button clicked.")
                        return True
                except Exception:
                    pass

            # Fallback: press Enter
            box.send_keys(Keys.RETURN)
            print("  Sent via Enter key (fallback).")
            return True

        except Exception as e:
            print(f"  Send error: {e}")
            time.sleep(2)

    return False


def wait_for_new_response(old_count, timeout=90):
    start_time = time.time()

    while time.time() - start_time < timeout:
        messages = get_assistant_messages()
        if len(messages) > old_count:
            return messages[-1]
        time.sleep(3)

    messages = get_assistant_messages()
    if messages:
        return messages[-1]

    return ""


# =====================================
# Log file
# =====================================

log_filename = r"D:\Final year\neural_assighment_3\prob_5\jias\jias_classic_log.txt"

with open(log_filename, "w", encoding="utf-8") as log_file:

    for i, paragraph in enumerate(paragraphs, 1):

        print(f"\nSending paragraph {i}...")

        prompt = f"{base_prompt}\n{paragraph}"

        old_messages = get_assistant_messages()
        old_count = len(old_messages)

        success = send_prompt(prompt)

        if not success:
            print(f"Failed to send paragraph {i}.")
            log_file.write(f"\n\n========== Paragraph {i} ==========\n\n")
            log_file.write("FAILED TO SEND\n")
            log_file.flush()
            continue

        print(f"Paragraph {i} sent. Waiting for response...")

        response = wait_for_new_response(old_count, timeout=90)

        log_file.write(f"\n\n========== Paragraph {i} ==========\n\n")

        if response:
            log_file.write(response)
            print(f"Response for paragraph {i} saved.")
        else:
            log_file.write("NO RESPONSE FOUND")
            print(f"No response found for paragraph {i}.")

        log_file.write("\n")
        log_file.flush()

        # Small delay between paragraphs
        time.sleep(5)


print("\nScript finished.")
print(f"Log saved at: {log_filename}")