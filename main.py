import streamlit as st

# 🎈 페이지 설정 및 타이틀
st.set_page_config(page_title="배스킨라빈스 키오스크", layout="centered")
st.title("💖 배스킨라빈스 키오스크 (수정 버전) 💖")
st.header("✨ 달콤한 아이스크림을 선택해 주세요! ✨")

# 🍨 아이스크림 용기와 가격 설정
CONTAINER_OPTIONS = {
    "싱글 레귤러 (1가지 맛)": {"scoops": 1, "price": 4200},
    "더블 레귤러 (2가지 맛)": {"scoops": 2, "price": 8200},
    "파인트 (3가지 맛)": {"scoops": 3, "price": 9800},
    "쿼터 (4가지 맛)": {"scoops": 4, "price": 18500},
    "패밀리 (5가지 맛)": {"scoops": 5, "price": 26000},
    "하프갤런 (6가지 맛)": {"scoops": 6, "price": 31500}
}

# 🍦 예시 아이스크림 맛 (실제와 다를 수 있습니다)
FLAVOR_OPTIONS = [
    "민트 초콜릿 칩", "엄마는 외계인", "아몬드 봉봉", "베리베리 스트로베리",
    "사랑에 빠진 딸기", "슈팅스타", "바람과 함께 사라지다", "뉴욕 치즈케이크",
    "월넛", "체리쥬빌레", "피스타치오 아몬드", "초코나무 숲"
]

# --- 1단계: 식사 장소 선택 ---
st.subheader("1️⃣ 드시는 곳을 선택해 주세요.")
eat_place = st.radio(
    "매장에서 드실 건가요, 포장해서 가실 건가요? 🏡",
    ["매장 🍽️", "포장 🎁"],
    index=0,
    horizontal=True
)
st.write(f"👉 선택: **{eat_place}**")

# --- 2단계: 용기 선택 ---
st.subheader("2️⃣ 용기를 선택해 주세요.")
container_names = list(CONTAINER_OPTIONS.keys())
selected_container_name = st.selectbox(
    "원하는 용기 타입을 골라주세요.",
    container_names
)

selected_container_info = CONTAINER_OPTIONS[selected_container_name]
num_scoops = selected_container_info["scoops"]
base_price = selected_container_info["
