import streamlit as st

# 1. إعدادات الصفحة الفخمة والملكية
st.set_page_config(
    page_title="Mojtaba Ali | Financial Intelligence",
    page_icon="👑",
    layout="centered"
)

# تصميم الواجهة الكلاس بالألوان الفخمة (كروت عمودية واضحة وجريئة جداً)
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
    .card-save-invest { background: rgba(16, 185, 129, 0.07); border: 2px solid #10b981; }
    .card-tax { background: rgba(239, 68, 68, 0.07); border: 2px solid #ef4444; }
    .card-wants { background: rgba(212, 175, 55, 0.08); border: 2px solid #D4AF37; }
    
    .card-title { font-size: 18px; font-weight: bold; color: #ffffff; margin-bottom: 8px; display: block; }
    .card-value { font-size: 40px; font-weight: 800; color: #ffffff; margin: 0; }
    
    /* عرض قائمة الالتزامات بخط كبير وواضح وبصفه السعر */
    .expense-item { font-size: 20px; font-weight: bold; color: #ffffff; background: #131722; padding: 10px 20px; border-radius: 8px; margin-bottom: 8px; display: flex; justify-content: space-between; border-right: 4px solid #ef4444; }
    
    /* فوتر مخصص على اليسار بالكامل */
    .footer-left { text-align: left; direction: ltr; color: #778899; font-size: 13px; margin-top: 60px; border-top: 1px solid #1c2333; padding-top: 25px; padding-left: 10px; }
    </style>
""", unsafe_allow_html=True)

# الهيدر الأساسي للموقع
st.markdown("<div class='royal-title'>الميزان الذكي لإدارة الثروات</div>", unsafe_allow_html=True)
st.markdown("<div class='royal-subtitle'>منظومة مالية مؤتمتة وحاسمة بمفهوم الثراء العالمي 50-30-20</div>", unsafe_allow_html=True)

# إدارة الـ session_state لحفظ البيانات ومنع تصفيرها
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'expenses_list' not in st.session_state:
    st.session_state.expenses_list = []
if 'salary' not in st.session_state:
    st.session_state.salary = 100.0
if 'currency' not in st.session_state:
    st.session_state.currency = "دولار أمريكي ($)"

# ==================== 🌟 المرحلة الأولى: تحديد نظام العملة ورأس المال التلقائي ====================
if st.session_state.step == 1:
    st.markdown("### 📥 خطوة 1: تحديد رأس المال والعملة")
    
    currency_type = st.radio("اختر عملة النظام المالي الأساسية:", ["دولار أمريكي ($)", "دينار عراقي (IQD)"], horizontal=True)
    st.session_state.currency = currency_type
    
    # ضبط القيم التلقائية (100,000 للدينار و 100 للدولار) مثل ما ردت بالضبط
    if "دينار" in currency_type:
        default_val = 100000
        step_val = 25000
        symbol = "د.ع"
    else:
        default_val = 100
        step_val = 10
        symbol = "$"
        
    st.session_state.salary = st.number_input(f"أدخل إجمالي رأس المال الحالي ({symbol}):", min_value=0, value=default_val, step=step_val)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("التالي: إضافة الضرائب والالتزامات إن وجدت ➡️"):
        st.session_state.step = 2
        st.rerun()

# ==================== 🌟 المرحلة الثانية: إضافة الضرائب والالتزامات (مربعين منفصلين وصافيين) ====================
elif st.session_state.step == 2:
    symbol = "د.ع" if "دينار" in st.session_state.currency else "$"
    
    st.markdown(f"### 📝 خطوة 2: إضافة الضرائب والالتزامات (رأس المال الحالي: {st.session_state.salary:,} {symbol})")
    st.caption("اكتب اسم الالتزام بالمربع الأول ومبلغه بالمربع الثاني، ثم اضغط إضافة.")
    
    col_name, col_val = st.columns([2, 1])
    with col_name:
        exp_name = st.text_input("نوع أو اسم الالتزام (مثال: نت، أكل، ضرائب):", key="name_input")
    with col_val:
        exp_val = st.number_input(f"المبلغ الصافي ({symbol}):", min_value=0, value=0, key="val_input")
        
    if st.button("➕ إدراج هذا الالتزام / ضريبة أخرى"):
        if exp_val > 0:
            final_name = exp_name.strip() if exp_name.strip() else "التزام مضاف"
            # خزن على شكل ديكشنري داخل المصفوفة لمنع تداخل أو مسح الأرقام
            st.session_state.expenses_list.append({"name": final_name, "value": float(exp_val)})
            st.toast(f"تم تسجيل {final_name} بنجاح!", icon="✅")
            st.rerun()
        else:
            st.error("⚠️ يرجى كتابة مبلغ أكبر من صفر لإضافته.")

    # استعراض الالتزامات المضافة حالياً في هذه الخطوة
    if st.session_state.expenses_list:
        st.markdown("<br>📋 **الالتزامات المضافة حالياً:**", unsafe_allow_html=True)
        for item in st.session_state.expenses_list:
            st.write(f"🔸 {item['name']}: {item['value']:,} {symbol}")
        if st.button("🗑️ تفريغ كافة الالتزامات والبدء مجدداً"):
            st.session_state.expenses_list = []
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

# ==================== 🌟 المرحلة الثالثة: التقرير المالي الحاسم (الأربع مربعات الثابتة) ====================
elif st.session_state.step == 3:
    symbol = "د.ع" if "دينار" in st.session_state.currency else "$"
    st.markdown("### 📊 التقرير المالي النهائي الحاسم")
    
    # العمليات الحسابية المؤتمتة الصارمة (نظام الأغنياء 50-30-20)
    salary = float(st.session_state.salary)
    
    # 1. حصة بناء الثروة والادخار التلقائية (20%)
    future_wealth = salary * 0.20
    
    # 2. حصة ميزانية الالتزامات والضرائب المقدرة تلقائياً (50%)
    allowed_needs = salary * 0.50
    
    # جمع كافة الضرائب والالتزامات التي أدخلها المستخدم (بدون أي تصفير)
    total_added_taxes = float(sum(item['value'] for item in st.session_state.expenses_list))
    
    # 3. حصة صافي الأرباح للرفاهية الحرة تلقائياً (30%)
    allowed_wants = salary * 0.30
    
    # إذا تجاوزت المصاريف والضرائب الـ 50% تلتهم من حصة الرفاهية تلقائياً لحماية الادخار
    if total_added_taxes > allowed_needs:
        final_free_cash = allowed_wants - (total_added_taxes - allowed_needs)
    else:
        final_free_cash = allowed_wants

    # ----------- 📊 عرض المربعات الثابتة عمودياً وبخط كبير وواضح جداً -----------
    
    # 1. مربع حصة الادخار والاستثمار التلقائي (20%)
    st.markdown(f"""
        <div class="vertical-card card-save-invest">
            <span class="card-title">🔒 أولاً: حصنة بناء الثروة (الادخار والاستثمار المقفل 20%)</span>
            <p class="card-value">{future_wealth:,} {symbol}</p>
            <small style="color:#8a9ab0;">مبلغ مؤمن تلقائياً في الخزنة الحصينة للمستقبل</small>
        </div>
    """, unsafe_allow_html=True)
    
    # 2. مربع عرض قائمة الضرائب بالتفصيل وبخط كبير (اسم المصرف وبصفه السعر)
    st.markdown("<h4 style='color:#fff; margin-bottom:10px;'>📋 ثانياً: بيان الضرائب والالتزامات المفصلة:</h4>", unsafe_allow_html=True)
    if st.session_state.expenses_list:
        for item in st.session_state.expenses_list:
            st.markdown(f"""
                <div class="expense-item">
                    <span>🔸 {item['name']}</span>
                    <span>{item['value']:,} {symbol}</span>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("<div class='expense-item'><span>لا توجد ضرائب أو التزامات مضافة</span><span>0 {symbol}</span></div>", unsafe_allow_html=True)
        
    # 3. مربع مجموع الضرائب والالتزامات
    st.markdown(f"""
        <div class="vertical-card card-tax">
            <span class="card-title">📊 ثالثاً: إجمالي مجموع الضرائب والالتزامات</span>
            <p class="card-value">{total_added_taxes:,} {symbol}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 4. مربع صافي الأرباح والرفاهية الحرة (المتبقي الفعلي)
    st.markdown(f"""
        <div class="vertical-card card-wants">
            <span class="card-title">💸 رابعاً: صافي الأرباح للرفاهية الحرة (حصة الـ 30%)</span>
            <p class="card-value" style="color:#D4AF37;">{final_free_cash:,} {symbol}</p>
            <small style="color:#8a9ab0;">الفلوس الصافية المتاحة إلك لتصرفها وتتونس بيها بكل حرية مطلقة</small>
        </div>
    """, unsafe_allow_html=True)
    
    # زر إعادة الحساب بالكامل
    if st.button("🔄 إعادة حساب ميزانية جديدة (إعادة بدء)"):
        st.session_state.step = 1
        st.session_state.expenses_list = []
        st.rerun()

# 4. فوتر الحقوق الملكي بأسفل الصفحة ومحاذاته على اليسار بالكامل بلمسة IT
st.markdown(f"""
    <div class="footer-left">
        <p style="margin: 0 0 5px 0;">All Rights Reserved © 2026 | Software Engineering by <b>Mojtaba Ali</b></p>
        <a class="insta-link" href="https://instagram.com/1jit" target="_blank">📸 Instagram: 1jit</a>
    </div>
""", unsafe_allow_html=True)
