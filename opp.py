import streamlit as st
from PIL import Image

# 전체 페이지 설정: 넓은 레이아웃, 아이콘 및 제목
st.set_page_config(
    page_title="웹페이지와 인공지능",
    page_icon="✨",
    layout="wide"
)

# 사용자 정의 CSS (배경 이미지 및 텍스트 스타일)
custom_css = """
<style>
/* Streamlit 기본 패딩 제거 */
.stApp {
    margin: 0;
    padding: 0;
}

/* 모든 페이지의 배경 이미지 스타일 */
.background-page {
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    min-height: 100vh; /* 화면 전체 높이 사용 */
    display: flex;
    flex-direction: column;
    justify-content: center; /* 세로 중앙 정렬 */
    align-items: center; /* 가로 중앙 정렬 */
    color: white; /* 텍스트 색상 (배경에 따라 조절) */
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7); /* 텍스트 그림자 */
    padding: 20px;
    box-sizing: border-box;
}

/* 특정 페이지 배경 이미지 */
.title-page {
    background-image: url('https://user-images.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME/main/image_introduction.jpg'); /* GitHub에서 이미지 호스팅 필요 */
}
.toc-page {
    background-image: url('https://user-images.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME/main/image_introduction.jpg'); /* GitHub에서 이미지 호스팅 필요 */
}
.section-1-page {
    background-image: url('https://user-images.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME/main/image_introduction.jpg'); /* GitHub에서 이미지 호스팅 필요 */
}
.section-2-page {
    background-image: url('https://user-images.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME/main/image_4.jpg'); /* GitHub에서 이미지 호스팅 필요 */
}
.section-3-page {
    background-image: url('https://user-images.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME/main/image_7.jpg'); /* GitHub에서 이미지 호스팅 필요 */
}

/* 텍스트 컨테이너 스타일 (가독성 향상) */
.content-box {
    background-color: rgba(0, 0, 0, 0.5); /* 반투명 배경 */
    padding: 30px 40px;
    border-radius: 10px;
    max-width: 800px;
    text-align: left;
}

/* 제목 및 헤더 스타일 */
.main-title {
    font-size: 4em;
    font-weight: bold;
    text-align: center;
    margin-bottom: 50px;
}
.section-title {
    font-size: 2.5em;
    font-weight: bold;
    margin-bottom: 20px;
}
.section-subtitle {
    font-size: 1.8em;
    font-weight: bold;
    margin-top: 30px;
    margin-bottom: 15px;
}
p, li {
    font-size: 1.2em;
    line-height: 1.6;
}
ul {
    padding-left: 20px;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# GitHub에서 이미지 호스팅 URL로 변경 필요!
# Streamlit Community Cloud에 배포 시에는 GitHub의 raw 이미지 URL을 사용해야 합니다.
# 예: https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME/main/image_introduction.jpg
# YOUR_GITHUB_USERNAME과 YOUR_REPOSITORY_NAME을 실제 값으로 변경하세요.
github_raw_url_prefix = "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME/main/"

# 페이지 선택을 위한 세션 상태
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'title'

# 사이드바 네비게이션
st.sidebar.title("페이지 이동")
if st.sidebar.button("시작 페이지"):
    st.session_state.current_page = 'title'
if st.sidebar.button("목차"):
    st.session_state.current_page = 'toc'
if st.sidebar.button("1. 웹 페이지 개발 과정"):
    st.session_state.current_page = 'section1'
if st.sidebar.button("2. 프론트엔드와 백엔드란?"):
    st.session_state.current_page = 'section2'
if st.sidebar.button("3. 웹 페이지 개발에서 인공지능의 역할"):
    st.session_state.current_page = 'section3'


# --- 페이지 내용 ---

# 시작 페이지: "웹페이지와 인공지능" 제목
if st.session_state.current_page == 'title':
    st.markdown(f"""
    <div class="background-page title-page" style="background-image: url('{github_raw_url_prefix}image_introduction.jpg');">
        <div class="content-box" style="background-color: rgba(0, 0, 0, 0.6);">
            <h1 class="main-title">웹 페이지와 인공지능</h1>
            <p style="text-align: center; font-size: 1.5em;">웹 개발의 핵심과 인공지능의 융합</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 목차 페이지
elif st.session_state.current_page == 'toc':
    st.markdown(f"""
    <div class="background-page toc-page" style="background-image: url('{github_raw_url_prefix}image_introduction.jpg');">
        <div class="content-box">
            <h2 class="section-title" style="text-align: center;">목차</h2>
            <ul style="list-style-type: none; padding: 0;">
                <li><p><a href="#웹-페이지-개발-과정" style="color: white; text-decoration: none;">1. 웹 페이지 개발 과정</a></p></li>
                <li><p><a href="#프론트엔드와-백엔드란?" style="color: white; text-decoration: none;">2. 프론트엔드와 백엔드란?</a></p></li>
                <li><p><a href="#웹-페이지-개발에서-인공지능의-역할" style="color: white; text-decoration: none;">3. 웹 페이지 개발에서 인공지능의 역할</a></p></li>
            </ul>
            <p style="text-align: center; margin-top: 30px;">(왼쪽 사이드바를 이용하여 페이지를 이동하세요)</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 1. 웹 페이지 개발 과정
elif st.session_state.current_page == 'section1':
    st.markdown(f"""
    <div class="background-page section-1-page" style="background-image: url('{github_raw_url_prefix}image_introduction.jpg');">
        <div class="content-box">
            <h2 class="section-title">1. 웹 페이지 개발 과정</h2>
            <p>웹 페이지 개발은 다음과 같은 체계적인 단계를 거쳐 진행됩니다.</p>
            <ul>
                <li><p><strong>프로젝트 기획</strong>: 웹사이트의 목표, 대상 사용자, 기능, 콘텐츠 등을 정의하는 단계입니다.</p></li>
                <li><p><strong>디자인</strong>: 사용자 인터페이스(UI) 및 사용자 경험(UX)을 설계하는 단계입니다. 와이어프레임, 목업, 프로토타입 등을 제작합니다.</p></li>
                <li><p><strong>개발</strong>: 실제로 코드를 작성하여 웹 페이지를 구현하는 단계입니다. 프론트엔드와 백엔드 개발이 이루어집니다.</p></li>
                <li><p><strong>테스트</strong>: 개발된 웹 페이지가 정상적으로 작동하는지, 버그는 없는지, 사용성은 좋은지 등을 확인하는 단계입니다.</p></li>
                <li><p><strong>배포 및 유지 보수</strong>: 완성된 웹 페이지를 서버에 올려 사용자에게 공개하고, 이후 발생하는 문제점을 해결하고 기능을 업데이트하는 단계입니다.</p></li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 2. 프론트엔드와 백엔드란?
elif st.session_state.current_page == 'section2':
    st.markdown(f"""
    <div class="background-page section-2-page" style="background-image: url('{github_raw_url_prefix}image_4.jpg');">
        <div class="content-box">
            <h2 class="section-title">2. 프론트엔드와 백엔드란?</h2>
            <p>웹 개발은 크게 두 가지 영역으로 나뉩니다.</p>
            <ul>
                <li><p><strong>프론트엔드 (Frontend)</strong>: 사용자가 직접 보고 상호작용하는 웹사이트의 화면을 제작하는 부분입니다. HTML, CSS, JavaScript 등의 기술을 사용하여 웹 페이지의 구조, 디자인, 동적인 요소를 만듭니다.</p></li>
                <li><p><strong>백엔드 (Backend)</strong>: 눈에 보이지 않는 곳에서 데이터 저장 및 처리, 서버 로직, 데이터베이스 관리 등을 담당합니다. Python, Java, Node.js 등 다양한 언어와 프레임워크가 사용됩니다.</p></li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. 웹 페이지 개발에서 인공지능의 역할
elif st.session_state.current_page == 'section3':
    st.markdown(f"""
    <div class="background-page section-3-page" style="background-image: url('{github_raw_url_prefix}image_7.jpg');">
        <div class="content-box">
            <h2 class="section-title">3. 웹 페이지 개발에서 인공지능의 역할</h2>
            <p>인공지능(AI)은 웹 페이지 개발의 다양한 영역에서 활용되고 있습니다.</p>
            <ul>
                <li><p><strong>정보 요약</strong>: 긴 텍스트 콘텐츠를 AI가 자동으로 요약하여 사용자에게 핵심 정보를 빠르게 제공합니다.</p></li>
                <li><p><strong>카테고리 분류</strong>: 방대한 데이터를 AI가 자동으로 분석하여 적절한 카테고리로 분류함으로써 효율적인 정보 관리를 돕습니다.</p></li>
                <li><p><strong>AI 챗봇</strong>: 고객 문의에 자동으로 응답하거나, 사용자에게 맞춤형 정보를 제공하여 웹사이트의 상호작용성을 높입니다.</p></li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
