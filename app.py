import streamlit as st

# 1. إعدادات الصفحة الفخمة والكلاس باسمك
st.set_page_config(
    page_title="Mojtaba Ali - Financial Smart System",
    page_icon="👑",
    layout="centered"
)

# تصميم الألوان والـ Styling الفخم (Dark Mode مع ذهبي ملكي وأزرق كلاس)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #D4AF37; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; font-weight: bold; }
    h3 { color: #4A90E2; }
    .stNumberInput div div input { background-color: #1f293d !important; color: white !important; border: 1px solid #D4AF37 !important; }
    .stTextInput div div input { background-color: #1f293d !important; color: white !important; border: 1px solid #4A90E2 !important; }
    .css-1kyx60b { background-color: #1a2238; border-radius: 15px; padding: 20px; border: 1px solid #334155; }
    .footer { text-align: center; color: #888; font-size: 14px; margin-top: 50px; border-top: 1px solid #334155; padding-top: 20px; }
    .insta-btn { display: block; text-align: center; background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); color: white !important; padding: 10px; border-radius: 8px; text-decoration: none; font-weight: bold; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# 2. الهيدر الفخم
st.markdown("<h1>👑 الميزان الذكي لإدارة الأموال 👑</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa; font-style: italic;'>نظام مالي ذكي ومطور حصرياً بواسطة Mojtaba Ali</p>", unsafe_allow_html=True)
st.markdown("---")

# 3. مدخلات المستخدم (الراتب الأساسي)
st.subheader("💰 الخطوة الأولى: أدخل رأس المال")
salary = st.number_input("الراتب الشهري الحالي (دينار عراقي):", min_value=0, value=500000, step=25000)

# 4. الحسبة الصارمة (الادخار والاستثمار)
saving_ratio = 0.15      # 15% ادخار مقدّس
invest_ratio = 0.15      # 15% استثمار ذكي

savings = salary * saving_ratio
investment = salary * invest_ratio
free_cash = salary - (savings + investment)

# 5. ميزة الأزرار والمصاريف المتغيرة ديناميكياً
st.markdown("---")
st.subheader("📝 الخطوة الثانية: المصاريف الإضافية (الضرائب، النت، الإيجار...) ")

if 'expenses' not in st.session_state:
    st.session_state.expenses = {}

col1, col2 = st.columns(2)
with col1:
    exp_name = st.text_input("اسم المصروف الجديد (مثال: ضرائب):", key="new_exp_name")
with col2:
    exp_val = st.number_input("المبلغ (دينار):", min_value=0, value=0, step=5000, key="new_exp_val")

if st.button("➕ إضافة المصروف فوراً ونظام الحساب الذكي"):
    if exp_name and exp_val > 0:
        st.session_state.expenses[exp_name] = exp_val
        st.success(f"تم إضافة {exp_name} بنجاح!")

total_added_expenses = 0
if st.session_state.expenses:
    st.markdown("### 📋 المصاريف التي تم تسجيلها هذا الشهر:")
    for name, val in list(st.session_state.expenses.items()):
        st.write(f"🔹 **{name}**: {val:,} دينار")
        total_added_expenses += val
    if st.button("🗑️ تفريغ كافة المصاريف والبدء من جديد"):
        st.session_state.expenses = {}
        st.rerun()

# 6. التعديل الذكي تلقائياً
final_free_cash = free_cash - total_added_expenses

# 7. لوحة عرض النتائج الفخمة (Dashboard)
st.markdown("---")
st.markdown("### 📊 التقرير المالي النهائي الحاسم")

c1, c2 = st.columns(2)
with c1:
    st.info(f"🔒 **مبلغ الادخار المقفل (15%):**\n### {savings:,} دينار")
with c2:
    st.warning(f"📈 **مبلغ الاستثمار المقفل (15%):**\n### {investment:,} دينار")

st.markdown("### 💸 الفلوس الزايدة المتاحة الك للصرف والوناسة بكل حرية:")
if final_free_cash >= 0:
    st.success(f"## {final_free_cash:,} دينار عراقي")
    st.caption("✅ جميع حصص الادخار والاستثمار مؤمنة بالكامل في الخزنة الحصينة.")
else:
    st.error(f"## {final_free_cash:,} دينار عراقي (بالسالب!)")
    st.markdown("⚠️ **تنبيه ذكي من النظام:** مصاريفك الإضافية بلعت الفلوس الزايدة ودخلت على الخط الأحمر! يرجى مراجعة الصرف الحر فوراً.")

# 8. الفوتر الفخم بإمضاء الحقوق لك وزر الانستغرام
st.markdown(f"""
    <div class="footer">
        <p>جميع الحقوق محفوظة © 2026 | تطوير وإشراف: <b>Mojtaba Ali</b></p>
        <p style='font-size: 12px; color:#aaa;'>للتواصل والمتابعة عبر المطور:</p>
        <a class="insta-btn" href="https://instagram.com" target="_blank">📸 تابعني على انستغرام</a>
    </div>
""", unsafe_allow_html=True)
