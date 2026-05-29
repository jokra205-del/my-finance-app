import streamlit as st
import re

# 1. إعدادات الصفحة الكلاس والملكية
st.set_page_config(
    page_title="Mojtaba Ali | Financial Intelligence",
    page_icon="👑",
    layout="centered"
)

# تصميم الواجهة بالألوان الملكية الفاخرة (Dark Obsidian & Matte Gold)
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
    
    /* كروت عرض التقارير المالية بنظام الأغنياء الكلاس */
    .report-card-needs { background: rgba(59, 130, 246, 0.08); border: 1px solid #3b82f6; border-radius: 12px; padding: 22px; text-align: center; }
    .report-card-future { background: rgba(16, 185, 129, 0.08); border: 1px solid #10b981; border-radius: 12px; padding: 22px; text-align: center; }
    .report-card-wants { background: rgba(212, 175, 55, 0.08); border: 1px solid #D4AF37; border-radius: 12px; padding: 28px; text-align: center; margin-top: 18px; }
    
    /* فوتر مخصص على اليسار بالكامل جوة */
    .footer-left { text-align: left; direction: ltr; color: #778899; font-size: 13px; margin-top: 60px; border-top: 1px solid #1c2333; padding-top: 25px; padding-left: 10px; }
    </style>
""", unsafe_allow_html=True)

# الهيدر الملكي الكلاس
st.markdown("<div class='royal-title'>الميزان الذكي لإدارة الثروات</div>", unsafe_allow_html=True)
st.markdown("<div class='royal-subtitle'>منظومة مالية مؤتمتة وحاسمة بمفهوم الثراء العالمي 50-30-20</div>", unsafe_allow_html=True)

# إدارة حالة التنقل (Wizard Steps)
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'expenses' not in st.session_state:
    st.session_state.expenses = {}

# اختيارات العملة المدعومة ملكياً
currency_type = st.radio("اختر عملة النظام المالي للحساب:", ["دينار عراقي (IQD)", "دولار أمريكي ($)"], horizontal=True)
symbol = "د.ع" if "دينار" in currency_type else "$"

st.markdown("---")

# دالة ذكية لاستخراج الأرقام من النصوص العربية والانكليزية لضمان عدم حدوث خطأ
def extract_amount_from_text(text):
    numbers = re.findall(r'\d[\d,]*', text)
    if numbers:
        return int(numbers[0].replace(',', ''))
    return None

# ==================== 🌟 المرحلة الأولى: إدخال رأس المال ====================
if st.session_state.step == 1:
    st.markdown("### 📥 إيداع رأس المال الإجمالي")
    
    # ضبط القيم التلقائية الفخمة حسب طلبك (100,000 للدينار و 100 للدولار)
    if symbol == "د.ع":
        default_val = 100000
        step_val = 25000
    else:
        default_val = 100
        step_val = 10
        
    st.session_state.salary = st.number_input(f"أدخل قيمة رأس المال الحالي المستهدف ({symbol}):", min_value=0, value=default_val, step=step_val)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("التالي: كشف الالتزامات والضرائب ➡️"):
        st.session_state.step = 2
        st.rerun()

# ==================== 🌟 المرحلة الثانية: إضافة الالتزامات والمصاريف ====================
elif st.session_state.step == 2:
    st.markdown("### 📝 بيان الالتزامات الثابتة (نت، ضرائب، إيجار...)")
    st.caption("أكتب براحتك بالعربي، السيستم ذكي جداً وسيستخرج الأرقام تلقائياً (مثال: 'نت 50000' أو 'ضرائب 40 دولار').")
    
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

# ==================== 🌟 المرحلة الثالثة: التقرير المالي الحاسم بطريقة الأغنياء ====================
elif st.session_state.step == 3:
    st.markdown("### 📊 التقرير المالي النهائي الحاسم")
    
    # العمليات الحسابية الكلاس الصافية
    salary = st.session_state.salary
    
    # 20% للمستقبل وبناء الأصول (ثابتة ومحمية فوراً)
    future_growth = salary * 0.20
    
    # 50% للالتزامات
    total_added_expenses = sum(st.session_state.expenses.values())
    
    # 30% لصافي الأرباح والرفاهية الحرة
    allowed_wants = salary * 0.30
    
    # حساب المتبقي الحقيقي للرفاهية
    final_free_cash = allowed_wants - total_added_expenses
    
    # عرض الكروت بلغة الملوك والأغنياء
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
            <div class="report-card-needs">
                <span style="color:#3b82f6; font-weight:bold; font-size:13px;">📋 ميزانية إدارة الالتزامات (50%)</span>
                <p style="color:#8a9ab0; margin:5px 0 0 0; font-size:11px;">الحد الأقصى المسموح: {salary * 0.50:,} {symbol}</p>
                <h3 style="color:#fff; margin:5px 0 0 0;">المجموع الفعلي: {total_added_expenses:,} {symbol}</h3>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
            <div class="report-card-future">
                <span style="color:#10b981; font-weight:bold; font-size:13px;">🔒 خزنة الأصول وبناء الثروة (20%)</span>
                <p style="color:#8a9ab0; margin:5px 0 0 0; font-size:11px;">(حصة الادخار والاستثمار المقفلة)</p>
                <h3 style="color:#fff; margin:5px 0 0 0;">{future_growth:,} {symbol}</h3>
            </div>
        """, unsafe_allow_html=True)
        
    # تفصيل الالتزامات والضرائب بالكامل
    if st.session_state.expenses:
        with st.expander("📋 استعراض كشف الالتزامات المفصل"):
            for name, val in st.session_state.expenses.items():
                st.write(f"🔹 **{name}**: {val:,} {symbol}")
        
    # عرض صافي الأرباح المتاحة للصرف الحر والوناسة
    st.markdown(f"""
        <div class="report-card-wants">
            <span style="color:#D4AF37; font-weight:bold; font-size:16px;">💸 صافي الأرباح والرفاهية الحرة (حصة الـ 30%)</span>
            <h1 style="color:#fff; margin:15px 0 0 0;">{final_free_cash:,} {symbol}</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # التوجيه الاستراتيجي الفخم
    st.markdown("<br>", unsafe_allow_html=True)
    if final_free_cash >= 0:
        st.success("✅ الإستراتيجية المالية مستقرة وضمن نطاق الثراء الحصين. الأصول والمدخرات مؤمنة بالكامل.")
    else:
        st.error("⚠️ تنبيه مالي حرج: الالتزامات تجاوزت النطاق الآمن وتأكل من حصة أرباحك الحرة! يرجى مراجعة المصاريف لتجنب العجز.")
        
    if st.button("🔄 بناء ميزانية مالية جديدة"):
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
