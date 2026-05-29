import streamlit as st
import re

# 1. إعدادات الصفحة الفخمة الملكية
st.set_page_config(
    page_title="Mojtaba Ali | Financial Intelligence",
    page_icon="👑",
    layout="centered"
)

# تصميم الواجهة الكلاس بالألوان الفخمة (كروت عمودية واضحة وجريئة)
st.markdown("""
    <style>
    /* الخلفية العامة */
    .main { background-color: #0b0d12; }
    
    /* الهيدر الملكي */
    .royal-title { color: #D4AF37; font-family: 'Segoe UI', sans-serif; text-align: center; font-weight: 800; font-size: 34px; letter-spacing: 1px; margin-bottom: 5px; }
    .royal-subtitle { text-align: center; color: #8a9ab0; font-size: 15px; margin-bottom: 30px; }
    
    /* ستايل صناديق الإدخال */
    .stNumberInput div div input, .stTextInput div div input { background-color: #131722 !important; color: #fff !important; border: 1px solid #2a3142 !important; border-radius: 8px !important; font-size: 18px !important; font-weight: bold !important; }
    .stNumberInput div div input:focus, .stTextInput div div input:focus { border: 1px solid #D4AF37 !important; box-shadow: 0 0 5px rgba(212, 175, 55, 0.3) !important; }
    
    /* أزرار ملوك المال */
    .stButton>button { background: linear-gradient(135deg, #D4AF37 0%, #AA7C11 100%) !important; color: #0b0d12 !important; font-weight: bold !important; border: none !important; border-radius: 8px !important; padding: 12px 30px !important; transition: all 0.3s ease !important; width: 100%; font-size: 18px !important; }
    .stButton>button:hover { transform: translateY(-2px) !important; box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4) !important; }
    
    /* زر الانستغرام الفخم بالفوتر جوه على اليسار */
    .insta-link { display: inline-flex; align-items: center; justify-content: center; background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); color: white !important; padding: 6px 14px; border-radius: 20px; text-decoration: none; font-weight: bold; font-size: 12px; box-shadow: 0 4px 10px rgba(230,104,60,0.2); margin-left: 10px; }
    
    /* الكروت العمودية الفخمة بكتابة كبيرة جداً */
    .vertical-card { border-radius: 12px; padding: 25px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }
    .card-needs { background: rgba(59, 130, 246, 0.07); border: 2px solid #3b82f6; }
    .card-future { background: rgba(16, 185, 129, 0.07); border: 2px solid #10b981; }
    .card-wants { background: rgba(212, 175, 55, 0.08); border: 2px solid #D4AF37; }
    
    .card-title { font-size: 16px; font-weight: bold; color: #8a9ab0; margin-bottom: 8px; display: block; }
    .card-value { font-size: 36px; font-weight: 800; color: #ffffff; margin: 0; }
    
    /* فوتر مخصص على اليسار بالكامل */
    .footer-left { text-align: left; direction: ltr; color: #778899; font-size: 13px; margin-top: 60px; border-top: 1px solid #1c2333; padding-top: 25px; padding-left: 10px; }
    </style>
""", unsafe_allow_html=True)

# الهيدر الأساسي للموقع
st.markdown("<div class='royal-title'>الميزان الذكي لإدارة الثروات</div>", unsafe_allow_html=True)
st.markdown("<div class='royal-subtitle'>منظومة مالية مؤتمتة وحاسمة بمفهوم الثراء العالمي 50-30-20</div>", unsafe_allow_html=True)

# إدارة الـ session_state لمنع تصفير أو فقدان البيانات أثناء التنقل
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'expenses' not in st.session_state:
    st.session_state.expenses = {}
if 'salary' not in st.session_state:
    st.session_state.salary = 100.0
if 'currency' not in st.session_state:
    st.session_state.currency = "دولار أمريكي ($)"

# دالة ذكية لاستخراج الأرقام من النصوص بشكل صحيح
def extract_amount_from_text(text):
    numbers = re.findall(r'\d[\d,]*', text)
    if numbers:
        return int(numbers[0].replace(',', ''))
    return None

# ==================== 🌟 المرحلة الأولى: اختيار العملة ورأس المال (قفل الاختيار عند التالي) ====================
if st.session_state.step == 1:
    st.markdown("### 📥 إيداع رأس المال وتحديد النظام")
    
    # اختيار العملة بالبداية
    currency_type = st.radio("اختر عملة النظام المالي الأساسية للحساب (سيتم قفلها بعد هذه الخطوة):", ["دولار أمريكي ($)", "دينار عراقي (IQD)"], horizontal=True)
    st.session_state.currency = currency_type
    
    # تعيين القيمة التلقائية حسب طلبك بالضبط وبدون أي خربطة
    if "دينار" in currency_type:
        default_val = 100000
        step_val = 25000
        symbol = "د.ع"
    else:
        default_val = 100
        step_val = 10
        symbol = "$"
        
    st.session_state.salary = st.number_input(f"أدخل قيمة رأس المال الحالي المستهدف ({symbol}):", min_value=0, value=default_val, step=step_val)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("التالي: بيان الالتزامات والضرائب ➡️"):
        st.session_state.step = 2
        st.rerun()

# ==================== 🌟 المرحلة الثانية: إضافة الالتزامات والمصاريف ====================
elif st.session_state.step == 2:
    symbol = "د.ع" if "دينار" in st.session_state.currency else "$"
    
    st.markdown(f"### 📝 بيان الالتزامات الثابتة (رأس المال الحالي: {st.session_state.salary:,} {symbol})")
    st.caption("اكتب براحتك بالعربي (مثال: 'نت 50000' أو 'ضرائب 40 دولار') والسيستم راح يحسبها فوراً.")
    
    user_input_text = st.text_input("اكتب تفاصيل الالتزام والمبلغ هنا:")
    
    if st.button("➕ إدراج الالتزام في الحسبة الملكية"):
        if user_input_text:
            extracted_val = extract_amount_from_text(user_input_text)
            if extracted_val and extracted_val > 0:
                cleaned_name = re.sub(r'\d[\d,]*', '', user_input_text).replace('مال', '').replace('من', '').strip()
                if not cleaned_name:
                    cleaned_name = "التزام مضاف"
                st.session_state.expenses[cleaned_name] = extracted_val
                st.toast(f"تم إدراج [{cleaned_name}] بمبلغ {extracted_val:,} {symbol} بنجاح!", icon="✅")
            else:
                st.error("⚠️ يرجى كتابة الأرقام والمبلغ بوضوح داخل النص ليتمكن النظام من قراءتها.")

    # عرض الالتزامات الحالية إن وجدت
    if st.session_state.expenses:
        st.markdown("<br>📋 **بيان الالتزامات المدرجة حالياً:**", unsafe_allow_html=True)
        for name, val in list(st.session_state.expenses.items()):
            st.write(f"🔸 {name}: {val:,} {symbol}")
        if st.button("🗑️ تفريغ كافة البيانات والبدء مجدداً"):
            st.session_state.expenses = {}
            st.rerun()
            
    st.markdown("<br>", unsafe_allow_html=True)
    col_back, col_next = st.columns(2)
    with col_back:
        if st.button("⬅️ الرجوع للخلف"):
            st.session_state.step = 1
            st.rerun()
    with col_next:
        if st.button("إنهاء وإصدار التقرير الحاسم 📊"):
            st.session_state.step = 3
            st.rerun()

# ==================== 🌟 المرحلة الثالثة: التقرير المالي الحاسم (كروت عمودية ملوك مال) ====================
elif st.session_state.step == 3:
    symbol = "د.ع" if "دينار" in st.session_state.currency else "$"
    st.markdown("### 📊 التقرير المالي النهائي الحاسم")
    
    # العمليات الحسابية المعتمدة الصافية لقاعدة 50-30-20
    salary = float(st.session_state.salary)
    
    # الحسابات الأساسية المقفلة
    future_growth = salary * 0.20  # خزنة الأصول وبناء الثروة (20%)
    allowed_needs = salary * 0.50  # الحد الأقصى للالتزامات (50%)
    allowed_wants = salary * 0.30  # صافي الأرباح للرفاهية (30%)
    
    total_added_expenses = float(sum(st.session_state.expenses.values()))
    
    # موازنة صافي الربح الفعلي بعد خصم الالتزامات
    final_free_cash = allowed_wants - (total_added_expenses - allowed_needs if total_added_expenses > allowed_needs else 0)
    
    # ----------- 📊 عرض الكروت عمودياً كارت جوة كارت وبخط كبير جداً -----------
    
    # 1. كارت خزنة الأصول وبناء الثروة (20%)
    st.markdown(f"""
        <div class="vertical-card card-future">
            <span class="card-title">🔒 خزنة الأصول وبناء الثروة (حصة الادخار والاستثمار الـ 20%)</span>
            <p class="card-value">{future_growth:,} {symbol}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 2. كارت ميزانية إدارة الالتزامات (50%)
    st.markdown(f"""
        <div class="vertical-card card-needs">
            <span class="card-title">📋 ميزانية إدارة الالتزامات والضرائب الثابتة (حصة الـ 50%)</span>
            <p class="card-value">{total_added_expenses:,} / {allowed_needs:,} {symbol}</p>
            <small style="color:#8a9ab0;">(المجموع الحالي من المصاريف / الحد الأقصى المسموح به)</small>
        </div>
    """, unsafe_allow_html=True)
    
    # تفصيل الالتزامات والضرائب بالكامل
    if st.session_state.expenses:
        with st.expander("📋 استعراض كشف الالتزامات المفصل اللي ضفتها"):
            for name, val in st.session_state.expenses.items():
                st.write(f"🔹 **{name}**: {val:,} {symbol}")
                
    # 3. كارت صافي الأرباح والرفاهية الحرة (30%)
    st.markdown(f"""
        <div class="vertical-card card-wants">
            <span class="card-title">💸 صافي الأرباح للرفاهية الحرة (حصة الـ 30% القابلة للصرف)</span>
            <p class="card-value" style="color:#D4AF37;">{final_free_cash:,} {symbol}</p>
            <small style="color:#8a9ab0;">المبلغ المتاح إلك تصرفه وتتونس بيه بكل حرية</small>
        </div>
    """, unsafe_allow_html=True)
    
    # التوجيه الاستراتيجي الفخم
    st.markdown("<br>", unsafe_allow_html=True)
    if total_added_expenses <= allowed_needs:
        st.success("✅ الإستراتيجية المالية مستقرة وضمن نطاق الثراء الحصين. الأصول والمدخرات مؤمنة بالكامل.")
    else:
        st.error("⚠️ تنبيه مالي حرج: الالتزامات تجاوزت النطاق الآمن وتأكل من حصة أرباحك الحرة! ينصح بتقليل الصرف لحماية ثروتك.")
        
    if st.button("🔄 إعادة حساب ميزانية جديدة (إعادة بدء)"):
        st.session_state.step = 1
        st.session_state.expenses = {}
        st.rerun()

# 4. فوتر الحقوق الملكي بأسفل الصفحة ومحاذاته على اليسار بالكامل بلمسة IT
st.markdown(f"""
    <div class="footer-left">
        <p style="margin: 0 0 5px 0;">All Rights Reserved © 2026 | Software Engineering by <b>Mojtaba Ali</b></p>
        <a class="insta-link" href="https://instagram.com/1jit" target="_blank">📸 Instagram: 1jit</a>
    </div>
""", unsafe_allow_html=True)
