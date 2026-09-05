# -*- coding: utf-8 -*-
"""MOA UI 다국어 문자열. UI 라벨은 사전 번역(고정), 사용자 맞춤 설명문은 Gemini가 생성."""

LANGS = {
    "ko": "한국어",
    "en": "English",
    "zh": "中文",
    "vi": "Tiếng Việt",
}

# Gemini에게 넘길 언어 표기
LANG_FULL = {
    "ko": "Korean",
    "en": "English",
    "zh": "Simplified Chinese",
    "vi": "Vietnamese",
}

S = {
    "app_title": {
        "ko": "MOA · Money On Arrival",
        "en": "MOA · Money On Arrival",
        "zh": "MOA · Money On Arrival",
        "vi": "MOA · Money On Arrival",
    },
    "tagline": {
        "ko": "계좌가 없어도, 같이 나눠 낼 수 있게",
        "en": "Split the bill even before you have a Korean bank account",
        "zh": "还没有韩国账户，也能一起分摊账单",
        "vi": "Chia tiền cùng bạn bè ngay cả khi chưa có tài khoản ngân hàng",
    },
    "nav_settle": {
        "ko": "1. 모아 정산",
        "en": "1. Settle Bridge",
        "zh": "1. 分摊结算",
        "vi": "1. Chia tiền",
    },
    "nav_nav": {
        "ko": "2. 계좌 개설 내비게이터",
        "en": "2. Account Navigator",
        "zh": "2. 开户导航",
        "vi": "2. Hướng dẫn mở tài khoản",
    },
    "nav_doc": {
        "ko": "3. 금융서류 통역 · 사기 경보",
        "en": "3. Doc Decoder & Scam Alert",
        "zh": "3. 金融文件解读与诈骗警报",
        "vi": "3. Giải mã giấy tờ & cảnh báo lừa đảo",
    },
    "nav_about": {
        "ko": "서비스 소개",
        "en": "About",
        "zh": "关于",
        "vi": "Giới thiệu",
    },
    "nav_home": {
        "ko": "홈",
        "en": "Home",
        "zh": "首页",
        "vi": "Trang chủ",
    },
    "language": {"ko": "언어", "en": "Language", "zh": "语言", "vi": "Ngôn ngữ"},
    "demo_badge": {
        "ko": "데모 모드 (AI 키 없이 예시 응답)",
        "en": "Demo mode (sample responses, no AI key)",
        "zh": "演示模式（示例回复，无 AI 密钥）",
        "vi": "Chế độ demo (phản hồi mẫu, không có khóa AI)",
    },
    "ai_on": {
        "ko": "Gemini 연결됨",
        "en": "Gemini connected",
        "zh": "已连接 Gemini",
        "vi": "Đã kết nối Gemini",
    },
}


def t(key: str, lang: str) -> str:
    return S.get(key, {}).get(lang, S.get(key, {}).get("en", key))
