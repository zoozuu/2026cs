import streamlit as st
from pathlib import Path
from datetime import date
import html
import base64

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
# 기본 데이터
# =========================
EVENT_DATE = date(2026, 7, 10)
DEADLINE_DATE = date(2026, 7, 7)
RIRO_URL = "https://riro.kr/?347eaa"


def static_url(relative_path):
    """
    static 폴더 안 파일을 Streamlit 앱에서 연결하기 위한 경로
    예: static/results/2025/a.pdf → app/static/results/2025/a.pdf
    """
    return f"app/static/{relative_path}"


projects_2025 = [
    {
        "title": "도시소음 회피 가이드 시스템",
        "file": "results/2025/noise-avoidance-guide.pdf",
        "tag": "생활 문제 해결"
    },
    {
        "title": "가짜뉴스 판별 프로그램",
        "file": "results/2025/fake-news-detector.pdf",
        "tag": "인공지능 · 미디어"
    },
    {
        "title": "고등학교 내에서 발생하는 입시정보격차 해소; 스마트 입시정보 알림 키오스크 시스템",
        "file": "results/2025/smart-admission-info-kiosk.pdf",
        "tag": "교육 · 정보격차"
    },
    {
        "title": "고령화 사회에서 노인성 질환 조기 진단을 위한 활성 산소 바이오센서 모니터링 시스템 구현",
        "file": "results/2025/reactive-oxygen-biosensor.pdf",
        "tag": "바이오센서 · 헬스케어"
    },
    {
        "title": "고령 환자를 위한 정보과학 기반 복약 알림 시스템",
        "file": "results/2025/medicine-reminder-system.pdf",
        "tag": "헬스케어 · 알림 시스템"
    },
]

projects_2024 = [
    {
        "title": "필터 버블 현상 개선 프로그램",
        "file": "results/2024/filter-bubble-html.pdf",
        "tag": "HTML"
    },
    {
        "title": "학교 엘레베이터 불필요한 탑승 제한하기",
        "file": "results/2024/school-elevator-arduino.pdf",
        "tag": "아두이노"
    },
    {
        "title": "고령화시대에 올바른 약물 사용방안",
        "file": "results/2024/proper-medication-orange-python.pdf",
        "tag": "오렌지3 · 파이썬"
    },
    {
        "title": "자율주행자동차의 딜레마 상황에서의 윤리적 판단 문제",
        "file": "results/2024/autonomous-car-ethics-python.pdf",
        "tag": "파이썬"
    },
    {
        "title": "현대 사회의 노인 치매 발생 해결하기",
        "file": "results/2024/elderly-dementia-python.pdf",
        "tag": "파이썬"
    },
    {
        "title": "청년 실업 문제 해결",
        "file": "results/2024/youth-unemployment-website-plan.pdf",
        "tag": "웹사이트 기획"
    },
    {
        "title": "자율주행자동차 해킹 해결방안",
        "file": "results/2024/autonomous-car-hacking-plan.pdf",
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

    .poster-click-guide {
        color: var(--yellow);
        font-weight: 900;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 0 0 10px rgba(255,242,122,0.5);
    }

    .poster-thumb {
        width: 100%;
        border-radius: 24px;
        border: 1px solid rgba(101,255,242,0.45);
        box-shadow: 0 0 26px rgba(101,255,242,0.24);
        cursor: zoom-in;
        transition: 0.2s ease;
    }

    .poster-thumb:hover {
        transform: scale(1.015);
        box-shadow:
            0 0 34px rgba(101,255,242,0.32),
            0 0 24px rgba(255,43,214,0.20);
    }

    .poster-modal-check {
        display: none;
    }

    .poster-modal {
        display: none;
        position: fixed;
        z-index: 999999;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.88);
        backdrop-filter: blur(6px);
        align-items: center;
        justify-content: center;
        padding: 28px;
    }

    .poster-modal-check:checked + .poster-modal {
        display: flex;
    }

    .poster-modal img {
        max-width: min(92vw, 760px);
        max-height: 92vh;
        border-radius: 20px;
        box-shadow:
            0 0 30px rgba(101,255,242,0.45),
            0 0 45px rgba(255,43,214,0.25);
    }

    .poster-close {
        position: fixed;
        top: 24px;
        right: 30px;
        color: white;
        font-size: 2.2rem;
        font-weight: 900;
        cursor: pointer;
        text-shadow: 0 0 14px rgba(101,255,242,0.8);
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

    .apply-box {
        margin-top: 28px;
        margin-bottom: 14px;
        padding: 28px;
        border-radius: 26px;
        background:
            linear-gradient(135deg, rgba(255,43,214,0.18), rgba(101,255,242,0.12)),
            rgba(5, 29, 35, 0.86);
        border: 1px solid rgba(255,43,214,0.45);
        box-shadow:
            0 0 28px rgba(255,43,214,0.16),
            0 0 18px rgba(101,255,242,0.12);
        text-align: center;
    }

    .apply-title {
        color: #ffffff;
        font-size: clamp(1.6rem, 4vw, 2.5rem);
        font-weight: 900;
        margin-bottom: 10px;
        text-shadow:
            0 0 14px rgba(255,43,214,0.7),
            0 0 20px rgba(101,255,242,0.35);
    }

    .apply-text {
        color: var(--muted);
        font-size: 1.05rem;
        margin-bottom: 20px;
        line-height: 1.6;
    }

    .apply-button {
        display: inline-block;
        padding: 15px 28px;
        border-radius: 999px;
        background: linear-gradient(135deg, #ff2bd6, #65fff2);
        color: #061014 !important;
        font-size: 1.15rem;
        font-weight: 900;
        text-decoration: none !important;
        box-shadow:
            0 0 20px rgba(255,43,214,0.35),
            0 0 22px rgba(101,255,242,0.25);
        transition: 0.18s ease;
    }

    .apply-button:hover {
        transform: translateY(-3px);
        filter: brightness(1.12);
    }

    .contact-text {
        margin-top: 18px;
        color: #fffbd0;
        font-size: 1.05rem;
        font-weight: 900;
        text-shadow: 0 0 10px rgba(255,242,122,0.35);
    }

    .result-highlight {
        margin-top: 8px;
        margin-bottom: 24px;
        padding: 26px;
        border-radius: 26px;
        background:
            linear-gradient(135deg, rgba(101,255,242,0.16), rgba(255,43,214,0.16)),
            rgba(3, 18, 24, 0.82);
        border: 1px solid rgba(101,255,242,0.50);
        box-shadow:
            0 0 30px rgba(101,255,242,0.18),
            inset 0 0 26px rgba(255,43,214,0.06);
    }

    .result-highlight-title {
        color: #ffffff;
        font-size: clamp(1.45rem, 3.5vw, 2.15rem);
        font-weight: 900;
        margin-bottom: 10px;
        text-shadow:
            0 0 12px rgba(101,255,242,0.75),
            0 0 22px rgba(255,43,214,0.32);
    }

    .result-highlight-text {
        color: var(--yellow);
        font-size: 1.12rem;
        font-weight: 900;
        line-height: 1.6;
        text-shadow: 0 0 10px rgba(255,242,122,0.38);
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

        .poster-modal img {
            max-width: 96vw;
            max-height: 88vh;
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
    url = static_url(project["file"])

    st.markdown(
        f"""
        <a class="project-card" href="{url}" target="_blank" rel="noopener noreferrer">
            <span class="project-year">{year}</span>
            <span class="project-tag">{tag}</span>
            <div class="project-title">{title}</div>
            <div class="project-more">클릭해서 결과물 확인하기 →</div>
        </a>
        """,
        unsafe_allow_html=True
    )


def render_project_grid(projects, year):
    cols = st.columns(2)
    for i, project in enumerate(projects):
        with cols[i % 2]:
            render_project_card(project, year)


def image_to_base64(path):
    suffix = path.suffix.lower()

    if suffix in [".jpg", ".jpeg"]:
        mime = "image/jpeg"
    else:
        mime = "image/png"

    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    return f"data:{mime};base64,{encoded}"


def find_poster():
    candidates = [
        Path("static/poster.png"),
        Path("poster.png"),
        Path("static/poster.jpg"),
        Path("poster.jpg"),
        Path("static/poster.jpeg"),
        Path("poster.jpeg"),
    ]

    for path in candidates:
        if path.exists():
            return path
    return None


def render_clickable_poster(path):
    img_src = image_to_base64(path)

    st.markdown(
        f"""
        <div class="poster-click-guide">포스터를 클릭하면 크게 볼 수 있어요 🔍</div>

        <label for="poster-modal-toggle">
            <img class="poster-thumb" src="{img_src}">
        </label>

        <input type="checkbox" id="poster-modal-toggle" class="poster-modal-check">

        <div class="poster-modal">
            <label for="poster-modal-toggle" class="poster-close">×</label>
            <label for="poster-modal-toggle">
                <img src="{img_src}">
            </label>
        </div>
        """,
        unsafe_allow_html=True
    )


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
        render_clickable_poster(poster_path)
    else:
        st.markdown(
            """
            <div class="poster-click-guide">포스터 이미지 준비 중</div>
            <div style="padding:34px; min-height:420px; display:flex; align-items:center; justify-content:center; border-radius:24px; border:1px solid rgba(101,255,242,0.45); box-shadow:0 0 26px rgba(101,255,242,0.24);">
                <div style="text-align:center;">
                    <div style="font-size:4rem;">🐱‍💻</div>
                    <div style="font-size:1.4rem; font-weight:900; color:#65fff2; margin-top:10px;">
                        static/poster.png
                    </div>
                    <div style="color:#b6d8dc; margin-top:8px;">
                        포스터 이미지를 static 폴더에 넣으면 여기에 표시됩니다.
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
# 신청하기
# =========================
st.markdown(
    f"""
    <div class="apply-box">
        <div class="apply-title">지금 바로 신청하기!</div>
        <div class="apply-text">
            참가를 희망하는 학생은 리로스쿨에서 신청하고 참가 계획서를 제출해주세요.
        </div>
        <a class="apply-button" href="{RIRO_URL}" target="_blank" rel="noopener noreferrer">
            리로스쿨 신청 페이지로 이동하기 →
        </a>
        <div class="contact-text">
            문의: 3층 진로상담복지부 김지우T
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# 지난 학생 결과물
# =========================
st.markdown('<div class="section-title">학생 결과물 확인하기</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="result-highlight">
        <div class="result-highlight-title">작년·재작년 선배들은 어떤 문제를 해결했을까요?</div>
        <div class="result-highlight-text">
            아래 결과물 제목 카드를 클릭하면 이전 학생들이 제작한 발표 자료와 결과물을 바로 확인할 수 있습니다.
            아이디어를 정하기 전에 꼭 한 번 둘러보세요!
        </div>
    </div>
    """,
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
        정보과학탐구한마당 · 다양한 문제를 발견하고, 소프트웨어로 해결해보세요.<br>
        문의: 3층 진로상담복지부 김지우T
    </div>
    """,
    unsafe_allow_html=True
)
