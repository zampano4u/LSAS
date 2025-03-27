import streamlit as st

performance_items = [1, 2, 3, 4, 6, 8, 9, 13, 14, 16, 17, 20, 21]
social_items = [5, 7, 10, 11, 12, 15, 18, 19, 22, 23, 24]

questions = {
    1: "공공장소에서 전화 걸기",
    2: "소규모 그룹 활동에 참여하기",
    3: "공공장소에서 음식 먹기",
    4: "공공장소에서 타인과 술 마시기",
    5: "권위자와 대화하기",
    6: "청중 앞에서 연기하거나 발표하기",
    7: "파티에 가기",
    8: "타인이 관찰하는 상황에서 일하기",
    9: "타인이 보는 앞에서 글쓰기",
    10: "잘 모르는 사람에게 전화 걸기",
    11: "잘 모르는 사람들과 대화하기",
    12: "낯선 사람 만나기",
    13: "공공 화장실에서 소변보기",
    14: "이미 사람들이 앉아 있는 방에 들어가기",
    15: "관심의 중심이 되는 상황",
    16: "회의에서 의견 말하기",
    17: "시험 치르기",
    18: "잘 모르는 사람에게 반대 의견이나 불만 표현하기",
    19: "잘 모르는 사람의 눈 바라보기",
    20: "그룹 앞에서 보고서 발표하기",
    21: "이성에게 접근하기",
    22: "상점에서 상품 환불하거나 교환하기",
    23: "파티 주최하기",
    24: "강압적인 판매원에게 저항하기"
}

st.title("LSAS 사회불안 척도")
st.subheader("각 문항의 불안과 회피 점수를 선택하세요")

# ✅ UI에서는 점수 + 정의 제공
anxiety_choices = [
    "0 - 없음",
    "1 - 경미한 불안",
    "2 - 중간 정도의 불안",
    "3 - 심한 불안"
]

avoidance_choices = [
    "0 - 전혀 회피하지 않음 (0%)",
    "1 - 가끔 회피함 (1–33%)",
    "2 - 자주 회피함 (33–67%)",
    "3 - 거의 항상 회피함 (67–100%)"
]

responses = {}

with st.form("LSAS_form"):
    for idx in range(1, 25):
        col1, col2 = st.columns(2)
        with col1:
            anxiety_label = st.selectbox(f"{questions[idx]} - 불안", anxiety_choices, index=1, key=f"a{idx}")
        with col2:
            avoidance_label = st.selectbox(f"{questions[idx]} - 회피", avoidance_choices, index=0, key=f"v{idx}")
        # 숫자 점수만 저장
        responses[idx] = {
            'anxiety': int(anxiety_label.split(" - ")[0]),
            'avoidance': int(avoidance_label.split(" - ")[0])
        }

    submitted = st.form_submit_button("결과 계산하기")

if submitted:
    performance_score = sum(responses[i]['anxiety'] + responses[i]['avoidance'] for i in performance_items)
    social_score = sum(responses[i]['anxiety'] + responses[i]['avoidance'] for i in social_items)
    total_score = performance_score + social_score

    if total_score >= 60:
        interpretation = "범불안 사회불안장애 가능성 높음"
    elif total_score >= 30:
        interpretation = "사회불안장애 가능성 있음"
    else:
        interpretation = "정상 범위"

    # ✅ 출력: 점수만 표시 (정의 제외)
    result_lines = ["LSAS\n"]
    for i, idx in enumerate(range(1, 25), start=1):
        a = responses[idx]['anxiety']
        v = responses[idx]['avoidance']
        line = f"{i}. {questions[idx]} - 불안: {a}점 / 회피: {v}점"
        result_lines.append(line)

    result_lines.append("")
    result_lines.append(f"Performance 점수: {performance_score}점")
    result_lines.append(f"Social Interaction 점수: {social_score}점")
    result_lines.append(f"총점: {total_score}점")
    result_lines.append(f"결과 해석: {interpretation}")

    result_text = "\n".join(result_lines)

    st.markdown("## 📌 평가 결과")
    st.code(result_text, language="text")

