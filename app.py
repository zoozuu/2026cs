import streamlit as st
from pathlib import Path
from datetime import date
import html

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="정보과학탐구한마당",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# 데이터
# =========================
EVENT_DATE = date(2026, 7, 10)
DEADLINE_DATE = date(2026, 7, 7)

projects_2025 = [
    {
        "title": "도시소음 회피 가이드 시스템",
        "url": "https://canva.link/9hrxwjm3wlbwaxr",
        "tag": "생활 문제 해결"
    },
    {
        "title": "가짜뉴스 판별 프로그램",
        "url": "https://canva.link/x1sdtfz6c1f2sb4",
        "tag": "인공지능 · 미디어"
    },
    {
        "title": "고등학교 내에서 발생하는 입시정보격차 해소; 스마트 입시정보 알림 키오스크 시스템",
        "url": "https://canva.link/ca34a90d7xhiprb",
        "tag": "교육 · 정보격차"
    },
    {
        "title": "고령화 사회에서 노인성 질환 조기 진단을 위한 활성 산소 바이오센서 모니터링 시스템 구현",
        "url": "https://canva.link/cm17w6ie1zssx1c",
        "tag": "바이오센서 · 헬스케어"
    },
    {
        "title": "고령 환자를 위한 정보과학 기반 복약 알림 시스템",
        "url": "https://canva.link/s2rbuerihe55j62",
        "tag": "헬스케어 · 알림 시스템"
    },
]

projects_2024 = [
    {
        "title": "필터 버블 현상 개선 프로그램",
        "url": "https://drive.google.com/file/d/1PGg1fWUEKdU8kWDxyQDWq99vGPzirnXe/view?usp=drive_link",
        "tag": "HTML"
    },
    {
        "title": "학교 엘레베이터 불필요한 탑승 제한하기",
        "url": "https://drive.google.com/file/d/1HdaaN40tkxYg-U6KVlIYg5uC5T-K3Mbj/view?usp=drive_link",
        "tag": "아두이노"
    },
    {
        "title": "고령화시대에 올바른 약물 사용방안",
        "url": "https://drive.google.com/file/d/1I5cIqVknfG-595Gvm9RCk5kl_9J1SrsK/view?usp=drive_link",
        "tag": "오렌지3 · 파이썬"
    },
    {
        "title": "자율주행자동차의 딜레마 상황에서의 윤리적 판단 문제",
        "url": "https://drive.google.com/file/d/1rsxNTXO6PRFIN1_5VEaqWuQotaL6Fp4j/view?usp=drive_link",
        "tag": "파이썬"
    },
    {
        "title": "현대 사회의 노인 치매 발생 해결하기",
        "url": "https://drive.google.com/file/d/1CAlR3bl4glJS8lhQESyK1hZUbOR_kEM5/view?usp=sharing",
        "tag": "파이썬"
    },
    {
        "title": "청년 실업 문제 해결",
        "url": "https://drive.google.com/file/d/1XMCcLyd4ki9TPM4Mp6B2wdOsr9uYi8tt/view?usp=drive_link",
        "tag": "웹사이트 기획"
    },
    {
        "title": "자율주행자동차 해킹 해결방안",
        "url": "https://drive.google.com/file/d/1sBmhK2Vf2FX10zt4LmY_UmmOJ4XdyXxV/view?usp=drive_link",
        "tag": "프로그램 기획"
    },
]

# =========================
# CSS 디자인
# =========================
st.markdown(
    """
    <style>
    :root {
        --bg: #041b20;
        --card: rgba(7, 38, 45, 0.78);
        --cyan: #65fff2;
        --pink: #ff2bd6;
        --yellow: #fff27a;
        --text: #eaffff;
        --muted: #b6d8dc;
    }

    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(circle at 18% 12%, rgba(101, 255, 242, 0.16), transparent 30%),
            radial-gradient(circle at 82% 8%, rgba(255, 43, 214, 0.18), transparent 28%),
            radial-gradient(circle at 50% 95%, rgba(101, 255, 242, 0.12), transparent 34%),
            linear-gradient(135deg, #021014 0%, #06262c 45%, #030b10 100%);
        color: var(--text);
    }

    [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }

    .block-container {
        padding-top: 2.3rem;
        padding-bottom: 4rem;
        max-width: 1200px;
    }

    h1, h2, h3, p, div, span {
        word-break: keep-all;
    }

    .hero {
        border: 1px solid rgba(101,255,242,0.45);
        border-radius: 28px;
        padding: 34px;
        background:
            linear-gradient(135deg, rgba(101,255,242,0.08), rgba(255,43,214,0.08)),
            rgba(4, 20, 25, 0.72);
        box-shadow:
            0 0 30px rgba(101,255,242,0.14),
            inset 0 0 30px rgba(255,43,214,0.05);
        margin-bottom: 24px;
    }

    .neon-title {
        font-size: clamp(2.4rem, 6vw, 5.2rem);
        line-height: 1.02;
        font-weight: 900;
        letter-spacing: -0.06em;
        color: #dfffff;
        text-shadow:
            0 0 8px rgba(101,255,242,0.95),
            0 0 24px rgba(101,255,242,0.65),
            0 0 42px rgba(255,43,214,0.40);
        margin-bottom: 18px;
    }

    .sub-title {
        color: var(--yellow);
        font-size: 1.28rem;
        font-weight: 800;
        text-shadow: 0 0 12px rgba(255,242,122,0.6);
        margin-bottom: 22px;
    }

    .desc {
        color: var(--muted);
        font-size: 1.04rem;
        line-height: 1.75;
        margin-bottom: 24px;
    }

    .badge-row {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 10px;
    }

    .badge {
        display: inline-flex;
        align-items: center;
        gap: 7px;
        padding: 9px 14px;
        border-radius: 999px;
        border: 1px solid rgba(101,255,242,0.48);
        background: rgba(101,255,242,0.08);
        color: #eaffff;
        font-weight: 800;
        box-shadow: 0 0 14px rgba(101,255,242,0.16);
    }

    .pink-badge {
        border-color: rgba(255,43,214,0.55);
        background: rgba(255,43,214,0.10);
        box-shadow: 0 0 14px rgba(255,43,214,0.16);
    }

    .yellow-badge {
        border-color: rgba(255,242,122,0.65);
        background: rgba(255,242,122,0.10);
        color: #fffbd0;
        box-shadow: 0 0 14px rgba(255,242,122,0.14);
    }

    .poster-box {
        border-radius: 24px;
        overflow: hidden;
        border: 1px solid rgba(101,255,242,0.45);
        box-shadow: 0 0 26px rgba(101,255,242,0.24);
    }

    .section-title {
        margin-top: 32px;
        margin-bottom: 12px;
        font-size: 2rem;
        font-weight: 900;
        color: #eaffff;
        text-shadow: 0 0 16px rgba(101,255,242,0.50);
    }

    .section-caption {
        color: var(--muted);
        margin-bottom: 18px;
        font-size: 1.02rem;
    }

    .info-card {
        padding: 22px;
        min-height: 142px;
        border-radius: 22px;
        background: rgba(6, 34, 40, 0.74);
        border: 1px solid rgba(101,255,242,0.34);
        box-shadow: 0 0 18px rgba(101,255,242,0.10);
    }

    .info-card .label {
        color: var(--cyan);
        font-size: 0.9rem;
        font-weight: 900;
        margin-bottom: 9px;
    }

    .info-card .value {
        color: #ffffff;
        font-size: 1.35rem;
        font-weight: 900;
        line-height: 1.25;
    }

    .info-card .small {
        color: var(--muted);
        font-size: 0.92rem;
        margin-top: 8px;
        line-height: 1.45;
    }

    a.project-card {
        display: block;
        text-decoration: none !important;
        color: inherit !important;
        padding: 22px 22px 20px 22px;
        margin-bottom: 18px;
        border-radius: 22px;
        background:
            linear-gradient(135deg, rgba(101,255,242,0.10), rgba(255,43,214,0.07)),
            rgba(5, 29, 35, 0.86);
        border: 1px solid rgba(101,255,242,0.34);
        box-shadow: 0 0 20px rgba(101,255,242,0.10);
        transition: 0.18s ease;
        min-height: 152px;
    }

    a.project-card:hover {
        transform: translateY(-4px);
        border-color: rgba(255,43,214,0.72);
        box-shadow:
            0 0 28px rgba(255,43,214,0.22),
            0 0 20px rgba(101,255,242,0.16);
    }

    .project-year {
        display: inline-block;
        color: #061014;
        background: var(--cyan);
        padding: 5px 10px;
        border-radius: 999px;
        font-size: 0.82rem;
        font-weight: 900;
        margin-bottom: 14px;
    }

    .project-tag {
        display: inline-block;
        color: #fffbd0;
        border: 1px solid rgba(255,242,122,0.45);
        background: rgba(255,242,122,0.08);
        padding: 5px 10px;
        border-radius: 999px;
        font-size: 0.82rem;
        font-weight: 800;
        margin-left: 6px;
        margin-bottom: 14px;
    }

    .project-title {
        font-size: 1.22rem;
        line-height: 1.45;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 14px;
    }

    .project-more {
        color: var(--cyan);
        font-weight: 900;
        font-size: 0.95rem;
    }

    .step-box {
        padding: 22px;
        border-radius: 22px;
        background: rgba(6, 34, 40, 0.70);
        border: 1px solid rgba(255,255,255,0.10);
        margin-bottom: 14px;
    }

    .step-num {
        color: var(--pink);
        font-weight: 900;
        font-size: 1.05rem;
        margin-bottom: 5px;
    }

    .step-title {
        color: #ffffff;
        font-size: 1.15rem;
        font-weight: 900;
        margin-bottom: 5px;
    }

    .step-text {
        color: var(--muted);
        line-height: 1.6;
    }

    .footer {
        margin-top: 46px;
        padding: 24px;
        text-align: center;
        color: var(--muted);
        border-top: 1px solid rgba(101,255,242,0.25);
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }

    .stTabs [data-baseweb="tab"] {
        background: rgba(101,255,242,0.08);
        border-radius: 999px;
        color: #eaffff;
        padding: 10px 18px;
        border: 1px solid rgba(101,255,242,0.25);
    }

    .stTabs [aria-selected="true"] {
        background: rgba(255,43,214,0.20);
        border-color: rgba(255,43,214,0.55);
    }

    @media (max-width: 768px) {
        .hero {
            padding: 24px;
        }

        .info-card {
            min-height: auto;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 함수
# =========================
def render_project_card(project, year):
    title = html.escape(project["title"])
    tag = html.escape(project["tag"])
    url = project["url"]

    st.markdown(
        f"""
        <a class="project-card" href="{url}" target="_blank" rel="noopener noreferrer">
            <span class="project-year">{year}</span>
            <span class="project-tag">{tag}</span>
            <div class="project-title">{title}</div>
            <div class="project-more">결과물 보러가기 →</div>
        </a>
        """,
        unsafe_allow_html=True
    )


def render_project_grid(projects, year):
    cols = st.columns(2)
    for i, project in enumerate(projects):
        with cols[i % 2]:
            render_project_card(project, year)


def find_poster():
    candidates = [
        Path("poster.png"),
        Path("Techno love Party의 사본.png"),
        Path("Techno_love_Party.png"),
        Path("poster.jpg"),
        Path("poster.jpeg"),
    ]

    for path in candidates:
        if path.exists():
            return path
    return None


# =========================
# 히어로 영역
# =========================
today = date.today()
d_day = (EVENT_DATE - today).days
deadline_day = (DEADLINE_DATE - today).days

left, right = st.columns([1.25, 0.75], gap="large")

with left:
    st.markdown(
        """
        <div class="hero">
            <div class="neon-title">정보과학<br>탐구한마당</div>
            <div class="sub-title">우리 주변의 문제를 정보과학으로 해결하는 프로젝트 발표 행사</div>
            <div class="desc">
                앱, 프로그램, 알고리즘, 웹사이트, 데이터 분석 등 다양한 소프트웨어를 활용해
                문제 해결 방법을 만들고 공유하는 행사입니다.
                아래에서 작년과 재작년 학생들의 결과물을 먼저 살펴볼 수 있습니다.
            </div>
            <div class="badge-row">
                <span class="badge">💻 소프트웨어 활용</span>
                <span class="badge pink-badge">🚀 문제 해결 프로젝트</span>
                <span class="badge yellow-badge">🎤 3분 발표</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with right:
    poster_path = find_poster()

    if poster_path:
        st.markdown('<div class="poster-box">', unsafe_allow_html=True)
        st.image(str(poster_path), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            """
            <div class="poster-box" style="padding:34px; min-height:420px; display:flex; align-items:center; justify-content:center;">
                <div style="text-align:center;">
                    <div style="font-size:4rem;">🐱‍💻</div>
                    <div style="font-size:1.4rem; font-weight:900; color:#65fff2; margin-top:10px;">
                        poster.png
                    </div>
                    <div style="color:#b6d8dc; margin-top:8px;">
                        포스터 이미지를 같은 폴더에 넣으면 여기에 표시됩니다.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================
# 핵심 정보
# =========================
st.markdown('<div class="section-title">행사 핵심 정보</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="info-card">
            <div class="label">주제</div>
            <div class="value">자율</div>
            <div class="small">우리 주변의 다양한 문제를 찾아 해결하기</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="info-card">
            <div class="label">팀 구성</div>
            <div class="value">1~4인</div>
            <div class="small">개인 또는 팀 단위로 참여 가능</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    deadline_text = "마감 전" if deadline_day >= 0 else "마감 완료"
    st.markdown(
        f"""
        <div class="info-card">
            <div class="label">신청 마감</div>
            <div class="value">7.7.(화) 16:00</div>
            <div class="small">{deadline_text}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    event_text = f"D-{d_day}" if d_day > 0 else ("오늘 진행" if d_day == 0 else "행사 종료")
    st.markdown(
        f"""
        <div class="info-card">
            <div class="label">행사 일시</div>
            <div class="value">7.10.(금)</div>
            <div class="small">13:30 ~ 17:30 · 컴퓨터실<br>{event_text}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# 지난 결과물
# =========================
st.markdown('<div class="section-title">지난 학생 결과물 구경하기</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-caption">제목 카드를 클릭하면 학생들이 제작한 결과물 링크로 이동합니다.</div>',
    unsafe_allow_html=True
)

tab1, tab2, tab3 = st.tabs(["2025 결과물", "2024 결과물", "전체 보기"])

with tab1:
    render_project_grid(projects_2025, "2025")

with tab2:
    render_project_grid(projects_2024, "2024")

with tab3:
    render_project_grid(projects_2025, "2025")
    render_project_grid(projects_2024, "2024")

# =========================
# 참여 방법
# =========================
st.markdown('<div class="section-title">참여 흐름</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-caption">자세한 양식은 학교 홈페이지 또는 리로스쿨에서 확인하세요.</div>',
    unsafe_allow_html=True
)

s1, s2 = st.columns(2)

with s1:
    st.markdown(
        """
        <div class="step-box">
            <div class="step-num">STEP 01</div>
            <div class="step-title">팀 구성하기</div>
            <div class="step-text">1인부터 4인까지 자유롭게 팀을 구성합니다.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="step-box">
            <div class="step-num">STEP 02</div>
            <div class="step-title">신청 및 참가 계획서 제출</div>
            <div class="step-text">학교 홈페이지 또는 리로스쿨에 게시된 양식을 작성하여 제출합니다.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with s2:
    st.markdown(
        """
        <div class="step-box">
            <div class="step-num">STEP 03</div>
            <div class="step-title">활동 참여하기</div>
            <div class="step-text">2026년 7월 10일 금요일, 컴퓨터실에서 결과물을 제작합니다.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="step-box">
            <div class="step-num">STEP 04</div>
            <div class="step-title">결과물 제출 및 발표</div>
            <div class="step-text">정해진 시간까지 결과물을 제출하고, 3분 이내로 발표합니다.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# 하단
# =========================
st.markdown(
    """
    <div class="footer">
        정보과학탐구한마당 · 다양한 문제를 발견하고, 소프트웨어로 해결해보세요.
    </div>
    """,
    unsafe_allow_html=True
)
