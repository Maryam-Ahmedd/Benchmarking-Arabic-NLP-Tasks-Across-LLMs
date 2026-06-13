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
    """احتلت القضية الفلسطينية - قضية العرب الأولي منذ عام ١٩٤٨ الإهتمام الأكبر لدى جميع الزعماء المصريين، خاصة بعد الجلاء البريطاني عن مصر، إلا أن كل رئيس كان يتعامل معها بطريقة مختلفة، ولكن الجميع استندوا على مبادئ واحدة وهى، الوطنية، القومية والعروبة، حيث كان جمال عبد الناصر من أكثر الزعماء اهتماماً بها، فاعتبرها جزءاً من الأمن المصري، وليست مجرد قضية فلسطينية داخلية.""",

    """السكري داء مزمن يحدث عندما يعجز البنكرياس عن إنتاج الإنسولين بكمية كافية، أو عندما يعجز الجسم عن الاستخدام الفعّال للإنسولين الذي ينتجه. والإنسولين هو هرمون يضبط مستوى الغلوكوز في الدم. ويُعد فرط السكر في الدم، الذي يعرف أيضاً بارتفاع مستوى الغلوكوز في الدم، من النتائج الشائعة الدالة على وجود خلل في ضبط مستوى السكر في الدم، ويؤدي مع مرور الوقت إلى الإضرار الخطير بالعديد من أجهزة الجسم، ولاسيما الأعصاب والأوعية الدموية.""",

    """الطّاقة المتجددة هي الطّاقة المُستَمّدة من الموارد الطبيعية التي لا تنفذ وتتجدد باستمرار، مثل الرياح والمياه والشمس المتوفرة في معظم دول العالم، كما يمكن إنتاجها من حركة الأمواج والمد والجزر أو من طاقة حرارية أرضية وابتكارات أخرى. وتختلف الطاقة المتجددة أساسا عن الوقود الأحفوري من بترول وفحم وغاز الطبيعي، فلا يصدر عن الطّاقة المتجددة عادةً مخلّفات الوقود الأحفوري الضارّة للبيئة مثل تلك المؤدية لزيادة الاحتباس الحراري كثنائي أكسيد الكربون.""",

    """التصيَّد الاحتيالي هو عملية يقوم من خلالها المجرمون الإلكترونيون باستهداف الضحايا عبر إرسال رسائل بريد إلكتروني تبدو وكأنها مرسَلة من شركة شرعية للحصول على معلومات حساسة. غالبًا ما يتم استخدام هجمات التصيَّد الاحتيالي لخداع الأشخاص والحصول منهم على بيانات بطاقات الائتمان ومعلومات شخصية أخرى.""",

    """السياحة هي السفر بهدف الترفيه أو التطبيب أو الاكتشاف، وتشمل السياحة توفير الخدمات المتعلقة بالسفر. والسائح هو الشخص الذي يقوم بالانتقال لغرض السياحة لمسافة ثمانين كيلومترا على الأقل من منزله. وذلك حسب تعريف منظمة السياحة العالمية التابعة لهيئة الأمم المتحدة.""",

    """تعتمد أنظمة الذكاء الاصطناعي على مجموعات البيانات التي قد تكون عرضة لتسمم البيانات أو التلاعب بالبيانات أو تحيز البيانات أو الهجمات الإلكترونية التي يمكن أن تؤدي إلى اختراق أمن البيانات. يمكن للمؤسسات التخفيف من هذه المخاطر من خلال حماية سلامة البيانات وتنفيذ الأمان والتوافر طوال دورة حياة الذكاء الاصطناعي بأكملها، من التطوير إلى التدريب والنشر وما بعد النشر.""",

    """يعتبر التعليم الإلكتروني من الطرق والوسائل التي تدعم العملية التعليمية وتحول التعليم إلى طور الإبداع وتنمية المهارات والتفاعل من طور التلقين، ويعرف بأنّه نظام تعليمي تفاعلي يقدم للمتعلم باستعمال تكنولوجيات المعلومات والاتصال، ويعتمد على بيئة إلكترونية رقمية متكاملة تعرض كافة المقررات الدراسية عبر الشبكات الإلكترونية، كما يوفر سبل التوجيه والإرشاد وتنظيم الاختبارات بالإضافة إلى إدارة المصادر والعمليات وتقويمها.""",

    """إنّ القراءة هي رياضة العقل، فبالقراءة نُحافظ على قوة وصحة العقل كما نُحافظ بالرياضة على قوة الجسم ولياقته، حيث تُساهم القراءة بتعزيز قدرة الدماغ وحمايته من أعراض الشيخوخة وأمراضها في المستقبل، مثل ضعف الذاكرة واختلالات وظائف الدماغ.""",

    """ترجع فكرة إقامة كأس العالم إلى أول اجتماع للاتحاد الدولي لكرة القدم عام 1904 في باريس، وبحضور سبع دول هي: سويسرا، بلجيكا، الدانمارك، فرنسا، هولندا، إسبانيا، والسويد. حيث تبنى الاتحاد الدولي فكرة إقامة بطولة عالمية لكرة القدم، بعد أن استغرق القرار وقتا طويلا للاتفاق عليه بسبب عدة صعوبات.""",

    """وجد الباحثون أنه سيكون لهذه الانفجارات طاقات وترددات مماثلة لانفجارات الأشعة السينية، مع ذلك فإن هذا ليس بدليل حاسم، إذ ما يزال الباحثون بحاجة إلى تحديد ما إذا كانت هذه الانفجارات التي تحركها المادة المظلمة تختلف عن نظيراتها الفلكية المألوفة وما هي درجة اختلافها عنها.""",

    """يمكن تقسيم ملوّثات الهواء إلى ملوثّات غير مرئيّة، وملوّثات مرئيّة كالدخان الذي يتصاعد من مداخن المصانع أو الذي يخرج من عوادم المركبات، حيث تتسبب هذه الملوِّثات بالعديد من الآثار الخطيرة على حياة البشر؛ إذ تزيد من نسبة الإصابة بالعديد من الأمراض، إضافة إلى التسبب بضيق النفس، وحُرقَة الأعين وقد يؤدي تلوّث الهواء إلى الموت السريع في بعض الأحيان.""",

    """الانقراض عملية طبيعية خلال مسيرة التطور. تطورت الأنواع واختفت ببطء خلال الأزمنة الجيولوجية نتيجة التغيرات المناخية وعدم قدرتها على التكيف مع علاقات التنافس والافتراس. ولكن منذ بداية القرن السابع عشر ازداد معدل الانقراض بشكل ملحوظ بسبب الزيادة في عدد سكان العالم واستهلاك الإنسان للموارد الطبيعية.""",

    """يؤثر التدخين بشكل سلبي في جسم الإنسان؛ حيث ينتج عنه العديد من الآثار السلبية المؤذية للفرد، وقد تؤدي بعضها إلى مضاعفات تهدّد الحياة، وفي الحقيقة فإنّ التدخين يؤذي جميع أعضاء الجسم تقريباً؛ حيث إنّه يؤثر في الجهاز التنفسي، والجهاز الدوراني، والجهاز التناسلي، والجلد، والعيون.""",

    """في ثمانينيات القرن الماضي، شهد مضيق هرمز ما يُعرف بـ"حرب الناقلات" بين إيران والولايات المتحدة حول شحنات النفط العالمية. حينها، لجأت إيران إلى فرض نفوذها في مضيق هرمز عبر استهداف ناقلات النفط العالمية، حيث استخدمت الصواريخ والألغام البحرية والقوارب السريعة لفرض سيطرة غير مباشرة على المضيق."""
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

log_filename = r"D:\Final year\neural_assighment_3\prob_5\jias\jias_modern_log.txt"

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