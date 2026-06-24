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

faq_items = [
    {
        "question": "Q1. 정보과학탐구한마당은 어떤 행사인가요?",
        "answer": """
우리 주변의 문제를 발견하고, 소프트웨어나 정보과학적 아이디어를 활용해 해결 방법을 제안하는 행사입니다.

앱, 웹사이트, 프로그램, 알고리즘, 데이터 분석, 인공지능 활용, 아두이노 등 다양한 방식으로 참여할 수 있습니다.

중요한 것은 단순히 멋진 기술을 사용하는 것이 아니라, **문제를 발견하고 그 문제를 어떻게 해결하려 했는지 보여주는 것**입니다.
"""
    },
    {
        "question": "Q2. 꼭 코딩을 잘해야 참여할 수 있나요?",
        "answer": """
아니요. 코딩 실력이 뛰어나지 않아도 참여할 수 있습니다.

직접 프로그램을 만들 수도 있지만, 다음과 같은 방식도 가능합니다.

- 앱 화면 설계하기
- 웹사이트 기획안 만들기
- 알고리즘 흐름도 만들기
- 데이터 분석 결과 발표하기
- 아두이노나 인공지능 활용 아이디어 제안하기
- 프로그램의 일부 기능만 구현하기

정보과학탐구한마당은 코딩 실력만 평가하는 행사가 아니라, **문제를 어떻게 바라보고 해결 방법을 구상했는지**를 보여주는 행사입니다.
"""
    },
    {
        "question": "Q3. 주제는 어떻게 정하면 좋나요?",
        "answer": """
먼저 “내가 평소에 불편하다고 느낀 것”을 떠올려보세요.

다음 질문에서 시작하면 주제를 찾기 쉽습니다.

- 학교에서 반복적으로 불편한 점은 없을까?
- 친구들이 자주 겪는 문제는 무엇일까?
- 우리 사회에서 해결되면 좋을 문제는 무엇일까?
- 데이터를 활용하면 더 잘 판단할 수 있는 문제는 없을까?
- 앱이나 프로그램이 있으면 더 편리해질 일이 있을까?

학교생활, 환경, 건강, 교통, 미디어, 고령화, 안전, 학습, 진로, 생활 불편 등에서 문제를 찾을 수 있습니다.
"""
    },
    {
        "question": "Q4. 주제가 작거나 평범해도 괜찮나요?",
        "answer": """
괜찮습니다. 오히려 주변에서 실제로 겪는 작은 불편함이 좋은 주제가 될 수 있습니다.

예를 들어 다음과 같은 주제도 충분히 가능합니다.

- 교내 분실물을 쉽게 찾는 방법
- 급식 대기 시간을 줄이는 방법
- 수행평가 일정을 놓치지 않게 돕는 방법
- 자습실 자리 이용을 편리하게 하는 방법
- 학교 분리수거 실수를 줄이는 방법

중요한 것은 주제가 거창한지가 아니라, **문제가 구체적이고 해결 방법이 잘 연결되어 있는지**입니다.
"""
    },
    {
        "question": "Q5. 정보과학적 해결 방법이란 무엇인가요?",
        "answer": """
정보과학적 해결 방법이란 컴퓨터, 데이터, 알고리즘, 소프트웨어, 인공지능, 센서 등을 활용해 문제를 해결하려는 방법을 말합니다.

예를 들면 다음과 같습니다.

- 조건에 따라 결과를 알려주는 프로그램 만들기
- 데이터를 분석해 문제의 원인 찾기
- 사용자가 입력한 정보를 바탕으로 맞춤형 안내 제공하기
- 센서를 이용해 상황 감지하기
- 반복되는 일을 자동화하기
- 앱이나 웹사이트로 정보를 쉽게 제공하기

꼭 어려운 기술을 써야 하는 것은 아닙니다. 문제 해결 과정이 잘 드러나면 됩니다.
"""
    },
    {
        "question": "Q6. 탐구는 어떤 순서로 진행하면 되나요?",
        "answer": """
다음 흐름으로 진행하면 좋습니다.

1. **문제 발견하기**  
   주변에서 불편하거나 개선이 필요한 문제를 찾습니다.

2. **원인 분석하기**  
   왜 이런 문제가 생기는지 조사하거나 관찰합니다.

3. **해결 방법 구상하기**  
   앱, 웹사이트, 프로그램, 알고리즘, 데이터 분석 등 어떤 방식으로 해결할지 정합니다.

4. **결과물 만들기**  
   실제 프로그램, 발표 자료, 시제품 화면, 알고리즘 설명, 데이터 분석 결과 등을 제작합니다.

5. **효과 설명하기**  
   이 방법이 문제 해결에 어떤 도움이 되는지 발표합니다.
"""
    },
    {
        "question": "Q7. 결과물은 꼭 완성된 프로그램이어야 하나요?",
        "answer": """
아닙니다. 완성도 높은 프로그램이면 좋지만, 반드시 완전한 앱이나 프로그램일 필요는 없습니다.

다음 중 한 가지 이상이 드러나면 좋습니다.

- 문제를 해결하기 위한 프로그램 화면
- 앱이나 웹사이트 시안
- 알고리즘 흐름도
- 간단한 코드 실행 결과
- 데이터 분석 결과
- 시제품 사진 또는 작동 설명
- 사용자가 이 결과물을 어떻게 활용할 수 있는지에 대한 설명

완성도보다 중요한 것은 **문제 해결 과정이 잘 보이는 것**입니다.
"""
    },
    {
        "question": "Q8. 어떤 도구를 사용하면 좋나요?",
        "answer": """
자신이 사용할 수 있는 도구를 자유롭게 선택하면 됩니다.

예를 들어 다음과 같은 도구를 활용할 수 있습니다.

- 파이썬
- 스크래치
- 엔트리
- HTML/CSS
- Streamlit
- 앱 제작 도구
- 오렌지3
- 아두이노
- 엑셀 또는 구글 스프레드시트
- Canva, Figma 등 화면 설계 도구

꼭 어려운 도구를 사용할 필요는 없습니다. 자신이 다룰 수 있는 도구로 문제 해결 과정을 잘 보여주는 것이 중요합니다.
"""
    },
    {
        "question": "Q9. 아이디어가 떠오르지 않을 때는 어떻게 하나요?",
        "answer": """
먼저 “불편했던 순간”을 적어보세요.

다음 문장을 완성해보면 주제를 찾기 쉽습니다.

- 나는 학교에서 ________할 때 불편했다.
- 친구들이 ________ 때문에 어려움을 겪는 것 같다.
- 우리 사회에서 ________ 문제가 해결되면 좋겠다.
- ________을 더 쉽고 편하게 할 수 있는 방법이 있으면 좋겠다.
- 데이터를 활용하면 ________을 더 잘 알 수 있을 것 같다.

이 문장에서 나온 불편함을 앱, 프로그램, 알고리즘, 데이터 분석 등으로 해결할 방법을 생각해보면 됩니다.
"""
    },
    {
        "question": "Q10. 주제 예시를 들어줄 수 있나요?",
        "answer": """
다음과 같은 주제를 생각해볼 수 있습니다.

- 급식 대기 시간을 줄이는 알림 시스템
- 학교 엘리베이터 불필요한 이용을 줄이는 장치
- 가짜뉴스를 판별하는 프로그램
- 시험 기간 학습 계획을 도와주는 앱
- 교내 분실물을 쉽게 찾는 웹사이트
- 고령자를 위한 복약 알림 시스템
- 환경 보호를 위한 분리수거 안내 프로그램
- 청소년 수면 습관 분석 및 개선 프로그램
- 학교 주변 소음이나 교통 문제 해결 시스템
- 진로 정보 격차를 줄이는 정보 제공 서비스

단순히 이 주제들은 예시이며, 조금 더 기발하고 재미있는 주제를 선정해보세요!
"""
    },
    {
        "question": "Q11. 프로그램이 중간에 오류가 나거나 시간 안에 다 못 만들면 어떻게 하나요?",
        "answer": """
오류가 나도 괜찮습니다. 활동 시간 안에 모든 기능을 완성하지 못해도 괜찮습니다.

중요한 것은 다음 내용을 설명할 수 있는 것입니다.

- 어떤 문제를 해결하려고 했는지
- 어떤 기능을 만들려고 했는지
- 어디까지 구현했는지
- 어떤 오류나 어려움이 있었는지
- 다음에 어떻게 보완할 수 있는지

처음부터 너무 큰 기능을 만들기보다, **핵심 기능 1~2개를 정해서 집중하는 것**이 좋습니다.
"""
    },
    {
        "question": "Q12. 팀으로 참여하면 역할을 어떻게 나누면 좋나요?",
        "answer": """
팀으로 참여할 경우 역할을 나누면 더 효율적으로 진행할 수 있습니다.

예를 들어 다음과 같이 나눌 수 있습니다.

- 문제 조사 담당
- 아이디어 및 해결 방법 설계 담당
- 코드 또는 결과물 제작 담당
- 발표 자료 제작 담당
- 발표 담당

모든 팀원이 코딩을 잘할 필요는 없습니다. 각자 잘할 수 있는 역할을 맡아 협력하면 됩니다.
"""
    },
    {
        "question": "Q13. 발표는 어떻게 하면 되나요?",
        "answer": """
3분 이내로 핵심만 발표하면 됩니다.

발표에는 다음 내용이 들어가면 좋습니다.

- 어떤 문제를 발견했는지
- 왜 이 문제가 중요하다고 생각했는지
- 어떤 정보과학적 방법으로 해결하려 했는지
- 만든 결과물이 어떻게 작동하는지
- 이 결과물이 어떤 도움이 될 수 있는지
- 아쉬운 점이나 보완하고 싶은 점은 무엇인지

발표 시간이 짧기 때문에 모든 내용을 길게 설명하기보다 핵심이 잘 보이도록 정리하는 것이 좋습니다.
"""
    },
    {
        "question": "Q14. 좋은 프로젝트의 기준은 무엇인가요?",
        "answer": """
좋은 프로젝트는 기술이 복잡한 프로젝트가 아니라, **문제와 해결 방법이 잘 연결된 프로젝트**입니다.

다음이 잘 드러나면 좋습니다.

- 해결하려는 문제가 구체적인가?
- 누가 이 문제로 불편함을 겪는가?
- 정보과학적 방법을 활용했는가?
- 결과물이 문제 해결에 도움이 되는가?
- 아이디어가 창의적인가?
- 발표에서 탐구 과정이 잘 설명되는가?
"""
    },
    {
        "question": "Q15. 처음 시작할 때 가장 먼저 해야 할 일은 무엇인가요?",
        "answer": """
가장 먼저 “문제 한 문장”을 정해보세요.

예를 들면 다음과 같습니다.

- 우리 학교 학생들은 분실물을 찾기 어렵다.
- 급식 대기 시간이 길어 불편하다.
- 수행평가 일정을 놓치는 학생들이 있다.
- 가짜뉴스를 구별하기 어려운 경우가 많다.
- 고령자는 약 복용 시간을 잊기 쉽다.

그다음 이 문제를 해결하기 위한 앱, 프로그램, 알고리즘, 데이터 분석 방법을 생각하면 됩니다.

처음부터 완벽한 결과물을 만들려고 하기보다, **작은 문제 하나를 구체적으로 해결하는 것**에서 시작해보세요.
"""
    },
]

# =========================
# CSS 디자인
# =========================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Jua&family=Gaegu:wght@400;700&display=swap');

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

    h1, h2, h3, p, div, span, button, summary, label, a {
        word-break: keep-all;
        font-family: 'Jua', 'Noto Sans KR', 'Apple SD Gothic Neo', sans-serif;
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
    font-family: 'Black Han Sans', 'Jua', 'Noto Sans KR', sans-serif;
    font-size: clamp(2.7rem, 6.5vw, 5.6rem);
    line-height: 1.05;
    font-weight: 900;
    letter-spacing: -0.02em;
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

    .faq-core {
        margin-top: 34px;
        margin-bottom: 18px;
        padding: 22px 26px;
        border-radius: 22px;
        text-align: center;
        background: rgba(6, 34, 40, 0.68);
        border: 1px solid rgba(101,255,242,0.28);
        box-shadow: 0 0 16px rgba(101,255,242,0.08);
    }

    .faq-core-title {
        color: #f4ffff;
        font-size: clamp(1.15rem, 2.8vw, 1.65rem);
        line-height: 1.55;
        font-weight: 700;
        text-shadow: 0 0 8px rgba(101,255,242,0.25);
    }

    .faq-guide {
        color: var(--muted);
        font-size: 1.02rem;
        margin-bottom: 18px;
    }

    div[data-testid="stExpander"] {
        background: rgba(6, 34, 40, 0.72);
        border: 1px solid rgba(101,255,242,0.28);
        border-radius: 18px;
        box-shadow: 0 0 16px rgba(101,255,242,0.08);
        margin-bottom: 10px;
    }

    div[data-testid="stExpander"] summary {
        color: #ffffff;
        font-weight: 900;
        font-size: 1.02rem;
    }

    div[data-testid="stExpander"] p,
    div[data-testid="stExpander"] li {
        color: #d8f4f6;
        line-height: 1.7;
        font-size: 0.98rem;
    }

    div[data-testid="stExpander"] strong {
        color: var(--yellow);
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
                아래에서 이전 참가 학생들의 결과물을 먼저 살펴볼 수 있습니다.
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
        <div class="result-highlight-title">선배들의 결과물을 보고 아이디어를 얻어보세요!</div>
        <div class="result-highlight-text">
            아래 결과물 제목 카드를 클릭하면 이전 학생들이 제작한 발표 자료와 결과물을 바로 확인할 수 있습니다.
            관심 있는 주제, 해결 방식, 발표 구성을 참고해 나만의 프로젝트를 구상해보세요!
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
# FAQ
# =========================
st.markdown(
    """
    <div class="faq-core">
        <div class="faq-core-title">
            정보과학탐구한마당은 코딩 실력 대회가 아니라,<br>
            우리 주변의 문제를 정보과학적으로 해결해보는 프로젝트 발표 행사입니다.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="section-title">자주 묻는 질문</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="faq-guide">궁금한 질문을 클릭하면 답변을 확인할 수 있습니다.</div>',
    unsafe_allow_html=True
)

for item in faq_items:
    with st.expander(item["question"]):
        st.markdown(item["answer"])

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
