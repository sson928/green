import streamlit as st
import pandas as pd
import plotly.express as px
import time
import os

# 🏠 홈 페이지
def home_page():
    st.title("🌿 지구를 살리는 그린 식단 챌린지")
    st.image("home.png", use_container_width=True)
    st.write("""
    이 수업은 탄소배출량을 줄일 수 있는 급식 메뉴를 설계하는 활동입니다. 
    각 차시별로 단계적으로 학습하며 지속 가능한 식사를 이해하고 
    나만의 친환경 그린 급식을 설계해보세요! 
    """)
                            
def first_session_page():
    st.write("✅ 1차시 페이지가 정상적으로 로드되었습니다!")  # 디버깅 메시지
  
    # 이미지 삽입
    st.image("0session.png", use_container_width=True)
    
    # 🟢 주요 개념 정리
    st.subheader("💡 주요 개념")
    st.markdown("""
    - **지속 가능한 식생활**: 환경에 미치는 영향을 줄이고, 건강한 식습관을 유지하는 생활 방식.
    - **탄소 발자국(Carbon Footprint)**: 상품과 서비스가 배출하는 온실가스의 총량. 
    """)
    try:
        st.image("carbon.png", 
                 caption="탄소 발자국 설명 이미지", 
                 use_container_width=True)
    except Exception as e:
        st.error(f"이미지 불러오기 오류: {e}")
    
    
    # 🟢 국가별 온실가스 배출량 분포도
    st.subheader("🌍 국가별 온실가스 배출량 분포도")
    try:
        # Updated list of countries and emissions
        map_emissions = {
            "국가": ["중국", "미국", "인도", "러시아", "한국", "브라질", "독일", "일본", "캐나다", "멕시코", 
                    "이탈리아", "프랑스", "영국", "남아프리카공화국", "이집트", "호주", "인도네시아", "터키", 
                    "이란", "스페인", "베트남", "말레이시아", "사우디아라비아", "태국", "폴란드", 
                    "파키스탄", "우크라이나", "방글라데시", "아르헨티나", "필리핀", "콜롬비아", 
                    "캐냐", "나이지리아", "베네수엘라", "페루", "스웨덴", "노르웨이", "핀란드", 
                    "덴마크", "뉴질랜드", "칠레", "그리스", "포르투갈", "체코", "헝가리", 
                    "루마니아", "이란", "이집트", "남아프리카"],
            "배출량(억 톤 CO₂e)": [110, 60, 40, 35, 7.6, 5.4, 8.2, 9.6, 6.5, 6.1, 
                             4.2, 3.9, 4.8, 5.7, 3.2, 5.8, 7.5, 6.7, 8.9, 4.1, 
                             3.8, 3.2, 10.0, 5.5, 3.3, 2.8, 3.1, 2.9, 2.7, 2.6, 
                             1.9, 2.1, 2.3, 2.2, 0.8, 0.9, 0.7, 0.6, 1.2, 
                             1.5, 1.7, 1.6, 1.1, 1.0, 2.2, 2.4, 2.6, 3.2, 2.8],
            "위도": [35.8617, 37.0902, 20.5937, 61.524, 35.9078, -14.235, 51.1657, 36.2048, 56.1304, 23.6345, 
                   41.8719, 46.6034, 55.3781, -30.5595, 26.8206, -25.2744, -0.7893, 38.9637, 
                   32.4279, 40.4637, 14.0583, 4.2105, 23.8859, 15.8700, 51.9194, 
                   30.3753, 48.3794, 23.6850, -38.4161, 12.8797, 4.5709, 
                   -1.286389, 9.082, 6.4238, -9.19, 60.1282, 60.4720, 61.9241, 
                   56.2639, -40.9006, -35.6751, 39.0742, 39.3999, 49.8175, 47.1625, 
                   45.9432, 32.4279, 26.8206, -30.5595],
            "경도": [104.1954, -95.7129, 78.9629, 105.3188, 127.7669, -51.9253, 10.4515, 138.2529, -106.3468, -102.5528, 
                   12.5674, 2.3490, -3.435973, 22.9375, 30.8025, 133.7751, 113.9213, 35.2433, 
                   53.6880, -3.7492, 108.2772, 101.9758, 45.0792, 100.9925, 19.1451, 
                   69.3451, 31.1656, 90.3563, -63.6167, 121.7740, -74.2973, 
                   36.8219, 8.6753, -66.5897, -75.0152, 18.6435, 8.4689, 25.7482, 
                   9.5018, 174.8859, -71.543, 21.8243, -8.2245, 15.472962, 19.5033, 
                   24.9668, 53.6880, 30.8025, 22.9375]
        }

        map_df = pd.DataFrame(map_emissions)
        threshold = map_df["배출량(억 톤 CO₂e)"].median()
        st.metric("온실가스 배출량 기준치 (중앙값)", f"{threshold} 억 톤 CO₂e")

        fig_map = px.scatter_geo(
            map_df, 
            lat="위도", 
            lon="경도", 
            size="배출량(억 톤 CO₂e)", 
            hover_name="국가", 
            color="배출량(억 톤 CO₂e)", 
            color_continuous_scale=["blue", "lightblue", "yellow", "orange", "red"],
            projection="natural earth"
        )
        st.plotly_chart(fig_map)
    except Exception as e:
        st.error(f"지도 시각화 오류: {e}")
        
 # 🟢 2005-2024 국가별 탄소 배출량 변화 시각화
    st.subheader("📈 2005년부터 2024년까지의 국가별 탄소 배출량 변화")
    
    # 📊 **1. 데이터 생성 (18개 국가 추가)**
    df = pd.DataFrame({
        'Country': ['중국', '미국', '인도', '러시아', '일본', '독일', '영국', '프랑스', '브라질', '대한민국',
                    '캐나다', '호주', '멕시코', '인도네시아', '사우디아라비아', '남아프리카공화국', '터키', '이탈리아'],
        '2024 CO2 Emissions (Billion Tons)': [13, 6.5, 3.5, 2.1, 1.6, 1.3, 1.2, 0.9, 0.7, 0.8, 0.9, 0.8, 0.7, 1.1, 2.5, 1.3, 1.0, 0.7],
        '2020 CO2 Emissions (Billion Tons)': [12, 6, 3, 2, 1.5, 1.2, 1.1, 0.8, 0.6, 0.7, 0.8, 0.7, 0.6, 1.0, 2.2, 1.2, 0.9, 0.6],
        '2015 CO2 Emissions (Billion Tons)': [10, 5.8, 2.8, 2.2, 1.8, 1.3, 1.0, 0.9, 0.5, 0.6, 0.7, 0.6, 0.5, 0.8, 2.0, 1.0, 0.8, 0.5],
        '2010 CO2 Emissions (Billion Tons)': [9, 5.5, 2.5, 2.5, 2.0, 1.4, 1.2, 0.8, 0.4, 0.5, 0.6, 0.5, 0.4, 0.7, 1.8, 0.9, 0.7, 0.4],
        '2005 CO2 Emissions (Billion Tons)': [7, 6.0, 2.0, 2.0, 2.1, 1.5, 1.3, 0.7, 0.3, 0.4, 0.5, 0.4, 0.3, 0.6, 1.5, 0.8, 0.6, 0.3]
    })

    selected_countries = st.multiselect(
        '국가를 선택하세요:', 
        options=df['Country'].unique(), 
        default=['중국', '미국', '인도']
    )

    filtered_df = df[df['Country'].isin(selected_countries)]

    melted_df = pd.melt(filtered_df, id_vars='Country', 
                        value_vars=['2005 CO2 Emissions (Billion Tons)', 
                                    '2010 CO2 Emissions (Billion Tons)', 
                                    '2015 CO2 Emissions (Billion Tons)', 
                                    '2020 CO2 Emissions (Billion Tons)', 
                                    '2024 CO2 Emissions (Billion Tons)'],
                        var_name='Year', value_name='CO2 Emissions')

    melted_df['Year'] = melted_df['Year'].str.extract(r'(\d{4})')

    if not melted_df.empty:
        fig = px.line(melted_df, x='Year', y='CO2 Emissions', color='Country', 
                      title='2005년부터 2024년까지의 국가별 탄소 배출량 변화', 
                      markers=True)
        st.plotly_chart(fig)
    else:
        st.warning('⛔️ 국가를 선택하세요!')
        
    # 🟢 학습 질문
    st.subheader("📝 학습 질문")

    correct_answers = {
        "답변 1": "중국",  
        "답변 2": "0.8"  
    }

    # 📌 질문 1: 2024년 기준으로 온실가스를 가장 많이 배출하는 국가는 어디인가요?
    st.markdown("**1️⃣ 2024년 기준으로 온실가스를 가장 많이 배출하는 국가는 어디인가요?**")
    answer1 = st.text_input("정답을 입력하세요", key="q1")
    if answer1:
        if answer1.strip() == correct_answers["답변 1"]:
            st.success("✅ 정답입니다! 가장 많이 배출하는 국가는 **중국**입니다.")
        else:
            st.warning("❌ 힌트: 세계에서 가장 인구가 많은 나라입니다.")

    # 📌 질문 2: 2024년 한국의 탄소 배출량은 몇 억 톤인가요?
    st.markdown("**2️⃣ 2024년 한국의 탄소 배출량은 몇 억 톤인가요?**")
    answer2 = st.text_input("정답을 입력하세요 (숫자만 입력하세요)", key="q2")
    if answer2:
        if answer2.strip() == correct_answers["답변 2"]:
            st.success("✅ 정답입니다! 2024년 대한민국의 탄소 배출량은 **0.8억 톤**입니다.")
        else:
            st.warning("❌ 힌트: 위의 그래프에서 **대한민국의 2024년 탄소 배출량**을 확인해보세요.")

def second_session_page():
    st.write("✅ 2차시 페이지가 정상적으로 로드되었습니다!")  # 디버깅 메시지

    # 🌍 1️⃣ 타이틀 및 이미지 삽입
    st.image("1session.png", use_container_width=True)
    
    st.markdown("""
    - **식재료와 탄소 배출의 관계**: 고기(특히 소고기)는 탄소 배출량이 높고, 콩류나 두부는 배출량이 낮음.
    """)

    # 🟢 식재료별 탄소 배출량 시각화
    st.subheader("🍽️ 식재료별 탄소 배출량 시각화")

    try:
        # 🔹 데이터프레임 생성
        food_emissions = {
            "식재료": ["소고기", "돼지고기", "닭고기", "두부", "감자", "생선", "달걀", "우유", "쌀", "밀", 
                     "옥수수", "양배추", "당근", "브로콜리", "고구마"],
            "탄소 배출량(kg CO₂e/kg)": [27, 12, 6, 2, 0.2, 3, 4.5, 1.9, 2.7, 1.6, 
                                      1.1, 0.4, 0.3, 0.8, 0.9]
        }
        food_df = pd.DataFrame(food_emissions)

        # 🔹 멀티 셀렉트 위젯: 사용자가 선택할 수 있는 식재료 목록
        selected_foods = st.multiselect(
            '🌿 시각화할 식재료를 선택하세요:', 
            options=food_df['식재료'].unique(), 
            default=food_df['식재료'].unique()  # 기본값: 모든 식재료 선택
        )

        # 🔹 선택한 식재료에 맞게 데이터프레임 필터링
        filtered_df = food_df[food_df['식재료'].isin(selected_foods)]

        # 🔹 시각화 생성
        if not filtered_df.empty:
            fig2 = px.bar(
                filtered_df, 
                x="식재료", 
                y="탄소 배출량(kg CO₂e/kg)", 
                color="식재료", 
                color_discrete_sequence=px.colors.qualitative.Plotly,
                title="식재료별 탄소 배출량"
            )
            st.plotly_chart(fig2)
        else:
            st.warning('⛔️ 시각화할 식재료를 선택하세요!')
    except Exception as e:
        st.error(f"시각화 오류: {e}")

    # 🌍 2️⃣ 햄버거 탄소 배출량 설명
    st.markdown("""
    ---
    ### 🤔 햄버거 하나로 발생하는 탄소 배출량은 몇 kg일까요?
    여러분이 평소에 자주 먹는 햄버거 하나로 **얼마나 많은 탄소 배출이 발생할까요?**  
    놀라지 마세요! 햄버거 하나의 탄소 배출량은 약 **2.5kg CO₂e**입니다.  
    """)

    # 🌐 햄버거 이미지
    st.image('hamburger.gif', caption='🍔 햄버거 하나의 탄소 배출량 = 2.5kg CO₂e', use_container_width=True)

    # 🌍 3️⃣ 햄버거 탄소 배출량을 풍선으로 시각화
    st.markdown("""
    ---
    ## 🍃 **2.5kg CO₂e는 얼마나 많은 풍선에 해당할까요?**
    - 풍선 하나에 들어가는 이산화탄소의 양은 약 **0.1kg CO₂e**라고 가정합니다.
    - 즉, **2.5kg CO₂e = 25개의 풍선**에 해당합니다.
    - 아래에서 직접 **풍선이 하나씩 채워지는 모습을 확인**할 수 있습니다.  
    """)

    # 🔹 풍선 이미지 시각화
    st.header('🎈 25개의 풍선으로 탄소 배출 시각화')

    # 🌐 풍선 이미지 경로
    balloon_image_path = "balloon.png"  # 풍선 이미지 파일 (balloon.png) 준비 필요

    # 🎉 '풍선 채우기' 버튼 클릭 시 풍선 시각화
    if st.button('🎉 풍선 채우기 시작하기'):
        st.markdown("### 💨 풍선이 하나씩 채워집니다... 기다려주세요!")
        
        # 🔹 5개의 열로 풍선 배치
        col1, col2, col3, col4, col5 = st.columns(5)  
        total_balloons = 25  # 총 25개의 풍선을 채우기

        for i in range(1, total_balloons + 1):
            time.sleep(0.3)  # 풍선이 차오르는 시간 (0.3초마다)
            
            if i <= 5:
                col1.image(balloon_image_path, width=60)
            elif i <= 10:
                col2.image(balloon_image_path, width=60)
            elif i <= 15:
                col3.image(balloon_image_path, width=60)
            elif i <= 20:
                col4.image(balloon_image_path, width=60)
            else:
                col5.image(balloon_image_path, width=60)
        
        st.success('🎉 모든 풍선이 채워졌습니다! 🍔 햄버거 하나로 이렇게 많은 탄소가 배출됩니다.')

    # 🌍 4️⃣ 탄소 발자국의 위기성 전달
    st.markdown("""
    ---
    ### 🌀 **무엇을 할 수 있을까요?**
    - **햄버거 하나**만 먹어도 25개의 풍선에 해당하는 CO₂가 발생합니다.
    - **대체 메뉴**로 두부 샐러드와 같은 채식 식단을 선택하면, 이 탄소 발자국을 크게 줄일 수 있습니다.
    - 우리 모두 **작은 선택이 지구를 바꿀 수 있다는 사실을 기억해요!** 🌍
    """)
    


# 3차시 페이지 함수
def third_session_page():
    # 🌍 1️⃣ 타이틀 및 이미지 삽입
    st.image("2session.png", use_container_width=True)
    
    st.write("🌿 **목표**: 대체 식재료를 활용하여 탄소 배출량을 얼마나 줄일 수 있는지 확인해보세요.")
    
    st.markdown("""**💡 동기 유발:**
    이 수업에서는 탄소 배출량을 줄일 수 있는 방법을 탐구할 것입니다. 아래의 영상을 보고 어떤 음식이 탄소 배출량이 가장 높은지 알아보세요!
    """)
    
    st.video("https://youtu.be/SiCa05GHWQI")
    
    
    st.markdown("""**💡 참고:**
    - 모든 탄소 배출량 값은 **1인분 기준**으로 산정되었습니다.
    - 탄소 배출량 데이터는 'WWF 식품 배출량 보고서'와 'Our World in Data'를 참고하여 작성되었습니다.
    - 반찬과 디저트의 경우, 일부 대체 식재료가 탄소배출 기준을 초과할 수 있습니다. 이는 기존 메뉴와의 차이를 비교하는 것이며, 항상 더 낮은 탄소배출량을 보장하지는 않습니다. 이러한 경우, 메뉴의 영양가나 맛, 다양한 식단 제공의 필요성을 고려할 수 있습니다.
    """)
    
    # 초기 메뉴 데이터프레임 생성
    initial_menu = {
        "메뉴 종류": ["밥", "국", "반찬1", "반찬2", "반찬3", "디저트"],
        "기존 메뉴": ["백미밥", "소고기미역국", "돈까스", "감자채볶음", "배추김치", "케이크"],
        "탄소배출량(kg CO₂e)": [1.8, 2.8, 4.5, 1.0, 0.6, 5.0]
    }
    
    alternative_options = {
        "밥": ["백미밥", "현미밥", "잡곡밥", "콩밥", "귀리밥", "퀴노아밥"],
        "국": ["소고기미역국", "된장국", "콩나물국", "채소국", "시래기국", "감자국"],
        "반찬1": ["돈까스", "채소볶음", "두부조림", "콩고기구이", "버섯볶음", "생선구이"],
        "반찬2": ["감자채볶음", "버섯볶음", "나물무침", "해초샐러드", "시금치나물", "고구마샐러드"],
        "반찬3": ["배추김치", "오이무침", "무생채", "열무김치", "깍두기", "갓김치"],
        "디저트": ["케이크", "과일샐러드", "단팥죽", "견과류바", "고구마말랭이", "떡"]
    }
    
    alternative_emissions = {
        "백미밥": 1.8, "현미밥": 1.2, "잡곡밥": 1.0, "콩밥": 0.9, "귀리밥": 1.1, "퀴노아밥": 0.8,
        "소고기미역국": 2.8, "된장국": 1.0, "콩나물국": 0.8, "채소국": 0.6, "시래기국": 0.5, "감자국": 0.7,
        "돈까스": 4.5, "채소볶음": 1.8, "두부조림": 1.5, "콩고기구이": 1.2, "버섯볶음": 1.0, "생선구이": 3.0,
        "감자채볶음": 1.0, "버섯볶음": 0.7, "나물무침": 0.6, "해초샐러드": 0.5, "시금치나물": 0.4, "고구마샐러드": 0.9,
        "배추김치": 0.6, "오이무무침": 0.3, "무생채": 0.4, "열무김치": 0.5, "깍두기": 0.5, "갓김치": 0.6,
        "케이크": 5.0, "과일샐러드": 1.2, "단팥죽": 0.8, "견과류바": 1.5, "고구마말랭이": 0.9, "떡": 1.1
    }

    initial_df = pd.DataFrame(initial_menu)
    
    st.subheader("📋 기존 메뉴와 탄소배출량")
    st.dataframe(initial_df)
    
    st.subheader("🔄 대체 식재료 선택하기")
    for i, row in initial_df.iterrows():
        new_menu = st.radio(
            f"🍽️ {row['메뉴 종류']} 대체 식재료 선택", 
            options=alternative_options[row['메뉴 종류']], 
            index=0, 
            key=f"menu_{i}"
        )
        initial_df.loc[i, '대체 메뉴'] = new_menu
        initial_df.loc[i, '대체 탄소배출량(kg CO₂e)'] = alternative_emissions[new_menu]

    # 대체 전/후 탄소 배출량 비교 그래프 생성
    fig = px.bar(
        initial_df, 
        x="메뉴 종류", 
        y=["탄소배출량(kg CO₂e)", "대체 탄소배출량(kg CO₂e)"], 
        barmode="group", 
        title="대체 전/후 탄소 배출량 비교",
        text_auto=True,
        color_discrete_sequence=["#2ECC71", "#F1C40F"],
        labels={
            "value": "탄소배출량 (kg CO₂e)",
            "variable": "구분"
        }
    )
    fig.add_hline(y=2.0, line_dash="dot", line_color="red", annotation_text="탄소배출 기준선 (2.0 kg CO₂e)", annotation_position="top left")
    
    st.plotly_chart(fig, use_container_width=True)


## 4️⃣ 4차시 페이지
def fourth_session_page():
    
    # 🌍 1️⃣ 타이틀 및 이미지 삽입
    st.image("3session.png", use_container_width=True)
    
    # Nutritional standards for Korean adolescents (per meal)
    
    NUTRITIONAL_STANDARDS = {
    '탄수화물(g)': 43.0,  # Carbohydrates
    '단백질(g)': 22.0,    # Protein
    '지방(g)': 17.0,      # Fat
    '칼슘(mg)': 333.0,    # Calcium
    '철(mg)': 4.3,       # Iron
    '비타민(mg)': 25.0   # Vitamin C
}
    
    # 기준 탄소 배출량 설정 (수정 가능)
    emission_threshold = 6.0  # 기준치 (6 kg CO₂e)
    
    st.write("""
    📚 **목표:** 나만의 급식 메뉴를 설계하고, 해당 급식의 탄소 배출량과 영양소를 분석합니다.
    """)

    # 📘 메뉴 데이터를 저장할 빈 데이터프레임
    if 'menu_data' not in st.session_state:
        st.session_state['menu_data'] = pd.DataFrame(columns=[
            '메뉴 종류', '메뉴 이름', 
            '탄소배출량(kg CO₂e)', '탄수화물(g)', '단백질(g)', '지방(g)', '칼슘(mg)', '철(mg)', '비타민(mg)'
        ])

    st.subheader("🍱 나만의 급식 메뉴 설계")
    st.write("급식 메뉴를 직접 입력하고, 탄소 배출량과 영양소를 추가해보세요.")
    
    # 📘 메뉴 입력 양식
    with st.form("menu_form"):
        menu_type = st.selectbox("🍽️ 메뉴 종류 선택", ['밥', '국', '반찬1', '반찬2', '반찬3'], key='menu_type')
        menu_name = st.text_input("🍚 메뉴 이름", placeholder="예: 현미밥", key='menu_name')

        st.markdown("### 🔢 탄소 배출량 및 영양소 입력")
        carbon_emission = st.number_input("🌍 탄소배출량 (kg CO₂e)", min_value=0.0, step=0.01, format="%.2f")
        carb = st.number_input("🍞 탄수화물 (g)", min_value=0.0, step=0.01, format="%.2f")
        protein = st.number_input("🍗 단백질 (g)", min_value=0.0, step=0.01, format="%.2f")
        fat = st.number_input("🥑 지방 (g)", min_value=0.0, step=0.01, format="%.2f")
        calcium = st.number_input("🦴 칼슘 (mg)", min_value=0.0, step=0.01, format="%.2f")
        iron = st.number_input("🩸 철 (mg)", min_value=0.0, step=0.01, format="%.2f")
        vitamin = st.number_input("💊 비타민 (mg)", min_value=0.0, step=0.01, format="%.2f")
        
        submitted = st.form_submit_button("📤 급식 메뉴 추가")

        if submitted:
            if menu_name == "":
                st.error("❌ 메뉴 이름을 입력해주세요!")
            else:
                new_menu_data = pd.DataFrame({
                    '메뉴 종류': [menu_type],
                    '메뉴 이름': [menu_name],
                    '탄소배출량(kg CO₂e)': [carbon_emission],
                    '탄수화물(g)': [carb],
                    '단백질(g)': [protein],
                    '지방(g)': [fat],
                    '칼슘(mg)': [calcium],
                    '철(mg)': [iron],
                    '비타민(mg)': [vitamin]
                })
                
                st.session_state['menu_data'] = pd.concat([st.session_state['menu_data'], new_menu_data], ignore_index=True)
                st.success(f"✅ '{menu_name}' 메뉴가 성공적으로 추가되었습니다!")

    st.subheader("📋 나만의 급식 메뉴")
    if not st.session_state['menu_data'].empty:
        st.write("**등록된 급식 메뉴 목록**:")
        st.write(', '.join(st.session_state['menu_data']['메뉴 이름'].tolist()))
        
        total_values = st.session_state['menu_data'].iloc[:, 2:].sum()
        
        st.subheader("🌍 탄소 배출량 및 영양소 평가")
        if total_values['탄소배출량(kg CO₂e)'] > emission_threshold:
            st.error(f"🚨 **경고! 탄소 배출량이 기준치를 초과했습니다!**")
        else:
            st.success(f"🥳 **축하합니다! 당신의 메뉴는 그린 급식입니다!**")
        
        st.write("🌱 **영양소 평가**")
        for nutrient, standard in NUTRITIONAL_STANDARDS.items():
            total = total_values[nutrient]
            if total < standard:
                st.warning(f"⚠️ {nutrient}이(가) 부족합니다. 추가가 필요합니다. ({total:.2f} / {standard})")
            else:
                st.success(f"✅ {nutrient}이(가) 충분합니다! ({total:.2f} / {standard})")
    else:
        st.info("📥 아직 추가된 메뉴가 없습니다. 메뉴를 추가해보세요!")
    
    # 📘 참고 사이트 섹션 호출
    display_references()

# 📘 참고 사이트 표시 함수
def display_references():
    st.markdown("""
    <div style="border: 2px solid #4CAF50; padding: 15px; border-radius: 10px; background-color: #f9f9f9; margin-top: 20px;">
        <h3 style="color: #4CAF50;">🔗 참고 사이트</h3>
        <ul>
            <li>🥗 <a href="https://interactive.hankookilbo.com/v/co2e/" target="_blank" style="font-weight: bold; color: #1565C0;">한끼밥상 탄소계산기</a> — 음식을 선택하여 탄소 배출량을 계산할 수 있는 유용한 도구입니다.</li>
            <li>🥗 <a href="https://various.foodsafetykorea.go.kr/nutrient/" target="_blank" style="font-weight: bold; color: #1565C0;">식품영양성분 데이터베이스</a> — 음식의 탄수화물, 단백질, 지방 등의 영양소 함량을 검색할 수 있습니다.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    
def fifth_session_page():  # Corrected function name
    # 🌍 1️⃣ 타이틀 및 이미지 삽입
    st.image("4session.png", use_container_width=True)

    st.subheader("🖜️ 탄소발자국을 줄이기 위한 실천 방안")
    st.write("여러분이 실천해 본 탄소 발자국을 줄이기 위한 방법을 적어보세요!")
    
    # 📚 사용자 입력 평
    with st.form("suggestion_form"):
        user_name = st.text_input("👤 작성자 이름", "")
        suggestion = st.text_area("✍️ 실천 내용", placeholder="탄소 발자국을 줄이기 위해 노력해 본 내용을을 적어주세요.")
        uploaded_image = st.file_uploader("📷 이미지 올리기", type=["jpg", "jpeg", "png"])
        submitted = st.form_submit_button("📤 실천 내용 제출")
        
        if submitted:
            if user_name and suggestion:
                # 실천 방안을 표시하기 위해 세션 스트레이터에 저장
                if 'suggestion_board' not in st.session_state:
                    st.session_state['suggestion_board'] = []
                
                suggestion_entry = {'name': user_name, 'suggestion': suggestion}
                
                if uploaded_image is not None:
                    image_bytes = uploaded_image.getvalue()
                    suggestion_entry['image'] = image_bytes
                
                st.session_state['suggestion_board'].append(suggestion_entry)
                
                st.success(f"✅ '{user_name}'님의 실천 방안이 성공적으로 등록되었습니다!")
            else:
                st.error("❌ 이름과 실천 방안을 모두 입력해주세요.")
    
    # 📚 경가 "검색" 게시판 표시 필터링
    st.subheader("📈 공유 방안 게시판")
    if 'suggestion_board' in st.session_state and len(st.session_state['suggestion_board']) > 0:
        for i, suggestion in enumerate(reversed(st.session_state['suggestion_board'])):  # 번지순 표시
            st.markdown(f"**{suggestion['name']}**: {suggestion['suggestion']}")
            if 'image' in suggestion:
                st.image(suggestion['image'], width=200)
    else:
        st.info("📥 아직 등록된 실천 방안이 없습니다. 모두의 실천 방안을 공유해주세요!")
                
                
# 🌐 페이지 네비게이션
page = st.sidebar.selectbox(
    "페이지를 선택하세요", 
    ["🏠 홈", "🍽️ 1차시", "🍽️ 2차시", "🍽️ 3차시", "🍽️ 4차시", "🍽️ 5차시"]
)

if page == "🏠 홈":
    home_page()
elif page == "🍽️ 1차시":
    first_session_page()
elif page == "🍽️ 2차시":
    second_session_page()
elif page == "🍽️ 3차시":
    third_session_page()
elif page == "🍽️ 4차시":
    fourth_session_page()
elif page == "🍽️ 5차시":
    fifth_session_page()

                
                
