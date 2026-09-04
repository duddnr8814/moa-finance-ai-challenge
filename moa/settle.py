# -*- coding: utf-8 -*-
"""정산 계산 로직 — AI와 무관한 순수 함수. 테스트 가능."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Member:
    name: str
    has_account: bool = True
    lang: str = "ko"


@dataclass
class Item:
    name: str
    amount: int
    participants: list[str] = field(default_factory=list)


def shares(items: list[Item], members: list[Member]) -> dict[str, int]:
    """항목별 참여자에게 균등 분배. 원 단위 반올림 잔액은 첫 참여자가 흡수."""
    out = {m.name: 0 for m in members}
    for it in items:
        ps = [p for p in it.participants if p in out] or [m.name for m in members]
        base = it.amount // len(ps)
        rest = it.amount - base * len(ps)
        for i, p in enumerate(ps):
            out[p] += base + (rest if i == 0 else 0)
    return out


def balances(items: list[Item], members: list[Member], payer: str) -> dict[str, int]:
    """양수 = 이 사람이 payer에게 줘야 할 금액."""
    s = shares(items, members)
    s[payer] = s.get(payer, 0) - sum(it.amount for it in items)
    return s


def build_ledger(items: list[Item], members: list[Member], payer: str,
                 title: str, date: str) -> list[dict]:
    """정산 원장 항목 생성.

    계좌가 없는 멤버는 status='deferred' 로 기록된다.
    MOA는 자금을 직접 이동시키지 않는다 — 채무 사실과 정산 요청만 기록한다.
    """
    bal = balances(items, members, payer)
    by_name = {m.name: m for m in members}
    rows = []
    for name, amt in bal.items():
        if amt <= 0:
            continue
        m = by_name[name]
        rows.append({
            "title": title,
            "date": date,
            "from": name,
            "to": payer,
            "amount": amt,
            "status": "requested" if m.has_account else "deferred",
            "note": "" if m.has_account else "계좌 개설 후 정산 예정",
        })
    return rows


def net_summary(ledger: list[dict]) -> dict[str, int]:
    """이름별 미정산 잔액 합계."""
    out: dict[str, int] = {}
    for r in ledger:
        if r.get("settled"):
            continue
        out[r["from"]] = out.get(r["from"], 0) + r["amount"]
    return out


def won(n: int) -> str:
    return f"{n:,}원"
