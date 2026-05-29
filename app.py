import streamlit as st

# 1. إعدادات الصفحة الفخمة الملكية
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
st.markdown("<div class='royal-subtitle'>منظومة مالية مؤتمتة وحاسمة بمفهوم الثراء العالمي 50-30-20</div>", unsafe_allow_html=True)

# إدارة الـ session_state لمنع فقدان البيانات أثناء التنقل بين الصفحات
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'expenses' not in st.session_state:
    st.session_state.expenses = {}
if 'salary' not in st.session_state:
    st.session_state.salary = 100.0
if 'currency' not in st.session_state:
    st.session_state.currency = "دولار أمريكي ($)"

# ==================== 🌟 المرحلة الأولى: تحديد العملة ورأس المال ====================
if st.session_state.step == 1:
    st.markdown("### 📥 إيداع رأس المال وتحديد نظام العملة")
    
    # اختيار العملة بالبداية وقفلها
    currency_type = st.radio("اختر عملة النظام المالي للحساب (سيتم قفلها في الخطوات القادمة):", ["دولار أمريكي ($)", "دينار عراقي (IQD)"], horizontal=True)
    st.session_state.currency = currency_type
    
    # ضبط القيم التلقائية الفخمة (100,000 للدينار و 100 للدولار) حسب طلبك بالضبط
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
    if st.button("التالي: إضافة الضرائب والالتزامات ➡️"):
        st.session_state.step = 2
        st.rerun()

# ==================== 🌟 المرحلة الثانية: إضافة الالتزامات والضرائب (مربعات منفصلة وصافية) ====================
elif st.session_state.step == 2:
    symbol = "د.ع" if "دينار" in st.session_state.currency else "$"
    
    st.markdown(f"### 📝 بيان الالتزامات والضرائب الثابتة (رأس المال: {st.session_state.salary:,} {symbol})")
    st.caption("اكتب اسم الالتزام في المربع الأول، والمبلغ الصافي في المربع الثاني بدون أي كلمات أخرى.")
    
    # مربعين منفصلين بصف واحد لترتيب الواجهة
    col_name, col_val = st.columns([2, 1])
    with col_name:
        expense_name = st.text_input("اسم الالتزام أو الضريبة (مثال: نت، ضرائب):", key="exp_name_input")
    with col_val:
        expense_value = st.number_input(f"المبلغ ({symbol}):", min_value=0, value=0, key="exp_val_input")
    
    # زر واضح وصريح لإضافة التزام آخر
    if st.button("➕ إضافة هذا الالتزام / ضريبة أخرى"):
        if expense_value > 0:
            name_final = expense_name.strip() if expense_name.strip() else "التزام غير مسمى"
            st.session_state.expenses[name_final] = expense_value
            st.toast(f"تم تسجيل {name_final} بمبلغ {expense_value:,} {symbol} بنجاح!", icon="✅")
            st.rerun()
        else:
            st.error("⚠️ يرجى إدخال مبلغ أكبر من صفر لإضافته للحسبة.")

    # عرض كشف الالتزامات المضافة حالياً إن وجدت لتنبيه المستخدم
    if st.session_state.expenses:
        st.markdown("<br>📋 **الالتزامات والضرائب المسجلة حالياً:**", unsafe_allow_html=True)
        for name, val in list(st.session_state.expenses.items()):
            st.write(f"🔸 {name}: {val:,} {symbol}")
        if st.button("🗑️ تفريغ كافة الالتزامات والبدء مجدداً"):
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

# ==================== 🌟 المرحلة الثالثة: التقرير المالي النهائي الحاسم (الأربع مربعات الثابتة) ====================
elif st.session_state.step == 3:
    symbol = "د.ع" if "دينار" in st.session_state.currency else "$"
    st.markdown("### 📊 التقرير المالي النهائي الحاسم")
    
    # العمليات الحسابية الصارمة المبنية على قاعدة 50-30-20 الفخمة
    salary = float(st.session_state.salary)
    
    # 1. تقسيم الحصص الثابتة (10% ادخار، 10% استثمار) ليكون المجموع 20% لبناء الثروة
    savings_share = salary * 0.10
    investment_share = salary * 0.10
    
    # 2. حساب مجموع الضرائب والالتزامات المضافة من قبل المستخدم
    total_taxes_expenses = float(sum(st.session_state.expenses.values()))
    
    # 3. حساب الفلوس المتاحة للرفاهية والصرف الحر (حصة الـ 30%)
    allowed_needs = salary * 0.50
    allowed_wants = salary * 0.30
    
    # موازنة الحسبة في حال تجاوزت الالتزامات حصتها الـ 50% تلتهم من حصة الرفاهية
    if total_taxes_expenses > allowed_needs:
        final_free_cash = allowed_wants - (total_taxes_expenses - allowed_needs)
    else:
        final_free_cash = allowed_wants

    # ----------- 📊 عرض الأربع مربعات الثابتة عمودياً وبخط كبير جداً -----------
    
    # المربع الأول: الإدخار (10%)
    st.markdown(f"""
        <div class="vertical-card card-save">
            <span class="card-title">💰 أولاً: حصالة الادخار الملكية (حصة الـ 10%)</span>
            <p class="card-value">{savings_share:,} {symbol}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # المربع الثاني: الاستثمار (10%)
    st.markdown(f"""
        <div class="vertical-card card-invest">
            <span class="card-title">📈 ثانياً: خزنة الاستثمار وأصول الثروة (حصة الـ 10%)</span>
            <p class="card-value">{investment_share:,} {symbol}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # المربع الثالث: الضرائب والالتزامات
    st.markdown(f"""
        <div class="vertical-card card-tax">
            <span class="card-title">📋 ثالثاً: مجموع الضرائب والالتزامات المضافة</span>
            <p class="card-value">{total_taxes_expenses:,} {symbol}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # عرض تفصيلي للالتزامات في حال وجودها داخل منسدلة كلاس
    if st.session_state.expenses:
        with st.expander("🔍 كشف وتفاصيل الضرائب والالتزامات المسجلة"):
            for name, val in st.session_state.expenses.items():
                st.write(f"🔹 **{name}**: {val:,} {symbol}")
                
    # المربع الرابع: الفلوس الحرة للرفاهية (30%)
    st.markdown(f"""
        <div class="vertical-card card-wants">
            <span class="card-title">💸 رابعاً: صافي الأرباح للرفاهية الحرة (حصة الـ 30% القابلة للصرف)</span>
            <p class="card-value" style="color:#D4AF37;">{final_free_cash:,} {symbol}</p>
            <small style="color:#8a9ab0;">هذه الفلوس المتاحة إلك تصرفها وتتونس بيها بكل حرية مطلقة</small>
        </div>
    """, unsafe_allow_html=True)
    
    # التوجيه الاستراتيجي النهائي للملوك
    st.markdown("<br>", unsafe_allow_html=True)
    if final_free_cash >= 0:
        st.success("✅ الإستراتيجية المالية مستقرة وضمن نطاق الثراء الحصين. الأصول والمدخرات مؤمنة بالكامل.")
    else:
        st.error("⚠️ تنبيه مالي حرج: الالتزامات والضرائب تجاوزت النطاق الآمن وتأكل من حصة أرباحك الحرة!")
        
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
