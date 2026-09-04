# -*- coding: utf-8 -*-
"""Gemini 호출 래퍼.

설계 원칙
- API 키가 없거나 호출이 실패해도 앱은 절대 죽지 않는다 (심사 기간 무중단이 최우선).
- 실패 시 데모 응답으로 자동 강등하고, 화면에 그 사실을 표시한다.
- 모든 프롬프트는 KB를 근거로만 답하도록 제약하고, 확실하지 않으면 '확인 필요'라고 말하게 한다.
"""
from __future__ import annotations

import json
import os

MODEL = "gemini-2.5-flash"

SYSTEM_RULES = """You are MOA, a financial-settlement assistant for international students in Korea.
Rules you must never break:
1. Answer ONLY from the provided KNOWLEDGE BASE. If the knowledge base does not cover something,
   say plainly that it must be confirmed with the bank or the school's international office.
2. Never invent bank names, fee amounts, interest rates, or legal deadlines.
3. You are not a bank and you never move money. You only organise information and settlement records.
4. Never ask for or repeat passport numbers, alien registration numbers, account numbers,
   card numbers or passwords. If the user supplies one, tell them not to share it.
5. Write in the requested language, in short plain sentences a first-year student can read.
"""


def get_api_key() -> str | None:
    key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if key:
        return key.strip()
    try:
        import streamlit as st

        return str(st.secrets["GOOGLE_API_KEY"]).strip()
    except Exception:
        return None


def is_live() -> bool:
    return bool(get_api_key())


def _client():
    from google import genai

    return genai.Client(api_key=get_api_key())


def generate(prompt: str, images: list[tuple[bytes, str]] | None = None,
             as_json: bool = False, temperature: float = 0.3):
    """Gemini 호출. 반환값: (결과, live: bool, error: str|None)

    as_json=True 이면 dict/list 를, 아니면 문자열을 돌려준다.
    live=False 이면 데모 응답이라는 뜻이다.
    """
    if not is_live():
        return None, False, "no_api_key"

    try:
        from google.genai import types

        parts: list = [prompt]
        for data, mime in images or []:
            parts.append(types.Part.from_bytes(data=data, mime_type=mime))

        cfg = types.GenerateContentConfig(
            system_instruction=SYSTEM_RULES,
            temperature=temperature,
            response_mime_type="application/json" if as_json else "text/plain",
        )
        resp = _client().models.generate_content(model=MODEL, contents=parts, config=cfg)
        text = (resp.text or "").strip()
        if as_json:
            return json.loads(text), True, None
        return text, True, None
    except Exception as exc:  # 쿼터 초과·네트워크 장애·파싱 실패 모두 여기로
        return None, False, f"{type(exc).__name__}: {exc}"
