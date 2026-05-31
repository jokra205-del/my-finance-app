import streamlit as st
import json

# 1. إعدادات الصفحة الفخمة الملكية
st.set_page_config(
    page_title="Mojtaba Ali | Financial Intelligence",
    page_icon="👑",
    layout="centered"
)

# تصميم الواجهة الكلاس بالألوان الفخمة والكروت العمودية الواضحة جداً
st.markdown("""
    <style>
    /* الخلفية العامة */
    .main { background-color: #0b0d12; }
    
    /* الهيدر الملكي */
    .royal-title { color: #D4AF37; font-family: 'Segoe UI', sans-serif; text-align: center; font-weight: 800; font-size: 34px; letter-spacing: 1px; margin-bottom: 5px; }
    .royal-subtitle { text-align: center; color: #8a9ab0; font-size: 15px; margin-bottom: 30px; }
    
    /* ستايل صناديق الإدخال والـ selectbox */
    .stNumberInput div div input, .stTextInput div div input, .stSelectbox div div div { background-color: #131722 !important; color: #fff !important; border: 1px solid #2a3142 !important; border-radius: 8px !important; font-size: 18px !important; font-weight: bold !important; }
    .stNumberInput div div input:focus, .stTextInput div div input:focus { border: 1px solid #D4AF37 !important; box-shadow: 0 0 5px rgba(212, 175, 55, 0.3) !important; }
    
    /* أزرار ملوك المال */
    .stButton>button { background: linear-gradient(135deg, #D4AF37 0%, #AA7C11 100%) !important; color: #0b0d12 !important; font-weight: bold !important; border: none !important; border-radius: 8px !important; padding: 12px 30px !important; transition: all 0.3s ease !important; width: 100%; font-size: 18px !important; }
    .stButton>button:hover { transform: translateY(-2px) !important; box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4) !important; }
    
    /* زر الانستغرام الفخم بالفوتر جوه على اليسار */
    .insta-link { display: inline-flex; align-items: center; justify-content: center; background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); color: white !important; padding: 6px 14px; border-radius: 20px; text-decoration: none; font-weight: bold; font-size: 12px; box-shadow: 0 4px 10px rgba(230,104,60,0.2); margin-left: 10px; }
    
    /* الكروت العمودية الثابتة بكتابة كلاس وجريئة */
    .vertical-card { border-radius: 12px; padding: 25px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }
    .card-save { background: rgba(16, 185, 129, 0.07); border: 2px solid #10b981; }
    .card-invest { background: rgba(59, 130, 246, 0.07); border: 2px solid #3b82f6; }
    .card-tax { background: rgba(239, 68, 68, 0.08); border: 3px solid #ef4444; } /* المربع الأحمر الملكي للضرائب */
    .card-wants { background: rgba(212, 175, 55, 0.08); border: 2px solid #D4AF37; }
    
    .card-title { font-size: 18px; font-weight: bold; color: #ffffff; margin-bottom: 8px; display: block; }
    .card-value { font-size: 40px; font-weight: 800; color: #ffffff; margin: 0; }
    
    /* تفاصيل الالتزامات داخل المربع الأحمر */
    .tax-detail-item { font-size: 18px; color: #ffb3b3; margin: 5px 0; font-weight: bold; }
    
    /* صندوق التقرير التفاعلي والمصاريف */
    .action-box { background-color: #131722; border: 1px dashed #2a3142; border-radius: 12px; padding: 20px; margin-top: 25px; }
    .action-title { color: #D4AF37; font-size: 20px; font-weight: bold; margin-bottom: 15px; display: block; text-align: center; }
    
    /* فوتر مخصص على اليسار بالكامل */
    .footer-left { text-align: left; direction: ltr; color: #778899; font-size: 13px; margin-top: 60px; border-top: 1px solid #1c2333; padding-top: 25px; padding-left: 10px; }
    </style>
""", unsafe_allow_html=True)

# الهيدر الأساسي للموقع
st.markdown("<div class='royal-title'>الميزان الذكي لإدارة الثروات</div>", unsafe_allow_html=True)
st.markdown("<div class='royal-subtitle'>منظومة مالية مؤتمتة وحاسمة بمفهوم الثراء العالمي 50-30-20</div>", unsafe_allow_html=True)

# ==================== 🧠 مكون الحفظ الذكي في المتصفح LocalStorage ====================
# جافا سكريبت مخفي للاتصال بـ LocalStorage الخاص بجهاز المستخدم للمحافظة على البيانات
def ايداع_وحفظ_بالجهاز(key, data):
    js_code = f"<script>localStorage.setItem('{key}', '{json.dumps(data)}');</script>"
    st.components.v1.html(js_code, height=0)

# إدارة الـ session_state لمنع تصفير أو فقدان البيانات أثناء التنقل
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'num_expenses' not in st.session_state:
    st.session_state.num_expenses = 1 
if 'salary' not in st.session_state:
    st.session_state.salary = 100.0
if 'currency' not in st.session_state:
    st.session_state.currency = "دولار أمريكي ($)"

# متغيرات تراكم المحفظة الذكية
if 'wallet_initialized' not in st.session_state:
    st.session_state.wallet_initialized = False
    st.session_state.accumulated_savings = 0.0
    st.session_state.accumulated_investment = 0.0
    st.session_state.accumulated_wants = 0.0
    st.session_state.expense_log = []

# ==================== 🌟 المرحلة الأولى: تحديد نظام العملة ورأس المال التلقائي ====================
if st.session_state.step == 1:
    st.markdown("### 📥 خطوة 1: تحديد رأس المال والعملة")
    
    currency_type = st.radio("اختر عملة النظام المالي الأساسية الحالية للبرنامج:", ["دولار أمريكي ($)", "دينار عراقي (IQD)"], horizontal=True)
    st.session_state.currency = currency_type
    
    if "دينار" in currency_type:
        default_val = 100000
        step_val = 25000
        symbol = "د.ع"
    else:
        default_val = 100
        step_val = 10
        symbol = "$"
        
    st.session_state.salary = st.number_input(f"أدخل إجمالي رأس المال الحالي للعمل به ({symbol}):", min_value=0, value=default_val, step=step_val)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("التالي: إضافة الضرائب والالتزامات ➡️"):
        st.session_state.step = 2
        st.rerun()

# ==================== 🌟 المرحلة الثانية: إضافة الضرائب والالتزامات ====================
elif st.session_state.step == 2:
    symbol = "د.ع" if "دينار" in st.session_state.currency else "$"
    st.markdown(f"### 📝 خطوة 2: إضافة الضرائب والالتزامات (رأس المال: {st.session_state.salary:,} {symbol})")
    st.caption("اكتب اسم الالتزام ومبلغه، وإذا عندك التزام ثاني دوس الزر الجوه وراح يفتح لك مربع جديد تلقائياً وبدون ما ينمسح الفوق.")
    
    expenses_data = []
    for i in range(st.session_state.num_expenses):
        col_name, col_val = st.columns([2, 1])
        with col_name:
            exp_name = st.text_input(f"اسم الالتزام / الضريبة {i+1}:", key=f"name_{i}")
        with col_val:
            exp_val = st.number_input(f"المبلغ ({symbol}):", min_value=0, value=0, key=f"val_{i}")
        
        if exp_val > 0:
            expenses_data.append({"name": exp_name.strip() if exp_name.strip() else f"ضريبة {i+1}", "value": float(exp_val)})
            
    st.session_state.final_expenses = expenses_data

    if st.button("➕ إضافة ضريبة أو التزام آخر"):
        st.session_state.num_expenses += 1
        st.rerun()
        
    st.markdown("<br>", unsafe_allow_html=True)
    col_back, col_next = st.columns(2)
    with col_back:
        if st.button("⬅️ الرجوع للخلف"):
            st.session_state.step = 1
            st.rerun()
    with col_next:
        if st.button("إنهاء وإصدار التقرير المالي الحاسم 📊"):
            st.session_state.step = 3
            st.rerun()

# ==================== 🌟 المرحلة الثالثة: التقرير المالي الحاسم والمحفظة المحفوظة ====================
elif st.session_state.step == 3:
    symbol = "د.ع" if "دينار" in st.session_state.currency else "$"
    st.markdown("### 📊 التقرير المالي الذكي والمحفظة التراكمية")
    
    salary = float(st.session_state.salary)
    expenses_list = st.session_state.get('final_expenses', [])
    total_taxes = float(sum(item['value'] for
