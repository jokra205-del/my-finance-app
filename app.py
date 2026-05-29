import streamlit as st
import re

# 1. إعدادات الصفحة الكلاس والملكية
st.set_page_config(
    page_title="Mojtaba Ali | Financial Intelligence",
    page_icon="👑",
    layout="centered"
)

# تصميم الواجهة بالألوان الملكية الفاخرة
st.markdown("""
    <style>
    /* الخلفية العامة */
    .main { background-color: #0b0d12; }
    
    /* الهيدر والأنيميشن */
    .royal-title { color: #D4AF37; font-family: 'Segoe UI', sans-serif; text-align: center; font-weight: 800; font-size: 32px; letter-spacing: 1px; margin-bottom: 5px; }
    .royal-subtitle { text-align: center; color: #8a9ab0; font-size: 14px; margin-bottom: 30px; }
    
    /* ستايل صناديق الإدخال */
    .stNumberInput div div input, .stTextInput div div input { background-color: #131722 !important; color: #fff !important; border: 1px solid #2a3142 !important; border-radius: 8px !important; font-size: 16px !important; }
    .stNumberInput div div input:focus, .stTextInput div div input:focus { border: 1px solid #D4AF37 !important; box-shadow: 0 0 5px rgba(212, 175, 55, 0.3) !important; }
    
    /* أزرار التنقل الفخمة */
    .stButton>button { background: linear-gradient(135deg, #D4AF37 0%, #AA7C11 100%) !important; color: #0b0d12 !important; font-weight: bold !important; border: none !important; border-radius: 8px !important; padding: 10px 24px !important; transition: all 0.3s ease !important; width: 100%; font-size: 16px !important; }
    .stButton>button:hover { transform: translateY(-2px) !important; box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4) !important; }
    
    /* زر الانستغرام الفخم بالفوتر جوه على اليسار */
    .insta-link { display: inline-flex; align-items: center; justify-content: center; background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); color: white !important; padding: 5px 12px; border-radius: 20px; text-decoration: none; font-weight: bold; font-size: 12px; box-shadow: 0 4px 10px rgba(230,104,60,0.2); margin-left: 10px; }
    .insta-link:hover { transform: scale(1.05); }
    
    /* كروت عرض التقارير المالية بنظام الأغنياء */
    .report-card-needs { background: rgba(59, 130, 246, 0.1); border: 1px solid #3b82f6; border-radius: 12px; padding: 20px; text-align: center; }
    .report-card-future { background: rgba(16, 185, 129, 0.1); border: 1px solid #10b981; border-radius: 12px; padding: 20px; text-align: center; }
    .report-card-wants { background: rgba(212, 175, 55, 0.1); border: 1px solid #D4AF37; border-radius: 12px; padding: 25px; text-align: center; margin-top: 15px; }
    
    /* فوتر مخصص على اليسار بالكامل جوة */
    .footer-left { text-align: left; direction: ltr; color: #778899; font-size: 13px; margin-top: 60px; border-top: 1px solid #1c2333; padding-top: 25px; padding-left: 10px; }
    </style>
""", unsafe_allow_html=True)

# الهيدر الملكي
st.markdown("<div class='royal-title'>الميزان الذكي لإدارة الثروات</div>", unsafe_allow_html=True)
st.markdown("<div class='royal-subtitle'>منظومة مالية مؤتمتة لإدارة التدفقات النقدية بنظام الأغنياء 50-30-20</div>", unsafe_allow_html=True)

# إدارة حالة التنقل (Wizard Steps)
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'expenses' not in st.session_state:
    st.session_state.expenses = {}

# اختيارات العملة المدعومة
currency_type = st.radio("اختر عملة الحساب والنظام المالي:", ["دينار عراقي (IQD)", "دولار أمريكي ($)"], horizontal=True)
symbol = "د.ع" if "دينار" in currency_type else "$"

st.markdown("---")

# دالة ذكية لاستخراج الأرقام من النصوص العربية والانكليزية
def extract_amount_from_text(text):
    numbers = re.findall(r'\d[\d,]*', text)
    if numbers:
        return int(numbers[0].replace(',', ''))
    return None

# ==================== 🌟 المرحلة الأولى: إدخال رأس المال ====================
if st.session_state.step == 1:
    st.markdown("### 📥 أدخل رأس المال")
    default_val = 1500000 if symbol == "د.ع" else 1000
    step_val = 50000 if symbol == "د.ع" else 100
    
    st.session_state.salary = st.number_input(f"الرصيد أو رأس المال الإجمالي الحالي ({symbol}):", min_value=0, value=default_val, step=step_val)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("التالي: إضافة الالتزامات والضرائب ➡️"):
        st.session_state.step = 2
        st.rerun()

# ==================== 🌟 المرحلة الثانية: إضافة الالتزامات والمصاريف ====================
elif st.session_state.step == 2:
    st.markdown("### 📝 اكتب الالتزامات الثابتة والضرائب والنت")
    st.caption("اكتب براحتك بالعربي، مثلاً: 'ضرائب 40000' أو 'إيجار 300000' أو 'نت 50 دولار' والسيستم راح يفهمها فوراً.")
    
    user_input_text = st.text_input("اكتب الالتزام هنا:")
    
    if st.button("➕ إدراج الالتزام فوراً في الحسبة الذكية"):
        if user_input_text:
            extracted_val = extract_amount_from_text(user_input_text)
            if extracted_val and extracted_val > 0:
                cleaned_name = re.sub(r'\d[\d,]*', '', user_input_text).replace('مال', '').replace('من', '').strip()
                if not cleaned_name:
                    cleaned_name = "التزام مضاف"
                st.session_state.expenses[cleaned_name] = extracted_val
                st.toast(f"تم إدراج [{cleaned_name}] بمبلغ {extracted_val:,} {symbol} بنجاح!", icon="✅")
            else:
                st.error("⚠️ يرجى كتابة الرقم بشكل واضح داخل النص ليتمكن النظام من قراءتها.")

    # عرض الالتزامات الحالية إن وجدت
    if st.session_state.expenses:
        st.markdown("<br>📋 **الالتزامات والضرائب المسجلة حالياً:**", unsafe_allow_html=True)
        for name, val in list(st.session_state.expenses.items()):
            st.write(f"🔸 {name}: {val:,} {symbol}")
        if st.button("🗑️ تفريغ القائمة والبدء مجدداً"):
            st.session_state.expenses = {}
            st.rerun()
            
    st.markdown("<br>", unsafe_allow_html=True)
    col_back, col_next = st.columns(2)
    with col_back:
        if st.button("⬅️ الرجوع للخلف"):
            st.session_state.step = 1
            st.rerun()
    with col_next:
        if st.button("إنهاء وإظهار التقرير المالي الحاسم 📊"):
            st.session_state.step = 3
            st.rerun()

# ==================== 🌟 المرحلة الثالثة: التقرير المالي الحاسم بطريقة الأغنياء ====================
elif st.session_state.step == 3:
    st.markdown("### 📊 التقرير المالي النهائي الحاسم (قاعدة 50/30/20)")
    
    # حساب الحصص المالية حسب الأنظمة العالمية
    salary = st.session_state.salary
    
    # 50% للاحتياجات الثابتة والأساسية
    allowed_needs = salary * 0.50
    total_added_expenses = sum(st.session_state.expenses.values())
    
    # 20% للمستقبل (ادخار واستثمار معاً)
    future_growth = salary * 0.20
    
    # 30% للرغبات والوناسة والصرف الحر (مطروحاً منها أي زيادة في الالتزامات إن وجدت)
    allowed_wants = salary * 0.30
    final_free_cash = allowed_wants - (total_added_expenses - allowed_needs if total_added_expenses > allowed_needs else 0)
    
    # عرض الحصص بكروت ملكية متوازنة
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
            <div class="report-card-needs">
                <span style="color:#3b82f6; font-weight:bold; font-size:13px;">📊 ميزانية الاحتياجات والالتزامات (50%)</span>
                <p style="color:#8a9ab0; margin:5px 0 0 0; font-size:11px;">المسموح به: {allowed_needs:,} {symbol}</p>
                <h3 style="color:#fff; margin:5px 0 0 0;">المستهلك فعلياً: {total_added_expenses:,} {symbol}</h3>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
            <div class="report-card-future">
                <span style="color:#10b981; font-weight:bold; font-size:13px;">🔒 حصة بناء الثروة والمستقبل (20%)</span>
                <p style="color:#8a9ab0; margin:5px 0 0 0; font-size:11px;">(ادخار + استثمار مقفل)</p>
                <h3 style="color:#fff; margin:5px 0 0 0;">{future_growth:,} {symbol}</h3>
            </div>
        """, unsafe_allow_html=True)
        
    # عرض تفصيلي للالتزامات والضرائب التي أضافها الشخص
    if st.session_state.expenses:
        with st.expander("📋 عرض قائمة الالتزامات والضرائب بالتفصيل"):
            for name, val in st.session_state.expenses.items():
                st.write(f"🔹 **{name}**: {val:,} {symbol}")
        
    # عرض الفلوس الزايدة المتاحة للوناسة والصرف الحر (30%)
    st.markdown(f"""
        <div class="report-card-wants">
            <span style="color:#D4AF37; font-weight:bold; font-size:16px;">💸 الفلوس الزايدة المتاحة إلك للوناسة والصرف الحر (حصة الـ 30%)</span>
            <h1 style="color:#fff; margin:15px 0 0 0;">{final_free_cash:,} {symbol}</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # التوجيه الذكي للمستخدم
    st.markdown("<br>", unsafe_allow_html=True)
    if total_added_expenses <= allowed_needs:
        st.success("✅ توزيعك المالي مثالي جداً وضمن نطاق الأغنياء المستقر. حصة بناء الثروة مؤمنة بالكامل.")
    else:
        st.warning("⚠️ تنبيه: مصاريفك الثابتة تجاوزت الـ 50% المسموحة، السيستم قام تلقائياً بخصم الزيادة من حصة الوناسة لحماية مدخراتك المستقبيلة.")
        
    if st.button("🔄 إعادة حساب ميزانية جديدة"):
        st.session_state.step = 1
        st.session_state.expenses = {}
        st.rerun()

# 4. فوتر الحقوق الفخم بأسفل الصفحة ومحاذاته على اليسار بالكامل كما طلبت
st.markdown(f"""
    <div class="footer-left">
        <p style="margin: 0 0 5px 0;">All Rights Reserved © 2026 | Developed by <b>Mojtaba Ali</b></p>
        <a class="insta-link" href="https://instagram.com/1jit" target="_blank">📸 Instagram: 1jit</a>
    </div>
""", unsafe_allow_html=True)
