import streamlit as st

# 🎈 페이지 설정 및 타이틀
st.set_page_config(page_title="배스킨라빈스 키오스크", layout="centered")
st.title("💖 배스킨라빈스 키오스크 (최종 수정) 💖")
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

# 🍦 예시 아이스크림 맛
FLAVOR_OPTIONS = [
    "민트 초콜릿 칩", "엄마는 외계인", "아몬드 봉봉", "베리베리 스트로베리",
    "사랑에 빠진 딸기", "슈팅스타", "바람과 함께 사라지다", "뉴욕 치즈케이크",
    "월넛", "체리쥬빌레", "피스타치오 아몬드", "초코나무 숲"
]

# --- 세션 상태 초기화 (KeyError 방지) ---
if 'selected_flavors' not in st.session_state:
    st.session_state.selected_flavors = {}

# --- 1단계: 식사 장소 선택 ---
st.subheader("1️⃣ 드시는 곳을 선택해 주세요.")
eat_place = st.radio(
    "매장에서 드실 건가요, 포장해서 가실 건가요? 🏡",
    ["매장 🍽️", "포장 🎁"],
    index=0,
    horizontal=True,
    key="eat_place"
)
st.write(f"👉 선택: **{eat_place}**")

# --- 2단계: 용기 선택 ---
st.subheader("2️⃣ 용기를 선택해 주세요.")
container_names = list(CONTAINER_OPTIONS.keys())

# 용기 선택 시 세션 상태의 맛 선택 내용을 초기화하는 콜백 함수
def reset_flavors():
    st.session_state.selected_flavors = {}
    st.session_state.num_scoops = CONTAINER_OPTIONS[st.session_state.container_select]["scoops"]

selected_container_name = st.selectbox(
    "원하는 용기 타입을 골라주세요.",
    container_names,
    key="container_select",
    on_change=reset_flavors # 용기 변경 시 맛 초기화
)

selected_container_info = CONTAINER_OPTIONS[selected_container_name]
num_scoops = selected_container_info["scoops"]
base_price = selected_container_info["price"]
st.session_state.num_scoops = num_scoops # 세션 상태에 맛 개수 저장

st.info(
    f"🎉 **{selected_container_name}**를 선택하셨어요! "
    f"**총 {num_scoops}가지 맛**을 고르실 수 있으며, 기본 가격은 **{base_price:,}원**입니다."
)

# --- 3단계: 아이스크림 맛 선택 ---
st.subheader(f"3️⃣ 아이스크림 맛을 {num_scoops}가지 골라주세요. 🥳")

# 세션 상태에 저장된 맛을 기반으로 현재 선택된 맛 목록 재구성
current_flavors = [
    st.session_state.selected_flavors.get(f"flavor_select_{i}") 
    for i in range(num_scoops) 
    if st.session_state.selected_flavors.get(f"flavor_select_{i}") and st.session_state.selected_flavors.get(f"flavor_select_{i}") != "맛을 선택해 주세요"
]

# 용기에 맞는 개수만큼 맛을 선택할 수 있도록 반복
for i in range(num_scoops):
    # 기본값 설정: 세션 상태에 저장된 값이 있으면 그 값을 사용, 없으면 "맛을 선택해 주세요" 사용
    default_flavor = st.session_state.selected_flavors.get(f"flavor_select_{i}", "맛을 선택해 주세요")
    
    # 선택 박스
    flavor = st.selectbox(
        f"**{i+1}번째** 맛 선택:",
        ["맛을 선택해 주세요"] + FLAVOR_OPTIONS, 
        index=(FLAVOR_OPTIONS.index(default_flavor) + 1 if default_flavor in FLAVOR_OPTIONS else 0),
        key=f"flavor_select_{i}" # 고유 키
    )
    
    # 선택된 맛을 세션 상태에 저장
    st.session_state.selected_flavors[f"flavor_select_{i}"] = flavor

    # 현재 선택된 맛 목록 업데이트
    if flavor != "맛을 선택해 주세요":
        # 현재 선택된 맛 목록에 해당 맛이 아직 없으면 추가 (중복 방지를 위해 Set/List 관리는 복잡하므로 여기서는 간단히 처리)
        pass 

# 최종적으로 선택된 맛만 추출
selected_flavors_list = [
    st.session_state.selected_flavors[f"flavor_select_{i}"] 
    for i in range(num_scoops) 
    if st.session_state.selected_flavors.get(f"flavor_select_{i}") != "맛을 선택해 주세요"
]

# 선택된 맛 목록 보여주기
if selected_flavors_list:
    st.markdown("---")
    st.subheader("✔️ 선택하신 맛 목록")
    st.write(f"총 **{len(selected_flavors_list)} / {num_scoops}가지** 맛을 선택하셨습니다.")
    flavor_list_markdown = ""
    for idx, flavor in enumerate(selected_flavors_list):
        flavor_list_markdown += f"* **{idx+1}**. {flavor} 😋\n"
    st.markdown(flavor_list_markdown)


# --- 4단계: 주문 내역 및 결제 선택 ---
st.markdown("---")
st.subheader("4️⃣ 주문 확인 및 결제 방법을 선택해 주세요! 💳")

# 주문 내역 요약 및 결제 활성화 조건 체크
if len(selected_flavors_list) == num_scoops:
    total_price = base_price
    
    st.success("✅ 맛 선택이 완료되었습니다!")
    st.subheader(f"💰 총 결제 금액: **{total_price:,}원**")
    
    st.markdown("""
    ### 📝 주문 상세 내역
    * **장소**: {eat_place}
    * **용기**: {selected_container_name}
    * **맛 개수**: {num_scoops}가지
    * **선택된 맛**: {selected_flavors_str}
    * **총 금액**: {total_price:,}원
    """.format(
        eat_place=eat_place,
        selected_container_name=selected_container_name,
        num_scoops=num_scoops,
        selected_flavors_str=', '.join(selected_flavors_list),
        total_price=total_price
    ))
    
    # 결제 수단 선택
    st.subheader("어떤 방법으로 결제하시겠어요?")
    
    payment_method = st.radio(
        "결제 수단:",
        ["카드 결제 💳", "현금 결제 💵", "기프티콘/상품권 🎁"],
        index=0,
        horizontal=True,
        key="payment_select"
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
    st.warning(f"⚠️ 아이스크림 맛을 **{num_scoops}가지** 모두 선택해 주세요. (현재 {len(selected_flavors_list)}가지 선택)")


# --- 친절한 마무리 인사 ---
st.sidebar.title("💁‍♀️ 키오스크 안내")
st.sidebar.sidebar.info("이 코드는 Streamlit 기본 기능만을 활용하여 제작되었습니다. 실제 결제 기능은 포함되어 있지 않은 시뮬레이션입니다.")
