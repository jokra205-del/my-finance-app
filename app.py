import streamlit as st
import json

# 1. إعدادات الصفحة الفخمة الملكية
st.set_page_config(
    page_title="Mojtaba Ali | Financial Intelligence",
    page_icon="👑",
    layout="wide"  # تحويل العرض إلى واسع ليناسب التقسيم اليمين واليسار
)

# تصميم الواجهة الكلاس بالألوان الفخمة والكروت العمودية الواضحة جداً
st.markdown("""
    <style>
    /* الخلفية العامة */
    .main { background-color: #0b0d12; }
    
    /* الهيدر الملكي */
    .royal-title { color: #D4AF37; font-family: 'Segoe UI', sans-serif; text-align: center; font-weight: 800; font-size: 36px; letter-spacing: 1px; margin-bottom: 5px; }
    .royal-subtitle { text-align: center; color: #8a9ab0; font-size: 16px; margin-bottom: 30px; }
    
    /* لوحة الشرح الترحيبية في البداية */
    .welcome-box { background: rgba(212, 175, 55, 0.05); border: 1px solid #D4AF37; border-radius: 12px; padding: 20px; margin-bottom: 25px; text-align: right; }
    .welcome-title { color: #D4AF37; font-size: 20px; font-weight: bold; margin-bottom: 10px; display: block; }
    .welcome-text { color: #c4d1e6; font-size: 15px; line-height: 1.6; }
    
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
    
    .card-title { font-size: 19px; font-weight: bold; color: #ffffff; margin-bottom: 8px; display: block; }
    .card-value { font-size: 42px; font-weight: 800; color: #ffffff; margin: 0; }
    
    /* تفاصيل الالتزامات داخل المربع الأحمر */
    .tax-detail-item { font-size: 18px; color: #ffb3b3; margin: 8px 0; font-weight: bold; }
    
    /* صندوق التقرير التفاعلي والمصاريف */
    .action-box { background-color: #131722; border: 2px solid #2a3142; border-radius: 12px; padding: 25px; margin-bottom: 20px; }
    .action-title { color: #D4AF37; font-size: 22px; font-weight: bold; margin-bottom: 15px; display: block; text-align: center; border-bottom: 1px solid #2a3142; padding-bottom: 10px; }
    
    /* فوتر مخصص على اليسار بالكامل */
    .footer-left { text-align: left; direction: ltr; color: #778899; font-size: 13px; margin-top: 60px; border-top: 1px solid #1c2333; padding-top: 25px; padding-left: 10px; }
    </style>
""", unsafe_allow_html=True)

# الهيدر الأساسي للموقع
st.markdown("<div class='royal-title'>الميزان الذكي لإدارة الثروات</div>", unsafe_allow_html=True)
st.markdown("<div class='royal-subtitle'>منظومة مالية مؤتمتة وحاسمة بمفهوم الثراء العالمي 50-30-20</div>", unsafe_allow_html=True)

# ==================== 🧠 مكون الحفظ الذكي في المتصفح LocalStorage ====================
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
    # 👑 إضافة اللوحة الترحيبية الشارحة للنظام بالبداية
    st.markdown("""
        <div class="welcome-box">
            <span class="welcome-title">👑 أهلاً بك في منظومة الذكاء المالي التراكمية</span>
            <p class="welcome-text">
                هذا النظام مصمم لإدارة ثروتك بشكل ذكي ومحفوظ بالكامل <b>على جهازك الشخصي</b> دون الحاجة لسيرفرات للحفاظ على الخصوصية.<br>
                <b>كيف يعمل النظام؟</b><br>
                1. تقوم بإدخال رأس المال والضرائب ليتم تقسيم الصافي فوراً حسب قاعدة الأغنياء المرنة (20% ادخار، 30% استثمار، 50% رفاهية حرة).<br>
                2. ستحصل على <b>لوحة تحكم تفاعلية ذكية</b> تمكنك من إيداع أموال جديدة في أي وقت ليتم دمجها تراكمياً مع المبالغ السابقة، بالإضافة لخصم مصاريفك اليومية وإصدار تقارير حاسمة لاستهلاكك أولاً بأول!
            </p>
        </div>
    """, unsafe_allow_html=True)

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
    
    total_taxes = float(sum([item['value'] for item in expenses_list]))
    remaining_net = max(0.0, salary - total_taxes)
    
    # الحساب الأولي الأساسي للـ Session الأول فقط
    if not st.session_state.wallet_initialized:
        st.session_state.accumulated_savings = remaining_net * 0.20
        st.session_state.accumulated_investment = remaining_net * 0.30
        st.session_state.accumulated_wants = remaining_net * 0.50
        st.session_state.wallet_initialized = True

    # ----------- 📊 عرض الثلاث خزن الأساسية في الأعلى بشكل واضح وجذاب -----------
    col_card1, col_card2, col_card3 = st.columns(3)
    
    with col_card1:
        st.markdown(f"""
            <div class="vertical-card card-save">
                <span class="card-title">💰 حصالة الادخار الملكية (20%)</span>
                <p class="card-value">{st.session_state.accumulated_savings:,.2f} {symbol}</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col_card2:
        st.markdown(f"""
            <div class="vertical-card card-invest">
                <span class="card-title">📈 خزنة الاستثمار والأصول (30%)</span>
                <p class="card-value">{st.session_state.accumulated_investment:,.2f} {symbol}</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col_card3:
        st.markdown(f"""
            <div class="vertical-card card-wants">
                <span class="card-title">💸 صافي الرفاهية الحرة (50%)</span>
                <p class="card-value" style="color:#D4AF37;">{st.session_state.accumulated_wants:,.2f} {symbol}</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 🔀 تقسيم الصفحة الأخيرة: اليمين لوحة التحكم الذكية، واليسار مربع الضرائب والالتزامات
    col_right_panel, col_left_panel = st.columns([1.3, 1])  # جهة اليمين أعرض قليلاً للتحكم والتفاعل

    # ==================== ➡️ جهة اليمين: لوحة التحكم التفاعلية الذكية (إيداع وصرف) ====================
    with col_right_panel:
        st.markdown("<div class='action-box'>", unsafe_allow_html=True)
        st.markdown("<span class='action-title'>⚡ لوحة التحكم التفاعلية الذكية</span>", unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["💵 إيداع أموال جديدة", "📉 تسجيل حركة صرف", "📜 تقرير السجل المالي"])
        
        with tab1:
            st.write("كلما تجيك فلوس جديدة، اكتبها هنا وراح تتقسم تلقائياً وتتزود على الخزن الفوق بدون ما تمسح القديم!")
            new_deposit = st.number_input(f"المبلغ المراد إيداعه وتوزيعه ({symbol}):", min_value=0.0, step=10.0, key="dep_input")
            if st.button("تأكيد الإيداع الحواري ودمجه بالمحفظة 📥"):
                if new_deposit > 0:
                    st.session_state.accumulated_savings += new_deposit * 0.20
                    st.session_state.accumulated_investment += new_deposit * 0.30
                    st.session_state.accumulated_wants += new_deposit * 0.50
                    
                    st.session_state.expense_log.insert(0, f"📥 تم إيداع {new_deposit:,} {symbol} وتوزيعها بنجاح.")
                    
                    ايداع_وحفظ_بالجهاز("mojtaba_wallet", {
                        "save": st.session_state.accumulated_savings,
                        "invest": st.session_state.accumulated_investment,
                        "wants": st.session_state.accumulated_wants
                    })
                    st.success("تمت إضافة المبلغ وتحديث الصناديق الفوق فوراً بنجاح!")
                    st.rerun()

        with tab2:
            st.write("اكتب شكد صرفت فلوس وحدد من أي صندوق تريد تطرحها حتى تسوي تقرير حاسم للاستهلاك:")
            expense_amount = st.number_input(f"المبلغ المصروف ({symbol}):", min_value=0.0, step=10.0, key="exp_input")
            target_fund = st.selectbox("اصرف هذا المبلغ من قسم:", ["💸 صافي الأرباح للرفاهية الحرة", "💰 حصالة الادخار الملكية", "📈 خزنة الاستثمار والأصول"])
            
            if st.button("تحديث وخصم المصاريف فوراً 📉"):
                if expense_amount > 0:
                    if target_fund == "💸 صافي الأرباح للرفاهية الحرة":
                        st.session_state.accumulated_wants -= expense_amount
                        fund_name = "الرفاهية"
                    elif target_fund == "💰 حصالة الادخار الملكية":
                        st.session_state.accumulated_savings -= expense_amount
                        fund_name = "الادخار"
                    else:
                        st.session_state.accumulated_investment -= expense_amount
                        fund_name = "الاستثمار"
                    
                    st.session_state.expense_log.insert(0, f"📉 تم صرف {expense_amount:,} {symbol} من قسم {fund_name}.")
                    
                    ايداع_وحفظ_بالجهاز("mojtaba_wallet", {
                        "save": st.session_state.accumulated_savings,
                        "invest": st.session_state.accumulated_investment,
                        "wants": st.session_state.accumulated_wants
                    })
                    st.warning(f"تم خصم {expense_amount} من حساب {fund_name} وتحديث التقرير الحاسم!")
                    st.rerun()
                    
        with tab3:
            st.write("📋 سجل حركات حسابك التراكمي الحاسم:")
            if st.session_state.expense_log:
                for log in st.session_state.expense_log:
                    st.markdown(f"<p style='color:#8a9ab0; font-weight:bold; margin:5px 0;'>{log}</p>", unsafe_allow_html=True)
            else:
                st.caption("السجل فارغ حالياً، لم يتم إجراء عمليات إيداع أو صرف بعد.")
                
        st.markdown("</div>", unsafe_allow_html=True)

    # ==================== ⬅️ جهة اليسار: مجموع كافة الضرائب والالتزامات التفصيلية ====================
    with col_left_panel:
        tax_items_html = ""
        if expenses_list:
            for item in expenses_list:
                tax_items_html += f"<div class='tax-detail-item'>🔸 {item['name']}: {item['value']:,} {symbol}</div>"
        else:
            tax_items_html = "<div class='tax-detail-item'>لا توجد ضرائب أو التزامات مضافة</div>"
            
        st.markdown(f"""
            <div class="vertical-card card-tax" style="height: 100%; min-height: 380px;">
                <span class="card-title">🛑 مجموع الضرائب والالتزامات الثابتة</span>
                <p class="card-value" style="margin-bottom: 20px; color: #ff4b4b;">{total_taxes:,} {symbol}</p>
                <div style="text-align: right; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 15px;">
                    <p style="color: #8a9ab0; font-size: 14px; margin-bottom: 10px;">تفاصيل بنود الاستهلاك الثابتة:</p>
                    {tax_items_html}
                </div>
            </div>
        """, unsafe_allow_html=True)

    # زر إعادة البدء وتصفير المحفظة بالكامل أسفل الصفحة
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🔄 تصفير المحفظة وإعادة حساب ميزانية جديدة بالكامل"):
        st.session_state.step = 1
        st.session_state.num_expenses = 1
        st.session_state.wallet_initialized = False
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
