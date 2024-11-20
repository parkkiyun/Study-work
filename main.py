import streamlit as st
from PIL import Image

# 기본 홈 페이지 내용
st.title("교외체험학습 관리 시스템", anchor="center")
logo = Image.open('images/logo.png')
col1, col2 = st.columns([0.5, 8])
with col1:
    st.image(logo, use_column_width=True)
with col2:
    st.subheader("온양한올고등학교", anchor="center")
    
# 메인 페이지 설명
st.write("이 앱은 교외체험학습 신청서 및 결과보고서를 작성하기 위한 멀티페이지 애플리케이션입니다.")

st.subheader("페이지 설명")
st.markdown("""
**교외체험학습 신청서**
""")
st.info("""
교외체험학습 신청을 위한 신청서를 작성합니다. 신청서는 여유롭게 체험학습 일주일 전에 작성하여 PDF 파일로 다운로드 하여 담임 선생님께 네이버 웍스로 제출합니다.
학습 계획이 많을 경우 자동으로 별지에 추가 작성 되지만 프로그램의 한계로 별지 수용 계획을 넘을 때에는 직접 한글로 작성하여 계획서를 따로 제출합니다.
""")

st.markdown("""
**교외체험학습 결과보고서**
""")
st.info("""
사진, 입장권, 참가확인서 등 증빙자료를 파일 업로드 기능을 통해 첨부해 주세요.
체험학습 종료 후 7일 이내 제출해 주세요.
결과 보고 내용이 많을 경우 직접 한글로 작성하여 계획서를 따로 제출합니다.
""")

st.info("왼쪽 사이드바를 사용해 페이지를 이동하세요.")
