import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meridian | E-Portfolio", page_icon="📊", layout="wide")

# Meridian Workforce Intelligence — figures taken from the supplied business-model workbook.
st.markdown("""
<style>
.stApp {background: #f5f7fb;}
.block-container {padding-top: 2rem; padding-bottom: 3rem; max-width: 1180px;}
.hero {background: linear-gradient(115deg,#102a43,#176b87); padding: 30px 34px; border-radius: 18px; color: white; margin-bottom: 18px;}
.hero h1 {color:white; font-size:2.15rem; margin:0 0 8px 0;}
.hero p {color:#e7f4fa; font-size:1.02rem; margin:0;}
.kpi {background:white; border:1px solid #e5eaf1; padding:17px 18px; border-radius:14px; min-height:100px;}
.kpi-label {font-size:.83rem; color:#64748b; margin-bottom:7px;}
.kpi-value {font-size:1.7rem; font-weight:750; color:#102a43;}
.stephead {font-size:1.5rem; font-weight:750; color:#102a43; margin:5px 0 2px;}
.muted {color:#64748b;}
.note {background:#eaf3f8; border-left:4px solid #176b87; padding:12px 15px; border-radius:7px; color:#17324d;}
.formula {background:#fff; border:1px solid #e5eaf1; border-radius:12px; padding:14px 16px; margin:8px 0;}
div[data-testid="stMetric"] {background:white; padding:14px; border:1px solid #e5eaf1; border-radius:12px;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div style="letter-spacing:2px;font-size:.78rem;font-weight:700;color:#a9d7e8;">AS-3 BUSINESS MODEL • E-PORTFOLIO</div>
  <h1>MERIDIAN WORKFORCE INTELLIGENCE</h1>
  <p>The right workforce. The right business decisions.<br>
  An AI-powered platform that forecasts workforce demand, identifies skill gaps and recommends HIRE • RESKILL • REDEPLOY.</p>
  <div style="margin-top:18px;font-size:.9rem;color:#d9edf5;">Presented by <b>Abhinav Sharma</b></div>
</div>
""", unsafe_allow_html=True)

st.markdown("### Explore the project in 3 steps")
step = st.radio(
    "Choose a step",
    ["1 · Problem", "2 · Calculation", "3 · Solution"],
    horizontal=True,
    label_visibility="collapsed"
)
st.divider()

# Core workbook values (₹ crore unless stated otherwise)
revenue = {
    "Basic subscriptions": 30.0,
    "Professional subscriptions": 45.0,
    "Enterprise subscriptions": 15.0,
    "Setup & integration": 8.5,
    "Consulting services": 1.5,
}
expenses = {
    "Employee salaries & benefits": 32.51808,
    "Technology & cloud": 24.0392,
    "Sales & marketing": 5.35,
    "Office & administration": 5.50248,
    "Legal, compliance & other": 4.9114428,
}
departments = pd.DataFrame({
    "Department": ["Engineering & Product", "AI & Data Science", "Sales & Business Development",
                   "Marketing", "Customer Success & Support", "Implementation & Consulting",
                   "HR", "Finance & Legal", "Operations & Admin", "Leadership"],
    "Employees": [55, 25, 35, 12, 35, 20, 6, 5, 5, 4]
})
total_revenue = sum(revenue.values())
total_expenses = sum(expenses.values())
operating_profit = total_revenue - total_expenses
margin = operating_profit / total_revenue
total_people = int(departments["Employees"].sum())

if step.startswith("1"):
    st.markdown('<div class="stephead">Step 1 — Understand the problem</div>', unsafe_allow_html=True)
    st.markdown('<p class="muted">The business need behind Meridian Workforce Intelligence.</p>', unsafe_allow_html=True)

    st.subheader("What is the business problem?")
    st.write(
        "Organisations need to make workforce decisions, but they may not have a clear, forward-looking view "
        "of how many people they need, which skills are missing, or whether they should hire, reskill existing "
        "employees, or redeploy people to other roles. Poor workforce planning can create skill shortages, "
        "extra costs and delays in business delivery."
    )
    st.markdown("#### The central managerial question")
    st.info(
        "How can Meridian build and scale an AI-powered workforce-planning business that helps organisations "
        "predict workforce demand, close skill gaps and make better HIRE, RESKILL or REDEPLOY decisions?"
    )

    st.subheader("Why does this matter?")
    a, b, c = st.columns(3)
    with a:
        st.markdown("**Unclear future demand**")
        st.write("Teams may not know how many people or which capabilities will be needed.")
    with b:
        st.markdown("**Skill gaps**")
        st.write("Existing employees may not have all the skills required for future work.")
    with c:
        st.markdown("**Cost and delivery pressure**")
        st.write("Poor planning can lead to unnecessary hiring, underused talent or delayed projects.")

    st.markdown("#### What Meridian is planning to build")
    st.write(
        "A platform that uses workforce data and AI to forecast demand, identify skill gaps and recommend "
        "the most suitable workforce action. The proposed customers are SMEs, mid-size companies, enterprises "
        "and Global Capability Centres (GCCs)."
    )
    st.markdown('<div class="note"><b>Important:</b> The ₹100 Cr ambition, customer volumes and workforce numbers in this project are planning assumptions from the workbook—not confirmed business results.</div>', unsafe_allow_html=True)

elif step.startswith("2"):
    st.markdown('<div class="stephead">Step 2 — Explain the calculation</div>', unsafe_allow_html=True)
    st.markdown('<p class="muted">The workbook uses a steady-state annual business model. Figures below are in Indian rupees.</p>', unsafe_allow_html=True)

    st.subheader("A. How does the plan reach ₹100 crore?")
    c1, c2, c3 = st.columns(3)
    c1.metric("Annual revenue plan", f"₹{total_revenue:.1f} Cr")
    c2.metric("Planned customers", "850")
    c3.metric("Annual revenue target", "₹100 Cr")
    rev_df = pd.DataFrame({"Revenue stream": list(revenue.keys()), "Revenue (₹ Cr)": list(revenue.values())})
    st.bar_chart(rev_df.set_index("Revenue stream"))
    st.dataframe(rev_df, hide_index=True, use_container_width=True)

    st.markdown("**Subscription calculation**")
    st.markdown("""
    <div class="formula">
    Basic: ₹6 lakh × 500 clients = ₹30 Cr<br>
    Professional: ₹15 lakh × 300 clients = ₹45 Cr<br>
    Enterprise: ₹30 lakh × 50 clients = ₹15 Cr
    </div>
    """, unsafe_allow_html=True)
    st.markdown("**Additional revenue calculation**")
    st.markdown("""
    <div class="formula">
    Setup & integration: ₹8.5 Cr<br>
    Consulting services: ₹1.5 Cr<br>
    <b>Total annual revenue = ₹30 + ₹45 + ₹15 + ₹8.5 + ₹1.5 = ₹100 Cr</b>
    </div>
    """, unsafe_allow_html=True)
    with st.expander("See the customer and service assumptions"):
        st.write("Subscription clients: 500 Basic + 300 Professional + 50 Enterprise = 850 clients.")
        st.write("New setup clients during the year: 100 Basic + 80 Professional + 15 Enterprise.")
        st.write("Consulting uptake: 10% of Basic, 20% of Professional and 50% of Enterprise clients.")

    st.divider()
    st.subheader("B. How is the workforce calculated?")
    p1, p2 = st.columns(2)
    p1.metric("Total planned employees", f"{total_people}")
    p2.metric("Number of functions", "10")
    st.dataframe(departments, hide_index=True, use_container_width=True)
    st.markdown("""
    <div class="formula">
    <b>Annual salary cost formula</b><br>
    Employees × Average monthly salary × 12 months<br><br>
    <b>Total salary and benefits in the workbook = ₹32.52 Cr</b><br>
    This includes the proposed 12% benefits and on-cost allowance.
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.subheader("C. How are operating costs and profit calculated?")
    exp_df = pd.DataFrame({"Cost category": list(expenses.keys()), "Annual cost (₹ Cr)": list(expenses.values())})
    st.bar_chart(exp_df.set_index("Cost category"))
    st.dataframe(exp_df, hide_index=True, use_container_width=True)
    m1, m2, m3 = st.columns(3)
    m1.metric("Operating expenses", f"₹{total_expenses:.2f} Cr")
    m2.metric("Operating profit", f"₹{operating_profit:.2f} Cr")
    m3.metric("Operating profit margin", f"{margin:.1%}")
    st.markdown(f"""
    <div class="formula">
    <b>Operating profit = Revenue − Operating expenses</b><br>
    ₹100 Cr − ₹{total_expenses:.2f} Cr = <b>₹{operating_profit:.2f} Cr</b><br><br>
    <b>Operating profit margin = Operating profit ÷ Revenue × 100</b><br>
    ₹{operating_profit:.2f} Cr ÷ ₹100 Cr × 100 = <b>{margin:.2%}</b>
    </div>
    """, unsafe_allow_html=True)
    st.caption("Operating profit is before depreciation, interest and income tax. Values are based on the workbook's planning assumptions and rounded for display.")

elif step.startswith("3"):
    st.markdown('<div class="stephead">Step 3 — Present the solution</div>', unsafe_allow_html=True)
    st.markdown('<p class="muted">The proposed business model, workforce structure and HR practices.</p>', unsafe_allow_html=True)

    st.subheader("1. The business solution")
    st.write(
        "Meridian will offer three annual subscription plans—Basic, Professional and Enterprise—"
        "along with setup and integration services and optional consulting. This creates recurring "
        "subscription revenue with additional income from implementation and advisory work."
    )
    plans = pd.DataFrame({
        "Plan": ["Basic", "Professional", "Enterprise"],
        "Target customer": ["Small companies", "Mid-size companies", "Large enterprises & GCCs"],
        "Annual price": ["₹6 lakh", "₹15 lakh", "₹30 lakh"],
        "Planned clients": [500, 300, 50],
    })
    st.dataframe(plans, hide_index=True, use_container_width=True)

    st.subheader("2. The people solution")
    st.write(
        "The proposed structure has 202 employees across 10 functions. The HR team has 6 people, "
        "with the HR Lead coordinating hiring, capability development, performance and employee experience."
    )
    st.markdown("**Employee lifecycle proposed for Meridian**")
    stages = [
        ("Attract", "Build employer brand and clear role profiles; use referrals and campus hiring."),
        ("Screen & assess", "Use role criteria, work samples and knowledge, skills and abilities."),
        ("Select & onboard", "Use structured interviews, scorecards, references and 30/60/90-day goals."),
        ("Perform & develop", "Set clear KPIs, provide feedback, learning paths and internal mobility."),
        ("Reward & retain", "Offer fair pay, recognition, wellbeing support and career growth.")
    ]
    for title, desc in stages:
        with st.container(border=True):
            st.markdown(f"**{title}**")
            st.write(desc)

    st.subheader("3. Example role: Sales & Business Development Manager")
    x, y, z = st.columns(3)
    with x:
        st.markdown("**KRA — What the role owns**")
        st.write("Build pipeline; win and grow accounts; negotiate contracts; hand clients to delivery.")
    with y:
        st.markdown("**KPI — How success is measured**")
        st.write("Qualified pipeline value; conversion rate; new annual contract value; client renewals.")
    with z:
        st.markdown("**KSA — Capabilities required**")
        st.write("Workforce-planning and SaaS knowledge; consultative selling, negotiation and CRM skills; trust-building and coordination abilities.")

    st.subheader("Project outcome")
    o1, o2, o3 = st.columns(3)
    o1.metric("Revenue ambition", "₹100 Cr")
    o2.metric("Planned workforce", "202 people")
    o3.metric("Operating margin plan", f"{margin:.1%}")
    st.success(
        "Meridian's proposed solution connects the business model with workforce planning: "
        "the right roles, the right skills and a clear employee lifecycle to support the growth ambition."
    )
    st.markdown('<div class="note"><b>Validation before implementation:</b> Meridian should test customer demand, willingness to pay, hiring timelines, salary benchmarks, cloud usage and office costs before treating these estimates as commitments.</div>', unsafe_allow_html=True)

st.divider()
st.caption("Source: Abhinav Sharma AS-3 presentation and Meridian Workforce Intelligence business-model Excel workbook. All financial and headcount figures are proposed planning assumptions.")
