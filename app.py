import streamlit as st

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
    
    /* ستايل صناديق الإدخال */
    .stNumberInput div div input, .stTextInput div div input { background-color: #131722 !important; color: #fff !important; border: 1px solid #2a3142 !important; border-radius: 8px !important; font-size: 18px !important; font-weight: bold !important; }
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
if 'num_expenses' not in st.session_state:
    st.session_state.num_expenses = 1 # نبدأ بمربع واحد تلقائياً
if 'salary' not in st.session_state:
    st.session_state.salary = 100.0
if 'currency' not in st.session_state:
    st.session_state.currency = "دولار أمريكي ($)"

# ==================== 🌟 المرحلة الأولى: تحديد نظام العملة ورأس المال التلقائي ====================
if st.session_state.step == 1:
    st.markdown("### 📥 خطوة 1: تحديد رأس المال والعملة")
    
    currency_type = st.radio("اختر عملة النظام المالي الأساسية الحالية للبرنامج:", ["دولار أمريكي ($)", "دينار عراقي (IQD)"], horizontal=True)
    st.session_state.currency = currency_type
    
    # ضبط القيم التلقائية الفخمة (100,000 للدينار و 100 للدولار)
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

# ==================== 🌟 المرحلة الثانية: إضافة الضرائب والالتزامات (مربعات ديناميكية تنزل جوة) ====================
elif st.session_state.step == 2:
    symbol = "د.ع" if "دينار" in st.session_state.currency else "$"
    st.markdown(f"### 📝 خطوة 2: إضافة الضرائب والالتزامات (رأس المال: {st.session_state.salary:,} {symbol})")
    st.caption("اكتب اسم الالتزام ومبلغه، وإذا عندك التزام ثاني دوس الزر الجوه وراح يفتح لك مربع جديد تلقائياً وبدون ما ينمسح الفوق.")
    
    # توليد المربعات بشكل ديناميكي بناءً على العدد المخزن بدون مسح البيانات السابقة
    expenses_data = []
    for i in range(st.session_state.num_expenses):
        col_name, col_val = st.columns([2, 1])
        with col_name:
            exp_name = st.text_input(f"اسم الالتزام / الضريبة {i+1}:", key=f"name_{i}")
        with col_val:
            exp_val = st.number_input(f"المبلغ ({symbol}):", min_value=0, value=0, key=f"val_{i}")
        
        if exp_val > 0:
            expenses_data.append({"name": exp_name.strip() if exp_name.strip() else f"ضريبة {i+1}", "value": float(exp_val)})
            
    # حفظ القائمة المحدثة بالـ session_state ليقرأها التقرير النهائي
    st.session_state.final_expenses = expenses_data

    # زر إضافة مربع جديد جوة المربع القديم فوراً وبدون ريفرش يمسح الكتابة
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

# ==================== 🌟 المرحلة الثالثة: التقرير المالي الحاسم (الأربع مربعات الثابتة مع المربع الأحمر المدمج) ====================
elif st.session_state.step == 3:
    symbol = "د.ع" if "دينار" in st.session_state.currency else "$"
    st.markdown("### 📊 التقرير المالي النهائي الحاسم")
    
    salary = float(st.session_state.salary)
    expenses_list = st.session_state.get('final_expenses', [])
    
    # 1. حساب مجموع الضرائب والالتزامات (المربع الأحمر بالكامل)
    total_taxes = float(sum(item['value'] for item in expenses_list))
    
    # 2. الحسبة الحوتية: استخراج الصافي المتبقي بعد طرح الضرائب بالكامل أولاً
    remaining_net = salary - total_taxes
    
    # تأمين الحسبة في حال كانت الضرائب أعلى من رأس المال
    if remaining_net < 0:
        remaining_net = 0
        
    # 3. تقسيم الصافي المتبقي بناءً على قاعدة الأغنياء المرنة (20% ادخار، 30% استثمار، 50% رفاهية)
    savings_share = remaining_net * 0.20
    investment_share = remaining_net * 0.30
    wants_share = remaining_net * 0.50

    # ----------- 📊 عرض الأربع مربعات الثابتة عمودياً وبخطوط واضحة جداً -----------
    
    # المربع الأول: الإدخار (20% من الصافي)
    st.markdown(f"""
        <div class="vertical-card card-save">
            <span class="card-title">💰 أولاً: حصالة الادخار الملكية (20% من الصافي)</span>
            <p class="card-value">{savings_share:,} {symbol}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # المربع الثاني: الاستثمار (30% من الصافي)
    st.markdown(f"""
        <div class="vertical-card card-invest">
            <span class="card-title">📈 ثانياً: خزنة الاستثمار وأصول الثروة (30% من الصافي)</span>
            <p class="card-value">{investment_share:,} {symbol}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # المربع الثالث: الضرائب والالتزامات (المربع الأحمر المدمج اللي يعرض كل شي جواه)
    tax_items_html = ""
    if expenses_list:
        for item in expenses_list:
            tax_items_html += f"<div class='tax-detail-item'>🔸 {item['name']}: {item['value']:,} {symbol}</div>"
    else:
        tax_items_html = "<div class='tax-detail-item'>لا توجد ضرائب أو التزامات مضافة</div>"
        
    st.markdown(f"""
        <div class="vertical-card card-tax">
            <span class="card-title">🛑 ثالثاً: مجموع كافة الضرائب والالتزامات (المربع الأحمر)</span>
            <p class="card-value" style="margin-bottom: 15px;">{total_taxes:,} {symbol}</p>
            <div style="text-align: right; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 10px;">
                {tax_items_html}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # المربع الرابع: الربح الصافي والرفاهية الحرة (50% من الصافي المتبقي)
    st.markdown(f"""
        <div class="vertical-card card-wants">
            <span class="card-title">💸 رابعاً: صافي الأرباح للرفاهية الحرة (50% من الصافي المتبقي)</span>
            <p class="card-value" style="color:#D4AF37;">{wants_share:,} {symbol}</p>
            <small style="color:#8a9ab0;">الفلوس المتاحة إلك تصرفها وتتونس بيها بكل حرية بعد تأمين الحصص الفوق</small>
        </div>
    """, unsafe_allow_html=True)
    
    # زر إعادة الحساب بالكامل وتصفير الخطوات
    if st.button("🔄 إعادة حساب ميزانية جديدة (إعادة بدء)"):
        st.session_state.step = 1
        st.session_state.num_expenses = 1
        if 'final_expenses' in st.session_state:
            del st.session_state.final_expenses
        st.rerun()

# 4. فوتر الحقوق الملكي بأسفل الصفحة ومحاذاته على اليسار بالكامل بلمسة IT
st.markdown(f"""
    <div class="footer-left">
        <p style="margin: 0 0 5px 0;">All Rights Reserved © 2026 | Software Engineering by <b>Mojtaba Ali</b></p>
        <a class="insta-link" href="https://instagram.com/1jit" target="_blank">📸 Instagram: 1jit</a>
    </div>
""", unsafe_allow_html=True)
