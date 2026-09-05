# -*- coding: utf-8 -*-
"""MOA · Money On Arrival
2026 금융 AI Challenge — 외국인 유학생 금융 정착 AI Agent (MVP)

UI: Canva 'Moa' 브랜드 시스템 (오렌지 그라데이션) 적용
실행: streamlit run app.py
"""
from __future__ import annotations

import datetime as dt

import streamlit as st

from moa import demo, kb, llm, settle
from moa.i18n import LANG_FULL, LANGS, t

st.set_page_config(page_title="MOA · Money On Arrival", page_icon="🪙", layout="wide")

# ------------------------------------------------------------------ 브랜드 시스템
CSS = """
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css');
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;800&display=swap');

:root{
  --moa-orange:#FE670F;
  --moa-amber:#FD9520;
  --moa-yellow:#F7C536;
  --moa-coral:#FB4658;
  --moa-magenta:#FF3C8D;
  --moa-ink:#100E0E;
  --moa-muted:#6B6B70;
  --moa-line:#ECECEF;
  --moa-bg:#F8F8F9;
  --moa-grad:linear-gradient(115deg,#FE670F 0%,#FD9520 58%,#F7C536 100%);
  --moa-grad-hot:linear-gradient(115deg,#FF3C8D 0%,#FB4658 40%,#FE670F 100%);
}

.stApp{background:var(--moa-bg);}
html, body, .stApp, .stApp p, .stApp span, .stApp div, .stApp label,
.stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp li, .stApp td, .stApp th{
  font-family:'Pretendard','Poppins',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
}
.block-container{padding-top:1.6rem; padding-bottom:3rem; max-width:1140px;}
.stApp h3, .stApp h4{color:var(--moa-ink); letter-spacing:-.02em;}

/* ---------- 워드마크 ---------- */
.moa-mark{font-family:'Poppins',sans-serif; font-weight:800; letter-spacing:-.03em;}

/* ---------- 히어로 ---------- */
.moa-hero{
  position:relative; overflow:hidden;
  background:var(--moa-grad); color:#fff;
  padding:30px 34px; border-radius:26px; margin-bottom:20px;
  box-shadow:0 18px 40px -22px rgba(254,103,15,.75);
}
.moa-hero::after{
  content:""; position:absolute; right:-70px; top:-90px; width:300px; height:300px;
  border-radius:50%; background:radial-gradient(circle at 35% 35%,rgba(255,255,255,.45),rgba(255,255,255,0) 62%);
}
.moa-hero h1{margin:0; font-size:2.1rem; color:#fff; font-family:'Poppins',sans-serif;
  font-weight:800; letter-spacing:-.035em; line-height:1.12;}
.moa-hero h1 small{display:block; font-size:1.02rem; font-weight:600; opacity:.95;
  letter-spacing:0; margin-top:4px;}
.moa-hero div[data-testid]{margin:0 !important; padding:0 !important;}
.moa-hero div[data-testid] a{display:none;}
.moa-hero p{margin:10px 0 0; font-size:1rem; opacity:.96; max-width:640px; line-height:1.55;}
.moa-hero .moa-kicker{display:inline-block; background:rgba(255,255,255,.22); color:#fff;
  padding:4px 13px; border-radius:999px; font-size:.76rem; font-weight:700;
  margin-bottom:12px; backdrop-filter:blur(2px);}
.moa-hero.slim{padding:20px 26px; border-radius:20px; margin-bottom:16px;}
.moa-hero.slim h1{font-size:1.4rem;}
.moa-hero.slim p{margin-top:6px; font-size:.92rem;}

/* ---------- 카드 ---------- */
.moa-card{border:1px solid var(--moa-line); border-radius:18px; padding:18px 20px;
  margin-bottom:12px; background:#fff; box-shadow:0 2px 10px -6px rgba(16,14,14,.16);}
.moa-card.warn{border:none; border-left:5px solid var(--moa-amber); background:#FFF7EC;}
.moa-card.danger{border:none; border-left:5px solid var(--moa-coral); background:#FFF1F3;}
.moa-card.ok{border:none; border-left:5px solid var(--moa-orange); background:#FFF3EA;}
.moa-card b{color:var(--moa-ink);}

.moa-feature{border:1px solid var(--moa-line); border-radius:20px; padding:20px;
  background:#fff; min-height:196px; box-shadow:0 2px 12px -8px rgba(16,14,14,.2);}
.moa-feature .num{font-family:'Poppins',sans-serif; font-weight:800; font-size:.8rem;
  color:#fff; background:var(--moa-grad); width:30px; height:30px; border-radius:10px;
  display:flex; align-items:center; justify-content:center; margin-bottom:12px;}
.moa-feature h4{margin:0 0 8px; font-size:1.05rem; letter-spacing:-.02em;}
.moa-feature p{margin:0; font-size:.88rem; color:var(--moa-muted); line-height:1.6;}

/* ---------- 배지 / 금액 ---------- */
.moa-pill{display:inline-block; padding:3px 11px; border-radius:999px; font-size:.74rem;
  font-weight:700; background:#FFF0E4; color:#C24A00; margin-right:6px;}
.moa-pill.grey{background:#F1F1F3; color:#5B5B61;}
.moa-pill.hot{background:var(--moa-grad-hot); color:#fff;}
.moa-amt{font-family:'Poppins',sans-serif; font-size:1.35rem; font-weight:800;
  color:var(--moa-ink); letter-spacing:-.02em;}
.moa-amt.plus{background:var(--moa-grad); -webkit-background-clip:text;
  -webkit-text-fill-color:transparent; background-clip:text;}
.moa-sub{font-size:.78rem; color:var(--moa-muted);}

/* ---------- 스텝 헤딩 ---------- */
.moa-step{display:flex; align-items:center; gap:10px; margin:24px 0 10px;}
.moa-step .n{font-family:'Poppins',sans-serif; font-weight:800; font-size:.82rem; color:#fff;
  background:var(--moa-ink); min-width:26px; height:26px; border-radius:9px;
  display:flex; align-items:center; justify-content:center;}
.moa-step .tx{font-weight:700; font-size:1.02rem; color:var(--moa-ink); letter-spacing:-.02em;}

/* ---------- 타임라인 ---------- */
.moa-tl{border:1px solid var(--moa-line); border-radius:16px; padding:14px 12px;
  background:#fff; min-height:124px;}
.moa-tl.done{background:var(--moa-grad); border:none; color:#fff;}
.moa-tl.done .d, .moa-tl.done b{color:#fff; opacity:.95;}
.moa-tl b{display:block; font-size:.83rem; line-height:1.35; margin-top:6px; color:var(--moa-ink);}
.moa-tl .d{font-size:.72rem; color:var(--moa-muted); margin-top:6px;}

/* ---------- 버튼 ---------- */
div.stButton > button{border-radius:999px; font-weight:700; border:1px solid var(--moa-line);
  padding:.5rem 1.1rem; transition:all .15s ease;}
div.stButton > button:hover{border-color:var(--moa-orange); color:var(--moa-orange);}
div.stButton > button[kind="primary"]{background:var(--moa-grad); border:none; color:#fff;
  box-shadow:0 10px 22px -14px rgba(254,103,15,.95);}
div.stButton > button[kind="primary"]:hover{filter:brightness(1.06); color:#fff;}

/* ---------- 사이드바 ---------- */
section[data-testid="stSidebar"]{background:#fff; border-right:1px solid var(--moa-line);}
.moa-side-logo{background:var(--moa-grad); color:#fff; border-radius:18px; padding:16px 18px;
  margin-bottom:14px;}
.moa-side-logo .w{font-family:'Poppins',sans-serif; font-weight:800; font-size:1.5rem;
  letter-spacing:-.03em; line-height:1;}
.moa-side-logo .s{font-size:.74rem; opacity:.95; margin-top:4px; font-weight:600;}

/* ---------- 폼 요소 ---------- */
.stTextInput input, .stTextArea textarea, .stDateInput input{border-radius:12px !important;}
div[data-baseweb="select"] > div{border-radius:12px !important;}
.stFileUploader section{border-radius:16px; border:1.5px dashed #E2C6B2; background:#FFFAF6;}
div[data-testid="stExpander"]{border-radius:16px; border:1px solid var(--moa-line);
  background:#fff; overflow:hidden;}
hr{border-color:var(--moa-line);}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


def hero(title: str, subtitle: str, kicker: str = "", slim: bool = False):
    k = f"<span class='moa-kicker'>{kicker}</span>" if kicker else ""
    st.markdown(
        f"<div class='moa-hero{' slim' if slim else ''}'>{k}<h1>{title}</h1>"
        f"<p>{subtitle}</p></div>",
        unsafe_allow_html=True,
    )


def step(n: str, text: str):
    st.markdown(f"<div class='moa-step'><span class='n'>{n}</span>"
                f"<span class='tx'>{text}</span></div>", unsafe_allow_html=True)


# ------------------------------------------------------------------ 상태
def init_state():
    ss = st.session_state
    ss.setdefault("lang", "ko")
    ss.setdefault("page", "home")
    ss.setdefault("members", [
        {"name": "Anna (내 친구·계좌 없음)", "has_account": False, "lang": "en"},
        {"name": "민수", "has_account": True, "lang": "ko"},
        {"name": "Linh", "has_account": False, "lang": "vi"},
    ])
    ss.setdefault("bill_items", [])
    ss.setdefault("ledger", [])
    ss.setdefault("last_error", None)


init_state()
L = st.session_state.lang


def go(page: str):
    st.session_state.page = page
    st.rerun()


def note_error(err):
    if err and err != "no_api_key":
        st.session_state.last_error = err


def ai_or_demo(prompt, images=None, as_json=False, fallback=None):
    out, live, err = llm.generate(prompt, images=images, as_json=as_json)
    note_error(err)
    if out is None:
        return fallback, False
    return out, True


# ------------------------------------------------------------------ 사이드바
NAV = ["home", "settle", "nav", "doc", "about"]
NAV_KEY = {"home": "nav_home", "settle": "nav_settle", "nav": "nav_nav",
           "doc": "nav_doc", "about": "nav_about"}

with st.sidebar:
    st.markdown(
        "<div class='moa-side-logo'><div class='w'>Moa</div>"
        "<div class='s'>Money On Arrival</div></div>", unsafe_allow_html=True)

    st.session_state.lang = st.selectbox(
        t("language", L), list(LANGS.keys()),
        format_func=lambda k: LANGS[k],
        index=list(LANGS.keys()).index(L),
    )
    L = st.session_state.lang

    st.session_state.page = st.radio(
        "Menu", NAV,
        format_func=lambda k: t(NAV_KEY[k], L),
        index=NAV.index(st.session_state.page),
        label_visibility="collapsed",
    )
    st.divider()
    if llm.is_live():
        st.success(t("ai_on", L), icon="✅")
    else:
        st.info(t("demo_badge", L), icon="🧪")
    if st.session_state.last_error:
        with st.expander("AI 오류 로그"):
            st.code(st.session_state.last_error)
    st.caption(f"KB 기준일 {kb.KB_UPDATED}")

page = st.session_state.page


# ================================================================== 0. 홈
FEATURES = [
    ("settle", "MOA 정산",
     "계좌가 아직 없는 친구도 빠지지 않고 나눠 낼 수 있게, 영수증을 읽어 분배하고 장부에 남깁니다."),
    ("nav", "계좌 개설 Navi",
     "지금 상황에서 계좌를 열려면 무엇부터 해야 하는지, 지식베이스를 근거로 모국어로 안내합니다."),
    ("doc", "금융 서류 통역 · 사기 경보",
     "서류나 금융 메시지를 올리면 모국어로 풀어 설명하고, 사기 신호가 있으면 경고합니다."),
]


def page_home():
    hero(f"Moa <small>Money On Arrival</small>", t("tagline", L),
         kicker="2026 금융 AI Challenge")

    st.markdown(
        "<div class='moa-card'><b>Welcome to Our Society</b><br>"
        "<span style='color:var(--moa-muted)'>계좌가 아직 없는 외국인 친구도 빠지지 않고 나눠 낼 수 있게, "
        "영수증을 읽어 분배하고 정산 장부에 남깁니다. "
        "MOA는 돈을 직접 옮기지 않고 <b>‘누가 누구에게 얼마’</b>만 기록합니다.</span></div>",
        unsafe_allow_html=True)

    step("3", "가지 주요 기능")
    st.caption("한국에 막 도착한 외국인 유학생이 은행 계좌를 갖기 전까지 "
               "금융 공백기를 버티게 해주는 AI 에이전트입니다.")

    cols = st.columns(3)
    for i, ((key, name, desc), col) in enumerate(zip(FEATURES, cols), start=1):
        with col:
            st.markdown(
                f"<div class='moa-feature'><div class='num'>{i}</div>"
                f"<h4>{name}</h4><p>{desc}</p></div>", unsafe_allow_html=True)
            if st.button(f"{name} →", key=f"go_{key}", use_container_width=True):
                go(key)

    st.markdown("")
    st.markdown(
        "<div class='moa-hero slim' style='background:var(--moa-grad-hot)'>"
        "<h1>IT’S HERE &nbsp;<span class='moa-mark'>Moa</span></h1>"
        "<p>AI 키가 없어도 데모 응답으로 전체 흐름을 그대로 시연할 수 있습니다.</p></div>",
        unsafe_allow_html=True)


# ================================================================== 1. 모아 정산
def page_settle():
    import pandas as pd

    hero(t("nav_settle", L),
         "계좌가 아직 없는 친구도 빠지지 않고 나눠 낼 수 있게, 영수증을 읽어 분배하고 정산 장부에 "
         "남깁니다. MOA는 돈을 직접 옮기지 않고 ‘누가 누구에게 얼마’만 기록합니다.", slim=True)

    # --- Step 1. 멤버
    step("1", "함께 낸 사람")
    mdf = pd.DataFrame(st.session_state.members)
    mdf = st.data_editor(
        mdf, num_rows="dynamic", use_container_width=True, key="member_editor",
        column_config={
            "name": st.column_config.TextColumn("이름", width="medium"),
            "has_account": st.column_config.CheckboxColumn("한국 계좌 있음"),
            "lang": st.column_config.SelectboxColumn("언어", options=list(LANGS.keys())),
        },
    )
    members = [settle.Member(str(r["name"]).strip(), bool(r["has_account"]), str(r["lang"]))
               for _, r in mdf.iterrows() if str(r.get("name", "")).strip()]
    st.session_state.members = [m.__dict__ for m in members]
    if len(members) < 2:
        st.warning("사람을 2명 이상 입력해 주세요.")
        return
    names = [m.name for m in members]
    no_acc = [m.name for m in members if not m.has_account]
    if no_acc:
        st.markdown(
            f"<div class='moa-card warn'>계좌가 없는 멤버: <b>{', '.join(no_acc)}</b> — "
            "이 사람들의 몫은 대납자에게 넘기고 <b>이연 정산(deferred)</b>으로 장부에 남깁니다.</div>",
            unsafe_allow_html=True)

    # --- Step 2. 영수증
    step("2", "영수증 읽기")
    c1, c2 = st.columns([3, 2])
    with c1:
        up = st.file_uploader("영수증 사진 (JPG/PNG)", type=["jpg", "jpeg", "png"])
    with c2:
        st.write("")
        st.write("")
        run = st.button("🔍 영수증 분석", use_container_width=True, type="primary")

    if run:
        images = None
        if up is not None:
            images = [(up.getvalue(), up.type or "image/jpeg")]
            st.image(up, width=260)
        prompt = (
            "Read this Korean receipt image and extract the line items.\n"
            "Return JSON exactly: {\"store\":str,\"date\":\"YYYY-MM-DD\",\"currency\":\"KRW\","
            "\"items\":[{\"name\":str,\"amount\":int}],\"total\":int}\n"
            "Amounts are Korean won integers with no separators. "
            "If the image is unreadable, return items as an empty list."
        )
        if images is None:
            parsed, live = demo.DEMO_RECEIPT, False
            st.info("샘플 영수증으로 시연합니다. 실제 영수증 사진을 올리면 AI가 읽습니다.", icon="🧪")
        else:
            parsed, live = ai_or_demo(prompt, images=images, as_json=True,
                                      fallback=demo.DEMO_RECEIPT)
            if not live:
                st.info("데모 영수증 데이터를 불러왔습니다 (AI 키 미연결 또는 호출 실패).", icon="🧪")
        rows = []
        for it in (parsed or {}).get("items", []):
            row = {"항목": it.get("name", ""), "금액": int(it.get("amount", 0) or 0)}
            for n in names:
                row[n] = True
            rows.append(row)
        st.session_state.bill_items = rows

    step("3", "항목 확인 · 누가 먹었는지 체크")
    base = st.session_state.bill_items or [{"항목": "", "금액": 0, **{n: True for n in names}}]
    idf = pd.DataFrame(base)
    for n in names:
        if n not in idf.columns:
            idf[n] = True
    idf = idf[["항목", "금액"] + names]
    idf = st.data_editor(
        idf, num_rows="dynamic", use_container_width=True, key="item_editor",
        column_config={"금액": st.column_config.NumberColumn("금액(원)", min_value=0, step=100)},
    )
    st.session_state.bill_items = idf.to_dict("records")

    items = []
    for _, r in idf.iterrows():
        amt = int(r["금액"] or 0)
        if amt <= 0:
            continue
        parts = [n for n in names if bool(r.get(n))]
        items.append(settle.Item(str(r["항목"]), amt, parts or names))
    if not items:
        st.info("금액이 있는 항목을 1개 이상 입력하면 정산이 계산됩니다.")
        return

    total = sum(i.amount for i in items)
    st.markdown(
        f"<div class='moa-card'><span class='moa-sub'>합계</span><br>"
        f"<span class='moa-amt plus'>{settle.won(total)}</span></div>",
        unsafe_allow_html=True)

    # --- Step 4. 대납자
    step("4", "실제로 결제한 사람")
    payer = st.selectbox("대납자", names,
                         index=next((i for i, m in enumerate(members) if m.has_account), 0))
    title = st.text_input("정산 이름", "저녁 모임")
    date = st.date_input("날짜", dt.date.today()).isoformat()

    bal = settle.balances(items, members, payer)
    step("5", "정산 결과")
    cols = st.columns(min(len(names), 4))
    for i, m in enumerate(members):
        amt = bal[m.name]
        with cols[i % len(cols)]:
            if m.name == payer:
                st.markdown(
                    f"<div class='moa-card ok'><b>{m.name}</b><br>"
                    f"<span class='moa-pill hot'>대납자</span>"
                    f"<br><span class='moa-amt plus'>+{settle.won(-amt)}</span><br>"
                    "<span class='moa-sub'>받을 금액</span></div>",
                    unsafe_allow_html=True)
            else:
                tag = ("<span class='moa-pill'>즉시 이체</span>" if m.has_account
                       else "<span class='moa-pill grey'>계좌 개설 후 정산</span>")
                st.markdown(
                    f"<div class='moa-card'><b>{m.name}</b><br>{tag}<br>"
                    f"<span class='moa-amt'>{settle.won(amt)}</span><br>"
                    "<span class='moa-sub'>보낼 금액</span></div>",
                    unsafe_allow_html=True)

    if st.button("📒 정산 장부에 기록하고 요청 메시지 만들기", type="primary"):
        rows = settle.build_ledger(items, members, payer, title, date)
        st.session_state.ledger.extend(rows)
        by_lang = {m.name: m.lang for m in members}
        step("6", "각 멤버에게 보낼 메시지")
        for r in rows:
            lg = by_lang.get(r["from"], "en")
            prompt = (
                f"Write a short, friendly settlement request message in {LANG_FULL[lg]}.\n"
                f"Recipient: {r['from']}. They owe {r['amount']} KRW to {r['to']} "
                f"for '{title}' on {date}.\n"
                + ("They do NOT have a Korean bank account yet, so say the amount is recorded "
                   "in the shared ledger and will be settled once their account is open. "
                   "Reassure them this is normal and they are not being left out.\n"
                   if r["status"] == "deferred" else
                   "They have a Korean bank account, so ask them to transfer it when convenient.\n")
                + "3 sentences maximum. No bank account numbers. Plain text only."
            )
            fb = (f"[{LANGS[lg]}] {r['from']}, {title} ({date}) — {settle.won(r['amount'])}. "
                  + ("계좌가 생기면 정산할 수 있게 장부에 적어 뒀어요. 지금은 신경 쓰지 않아도 돼요."
                     if r["status"] == "deferred" else "편할 때 보내주면 돼요!"))
            msg, live = ai_or_demo(prompt, fallback=fb)
            st.markdown(f"<div class='moa-card'><b>→ {r['from']}</b> "
                        f"<span class='moa-pill grey'>{LANGS[lg]}</span></div>",
                        unsafe_allow_html=True)
            st.code(msg, language=None)

    # --- 장부
    if st.session_state.ledger:
        step("📒", "정산 장부 (미정산)")
        ldf = pd.DataFrame(st.session_state.ledger)
        st.dataframe(ldf, use_container_width=True, hide_index=True)
        net = settle.net_summary(st.session_state.ledger)
        st.write(" · ".join(f"**{k}** {settle.won(v)}" for k, v in net.items()) or "-")
        if st.button("장부 비우기"):
            st.session_state.ledger = []
            st.rerun()


# ============================================================ 2. 계좌 개설 내비게이터
def page_navigator():
    hero(t("nav_nav", L),
         "지금 내 상황에서 계좌를 열려면 무엇부터 해야 하는지, 지식베이스를 근거로 모국어로 안내합니다.",
         slim=True)

    step("1", "내 상황 입력")
    c1, c2, c3 = st.columns(3)
    with c1:
        visa = st.selectbox("체류자격", ["D-2 유학", "D-4 어학연수", "D-10 구직", "기타"])
        arrived = st.date_input("입국일", dt.date.today() - dt.timedelta(days=10))
    with c2:
        arc = st.selectbox("외국인등록증(ARC)",
                           ["아직 신청 안 함", "신청함 · 수령 대기", "수령 완료"])
        phone = st.selectbox("본인 명의 휴대폰", ["없음", "선불 유심 개통", "후불 요금제 개통"])
    with c3:
        univ = st.text_input("학교 (선택)", "")
        region = st.text_input("지역 (선택)", "")

    dorm = st.checkbox("기숙사 입사확인서 또는 임대차계약서가 있다")
    enroll = st.checkbox("재학(입학) 증명서가 있다")

    # 진행 단계 시각화
    done = {"arrival": True,
            "sim": phone != "없음",
            "arc_apply": arc != "아직 신청 안 함",
            "limit_account": False,
            "arc_issue": arc == "수령 완료",
            "full_account": False}
    step("2", "정착 타임라인")
    tl = st.columns(len(kb.JOURNEY_STEPS))
    for col, stp in zip(tl, kb.JOURNEY_STEPS):
        is_done = done.get(stp["key"])
        mark = "✅" if is_done else "⬜"
        col.markdown(
            f"<div class='moa-tl{' done' if is_done else ''}'>{mark}"
            f"<b>{stp['ko']}</b><div class='d'>{stp['days']}</div></div>",
            unsafe_allow_html=True)

    st.markdown("")
    if st.button("🧭 내 상황에 맞는 다음 단계 받기", type="primary"):
        days = (dt.date.today() - arrived).days
        profile = (f"visa={visa}, days_since_arrival={days}, ARC={arc}, phone={phone}, "
                   f"university={univ or 'unknown'}, region={region or 'unknown'}, "
                   f"has_residence_proof={dorm}, has_enrollment_certificate={enroll}")
        prompt = (
            "KNOWLEDGE BASE:\n" + kb.kb_context() + "\n\n"
            f"STUDENT PROFILE: {profile}\n\n"
            f"Write a personalised action guide in {LANG_FULL[L]} with these sections, "
            "using markdown headings:\n"
            "1. Where you are now (2 sentences)\n"
            "2. Next 3 actions, in order, each one concrete sentence\n"
            "3. Documents to bring\n"
            "4. Expected timing\n"
            "5. Watch out for (include the passport-name-match rule and the account-lending warning)\n"
            "Only use facts from the knowledge base. Where the knowledge base says it varies by "
            "bank, say the student must call the branch first. Do not name specific banks "
            "except where the knowledge base does."
        )
        out, live = ai_or_demo(prompt, fallback=demo.DEMO_NAVIGATOR["ko"])
        if not live:
            st.info("데모 응답입니다 (AI 키 미연결 또는 호출 실패).", icon="🧪")
        st.markdown(out)

    with st.expander("📚 이 안내의 근거 (지식베이스 원문)"):
        for r in kb.ACCOUNT_RULES:
            st.markdown(f"**{r['topic']}** — {r['fact']}  \n"
                        f"<span class='moa-sub'>출처: {r['source']} · "
                        f"확신도: {r['confidence']}</span>", unsafe_allow_html=True)


# ======================================================= 3. 금융서류 통역 · 사기 경보
def page_decoder():
    hero(t("nav_doc", L),
         "은행 서류나 낯선 금융 메시지를 올리면 모국어로 풀어 설명하고, 사기 신호가 있으면 경고합니다.",
         slim=True)

    step("1", "서류 또는 메시지 올리기")
    up = st.file_uploader("서류·화면 캡처 (JPG/PNG)", type=["jpg", "jpeg", "png"], key="doc_up")
    txt = st.text_area("또는 받은 메시지를 붙여넣기",
                       placeholder="예) 계좌를 빌려주면 하루 30만원을 드립니다. 통장과 카드만 보내주세요.",
                       height=110)

    if st.button("🔎 해석하기", type="primary"):
        images = [(up.getvalue(), up.type or "image/jpeg")] if up else None
        prompt = (
            "KNOWLEDGE BASE:\n" + kb.kb_context() + "\n\n"
            f"USER TEXT: {txt or '(none)'}\n\n"
            "The user is an international student in Korea. Explain the attached document or "
            f"message in {LANG_FULL[L]}.\n"
            "Return JSON exactly: {\"summary\":str,\"key_points\":[str],"
            "\"risk_level\":\"safe\"|\"caution\"|\"danger\",\"risk_note\":str,"
            "\"matched_scam\":str}\n"
            "Set risk_level to danger if it matches any scam pattern in the knowledge base "
            "(especially requests to lend or sell a bank account or card). "
            "matched_scam is the Korean scam name from the knowledge base, or empty string."
        )
        res, live = ai_or_demo(prompt, images=images, as_json=True, fallback=demo.DEMO_DECODER)
        if not live:
            st.info("데모 응답입니다 (AI 키 미연결 또는 호출 실패).", icon="🧪")
        res = res or {}
        lvl = res.get("risk_level", "safe")
        css = {"danger": "danger", "caution": "warn"}.get(lvl, "ok")
        label = {"danger": "🚨 위험 — 사기 가능성 높음", "caution": "⚠️ 주의", "safe": "✅ 특이 위험 없음"}[lvl]
        step("2", "해석 결과")
        st.markdown(f"<div class='moa-card {css}'><b>{label}</b><br>{res.get('risk_note','')}</div>",
                    unsafe_allow_html=True)
        st.markdown(f"**요약**  \n{res.get('summary','')}")
        for p in res.get("key_points", []):
            st.markdown(f"- {p}")
        matched = res.get("matched_scam") or ""
        for s in kb.SCAM_PATTERNS:
            if matched and matched in s["name_ko"]:
                st.markdown(
                    f"<div class='moa-card danger'><b>{s['name_ko']}</b><br>"
                    f"<b>왜 위험한가</b> {s['why_dangerous']}<br>"
                    f"<b>지금 할 일</b> {s['action']}</div>", unsafe_allow_html=True)

    with st.expander("🚨 유학생 대상 금융사기 유형 (지식베이스)"):
        for s in kb.SCAM_PATTERNS:
            st.markdown(f"**{s['name_ko']}** ({s['severity']})  \n신호: {s['signal']}  \n"
                        f"대응: {s['action']}")


# ================================================================== 소개
def page_about():
    hero("The MOA", "한국에 막 도착한 외국인 유학생이 은행 계좌를 갖기 전까지의 "
         "금융 공백기를 버티게 해주는 AI 에이전트입니다.", slim=True)
    st.markdown("""
**문제**
- 국내 외국인 유학생은 25만 3,512명입니다 (2025-04-01 기준, 교육부·한국교육개발원).
- 입국 후 외국인등록증 발급과 계좌 개설까지 보통 몇 주가 걸립니다.
- 그동안 유학생은 더치페이·동아리 회비·기숙사 공동구매에서 사실상 배제되고,
  같이 어울리는 한국인 학생은 현금을 받아 두거나 ATM 무통장입금을 기다려야 합니다.

**MOA가 하는 일**
1. **모아 정산** — 영수증을 AI가 읽어 항목별로 나누고, 계좌가 없는 멤버 몫은 대납자에게 넘긴 뒤
   장부에 이연 기록합니다. 각자의 모국어로 정산 메시지를 만들어 줍니다.
2. **계좌 개설 내비게이터** — 체류자격·입국일·ARC 상태를 넣으면 지금 할 일 3가지와
   가져갈 서류를 모국어로 안내합니다.
3. **금융서류 통역 · 사기 경보** — 은행 서류나 수상한 메시지를 해석하고,
   통장 대여 요구 같은 사기 신호를 잡아냅니다.

**설계 원칙**
- MOA는 **자금을 이동시키지 않습니다.** 정산 기록과 요청 메시지만 만듭니다.
  (전자금융업 인가 없이 운영 가능한 범위로 의도적으로 한정했습니다.)
- 여권번호·외국인등록번호·계좌번호는 **수집하지 않습니다.**
- 생성형 AI는 내장 지식베이스를 근거로만 답하며, 근거가 없으면 "은행에 확인하라"고 말합니다.
- AI 호출이 실패해도 앱은 데모 응답으로 계속 동작합니다.
""")
    st.caption("2026 금융 AI Challenge 출품작 · MVP · 실제 금융거래를 제공하지 않는 시연용 서비스입니다.")


PAGES = {"home": page_home, "settle": page_settle, "nav": page_navigator,
         "doc": page_decoder, "about": page_about}
PAGES[page]()
