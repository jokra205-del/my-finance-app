import streamlit as st

# 1. إعدادات الصفحة الكلاس والملكية
st.set_page_config(
    page_title="Mojtaba Ali | Financial Intelligence",
    page_icon="👑",
    layout="centered"
)

# تصميم الواجهة بالألوان الملكية (أسود فاخر، ذهبي مطفأ، ولمسات براند الانستغرام)
st.markdown("""
    <style>
    /* الخلفية العامة */
    .main { background-color: #0b0d12; }
    
    /* الهيدر والأنيميشن */
    .royal-title { color: #D4AF37; font-family: 'Segoe UI', sans-serif; text-align: center; font-weight: 800; font-size: 32px; letter-spacing: 1px; margin-bottom: 5px; }
    .royal-subtitle { text-align: center; color: #8a9ab0; font-size: 14px; margin-bottom: 30px; }
    
    /* ستايل المطور فوق على اليسار */
    .dev-badge { position: absolute; top: -50px; left: 0px; background: rgba(212, 175, 55, 0.1); border: 1px solid #D4AF37; padding: 10px 18px; border-radius: 20px; color: #D4AF37; font-size: 13px; font-weight: bold; font-family: 'Segoe UI', sans-serif; box-shadow: 0 4px 10px rgba(0,0,0,0.3); }
    
    /* ستايل صناديق الإدخال */
    .stNumberInput div div input, .stTextInput div div input { background-color: #131722 !important; color: #fff !important; border: 1px solid #2a3142 !important; border-radius: 8px !important; font-size: 16px !important; }
    .stNumberInput div div input:focus, .stTextInput div div input:focus { border: 1px solid #D4AF37 !important; box-shadow: 0 0 5px rgba(212, 175, 55, 0.3) !important; }
    
    /* أزرار التنقل الفخمة */
    .stButton>button { background: linear-gradient(135deg, #D4AF37 0%, #AA7C11 100%) !important; color: #0b0d12 !important; font-weight: bold !important; border: none !important; border-radius: 8px !important; padding: 10px 24px !important; transition: all 0.3s ease !important; width: 100%; font-size: 16px !important; }
    .stButton>button:hover { transform: translateY(-2px) !important; box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4) !important; }
    
    /* زر الانستغرام الفخم بالفوتر وتحت التاج */
    .insta-link { display: inline-flex; align-items: center; justify-content: center; background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); color: white !important; padding: 6px 14px; border-radius: 20px; text-decoration: none; font-weight: bold; font-size: 13px; margin-top: 5px; box-shadow: 0 4px 10px rgba(230,104,60,0.2); }
    .insta-link:hover { transform: scale(1.05); }
    
    /* كروت عرض التقارير المالية */
    .report-card-save { background: rgba(16, 185, 129, 0.1); border: 1px solid #10b981; border-radius: 12px; padding: 20px; text-align: center; }
    .report-card-invest { background: rgba(59, 130, 246, 0.1); border: 1px solid #3b82f6; border-radius: 12px; padding: 20px; text-align: center; }
    .report-card-free { background: rgba(212, 175, 55, 0.1); border: 1px solid #D4AF37; border-radius: 12px; padding: 25px; text-align: center; margin-top: 15px; }
    
    .footer { text-align: center; color: #778899; font-size: 13px; margin-top: 60px; border-top: 1px solid #1c2333; padding-top: 25px; }
    </style>
""", unsafe_allow_html=True)

# 2. بصمة المطور والأشراف فوق على اليسار مع رابط الحساب المباشر لـ IT
st.markdown(f"""
    <div style="position: relative;">
        <div class="dev-badge">
            👑 بإشراف المطور: Mojtaba Ali 
            <br style="margin-bottom: 5px;">
            <a class="insta-link" href="https://instagram.com/1jit" target="_blank">📸 Instagram: 1jit</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# تباعد الهيدر
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<div class='royal-title'>الميزان الذكي لإدارة الثروات</div>", unsafe_allow_html=True)
st.markdown("<div class='royal-subtitle'>منظومة مالية مؤتمتة وحاسمة لحماية التدفقات النقدية</div>", unsafe_allow_html=True)

# إدارة حالة التنقل (Wizard Steps)
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'expenses' not in st.session_state:
    st.session_state.expenses = {}

# اختيارات العملة المدعومة ملكياً
currency_type = st.radio("اختر عملة الحساب والنظام المالي:", ["دينار عراقي (IQD)", "دولار أمريكي ($)"], horizontal=True)
symbol = "د.ع" if "دينار" in currency_type else "$"

st.markdown("---")

# ==================== 🌟 المرحلة الأولى: إدخال رأس المال ====================
if st.session_state.step == 1:
    st.markdown("### 📥 أدخل رأس المال")
    default_val = 500000 if symbol == "د.ع" else 500
    step_val = 25000 if symbol == "د.ع" else 50
    
    st.session_state.salary = st.number_input(f"الرصيد أو الراتب الشهري الحالي ({symbol}):", min_value=0, value=default_val, step=step_val)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("التالي: إضافة الالتزامات ➡️"):
        st.session_state.step = 2
        st.rerun()

# ==================== 🌟 المرحلة الثانية: إضافة الالتزامات والمصاريف ====================
elif st.session_state.step == 2:
    st.markdown("### 📝 هل لديك ضرائب، إيجار، إنترنت أو التزامات أخرى؟")
    
    col1, col2 = st.columns(2)
    with col1:
        exp_name = st.text_input("نوع الالتزام (مثال: ضرائب، نت):")
    with col2:
        exp_val = st.number_input(f"مبلغ الالتزام ({symbol}):", min_value=0, value=0, step=5000 if symbol == "د.ع" else 10)
        
    if st.button("➕ إدراج الالتزام فوراً في الحسبة الذكية"):
        if exp_name and exp_val > 0:
            st.session_state.expenses[exp_name] = exp_val
            st.toast(f"تم إدراج {exp_name} بنجاح!", icon="✅")

    # عرض الالتزامات الحالية إن وجدت
    if st.session_state.expenses:
        st.markdown("<br>📋 **الالتزامات الثابتة المسجلة:**", unsafe_allow_html=True)
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
        if st.button("إنهاء وإظهار التقرير الحاسم 📊"):
            st.session_state.step = 3
            st.rerun()

# ==================== 🌟 المرحلة الثالثة: التقرير المالي النهائي الحاسم ====================
elif st.session_state.step == 3:
    st.markdown("### 📊 التقرير المالي النهائي الحاسم")
    
    # العمليات الرياضية الصارمة للميزان المالي
    salary = st.session_state.salary
    savings = salary * 0.15
    investment = salary * 0.15
    total_expenses = sum(st.session_state.expenses.values())
    final_free_cash = salary - (savings + investment + total_expenses)
    
    # عرض المبالغ المقفلة والمحمية بكروت كلاس
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
            <div class="report-card-save">
                <span style="color:#10b981; font-weight:bold; font-size:14px;">🔒 مبلغ الادخار المقفل (15%)</span>
                <h2 style="color:#fff; margin:10px 0 0 0;">{savings:,} {symbol}</h2>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
            <div class="report-card-invest">
                <span style="color:#3b82f6; font-weight:bold; font-size:14px;">📈 مبلغ الاستثمار المقفل (15%)</span>
                <h2 style="color:#fff; margin:10px 0 0 0;">{investment:,} {symbol}</h2>
            </div>
        """, unsafe_allow_html=True)
        
    # عرض الفلوس الزايدة المتاحة للصرف بكل حرية
    st.markdown(f"""
        <div class="report-card-free">
            <span style="color:#D4AF37; font-weight:bold; font-size:16px;">💸 الفلوس الزايدة المتاحة لك للصرف والوناسة بحرية مطلقة</span>
            <h1 style="color:#fff; margin:15px 0 0 0;">{final_free_cash:,} {symbol}</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # التوجيه الذكي للمخدم
    st.markdown("<br>", unsafe_allow_html=True)
    if final_free_cash >= 0:
        st.success("✅ جميع حصص الاستثمار والادخار مؤمنة بالكامل في الخزنة الحصينة دون أي تهديد.")
    else:
        st.error("⚠️ تنبيه ذكي: الالتزامات الإضافية تجاوزت الفلوس الزايدة ودخلت بالخط الأحمر! ينصح بتقليل الصرف الحر لحماية مدخراتك.")
        
    if st.button("🔄 إعادة حساب ميزانية جديدة"):
        st.session_state.step = 1
        st.session_state.expenses = {}
        st.rerun()

# 4. فوتر الحقوق الفخم بأسفل الصفحة مع يوزرك المباشر للعالم
st.markdown(f"""
    <div class="footer">
        <p style="margin-bottom: 8px;">جميع الحقوق محفوظة © 2026 | الهندسة البرمجية بواسطة <b>Mojtaba Ali</b></p>
        <a class="insta-link" href="https://instagram.com/1jit" target="_blank">📸 Instagram: 1jit</a>
    </div>
""", unsafe_allow_html=True)
