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
    """يجب للرجل أن يكون سخيًا لا يبلغ التبذير، شجاعًا لا يبلغ الهَوَج، محترسًا لا يبلغ الجبن، ماضيًا لا يبلغ القحة، قوَّالًا لا يبلغ الهذر، صموتًا لا يبلغ العي، حليمًا لا يبلغ الذل، منتصرًا لا يبلغ الظلم، وقورًا لا يبلغ البلادة، ناقدًا لا يبلغ الطيش. ثُمَّ وجدنا رسول الله ﷺ قد جمع ذلك في كلمة واحدة، وهي قوله: «خير الأمور أوساطها»، فعلمنا أنه ﷺ قد أُوتي جوامع الكلم، وعُلِّم فصل الخطاب.""",

    """اعلم أن المعنى الحقير الفاسد واللفظ الساقط يعشش في القلب، ثُمَّ يبيض، ثُمَّ يفرخ، ثُمَّ يستفحل الفساد؛ لأن اللفظ الهجين الرديء عَلِقٌ باللسان، وآلف للسمع، وأشد التحامًا بالقلب من اللفظ النبيه الشريف والمعنى الرفيع الكريم. ولو جالست الجهال والحمقى والسفهاء شهرًا فقط، لكسبت من أوضار كلامهم وخبال معانيهم ما لم تكتسبه من مجالسة أهل البيان دهرًا؛ لأن الفساد أسرع إلى الناس وأشد التحامًا بالطبائع. والإنسان بالتعلم والتكلف، وبطول الاختلاف إلى العلماء ومدارسة كتب الحكماء، يجود لفظه، ويحسن أدبه، وهو لا يحتاج في الجهل إلى أكثر من ترك التعلم، وفي فساد البيان إلى أكثر من ترك التخير.""",

    """مَثَلُ الْجَلِيسِ الصَّالِحِ وَالسَّوْءِ كَحَامِلِ الْمِسْكِ وَنَافِخِ الْكِيرِ، فَحَامِلُ الْمِسْكِ إِمَّا أَنْ يُحْذِيَكَ، وَإِمَّا أَنْ تَبْتَاعَ مِنْهُ، وَإِمَّا أَنْ تَجِدَ مِنْهُ رِيحًا طَيِّبَةً، وَنَافِخُ الْكِيرِ إِمَّا أَنْ يُحْرِقَ ثِيَابَكَ، وَإِمَّا أَنْ تَجِدَ رِيحًا خَبِيثَةً.""",

    """﴿إِنَّ اللَّهَ يُحِبُّ الْمُحْسِنِينَ ۝ الَّذِينَ يُنفِقُونَ فِي السَّرَّاءِ وَالضَّرَّاءِ وَالْكَاظِمِينَ الْغَيْظَ وَالْعَافِينَ عَنِ النَّاسِ﴾""",

    """وكانَ البخيلُ إذا دُعِيَ إلى الطعامِ اعتلَّ بعِلَلٍ كثيرة، وإذا دَعَا غيرَه أحصى اللُّقمَ وعدَّ الأنفاس، يظنُّ أنَّ الكرمَ يُنقصُ مالَه، وما علِمَ أنَّ البخلَ يُنقصُ قدرَه بين الناس.""",

    """﴿يَا أَيُّهَا الَّذِينَ آمَنُوا اجْتَنِبُوا كَثِيرًا مِنَ الظَّنِّ إِنَّ بَعْضَ الظَّنِّ إِثْمٌ وَلَا تَجَسَّسُوا وَلَا يَغْتَب بَّعْضُكُم بَعْضًا ۚ أَيُحِبُّ أَحَدُكُمْ أَن يَأْكُلَ لَحْمَ أَخِيهِ مَيْتًا فَكَرِهْتُمُوهُ ۚ وَاتَّقُوا اللَّهَ ۚ إِنَّ اللَّهَ تَوَّابٌ رَّحِيمٌ﴾""",

    """إِنَّ الصِّدْقَ يَهْدِي إِلَى الْبِرِّ، وَإِنَّ الْبِرَّ يَهْدِي إِلَى الْجَنَّةِ، وَإِنَّ الرَّجُلَ لَيَصْدُقُ حَتَّى يَكُونَ صِدِّيقًا، وَإِنَّ الْكَذِبَ يَهْدِي إِلَى الْفُجُورِ، وَإِنَّ الْفُجُورَ يَهْدِي إِلَى النَّارِ، وَإِنَّ الرَّجُلَ لَيَكْذِبُ حَتَّى يُكْتَبَ عِنْدَ اللَّهِ كَذَّابًا.""",

    """اعلم وتحقق أن المناظرة الموضوعة لقصد الغلبة والإفحام وإظهار الفضل والشرف والتشدق عند الناس وقصد المباهاة والمماراة واستمالة وجوه الناس هي منبع جميع الأخلاق المذمومة عند الله المحمودة عند عدو الله إبليس ونسبتها إلى الفواحش الباطنة من الكبر والعجب والحسد والمنافسة وتزكية النفس وحب الجاه وغيرها كنسبة شرب الخمر إلى الفواحش الظاهرة من الزنا والقذف والقتل والسرقة.""",

    """فكذلك خلل البصيرة يجري مجراه وأطم منه وأعظم إذ النفس كالفارس والبدن كالفرس وعمى الفارس أضر من عمى الفرس ولمشابهة بصيرة الباطن لبصيرة الظاهر قال الله تعالى ما كذب الفؤاد ما رأى وقال تعالى وكذلك نرى إبراهيم ملكوت السموات والأرض الآية.""",

    """قالوا: مَن أكثرَ من الكلامِ كثرَ خطؤه، ومَن أكثرَ من الضحكِ قلَّتْ هيبتُه، ومَن مزحَ استخفَّ به الناس، ومَن خالطَ السفهاءَ احتقرَه الكرام.""",

    """ينبغي للعاقلِ ألّا يعجلَ في أمرٍ حتى يعرفَ وجهَ الصوابِ فيه، فإنَّ العجلةَ كثيرًا ما تُورثُ الندم، وقد قيلَ إنَّ مَن نظرَ في العواقبِ سلمَ من النوائب. والعاقلُ لا يغترُّ بقولِ كلِّ أحد، ولا يطمئنُّ إلى ظاهرِ الكلامِ حتى يختبرَ حقيقتَه، لأنَّ كثيرًا من الناسِ يُظهرونَ الودَّ بألسنتِهم ويُخفونَ الحسدَ في قلوبِهم.""",

    """سبعةٌ يُظلُّهم اللهُ في ظلِّه يومَ لا ظلَّ إلا ظلُّه: إمامٌ عادلٌ، وشابٌّ نشأَ في عبادةِ الله، ورجلٌ قلبُه معلَّقٌ بالمساجد، ورجلانِ تحابَّا في اللهِ اجتمعا عليه وتفرَّقا عليه، ورجلٌ دعته امرأةٌ ذاتُ منصبٍ وجمالٍ فقال: إني أخافُ الله، ورجلٌ تصدَّق بصدقةٍ فأخفاها حتى لا تعلمَ شمالُه ما تنفقُ يمينُه، ورجلٌ ذكرَ اللهَ خاليًا ففاضتْ عيناه.""",

    """ألا أُخبِرُكم بأكبرِ الكبائرِ؟ قُلنا: بلى يا رسولَ اللهِ. قالَ: الإشراكُ باللهِ، وعقوقُ الوالدينِ. وكانَ متكئًا فجلسَ فقالَ: ألا وقولُ الزورِ، وشهادةُ الزورِ. فما زالَ يُكرِّرُها حتى قُلنا: ليته سكت."""
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