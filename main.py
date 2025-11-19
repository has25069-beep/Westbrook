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
base_price = selected_container_info["price"]

st.info(
    f"🎉 **{selected_container_name}**를 선택하셨어요! "
    f"**총 {num_scoops}가지 맛**을 고르실 수 있으며, 기본 가격은 **{base_price:,}원**입니다."
)

# --- 3단계: 아이스크림 맛 선택 ---
st.subheader(f"3️⃣ 아이스크림 맛을 {num_scoops}가지 골라주세요. 🥳")

selected_flavors = []
# 용기에 맞는 개수만큼 맛을 선택할 수 있도록 반복
for i in range(num_scoops):
    # 키를 고유하게 만들어줘야 Streamlit이 오류 없이 처리합니다.
    flavor = st.selectbox(
        f"**{i+1}번째** 맛 선택:",
        ["맛을 선택해 주세요"] + FLAVOR_OPTIONS, # 첫번째 옵션으로 선택 유도
        key=f"flavor_select_{i}" # 고유 키
    )
    if flavor != "맛을 선택해 주세요":
        selected_flavors.append(flavor)

# 선택된 맛 목록 보여주기
if selected_flavors:
    st.markdown("---")
    st.subheader("✔️ 선택하신 맛 목록")
    st.write(f"총 **{len(selected_flavors)} / {num_scoops}가지** 맛을 선택하셨습니다.")
    flavor_list_markdown = ""
    for idx, flavor in enumerate(selected_flavors):
        flavor_list_markdown += f"* **{idx+1}**. {flavor} 😋\n"
    st.markdown(flavor_list_markdown)

# --- 4단계: 주문 내역 및 결제 선택 ---
st.markdown("---")
st.subheader("4️⃣ 주문 확인 및 결제 방법을 선택해 주세요! 💳")

# 주문 내역 요약 및 결제 활성화 조건 체크
if len(selected_flavors) == num_scoops:
    total_price = base_price # 현재는 추가 옵션이 없으므로 기본 가격이 총 가격입니다.
    
    st.success("✅ 맛 선택이 완료되었습니다!")
    st.subheader(f"💰 총 결제 금액: **{total_price:,}원**")
    
    st.markdown("""
    ### 📝 주문 상세 내역
    * **장소**: {eat_place}
    * **용기**: {selected_container_name}
    * **맛 개수**: {num_scoops}가지
    * **선택된 맛**: {', '.join(selected_flavors)}
    * **총 금액**: {total_price:,}원
    """.format(
        eat_place=eat_place,
        selected_container_name=selected_container_name,
        num_scoops=num_scoops,
        selected_flavors=selected_flavors,
        total_price=total_price
    ))
    
    # **결제 수단 선택 (수정된 부분)**
    st.subheader("어떤 방법으로 결제하시겠어요?")
    
    # 라디오 버튼 변수 이름을 고유하게 설정하여 오류 방지
    payment_method = st.radio(
        "결제 수단:",
        ["카드 결제 💳", "현금 결제 💵", "기프티콘/상품권 🎁"],
        index=0,
        horizontal=True
    )
    
    # 결제 버튼
    if st.button("결제하기 🚀"):
        st.balloons()
        st.success(
            f"**{selected_container_name}** **{total_price:,}원**에 대한 "
            f"**{payment_method}**가 완료되었습니다. 감사합니다! 😊"
        )
        st.write("잠시 후 주문 번호가 호출됩니다. 맛있게 드세요! 🙏")

else:
    st.warning(f"⚠️ 아이스크림 맛을 **{num_scoops}가지** 모두 선택해 주세요. (현재 {len(selected_flavors)}가지 선택)")


# --- 친절한 마무리 인사 ---
st.sidebar.title("💁‍♀️ 키오스크 안내")
st.sidebar.info("이 코드는 Streamlit 기본 기능만을 활용하여 제작되었습니다. 실제 결제 기능은 포함되어 있지 않은 시뮬레이션입니다.")
