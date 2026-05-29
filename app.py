import streamlit as st

# 1. إعدادات الصفحة الفخمة والملكية
st.set_page_config(
    page_title="Mojtaba Ali | Financial Intelligence",
    page_icon="👑",
    layout="centered"
)

# تصميم الواجهة الكلاس بالألوان الفخمة (كروت عمودية مرنة واضحة جداً)
st.markdown("""
    <style>
    /* الخلفية العامة */
    .main { background-color: #0b0d12; }
    
    /* الهيدر الملكي */
    .royal-title { color: #D4AF37; font-family: 'Segoe UI', sans-serif; text-align: center; font-weight: 800; font-size: 34px; letter-spacing: 1px; margin-bottom: 5px; }
    .royal-subtitle { text-align: center; color: #8a9ab0; font-size: 15px; margin-bottom: 30px; }
    
    /* ستايل صناديق الإدخال */
    .stNumberInput div div input { background-color: #131722 !important; color: #fff !important; border: 1px solid #2a3142 !important; border-radius: 8px !important; font-size: 18px !important; font-weight: bold !important; }
    .stNumberInput div div input:focus { border: 1px solid #D4AF37 !important; box-shadow: 0 0 5px rgba(212, 175, 55, 0.3) !important; }
    
    /* أزرار ملوك المال */
    .stButton>button { background: linear-gradient(135deg, #D4AF37 0%, #AA7C11 100%) !important; color: #0b0d12 !important; font-weight: bold !important; border: none !important; border-radius: 8px !important; padding: 12px 30px !important; transition: all 0.3s ease !important; width: 100%; font-size: 18px !important; }
    .stButton>button:hover { transform: translateY(-2px) !important; box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4) !important; }
    
    /* زر الانستغرام الفخم بالفوتر جوه على اليسار */
    .insta-link { display: inline-flex; align-items: center; justify-content: center; background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); color: white !important; padding: 6px 14px; border-radius: 20px; text-decoration: none; font-weight: bold; font-size: 12px; box-shadow: 0 4px 10px rgba(230,104,60,0.2); margin-left: 10px; }
    
    /* الكروت العمودية الثابتة بكتابة كلاس وجريئة */
    .vertical-card { border-radius: 12px; padding: 25px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }
    .card-save { background: rgba(16, 185, 129, 0.07); border: 2px solid #10b981; }
    .card-invest { background: rgba(59, 130, 246, 0.07); border: 2px solid #3b82f6; }
    .card-tax { background: rgba(239, 68, 68, 0.07); border: 2px solid #ef4444; }
    .card-wants { background: rgba(212, 175, 55, 0.08); border: 2px solid #D4AF37; }
    
    .card-title { font-size: 17px; font-weight: bold; color: #ffffff; margin-bottom: 8px; display: block; }
    .card-value { font-size: 38px; font-weight: 800; color: #ffffff; margin: 0; }
    
    /* فوتر مخصص على اليسار بالكامل */
    .footer-left { text-align: left; direction: ltr; color: #778899; font-size: 13px; margin-top: 60px; border-top: 1px solid #1c2333; padding-top: 25px; padding-left: 10px; }
    </style>
""", unsafe_allow_html=True)

# الهيدر الأساسي للموقع
st.markdown("<div class='royal-title'>الميزان الذكي لإدارة الثروات</div>", unsafe_allow_html=True)
st.markdown("<div class='royal-subtitle'>منظومة مالية مؤتمتة وحاسمة بمفهوم إدارة الثراء المرن</div>", unsafe_allow_html=True)

# إدارة الـ session_state لمنع فقدان البيانات أثناء التنقل
if 'step' not in st.session_state:
    st.session_state.step = 1

# ==================== 🌟 المرحلة الأولى: تحديد نظام العملة ورأس المال ====================
if st.session_state.step == 1:
    st.markdown("### 📥 خطوة 1: تهيئة الحساب والعملة")
    
    currency_type = st.radio("اختر عملة النظام المالي للحساب:", ["دولار أمريكي ($)", "دينار عراقي (IQD)"], horizontal=True)
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
        
    st.session_state.salary = st.number_input(f"أدخل إجمالي رأس المال أو الراتب الحالي ({symbol}):", min_value=0, value=default_val, step=step_val)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("التالي: توزيع الحصص المالية المخصصة ➡️"):
        st.session_state.step = 2
        st.rerun()

# ==================== 🌟 المرحلة الثانية: المستخدم يحدد المبالغ بكيفه بكل مرونة وحرية ====================
elif st.session_state.step == 2:
    symbol = "د.ع" if "دينار" in st.session_state.currency else "$"
    
    st.markdown(f"### 📝 خطوة 2: حدد مبالغ التوزيع الذكي (رأس المال الحالي: {st.session_state.salary:,} {symbol})")
    st.caption("أدخل المبالغ التي تريد تخصيصها لكل جانب بحرية تامة، والسيستم سيقوم بجمعها وحساب المتبقي تلقائياً.")
    
    # المستخدم يدخل المبالغ بكيفه وبدون نسب إجبارية
    val_step = 10000 if symbol == "د.ع" else 10
    
    save_input = st.number_input(f"المبلغ المخصص للادخار ({symbol}):", min_value=0, value=0, step=val_step)
    invest_input = st.number_input(f"المبلغ المخصص للاستثمار ({symbol}):", min_value=0, value=0, step=val_step)
    tax_input = st.number_input(f"المبلغ المخصص للضرائب والالتزامات الثابتة (مثل النت والبيت) ({symbol}):", min_value=0, value=0, step=val_step)
    
    # حفظ المدخلات في الـ session_state
    st.session_state.savings = save_input
    st.session_state.investment = invest_input
    st.session_state.taxes = tax_input
    
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

# ==================== 🌟 المرحلة الثالثة: التقرير المالي النهائي (الأربع مربعات الثابتة والواضحة) ====================
elif st.session_state.step == 3:
    symbol = "د.ع" if "دينار" in st.session_state.currency else "$"
    st.markdown("### 📊 التقرير المالي النهائي الحاسم")
    
    # جلب القيم التي أدخلها المستخدم بكيفه
    salary = float(st.session_state.salary)
    savings = float(st.session_state.savings)
    investment = float(st.session_state.investment)
    taxes = float(st.session_state.taxes)
    
    # الحسبة الذكية: رأس المال ناقص (الادخار + الاستثمار + الضرائب والالتزامات)
    final_free_cash = salary - (savings + investment + taxes)

    # ----------- 📊 عرض الأربع مربعات الثابتة عمودياً وبخط كبير وواضح جداً -----------
    
    # المربع الأول: الإدخار
    st.markdown(f"""
        <div class="vertical-card card-save">
            <span class="card-title">💰 أولاً: حصالة الادخار المخصصة</span>
            <p class="card-value">{savings:,} {symbol}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # المربع الثاني: الاستثمار
    st.markdown(f"""
        <div class="vertical-card card-invest">
            <span class="card-title">📈 ثانياً: خزنة الاستثمار وأصول الثروة</span>
            <p class="card-value">{investment:,} {symbol}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # المربع الثالث: الضرائب والالتزامات
    st.markdown(f"""
        <div class="vertical-card card-tax">
            <span class="card-title">📋 ثالثاً: مجموع الضرائب والالتزامات الثابتة</span>
            <p class="card-value">{taxes:,} {symbol}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # المربع الرابع: الفلوس الحرة للرفاهية (الناتج الصافي التلقائي)
    st.markdown(f"""
        <div class="vertical-card card-wants">
            <span class="card-title">💸 رابعاً: صافي الأرباح للرفاهية الحرة (المتبقي لك)</span>
            <p class="card-value" style="color:#D4AF37;">{final_free_cash:,} {symbol}</p>
            <small style="color:#8a9ab0;">هذه الفلوس المتاحة إلك تصرفها وتتونس بيها بكل حرية مطلقة بعد تأمين الحصص الفوق</small>
        </div>
    """, unsafe_allow_html=True)
    
    # التوجيه الاستراتيجي التلقائي
    st.markdown("<br>", unsafe_allow_html=True)
    if final_free_cash >= 0:
        st.success("✅ التوزيع المالي مستقر وآمن. صافي أرباحك بالموجب وخزائنك مؤمنة بالكامل.")
    else:
        st.error("⚠️ تنبيه عجز مالي: المبالغ التي قمت بتوزيعها تجاوزت إجمالي رأس المال الحالي! يرجى إعادة ضبط الميزانية.")
        
    if st.button("🔄 إعادة حساب ميزانية جديدة (إعادة بدء)"):
        st.session_state.step = 1
        st.rerun()

# 4. فوتر الحقوق الملكي بأسفل الصفحة ومحاذاته على اليسار بالكامل بلمسة IT
st.markdown(f"""
    <div class="footer-left">
        <p style="margin: 0 0 5px 0;">All Rights Reserved © 2026 | Software Engineering by <b>Mojtaba Ali</b></p>
        <a class="insta-link" href="https://instagram.com/1jit" target="_blank">📸 Instagram: 1jit</a>
    </div>
""", unsafe_allow_html=True)
