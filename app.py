import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Superstore Dashboard",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("train.csv")

        # Convert date columns safely
        df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
        df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

        return df

    except FileNotFoundError:
        st.error("❌ train.csv file not found! Put it in the same folder as app.py")
        st.stop()

df = load_data()

# ---------------- SIDEBAR NAVIGATION ----------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "📊 Sales Analysis", "🌍 Regional Analysis", "📂 Dataset"]
)

# ---------------- HOME PAGE ----------------
if page == "🏠 Home":

    st.title("📊 Superstore Sales Dashboard")
    st.markdown("### Internship Project - Data Analysis using Streamlit")

    total_sales = df["Sales"].sum()
    total_orders = df["Order ID"].nunique()
    total_customers = df["Customer ID"].nunique()

    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
    col2.metric("📦 Total Orders", total_orders)
    col3.metric("👥 Total Customers", total_customers)

# ---------------- SALES ANALYSIS ----------------
elif page == "📊 Sales Analysis":

    st.title("📊 Sales Analysis")

    sales_by_category = df.groupby("Category")["Sales"].sum()

    st.bar_chart(sales_by_category)

# ---------------- REGIONAL ANALYSIS ----------------
elif page == "🌍 Regional Analysis":

    st.title("🌍 Regional Sales Analysis")

    sales_by_region = df.groupby("Region")["Sales"].sum()

    st.bar_chart(sales_by_region)

# ---------------- DATASET PAGE ----------------
elif page == "📂 Dataset":

    st.title("📂 Dataset Preview")

    st.dataframe(df)

    st.write("Shape of dataset:", df.shape)
