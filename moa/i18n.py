# -*- coding: utf-8 -*-
"""MOA UI 다국어 문자열.

UI 라벨은 사전 번역(고정), 사용자 맞춤 설명문은 Gemini가 생성한다.
_T 의 값은 (ko, en, zh, vi) 순서의 4-튜플이다.
"""

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

LANG_ORDER = ["ko", "en", "zh", "vi"]

_T = {
    # ---------------------------------------------------------------- 공통
    "app_title": ("MOA · Money On Arrival",) * 4,
    "tagline": (
        "계좌가 없어도, 같이 나눠 낼 수 있게",
        "Split the bill even before you have a Korean bank account",
        "还没有韩国账户，也能一起分摊账单",
        "Chia tiền cùng bạn bè ngay cả khi chưa có tài khoản ngân hàng",
    ),
    "language": ("언어", "Language", "语言", "Ngôn ngữ"),
    "nav_home": ("홈", "Home", "首页", "Trang chủ"),
    "nav_settle": ("1. 모아 정산", "1. Settle Bridge", "1. 分摊结算", "1. Chia tiền"),
    "nav_nav": ("2. 계좌 개설 내비게이터", "2. Account Navigator",
                "2. 开户导航", "2. Hướng dẫn mở tài khoản"),
    "nav_doc": ("3. 금융서류 통역 · 사기 경보", "3. Doc Decoder & Scam Alert",
                "3. 金融文件解读与诈骗警报", "3. Giải mã giấy tờ & cảnh báo lừa đảo"),
    "nav_about": ("서비스 소개", "About", "关于", "Giới thiệu"),
    "demo_badge": (
        "데모 모드 (AI 키 없이 예시 응답)",
        "Demo mode (sample responses, no AI key)",
        "演示模式（示例回复，无 AI 密钥）",
        "Chế độ demo (phản hồi mẫu, không có khóa AI)",
    ),
    "ai_on": ("Gemini 연결됨", "Gemini connected", "已连接 Gemini", "Đã kết nối Gemini"),
    "ai_error_log": ("AI 오류 로그", "AI error log", "AI 错误日志", "Nhật ký lỗi AI"),
    "kb_asof": ("KB 기준일", "KB as of", "知识库基准日", "KB cập nhật"),
    "info_demo_response": (
        "데모 응답입니다 (AI 키 미연결 또는 호출 실패).",
        "This is a demo response (no AI key, or the call failed).",
        "这是演示回复（未连接 AI 密钥或调用失败）。",
        "Đây là phản hồi demo (chưa có khóa AI hoặc gọi thất bại).",
    ),

    # ---------------------------------------------------------------- 홈
    "home_kicker": ("2026 금융 AI Challenge",) * 4,
    "home_welcome_title": ("Welcome to Our Society",) * 4,
    "home_welcome_body": (
        "계좌가 아직 없는 외국인 친구도 빠지지 않고 나눠 낼 수 있게, 영수증을 읽어 분배하고 "
        "정산 장부에 남깁니다. MOA는 돈을 직접 옮기지 않고 <b>‘누가 누구에게 얼마’</b>만 기록합니다.",
        "So a friend who does not have a Korean bank account yet is never left out, MOA reads the "
        "receipt, splits it, and writes it into a shared ledger. MOA never moves money — it only "
        "records <b>who owes whom how much</b>.",
        "让还没有韩国账户的外国朋友也不被落下：MOA 读取小票、分摊金额并记入共享账本。"
        "MOA 不转移任何资金，只记录<b>谁欠谁多少钱</b>。",
        "Để người bạn chưa có tài khoản ngân hàng Hàn Quốc không bị bỏ lại, MOA đọc hoá đơn, "
        "chia tiền và ghi vào sổ chung. MOA không chuyển tiền — chỉ ghi lại <b>ai nợ ai bao nhiêu</b>.",
    ),
    "home_features_title": ("가지 주요 기능", "key features", "项主要功能", "tính năng chính"),
    "home_features_sub": (
        "한국에 막 도착한 외국인 유학생이 은행 계좌를 갖기 전까지 금융 공백기를 버티게 해주는 AI 에이전트입니다.",
        "An AI agent that carries newly arrived international students through the financial gap "
        "before they can open a bank account.",
        "一款帮助刚抵达韩国的留学生度过开户前金融空白期的 AI 助手。",
        "Một tác nhân AI giúp du học sinh mới đến Hàn Quốc vượt qua giai đoạn trống tài chính "
        "trước khi mở được tài khoản.",
    ),
    "feat_settle_name": ("MOA 정산", "MOA Settle", "MOA 分摊", "MOA Chia tiền"),
    "feat_settle_desc": (
        "계좌가 아직 없는 친구도 빠지지 않고 나눠 낼 수 있게, 영수증을 읽어 분배하고 장부에 남깁니다.",
        "Reads the receipt, splits it, and records it in the ledger so a friend without an account "
        "is never left out.",
        "读取小票、分摊金额并记入账本，让还没有账户的朋友也能一起分担。",
        "Đọc hoá đơn, chia tiền và ghi vào sổ để bạn chưa có tài khoản vẫn tham gia được.",
    ),
    "feat_nav_name": ("계좌 개설 Navi", "Account Navigator", "开户导航", "Hướng dẫn mở tài khoản"),
    "feat_nav_desc": (
        "지금 상황에서 계좌를 열려면 무엇부터 해야 하는지, 지식베이스를 근거로 모국어로 안내합니다.",
        "Tells you what to do first to open an account in your situation, in your own language, "
        "grounded in the knowledge base.",
        "根据知识库，用你的母语说明在当前情况下开户要先做什么。",
        "Cho biết cần làm gì trước để mở tài khoản trong hoàn cảnh của bạn, bằng tiếng mẹ đẻ, "
        "dựa trên cơ sở tri thức.",
    ),
    "feat_doc_name": ("금융 서류 통역 · 사기 경보", "Doc Decoder & Scam Alert",
                      "金融文件解读与诈骗警报", "Giải mã giấy tờ & cảnh báo lừa đảo"),
    "feat_doc_desc": (
        "서류나 금융 메시지를 올리면 모국어로 풀어 설명하고, 사기 신호가 있으면 경고합니다.",
        "Upload a document or a financial message and MOA explains it in your language, and warns "
        "you if it looks like a scam.",
        "上传文件或金融短信，MOA 用你的母语解释，并在有诈骗迹象时发出警告。",
        "Tải lên giấy tờ hoặc tin nhắn tài chính, MOA giải thích bằng tiếng của bạn và cảnh báo "
        "nếu có dấu hiệu lừa đảo.",
    ),
    "home_cta_sub": (
        "AI 키가 없어도 데모 응답으로 전체 흐름을 그대로 시연할 수 있습니다.",
        "Even without an AI key, the full flow runs on demo responses.",
        "即使没有 AI 密钥，也能用演示回复完整体验全部流程。",
        "Ngay cả khi không có khóa AI, toàn bộ luồng vẫn chạy bằng phản hồi demo.",
    ),

    # ---------------------------------------------------------------- 정산
    "settle_sub": (
        "계좌가 아직 없는 친구도 빠지지 않고 나눠 낼 수 있게, 영수증을 읽어 분배하고 정산 장부에 "
        "남깁니다. MOA는 돈을 직접 옮기지 않고 ‘누가 누구에게 얼마’만 기록합니다.",
        "MOA reads the receipt, splits it, and writes it into the ledger so a friend without an "
        "account is never left out. MOA never moves money — it only records who owes whom how much.",
        "MOA 读取小票、分摊金额并记入结算账本，让还没有账户的朋友也不被落下。"
        "MOA 不转移资金，只记录谁欠谁多少钱。",
        "MOA đọc hoá đơn, chia tiền và ghi vào sổ để bạn chưa có tài khoản không bị bỏ lại. "
        "MOA không chuyển tiền — chỉ ghi ai nợ ai bao nhiêu.",
    ),
    "s_step1": ("함께 낸 사람", "Who is splitting", "一起分摊的人", "Những người cùng chia"),
    "col_name": ("이름", "Name", "姓名", "Tên"),
    "col_has_account": ("한국 계좌 있음", "Has Korean account", "有韩国账户",
                        "Có tài khoản Hàn Quốc"),
    "col_lang": ("언어", "Language", "语言", "Ngôn ngữ"),
    "need_2_members": (
        "사람을 2명 이상 입력해 주세요.",
        "Please enter at least two people.",
        "请至少输入两个人。",
        "Vui lòng nhập ít nhất hai người.",
    ),
    "warn_no_account_pre": ("계좌가 없는 멤버", "Members without an account",
                            "没有账户的成员", "Thành viên chưa có tài khoản"),
    "warn_no_account_body": (
        "이 사람들의 몫은 대납자에게 넘기고 <b>이연 정산(deferred)</b>으로 장부에 남깁니다.",
        "Their share is carried by the payer and recorded in the ledger as a "
        "<b>deferred settlement</b>.",
        "他们的份额由垫付人承担，并作为<b>延期结算</b>记入账本。",
        "Phần của họ do người trả hộ gánh và được ghi vào sổ dưới dạng <b>thanh toán hoãn lại</b>.",
    ),
    "s_step2": ("영수증 읽기", "Read the receipt", "读取小票", "Đọc hoá đơn"),
    "receipt_upload": ("영수증 사진 (JPG/PNG)", "Receipt photo (JPG/PNG)",
                       "小票照片（JPG/PNG）", "Ảnh hoá đơn (JPG/PNG)"),
    "btn_analyze": ("🔍 영수증 분석", "🔍 Analyze receipt", "🔍 分析小票", "🔍 Phân tích hoá đơn"),
    "info_sample_receipt": (
        "샘플 영수증으로 시연합니다. 실제 영수증 사진을 올리면 AI가 읽습니다.",
        "Running on a sample receipt. Upload a real photo and the AI will read it.",
        "正在使用示例小票演示。上传真实照片后 AI 会读取。",
        "Đang dùng hoá đơn mẫu. Tải ảnh thật lên thì AI sẽ đọc.",
    ),
    "info_demo_receipt": (
        "데모 영수증 데이터를 불러왔습니다 (AI 키 미연결 또는 호출 실패).",
        "Loaded demo receipt data (no AI key, or the call failed).",
        "已载入演示小票数据（未连接 AI 密钥或调用失败）。",
        "Đã tải dữ liệu hoá đơn demo (chưa có khóa AI hoặc gọi thất bại).",
    ),
    "s_step3": ("항목 확인 · 누가 먹었는지 체크", "Check the items and who shared them",
                "确认项目 · 勾选谁享用了", "Kiểm tra món và ai đã dùng"),
    "col_item": ("항목", "Item", "项目", "Món"),
    "col_amount": ("금액(원)", "Amount (KRW)", "金额（韩元）", "Số tiền (KRW)"),
    "info_need_item": (
        "금액이 있는 항목을 1개 이상 입력하면 정산이 계산됩니다.",
        "Enter at least one item with an amount to calculate the split.",
        "输入至少一个带金额的项目即可计算分摊。",
        "Nhập ít nhất một món có số tiền để tính chia.",
    ),
    "total": ("합계", "Total", "合计", "Tổng"),
    "s_step4": ("실제로 결제한 사람", "Who actually paid", "实际付款的人", "Ai đã thanh toán"),
    "payer": ("대납자", "Payer", "垫付人", "Người trả hộ"),
    "settle_name": ("정산 이름", "Settlement name", "结算名称", "Tên khoản chia"),
    "settle_name_default": ("저녁 모임", "Dinner", "晚餐聚会", "Bữa tối"),
    "date_label": ("날짜", "Date", "日期", "Ngày"),
    "s_step5": ("정산 결과", "Settlement result", "结算结果", "Kết quả chia tiền"),
    "tag_receive": ("받을 금액", "To receive", "应收金额", "Sẽ nhận"),
    "tag_send": ("보낼 금액", "To send", "应付金额", "Cần trả"),
    "tag_transfer_now": ("즉시 이체", "Transfer now", "可立即转账", "Chuyển ngay"),
    "tag_after_account": ("계좌 개설 후 정산", "Settle after account opens",
                          "开户后结算", "Thanh toán sau khi mở tài khoản"),
    "btn_ledger": (
        "📒 정산 장부에 기록하고 요청 메시지 만들기",
        "📒 Record in the ledger and draft request messages",
        "📒 记入账本并生成催款消息",
        "📒 Ghi vào sổ và soạn tin nhắn nhắc",
    ),
    "s_step6": ("각 멤버에게 보낼 메시지", "Message for each member",
                "发给每位成员的消息", "Tin nhắn cho từng thành viên"),
    "ledger_title": ("정산 장부 (미정산)", "Ledger (outstanding)", "结算账本（未结）",
                     "Sổ chia tiền (chưa thanh toán)"),
    "ledger_clear": ("장부 비우기", "Clear the ledger", "清空账本", "Xoá sổ"),

    # ---------------------------------------------------------------- 계좌 개설 Navi
    "nav_sub": (
        "지금 내 상황에서 계좌를 열려면 무엇부터 해야 하는지, 지식베이스를 근거로 모국어로 안내합니다.",
        "Grounded in the knowledge base, MOA tells you in your own language what to do first to "
        "open an account in your current situation.",
        "MOA 依据知识库，用你的母语说明在当前情况下开户要先做什么。",
        "Dựa trên cơ sở tri thức, MOA cho biết bằng tiếng của bạn cần làm gì trước để mở tài khoản.",
    ),
    "n_step1": ("내 상황 입력", "Your situation", "填写你的情况", "Tình huống của bạn"),
    "visa_label": ("체류자격", "Visa status", "在留资格", "Loại thị thực"),
    "visa_opts": (
        "D-2 유학|D-4 어학연수|D-10 구직|기타",
        "D-2 Degree student|D-4 Language student|D-10 Job seeker|Other",
        "D-2 留学|D-4 语言研修|D-10 求职|其他",
        "D-2 Du học|D-4 Học tiếng|D-10 Tìm việc|Khác",
    ),
    "arc_label": ("외국인등록증(ARC)", "Alien Registration Card (ARC)",
                  "外国人登录证（ARC）", "Thẻ cư trú (ARC)"),
    "arc_opts": (
        "아직 신청 안 함|신청함 · 수령 대기|수령 완료",
        "Not applied yet|Applied · waiting|Received",
        "尚未申请|已申请 · 等待领取|已领取",
        "Chưa nộp|Đã nộp · đang chờ|Đã nhận",
    ),
    "phone_label": ("본인 명의 휴대폰", "Phone in your own name",
                    "本人名下手机", "Điện thoại đứng tên bạn"),
    "phone_opts": (
        "없음|선불 유심 개통|후불 요금제 개통",
        "None|Prepaid SIM|Postpaid plan",
        "没有|已开预付卡|已开后付套餐",
        "Chưa có|SIM trả trước|Gói trả sau",
    ),
    "univ_label": ("학교 (선택)", "University (optional)", "学校（可选）", "Trường (tuỳ chọn)"),
    "region_label": ("지역 (선택)", "Region (optional)", "地区（可选）", "Khu vực (tuỳ chọn)"),
    "arrived_label": ("입국일", "Arrival date", "入境日期", "Ngày nhập cảnh"),
    "chk_residence": (
        "기숙사 입사확인서 또는 임대차계약서가 있다",
        "I have a dormitory confirmation or a lease contract",
        "我有宿舍入住确认书或租赁合同",
        "Tôi có giấy xác nhận ký túc xá hoặc hợp đồng thuê nhà",
    ),
    "chk_enroll": (
        "재학(입학) 증명서가 있다",
        "I have a certificate of enrolment or admission",
        "我有在学（入学）证明",
        "Tôi có giấy chứng nhận nhập học",
    ),
    "n_step2": ("정착 타임라인", "Settlement timeline", "落地时间线", "Lộ trình ổn định"),
    "journey_arrival": ("입국 · 체류지 확보", "Arrival · secure housing",
                        "入境 · 确定住处", "Nhập cảnh · có chỗ ở"),
    "journey_sim": ("본인 명의 휴대폰(선불 유심) 개통", "Phone in your name (prepaid SIM)",
                    "开通本人名下手机（预付卡）", "Mở điện thoại đứng tên (SIM trả trước)"),
    "journey_arc_apply": ("외국인등록 신청", "Apply for alien registration",
                          "申请外国人登录", "Nộp đăng ký người nước ngoài"),
    "journey_limit_account": ("한도계좌 개설 (ARC 전 가능 은행)",
                              "Open a limited account (banks that allow it pre-ARC)",
                              "开限额账户（ARC 前可办的银行）",
                              "Mở tài khoản hạn mức (ngân hàng cho phép trước ARC)"),
    "journey_arc_issue": ("외국인등록증 수령", "Receive the ARC", "领取外国人登录证",
                          "Nhận thẻ ARC"),
    "journey_full_account": ("정식 계좌 전환 · 한도 해제", "Upgrade to a full account",
                             "转为正式账户 · 解除限额", "Chuyển sang tài khoản đầy đủ"),
    "btn_next_steps": (
        "🧭 내 상황에 맞는 다음 단계 받기",
        "🧭 Get the next steps for my situation",
        "🧭 获取适合我的下一步",
        "🧭 Nhận các bước tiếp theo cho tôi",
    ),
    "kb_expander": (
        "📚 이 안내의 근거 (지식베이스 원문)",
        "📚 Sources for this guidance (knowledge base)",
        "📚 本指引的依据（知识库原文）",
        "📚 Nguồn của hướng dẫn này (cơ sở tri thức)",
    ),
    "kb_source": ("출처", "Source", "来源", "Nguồn"),
    "kb_confidence": ("확신도", "Confidence", "可信度", "Độ tin cậy"),

    # ---------------------------------------------------------------- 서류 통역
    "doc_sub": (
        "은행 서류나 낯선 금융 메시지를 올리면 모국어로 풀어 설명하고, 사기 신호가 있으면 경고합니다.",
        "Upload a bank document or an unfamiliar financial message and MOA explains it in your "
        "language, and warns you if it shows scam signals.",
        "上传银行文件或陌生的金融短信，MOA 会用你的母语解释，并在出现诈骗信号时警告。",
        "Tải lên giấy tờ ngân hàng hoặc tin nhắn tài chính lạ, MOA giải thích bằng tiếng của bạn "
        "và cảnh báo nếu có dấu hiệu lừa đảo.",
    ),
    "d_step1": ("서류 또는 메시지 올리기", "Upload a document or message",
                "上传文件或消息", "Tải giấy tờ hoặc tin nhắn"),
    "doc_upload": ("서류·화면 캡처 (JPG/PNG)", "Document or screenshot (JPG/PNG)",
                   "文件或截图（JPG/PNG）", "Giấy tờ hoặc ảnh chụp màn hình (JPG/PNG)"),
    "doc_paste": ("또는 받은 메시지를 붙여넣기", "Or paste the message you received",
                  "或粘贴你收到的消息", "Hoặc dán tin nhắn bạn nhận được"),
    "doc_placeholder": (
        "예) 계좌를 빌려주면 하루 30만원을 드립니다. 통장과 카드만 보내주세요.",
        "e.g. Lend us your bank account and earn 300,000 KRW a day. Just send the passbook and card.",
        "例）把账户借给我们，每天给你 30 万韩元，只需寄来存折和银行卡。",
        "Ví dụ) Cho mượn tài khoản, mỗi ngày nhận 300.000 KRW. Chỉ cần gửi sổ và thẻ.",
    ),
    "btn_decode": ("🔎 해석하기", "🔎 Decode", "🔎 解读", "🔎 Giải mã"),
    "d_step2": ("해석 결과", "Result", "解读结果", "Kết quả"),
    "risk_danger": ("🚨 위험 — 사기 가능성 높음", "🚨 Danger — likely a scam",
                    "🚨 危险 — 极可能是诈骗", "🚨 Nguy hiểm — nhiều khả năng lừa đảo"),
    "risk_caution": ("⚠️ 주의", "⚠️ Caution", "⚠️ 注意", "⚠️ Thận trọng"),
    "risk_safe": ("✅ 특이 위험 없음", "✅ No particular risk", "✅ 未发现特别风险",
                  "✅ Không có rủi ro đặc biệt"),
    "summary_label": ("요약", "Summary", "摘要", "Tóm tắt"),
    "scam_expander": (
        "🚨 유학생 대상 금융사기 유형 (지식베이스)",
        "🚨 Financial scams targeting international students (knowledge base)",
        "🚨 针对留学生的金融诈骗类型（知识库）",
        "🚨 Các kiểu lừa đảo tài chính nhắm vào du học sinh (cơ sở tri thức)",
    ),
    "scam_signal": ("신호", "Signal", "信号", "Dấu hiệu"),
    "scam_action": ("대응", "What to do", "应对", "Cần làm gì"),
    "scam_why": ("왜 위험한가", "Why it is dangerous", "为什么危险", "Vì sao nguy hiểm"),
    "scam_now": ("지금 할 일", "Do this now", "现在要做的", "Làm ngay bây giờ"),

    # ---------------------------------------------------------------- 소개
    "about_title": ("The MOA",) * 4,
    "about_sub": (
        "한국에 막 도착한 외국인 유학생이 은행 계좌를 갖기 전까지의 금융 공백기를 버티게 해주는 AI 에이전트입니다.",
        "An AI agent that carries newly arrived international students through the financial gap "
        "before they can hold a bank account.",
        "一款帮助刚抵达韩国的留学生度过开户前金融空白期的 AI 助手。",
        "Một tác nhân AI giúp du học sinh mới đến Hàn Quốc vượt qua giai đoạn trống tài chính "
        "trước khi có tài khoản ngân hàng.",
    ),
    "about_body": (
        """**문제**
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
""",
        """**The problem**
- There are 253,512 international students in Korea (as of 2025-04-01, Ministry of Education / KEDI).
- After arrival, getting an Alien Registration Card and opening an account usually takes weeks.
- In the meantime students are effectively excluded from splitting bills, club fees and dorm group
  buys, and their Korean friends have to hold cash or wait for an ATM deposit.

**What MOA does**
1. **MOA Settle** — the AI reads the receipt, splits it item by item, carries the share of members
   without an account over to the payer, and records it in the ledger as deferred. It drafts the
   settlement message in each person's own language.
2. **Account Navigator** — enter your visa, arrival date and ARC status and MOA lists the next
   three actions and the documents to bring, in your language.
3. **Doc Decoder & Scam Alert** — MOA explains bank documents and suspicious messages, and catches
   scam signals such as a request to lend your bank account.

**Design principles**
- MOA **never moves money.** It only creates settlement records and request messages.
  (Deliberately scoped to what can run without an electronic financial business licence.)
- Passport numbers, registration numbers and account numbers are **never collected.**
- The generative AI answers only from the built-in knowledge base; without a basis it says
  "check with the bank".
- If the AI call fails, the app keeps working on demo responses.
""",
        """**问题**
- 韩国国内外国留学生共 253,512 名（2025-04-01 基准，教育部·韩国教育开发院）。
- 入境后办理外国人登录证并开户通常需要数周。
- 这段时间里，留学生在 AA 制、社团会费、宿舍团购中实际上被排除在外，
  同行的韩国学生只能先收现金或等待 ATM 无存折汇款。

**MOA 做什么**
1. **MOA 分摊** — AI 读取小票并逐项分摊，把没有账户成员的份额转给垫付人，
   并作为延期项记入账本，同时用各自的母语生成催款消息。
2. **开户导航** — 输入在留资格、入境日期与 ARC 状态，即可用母语获得接下来三件事和需带的材料。
3. **金融文件解读与诈骗警报** — 解读银行文件与可疑消息，识别出借账户等诈骗信号。

**设计原则**
- MOA **不转移资金**，只生成结算记录与催款消息。
  （刻意限定在无需电子金融业许可即可运营的范围内。）
- **不收集**护照号、外国人登录号与账号。
- 生成式 AI 仅依据内置知识库作答，没有依据时会说"请向银行确认"。
- 即使 AI 调用失败，应用也会以演示回复继续运行。
""",
        """**Vấn đề**
- Hàn Quốc có 253.512 du học sinh nước ngoài (tính đến 2025-04-01, Bộ Giáo dục · KEDI).
- Sau khi nhập cảnh, việc cấp thẻ ARC và mở tài khoản thường mất vài tuần.
- Trong thời gian đó, du học sinh gần như bị loại khỏi việc chia tiền, hội phí câu lạc bộ và mua
  chung ở ký túc xá; bạn bè Hàn Quốc phải giữ tiền mặt hoặc chờ chuyển khoản qua ATM.

**MOA làm gì**
1. **MOA Chia tiền** — AI đọc hoá đơn, chia theo từng món, chuyển phần của người chưa có tài khoản
   sang người trả hộ và ghi hoãn lại vào sổ, đồng thời soạn tin nhắn bằng tiếng mẹ đẻ của từng người.
2. **Hướng dẫn mở tài khoản** — nhập thị thực, ngày nhập cảnh và trạng thái ARC để nhận ba việc cần
   làm tiếp theo cùng giấy tờ cần mang, bằng tiếng của bạn.
3. **Giải mã giấy tờ & cảnh báo lừa đảo** — giải thích giấy tờ ngân hàng và tin nhắn đáng ngờ, phát
   hiện dấu hiệu lừa đảo như yêu cầu cho mượn tài khoản.

**Nguyên tắc thiết kế**
- MOA **không chuyển tiền.** Chỉ tạo bản ghi chia tiền và tin nhắn nhắc.
  (Cố ý giới hạn trong phạm vi vận hành được mà không cần giấy phép kinh doanh tài chính điện tử.)
- **Không thu thập** số hộ chiếu, số đăng ký người nước ngoài hay số tài khoản.
- AI chỉ trả lời dựa trên cơ sở tri thức tích hợp; nếu không có căn cứ, AI nói "hãy hỏi ngân hàng".
- Nếu gọi AI thất bại, ứng dụng vẫn chạy bằng phản hồi demo.
""",
    ),
    "about_caption": (
        "2026 금융 AI Challenge 출품작 · MVP · 실제 금융거래를 제공하지 않는 시연용 서비스입니다.",
        "2026 Finance AI Challenge entry · MVP · a demonstration service that provides no real "
        "financial transactions.",
        "2026 金融 AI Challenge 参赛作品 · MVP · 不提供真实金融交易的演示服务。",
        "Bài dự thi 2026 Finance AI Challenge · MVP · dịch vụ trình diễn, không thực hiện giao dịch "
        "tài chính thật.",
    ),
}

S = {k: dict(zip(LANG_ORDER, v)) for k, v in _T.items()}


def t(key: str, lang: str) -> str:
    d = S.get(key)
    if not d:
        return key
    return d.get(lang) or d.get("en") or key


def topts(key: str, lang: str) -> list[str]:
    """'a|b|c' 형태의 옵션 문자열을 리스트로."""
    return t(key, lang).split("|")
