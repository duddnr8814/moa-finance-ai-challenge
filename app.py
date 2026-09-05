# -*- coding: utf-8 -*-
"""MOA · Money On Arrival
2026 금융 AI Challenge — 외국인 유학생 금융 정착 AI Agent (MVP)

UI: Canva 'Moa' 브랜드 시스템 (오렌지 그라데이션) 적용
실행: streamlit run app.py
"""
from __future__ import annotations

import datetime as dt

import streamlit as st

from moa import demo, kb, kb_i18n, llm, settle
from moa.i18n import LANG_FULL, LANGS, t, topts

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
  background:#fff; min-height:240px; box-shadow:0 2px 12px -8px rgba(16,14,14,.2);}
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
  background:#fff; min-height:158px;}
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
        {"name": "Anna", "has_account": False, "lang": "en"},
        {"name": "Minsu", "has_account": True, "lang": "ko"},
        {"name": "Linh", "has_account": False, "lang": "vi"},
    ])
    ss.setdefault("bill_items", [])
    ss.setdefault("ledger", [])
    ss.setdefault("last_error", None)


init_state()
L = st.session_state.lang


def T(key: str) -> str:
    return t(key, L)


def won(n: int) -> str:
    return f"{n:,}원" if L == "ko" else f"{n:,} KRW"


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

    st.selectbox(T("language"), list(LANGS.keys()), key="lang",
                 format_func=lambda k: LANGS[k])

    st.radio("Menu", NAV, key="page",
             format_func=lambda k: t(NAV_KEY[k], L),
             label_visibility="collapsed")
    st.divider()
    if llm.is_live():
        st.success(T("ai_on"), icon="✅")
    else:
        st.info(T("demo_badge"), icon="🧪")
    if st.session_state.last_error:
        with st.expander(T("ai_error_log")):
            st.code(st.session_state.last_error)
    st.caption(f"{T('kb_asof')} {kb.KB_UPDATED}")

page = st.session_state.page


# ================================================================== 0. 홈
FEATURES = [("settle", "feat_settle_name", "feat_settle_desc"),
            ("nav", "feat_nav_name", "feat_nav_desc"),
            ("doc", "feat_doc_name", "feat_doc_desc")]


def page_home():
    hero("Moa <small>Money On Arrival</small>", T("tagline"), kicker=T("home_kicker"))

    st.markdown(
        f"<div class='moa-card'><b>{T('home_welcome_title')}</b><br>"
        f"<span style='color:var(--moa-muted)'>{T('home_welcome_body')}</span></div>",
        unsafe_allow_html=True)

    step("3", T("home_features_title"))
    st.caption(T("home_features_sub"))

    cols = st.columns(3)
    for i, ((key, nk, dk), col) in enumerate(zip(FEATURES, cols), start=1):
        with col:
            st.markdown(
                f"<div class='moa-feature'><div class='num'>{i}</div>"
                f"<h4>{T(nk)}</h4><p>{T(dk)}</p></div>", unsafe_allow_html=True)
            if st.button(f"{T(nk)} \u2192", key=f"go_{key}", use_container_width=True):
                go(key)

    st.markdown("")
    st.markdown(
        "<div class='moa-hero slim' style='background:var(--moa-grad-hot)'>"
        "<h1>IT\u2019S HERE &nbsp;<span class='moa-mark'>Moa</span></h1>"
        f"<p>{T('home_cta_sub')}</p></div>", unsafe_allow_html=True)


# ================================================================== 1. 모아 정산
def page_settle():
    import pandas as pd

    hero(T("nav_settle"), T("settle_sub"), slim=True)

    step("1", T("s_step1"))
    mdf = pd.DataFrame(st.session_state.members)
    mdf = st.data_editor(
        mdf, num_rows="dynamic", use_container_width=True, key="member_editor",
        column_config={
            "name": st.column_config.TextColumn(T("col_name"), width="medium"),
            "has_account": st.column_config.CheckboxColumn(T("col_has_account")),
            "lang": st.column_config.SelectboxColumn(T("col_lang"), options=list(LANGS.keys())),
        },
    )
    members = [settle.Member(str(r["name"]).strip(), bool(r["has_account"]), str(r["lang"]))
               for _, r in mdf.iterrows() if str(r.get("name", "")).strip()]
    st.session_state.members = [m.__dict__ for m in members]
    if len(members) < 2:
        st.warning(T("need_2_members"))
        return
    names = [m.name for m in members]
    no_acc = [m.name for m in members if not m.has_account]
    if no_acc:
        st.markdown(
            f"<div class='moa-card warn'>{T('warn_no_account_pre')}: "
            f"<b>{', '.join(no_acc)}</b> \u2014 {T('warn_no_account_body')}</div>",
            unsafe_allow_html=True)

    step("2", T("s_step2"))
    c1, c2 = st.columns([3, 2])
    with c1:
        up = st.file_uploader(T("receipt_upload"), type=["jpg", "jpeg", "png"])
    with c2:
        st.write("")
        st.write("")
        run = st.button(T("btn_analyze"), use_container_width=True, type="primary")

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
            st.info(T("info_sample_receipt"), icon="🧪")
        else:
            parsed, live = ai_or_demo(prompt, images=images, as_json=True,
                                      fallback=demo.DEMO_RECEIPT)
            if not live:
                st.info(T("info_demo_receipt"), icon="🧪")
        rows = []
        for it in (parsed or {}).get("items", []):
            row = {"item": it.get("name", ""), "amount": int(it.get("amount", 0) or 0)}
            for n in names:
                row[n] = True
            rows.append(row)
        st.session_state.bill_items = rows

    step("3", T("s_step3"))
    base = st.session_state.bill_items or [{"item": "", "amount": 0,
                                            **{n: True for n in names}}]
    idf = pd.DataFrame(base)
    for c in ("item", "amount"):
        if c not in idf.columns:
            idf[c] = "" if c == "item" else 0
    for n in names:
        if n not in idf.columns:
            idf[n] = True
    idf = idf[["item", "amount"] + names]
    idf = st.data_editor(
        idf, num_rows="dynamic", use_container_width=True, key="item_editor",
        column_config={
            "item": st.column_config.TextColumn(T("col_item"), width="medium"),
            "amount": st.column_config.NumberColumn(T("col_amount"), min_value=0, step=100),
        },
    )
    st.session_state.bill_items = idf.to_dict("records")

    items = []
    for _, r in idf.iterrows():
        amt = int(r["amount"] or 0)
        if amt <= 0:
            continue
        parts = [n for n in names if bool(r.get(n))]
        items.append(settle.Item(str(r["item"]), amt, parts or names))
    if not items:
        st.info(T("info_need_item"))
        return

    total = sum(i.amount for i in items)
    st.markdown(
        f"<div class='moa-card'><span class='moa-sub'>{T('total')}</span><br>"
        f"<span class='moa-amt plus'>{won(total)}</span></div>",
        unsafe_allow_html=True)

    step("4", T("s_step4"))
    payer = st.selectbox(T("payer"), names,
                         index=next((i for i, m in enumerate(members) if m.has_account), 0))
    title = st.text_input(T("settle_name"), T("settle_name_default"))
    date = st.date_input(T("date_label"), dt.date.today()).isoformat()

    bal = settle.balances(items, members, payer)
    step("5", T("s_step5"))
    cols = st.columns(min(len(names), 4))
    for i, m in enumerate(members):
        amt = bal[m.name]
        with cols[i % len(cols)]:
            if m.name == payer:
                st.markdown(
                    f"<div class='moa-card ok'><b>{m.name}</b><br>"
                    f"<span class='moa-pill hot'>{T('payer')}</span>"
                    f"<br><span class='moa-amt plus'>+{won(-amt)}</span><br>"
                    f"<span class='moa-sub'>{T('tag_receive')}</span></div>",
                    unsafe_allow_html=True)
            else:
                tag = (f"<span class='moa-pill'>{T('tag_transfer_now')}</span>" if m.has_account
                       else f"<span class='moa-pill grey'>{T('tag_after_account')}</span>")
                st.markdown(
                    f"<div class='moa-card'><b>{m.name}</b><br>{tag}<br>"
                    f"<span class='moa-amt'>{won(amt)}</span><br>"
                    f"<span class='moa-sub'>{T('tag_send')}</span></div>",
                    unsafe_allow_html=True)

    if st.button(T("btn_ledger"), type="primary"):
        rows = settle.build_ledger(items, members, payer, title, date)
        st.session_state.ledger.extend(rows)
        by_lang = {m.name: m.lang for m in members}
        step("6", T("s_step6"))
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
            fb = FALLBACK_MSG[lg].format(name=r["from"], title=title, date=date,
                                         amount=f"{r['amount']:,}")
            if r["status"] == "deferred":
                fb += " " + FALLBACK_DEFERRED[lg]
            else:
                fb += " " + FALLBACK_REQUESTED[lg]
            msg, live = ai_or_demo(prompt, fallback=fb)
            st.markdown(f"<div class='moa-card'><b>\u2192 {r['from']}</b> "
                        f"<span class='moa-pill grey'>{LANGS[lg]}</span></div>",
                        unsafe_allow_html=True)
            st.code(msg, language=None)

    if st.session_state.ledger:
        step("📒", T("ledger_title"))
        ldf = pd.DataFrame(st.session_state.ledger)
        st.dataframe(ldf, use_container_width=True, hide_index=True)
        net = settle.net_summary(st.session_state.ledger)
        st.write(" · ".join(f"**{k}** {won(v)}" for k, v in net.items()) or "-")
        if st.button(T("ledger_clear")):
            st.session_state.ledger = []
            st.rerun()


FALLBACK_MSG = {
    "ko": "{name}님, {title} ({date}) — {amount}원.",
    "en": "Hi {name}, {title} ({date}) — {amount} KRW.",
    "zh": "{name}，{title}（{date}）— {amount} 韩元。",
    "vi": "Chào {name}, {title} ({date}) — {amount} KRW.",
}
FALLBACK_DEFERRED = {
    "ko": "계좌가 생기면 정산할 수 있게 장부에 적어 뒀어요. 지금은 신경 쓰지 않아도 돼요.",
    "en": "It is written in our shared ledger and we will settle once your account is open. "
          "Nothing to do for now.",
    "zh": "已记入共享账本，等你开好账户再结算即可，现在不用担心。",
    "vi": "Mình đã ghi vào sổ chung, khi nào bạn mở tài khoản thì thanh toán. Giờ đừng lo nhé.",
}
FALLBACK_REQUESTED = {
    "ko": "편할 때 보내주면 돼요!",
    "en": "Send it over whenever it suits you!",
    "zh": "方便的时候转给我就好！",
    "vi": "Khi nào tiện bạn chuyển giúp mình nhé!",
}


# ============================================================ 2. 계좌 개설 내비게이터
def page_navigator():
    hero(T("nav_nav"), T("nav_sub"), slim=True)

    step("1", T("n_step1"))
    visa_opts, arc_opts, phone_opts = (topts("visa_opts", L), topts("arc_opts", L),
                                       topts("phone_opts", L))
    c1, c2, c3 = st.columns(3)
    with c1:
        visa_i = visa_opts.index(st.selectbox(T("visa_label"), visa_opts))
        arrived = st.date_input(T("arrived_label"), dt.date.today() - dt.timedelta(days=10))
    with c2:
        arc_i = arc_opts.index(st.selectbox(T("arc_label"), arc_opts))
        phone_i = phone_opts.index(st.selectbox(T("phone_label"), phone_opts))
    with c3:
        univ = st.text_input(T("univ_label"), "")
        region = st.text_input(T("region_label"), "")

    dorm = st.checkbox(T("chk_residence"))
    enroll = st.checkbox(T("chk_enroll"))

    VISA_EN = ["D-2 degree student", "D-4 language student", "D-10 job seeker", "other"]
    ARC_EN = ["not applied yet", "applied, waiting for issue", "received"]
    PHONE_EN = ["none", "prepaid SIM", "postpaid plan"]

    done = {"arrival": True,
            "sim": phone_i != 0,
            "arc_apply": arc_i != 0,
            "limit_account": False,
            "arc_issue": arc_i == 2,
            "full_account": False}
    step("2", T("n_step2"))
    tl = st.columns(len(kb.JOURNEY_STEPS))
    for col, stp in zip(tl, kb.JOURNEY_STEPS):
        is_done = done.get(stp["key"])
        mark = "✅" if is_done else "⬜"
        col.markdown(
            f"<div class='moa-tl{' done' if is_done else ''}'>{mark}"
            f"<b>{t('journey_' + stp['key'], L)}</b><div class='d'>{stp['days']}</div></div>",
            unsafe_allow_html=True)

    st.markdown("")
    if st.button(T("btn_next_steps"), type="primary"):
        days = (dt.date.today() - arrived).days
        profile = (f"visa={VISA_EN[visa_i]}, days_since_arrival={days}, ARC={ARC_EN[arc_i]}, "
                   f"phone={PHONE_EN[phone_i]}, university={univ or 'unknown'}, "
                   f"region={region or 'unknown'}, has_residence_proof={dorm}, "
                   f"has_enrollment_certificate={enroll}")
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
            st.info(T("info_demo_response"), icon="🧪")
        st.markdown(out)

    with st.expander(T("kb_expander")):
        for r in kb.ACCOUNT_RULES:
            st.markdown(
                f"**{kb_i18n.rule(r, 'topic', L)}** — {kb_i18n.rule(r, 'fact', L)}  \n"
                f"<span class='moa-sub'>{T('kb_source')}: {kb_i18n.rule(r, 'source', L)} · "
                f"{T('kb_confidence')}: {kb_i18n.confidence(r['confidence'], L)}</span>",
                unsafe_allow_html=True)


# ======================================================= 3. 금융서류 통역 · 사기 경보
def page_decoder():
    hero(T("nav_doc"), T("doc_sub"), slim=True)

    step("1", T("d_step1"))
    up = st.file_uploader(T("doc_upload"), type=["jpg", "jpeg", "png"], key="doc_up")
    txt = st.text_area(T("doc_paste"), placeholder=T("doc_placeholder"), height=110)

    if st.button(T("btn_decode"), type="primary"):
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
            st.info(T("info_demo_response"), icon="🧪")
        res = res or {}
        lvl = res.get("risk_level", "safe")
        css = {"danger": "danger", "caution": "warn"}.get(lvl, "ok")
        label = T({"danger": "risk_danger", "caution": "risk_caution"}.get(lvl, "risk_safe"))
        step("2", T("d_step2"))
        st.markdown(f"<div class='moa-card {css}'><b>{label}</b><br>{res.get('risk_note','')}</div>",
                    unsafe_allow_html=True)
        st.markdown(f"**{T('summary_label')}**  \n{res.get('summary','')}")
        for p in res.get("key_points", []):
            st.markdown(f"- {p}")
        matched = res.get("matched_scam") or ""
        for s in kb.SCAM_PATTERNS:
            if matched and matched in s["name_ko"]:
                st.markdown(
                    f"<div class='moa-card danger'>"
                    f"<b>{kb_i18n.scam(s, 'name', L)}</b><br>"
                    f"<b>{T('scam_why')}</b> {kb_i18n.scam(s, 'why', L)}<br>"
                    f"<b>{T('scam_now')}</b> {kb_i18n.scam(s, 'action', L)}</div>",
                    unsafe_allow_html=True)

    with st.expander(T("scam_expander")):
        for s in kb.SCAM_PATTERNS:
            st.markdown(
                f"**{kb_i18n.scam(s, 'name', L)}** "
                f"({kb_i18n.severity(s['severity'], L)})  \n"
                f"{T('scam_signal')}: {kb_i18n.scam(s, 'signal', L)}  \n"
                f"{T('scam_action')}: {kb_i18n.scam(s, 'action', L)}")


# ================================================================== 소개
def page_about():
    hero(T("about_title"), T("about_sub"), slim=True)
    st.markdown(T("about_body"))
    st.caption(T("about_caption"))


PAGES = {"home": page_home, "settle": page_settle, "nav": page_navigator,
         "doc": page_decoder, "about": page_about}
PAGES[page]()
