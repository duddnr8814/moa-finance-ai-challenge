# -*- coding: utf-8 -*-
"""지식베이스 표시용 번역.

kb.py의 한국어 원문은 Gemini 프롬프트에 주입되는 '근거'이므로 그대로 둔다.
이 모듈은 화면에 보여줄 때만 쓰는 번역본이며, 값은 (ko, en, zh, vi) 4-튜플이다.
번역이 없으면 t_kb()가 한국어 원문으로 폴백한다.
"""

from moa.i18n import LANG_ORDER


def _d(tup):
    return dict(zip(LANG_ORDER, tup))


# ---------------------------------------------------------------- 계좌 개설 규칙
_RULES = {
    "arc-timeline": {
        "topic": (
            "외국인등록증(ARC) 발급",
            "Getting the Alien Registration Card (ARC)",
            "外国人登录证（ARC）办理",
            "Cấp thẻ cư trú (ARC)",
        ),
        "fact": (
            "유학(D-2)·어학연수(D-4) 체류자격 외국인은 입국 후 출입국·외국인청에 외국인등록을 "
            "신청한다. 신청 후 카드 수령까지는 통상 수 주가 걸리며, 이 기간에는 등록증 실물이 "
            "없어 금융거래에 제약이 생긴다.",
            "Foreign nationals on a D-2 (degree) or D-4 (language) visa apply for alien "
            "registration at an immigration office after arriving. It usually takes several weeks "
            "from application to receiving the card, and during that gap you have no physical card, "
            "which limits what you can do financially.",
            "持 D-2（留学）或 D-4（语言研修）资格的外国人入境后需到出入境·外国人厅申请外国人登录。"
            "从申请到领卡通常需要数周，这段期间没有实体登录证，金融交易会受限。",
            "Người nước ngoài có thị thực D-2 (du học) hoặc D-4 (học tiếng) nộp đăng ký người nước "
            "ngoài tại cơ quan xuất nhập cảnh sau khi đến. Từ lúc nộp đến khi nhận thẻ thường mất "
            "vài tuần, và trong thời gian đó bạn chưa có thẻ nên bị hạn chế giao dịch tài chính.",
        ),
        "source": (
            "출입국·외국인정책본부 외국인등록 안내 (제도 개요)",
            "Korea Immigration Service, alien registration guide (overview of the system)",
            "出入境·外国人政策本部 外国人登录指南（制度概要）",
            "Cục Xuất nhập cảnh Hàn Quốc, hướng dẫn đăng ký người nước ngoài (tổng quan)",
        ),
    },
    "pre-arc-account": {
        "topic": (
            "ARC 발급 전 계좌 개설",
            "Opening an account before the ARC arrives",
            "ARC 下发前开户",
            "Mở tài khoản trước khi có ARC",
        ),
        "fact": (
            "일부 은행은 ARC 수령 전이라도 여권, 본인 명의 국내 휴대폰 번호, 체류지 증빙"
            "(기숙사 입사확인서·임대차계약서), 재학(입학) 증명 서류를 갖추면 '금융거래한도계좌' "
            "형태로 개설을 허용한다. 다만 취급 여부와 요구 서류는 은행·지점마다 달라 방문 전 "
            "확인이 필요하다.",
            "Some banks will open a limited-transaction account before you receive your ARC, if you "
            "bring a passport, a Korean phone number in your own name, proof of residence "
            "(dormitory confirmation or lease contract) and a certificate of enrolment or "
            "admission. Whether a branch does this at all, and which documents it asks for, varies "
            "by bank and branch — call before you go.",
            "部分银行在你领到 ARC 之前，只要备齐护照、本人名下的韩国手机号、居住证明"
            "（宿舍入住确认书或租赁合同）以及在学（入学）证明，就可以开立"
            "「金融交易限额账户」。但是否受理以及所需材料因银行与网点而异，前往前请先确认。",
            "Một số ngân hàng cho mở tài khoản hạn mức trước khi bạn nhận ARC, nếu bạn có hộ chiếu, "
            "số điện thoại Hàn Quốc đứng tên mình, giấy tờ chứng minh nơi ở (xác nhận ký túc xá "
            "hoặc hợp đồng thuê nhà) và giấy chứng nhận nhập học. Việc có nhận hồ sơ hay không và "
            "giấy tờ yêu cầu khác nhau theo từng ngân hàng, từng chi nhánh — hãy gọi hỏi trước.",
        ),
        "source": (
            "은행권 공통 안내 및 외국인 대상 실무 가이드",
            "Common bank guidance and practical guides for foreign residents",
            "银行业通用指引及面向外国人的实务指南",
            "Hướng dẫn chung của ngân hàng và cẩm nang thực tế cho người nước ngoài",
        ),
    },
    "limit-account": {
        "topic": (
            "금융거래한도계좌(한도제한계좌)",
            "Limited-transaction account",
            "金融交易限额账户",
            "Tài khoản hạn mức giao dịch",
        ),
        "fact": (
            "금융사기 예방을 위해 거래 목적이 확인되지 않은 신규 계좌는 한도제한계좌로 개설된다. "
            "2024년 5월 2일부터 한도제한계좌의 이체·ATM 출금 한도가 1일 30만원에서 100만원으로 "
            "상향되었다(창구 거래 한도는 별도).",
            "To prevent financial fraud, a new account opened without verified transaction purpose "
            "is issued as a limited-transaction account. Since 2 May 2024 the daily transfer and "
            "ATM withdrawal limit on such accounts rose from 300,000 KRW to 1,000,000 KRW "
            "(over-the-counter limits are separate).",
            "为防范金融诈骗，未确认交易目的的新开账户会以限额账户形式开立。自 2024 年 5 月 2 日起，"
            "限额账户的转账及 ATM 取款限额由每日 30 万韩元上调至 100 万韩元（柜台交易限额另计）。",
            "Để phòng chống gian lận tài chính, tài khoản mới chưa xác minh được mục đích giao dịch "
            "sẽ được mở dưới dạng tài khoản hạn mức. Từ ngày 2/5/2024, hạn mức chuyển khoản và rút "
            "ATM của loại tài khoản này tăng từ 300.000 KRW lên 1.000.000 KRW mỗi ngày (hạn mức "
            "giao dịch tại quầy tính riêng).",
        ),
        "source": (
            "금융위원회 보도자료 (2024-05-02 시행)",
            "Financial Services Commission press release (effective 2024-05-02)",
            "金融委员会新闻稿（2024-05-02 施行）",
            "Thông cáo của Ủy ban Dịch vụ Tài chính (hiệu lực 2024-05-02)",
        ),
    },
    "limit-release": {
        "topic": ("한도 해제", "Lifting the limit", "解除限额", "Gỡ hạn mức"),
        "fact": (
            "한도제한계좌는 거래 목적을 증빙하면 일반계좌로 전환할 수 있다. 유학생의 경우 "
            "재학증명서, 학비 납입 내역, 기숙사비·월세 자동이체, 장학금·아르바이트 소득 증빙 등이 "
            "목적 확인 자료로 쓰인다. 인정 서류와 기준은 은행마다 다르다.",
            "A limited account can be converted to a normal one once you evidence the purpose of "
            "your transactions. For students, a certificate of enrolment, tuition payment records, "
            "automatic dormitory or rent payments, and proof of scholarship or part-time income are "
            "commonly accepted. Which documents count, and the threshold, differ by bank.",
            "只要能证明交易目的，限额账户即可转为普通账户。留学生常用的证明包括在学证明、学费缴纳记录、"
            "宿舍费或房租自动扣款、奖学金及打工收入证明等。认可的材料与标准因银行而异。",
            "Tài khoản hạn mức có thể chuyển thành tài khoản thường khi bạn chứng minh được mục đích "
            "giao dịch. Với du học sinh, giấy chứng nhận đang học, biên lai đóng học phí, tự động "
            "trích nộp tiền ký túc xá hoặc tiền thuê nhà, chứng từ học bổng hay thu nhập làm thêm "
            "thường được chấp nhận. Giấy tờ được công nhận và tiêu chuẩn khác nhau theo ngân hàng.",
        ),
        "source": (
            "은행권 한도제한계좌 해제 기준 안내",
            "Bank guidance on lifting limited-account restrictions",
            "银行业限额账户解除标准指引",
            "Hướng dẫn của ngân hàng về gỡ hạn chế tài khoản hạn mức",
        ),
    },
    "phone-first": {
        "topic": (
            "본인 명의 휴대폰이 먼저",
            "The phone comes first",
            "先办本人名下手机",
            "Điện thoại trước đã",
        ),
        "fact": (
            "국내 계좌 개설과 모바일 뱅킹 본인확인에는 본인 명의 휴대폰 번호가 사실상 필수다. "
            "ARC가 없어도 여권으로 선불(프리페이드) 유심을 개통할 수 있는 통신사가 있어, 보통 "
            "'유심 → 계좌' 순서로 진행한다.",
            "A phone number in your own name is effectively required both to open an account and to "
            "verify yourself in mobile banking. Some carriers will activate a prepaid SIM on a "
            "passport alone, without an ARC, so the usual order is SIM first, account second.",
            "开立韩国账户和手机银行本人认证，实际上都需要本人名下的手机号。有些运营商仅凭护照即可开通预付卡，"
            "无需 ARC，因此通常按「先办卡、后开户」的顺序进行。",
            "Số điện thoại đứng tên bạn gần như là bắt buộc để mở tài khoản và xác minh danh tính "
            "trong ngân hàng di động. Một số nhà mạng cho mở SIM trả trước chỉ với hộ chiếu, không "
            "cần ARC, nên thứ tự thường là SIM trước, tài khoản sau.",
        ),
        "source": (
            "통신사 외국인 가입 안내 (제도 개요)",
            "Mobile carrier guidance for foreign subscribers (overview)",
            "运营商外国人入网指南（制度概要）",
            "Hướng dẫn đăng ký cho người nước ngoài của nhà mạng (tổng quan)",
        ),
    },
    "name-match": {
        "topic": (
            "여권 영문명 일치",
            "Your name must match your passport",
            "英文姓名须与护照一致",
            "Tên phải khớp với hộ chiếu",
        ),
        "fact": (
            "은행·통신사·학교에 등록하는 영문 이름은 여권과 공백·순서·미들네임까지 똑같아야 한다. "
            "표기가 어긋나면 본인확인이 실패해 계좌 개설이나 앱 인증이 막히는 일이 흔하다.",
            "The romanised name you register with a bank, a carrier and your university must match "
            "your passport exactly — spacing, order and middle name included. A mismatch commonly "
            "fails identity verification and blocks account opening or app authentication.",
            "在银行、运营商与学校登记的英文姓名，必须与护照完全一致，包括空格、顺序与中间名。"
            "一旦不符，本人认证会失败，常导致无法开户或无法完成 App 认证。",
            "Tên latinh bạn đăng ký với ngân hàng, nhà mạng và trường phải trùng khớp hoàn toàn với "
            "hộ chiếu — kể cả khoảng trắng, thứ tự và tên đệm. Sai lệch thường khiến xác minh danh "
            "tính thất bại và chặn việc mở tài khoản hay xác thực ứng dụng.",
        ),
        "source": (
            "금융권 실명확인 실무",
            "Real-name verification practice in Korean finance",
            "金融业实名确认实务",
            "Thực tiễn xác minh danh tính trong ngành tài chính Hàn Quốc",
        ),
    },
    "campus-branch": {
        "topic": (
            "캠퍼스 지점 활용",
            "Use the campus branch",
            "善用校园网点",
            "Dùng chi nhánh trong trường",
        ),
        "fact": (
            "대학 캠퍼스 안이나 인근 지점은 외국인 유학생 계좌 업무를 자주 다뤄 필요 서류 안내가 "
            "빠르고 영어 응대가 가능한 경우가 많다. 학교 국제처(International Office)가 은행과 "
            "단체 개설 행사를 여는 학기도 있다.",
            "Branches on or near a university campus handle student accounts often, so they explain "
            "the required documents quickly and frequently serve you in English. Some semesters the "
            "International Office runs a group account-opening event with a bank.",
            "校园内或附近的网点经常办理留学生开户业务，材料说明更快，且多数可用英语接待。"
            "有些学期学校国际处还会与银行合办集体开户活动。",
            "Chi nhánh trong hoặc gần khuôn viên trường xử lý tài khoản sinh viên thường xuyên nên "
            "hướng dẫn giấy tờ nhanh và nhiều nơi tiếp bằng tiếng Anh. Một số học kỳ, phòng Hợp tác "
            "quốc tế còn tổ chức buổi mở tài khoản tập thể cùng ngân hàng.",
        ),
        "source": (
            "대학 국제처 신입생 안내 관행",
            "Common practice of university international offices for new students",
            "高校国际处新生指引惯例",
            "Thông lệ hướng dẫn tân sinh viên của phòng Hợp tác quốc tế",
        ),
    },
    "prepaid-card": {
        "topic": (
            "계좌 개설 전 대안 결제수단",
            "Payment options before you have an account",
            "开户前的替代支付方式",
            "Cách thanh toán trước khi có tài khoản",
        ),
        "fact": (
            "계좌 개설 전 공백기에는 선불카드·선불 충전형 결제수단을 쓸 수 있다. 2026년 8월 토스가 "
            "전국 15개 대학 국제처를 통해 신입 외국인 유학생 대상 선불카드를 제공하기 시작했다. "
            "다만 선불카드는 '결제 수단'을 채워줄 뿐, 친구끼리 나눠 내고 정산하는 문제까지 "
            "해결하지는 않는다.",
            "During the gap before you have an account you can use a prepaid card or another "
            "top-up payment method. In August 2026 Toss began offering prepaid cards to incoming "
            "international students through the international offices of 15 universities. A prepaid "
            "card fills the 'means of payment' gap only — it does not solve splitting a bill with "
            "friends and settling up afterwards.",
            "在开户前的空白期，可以使用预付卡或充值型支付方式。2026 年 8 月，Toss 通过全国 15 所高校"
            "国际处开始向新入学的外国留学生提供预付卡。但预付卡只补上了「支付手段」，"
            "并不能解决朋友之间分摊与结算的问题。",
            "Trong giai đoạn chưa có tài khoản, bạn có thể dùng thẻ trả trước hoặc phương thức nạp "
            "tiền khác. Tháng 8/2026, Toss bắt đầu cấp thẻ trả trước cho tân du học sinh thông qua "
            "phòng Hợp tác quốc tế của 15 trường đại học. Tuy nhiên thẻ trả trước chỉ lấp chỗ trống "
            "về 'phương tiện thanh toán', không giải quyết việc chia tiền và quyết toán với bạn bè.",
        ),
        "source": (
            "데일리안 (2026-08-27) 토스 외국인 유학생 선불카드 출시 보도",
            "Dailian (2026-08-27), report on Toss launching prepaid cards for international students",
            "Dailian（2026-08-27）关于 Toss 推出留学生预付卡的报道",
            "Dailian (2026-08-27), bài báo về việc Toss ra mắt thẻ trả trước cho du học sinh",
        ),
    },
}

# ---------------------------------------------------------------- 사기 유형
_SCAMS = {
    "account-lending": {
        "name": (
            "통장 양도·대여 요구 (대포통장)",
            "Being asked to hand over or lend your bank account",
            "要求转让或出借账户（借名账户）",
            "Bị yêu cầu nhượng hoặc cho mượn tài khoản",
        ),
        "signal": (
            "계좌·체크카드·비밀번호를 빌려주면 돈을 준다고 제안",
            "An offer to pay you for lending your account, debit card or PIN",
            "提出只要借出账户、借记卡或密码就给钱",
            "Đề nghị trả tiền nếu bạn cho mượn tài khoản, thẻ ghi nợ hoặc mật khẩu",
        ),
        "why": (
            "전자금융거래법상 접근매체 양도·대여는 처벌 대상이다. 피해자가 아니라 가해자로 "
            "조사받게 되고, 금융거래가 장기간 막히며 체류자격에도 영향을 줄 수 있다.",
            "Transferring or lending an access medium is punishable under the Electronic Financial "
            "Transactions Act. You would be investigated as an offender, not a victim, your banking "
            "would be blocked for a long time, and your visa status could be affected.",
            "根据《电子金融交易法》，转让或出借接入媒介属于处罚对象。你会以加害人而非受害人身份接受调查，"
            "金融交易将长期受限，居留资格也可能受影响。",
            "Theo Luật Giao dịch Tài chính Điện tử, việc nhượng hoặc cho mượn phương tiện truy cập "
            "là hành vi bị xử phạt. Bạn sẽ bị điều tra với tư cách người vi phạm chứ không phải nạn "
            "nhân, giao dịch ngân hàng bị chặn lâu dài và tư cách lưu trú có thể bị ảnh hưởng.",
        ),
        "action": (
            "즉시 거절하고 대화 내용을 저장. 이미 넘겼다면 은행에 지급정지 요청 후 경찰(112) 신고.",
            "Refuse immediately and save the conversation. If you already handed it over, ask the "
            "bank to suspend payments and report it to the police (112).",
            "立即拒绝并保存聊天记录。若已交出，请先向银行申请止付，再报警（112）。",
            "Từ chối ngay và lưu lại đoạn hội thoại. Nếu đã đưa rồi, hãy yêu cầu ngân hàng phong toả "
            "rồi báo cảnh sát (112).",
        ),
    },
    "fake-part-time": {
        "name": (
            "고수익 아르바이트 위장",
            "Fake high-paying part-time job",
            "伪装成高薪兼职",
            "Việc làm thêm lương cao giả mạo",
        ),
        "signal": (
            "'단순 송금 업무', '입금된 돈을 인출해 전달' 같은 고수익 단기 알바 제안",
            "A short, well-paid job described as 'simple transfers' or 'withdraw the money that "
            "arrives and pass it on'",
            "以「简单转账」「把到账的钱取出来转交」为名的高薪短期兼职",
            "Việc ngắn hạn lương cao mô tả là 'chuyển khoản đơn giản' hay 'rút tiền vừa nhận rồi "
            "giao lại'",
        ),
        "why": (
            "보이스피싱 자금 세탁의 인출책 역할이며 형사 처벌 대상이다.",
            "This is the cash-out role in voice-phishing money laundering, and it is a criminal "
            "offence.",
            "这是电信诈骗洗钱链条中的取款环节，属于刑事犯罪。",
            "Đây là vai trò rút tiền trong đường dây rửa tiền lừa đảo qua điện thoại, và là tội hình sự.",
        ),
        "action": (
            "지원하지 말고 채용 공고와 대화를 캡처해 보관. 학교 국제처에 알린다.",
            "Do not apply. Screenshot the listing and the conversation, and tell your university's "
            "international office.",
            "不要应聘。截图保存招聘信息与聊天记录，并告知学校国际处。",
            "Đừng ứng tuyển. Chụp màn hình tin tuyển dụng và đoạn hội thoại, rồi báo phòng Hợp tác "
            "quốc tế của trường.",
        ),
    },
    "impersonation": {
        "name": (
            "출입국·검찰·경찰 사칭",
            "Someone posing as immigration, a prosecutor or the police",
            "冒充出入境·检察·警察",
            "Giả danh xuất nhập cảnh, viện kiểm sát hoặc cảnh sát",
        ),
        "signal": (
            "'체류 자격이 취소된다', '수사 중이니 안전계좌로 송금하라'는 전화·메시지",
            "A call or message saying your visa will be cancelled, or that you are under "
            "investigation and must transfer money to a 'safe account'",
            "来电或短信称「你的居留资格将被取消」「正在调查，请把钱转入安全账户」",
            "Cuộc gọi hoặc tin nhắn nói tư cách lưu trú của bạn sẽ bị huỷ, hoặc bạn đang bị điều tra "
            "và phải chuyển tiền vào 'tài khoản an toàn'",
        ),
        "why": (
            "정부기관은 전화로 송금을 요구하지 않는다. 전형적인 보이스피싱이다.",
            "Government bodies never ask for a transfer over the phone. This is textbook voice "
            "phishing.",
            "政府机关绝不会通过电话要求汇款。这是典型的电信诈骗。",
            "Cơ quan nhà nước không bao giờ yêu cầu chuyển tiền qua điện thoại. Đây là lừa đảo "
            "điển hình.",
        ),
        "action": (
            "끊고 직접 기관 대표번호로 재확인. 이미 송금했다면 즉시 은행과 112에 신고.",
            "Hang up and call the organisation back on its official number. If you already "
            "transferred, report it to your bank and to 112 at once.",
            "挂断后拨打该机关的官方总机号码核实。若已汇款，请立即向银行与 112 报案。",
            "Cúp máy và gọi lại theo số tổng đài chính thức của cơ quan đó. Nếu đã chuyển tiền, hãy "
            "báo ngân hàng và 112 ngay lập tức.",
        ),
    },
    "unlicensed-fx": {
        "name": (
            "무등록 환전·송금 브로커",
            "Unlicensed currency exchange or remittance broker",
            "无牌照兑换·汇款中介",
            "Môi giới đổi tiền hoặc chuyển tiền không phép",
        ),
        "signal": (
            "'은행보다 환율이 좋다'며 개인 계좌로 송금을 유도하는 SNS 환전상",
            "A social-media exchanger who claims a better rate than the bank and steers you to a "
            "personal account",
            "社交平台上的兑换商声称「汇率比银行好」，诱导你汇入个人账户",
            "Người đổi tiền trên mạng xã hội khoe tỷ giá tốt hơn ngân hàng và dụ bạn chuyển vào tài "
            "khoản cá nhân",
        ),
        "why": (
            "돈을 떼여도 보호받기 어렵고, 자금세탁 계좌에 연루될 수 있다.",
            "If the money disappears you have little protection, and you may be drawn into a money "
            "laundering account.",
            "钱被卷走后很难获得保护，还可能被卷入洗钱账户。",
            "Nếu mất tiền bạn khó được bảo vệ, và có thể bị liên đới vào tài khoản rửa tiền.",
        ),
        "action": (
            "등록된 은행·인가받은 소액해외송금업자만 이용한다.",
            "Use only registered banks or licensed small-sum overseas remittance providers.",
            "只使用已登记的银行或获批的小额海外汇款业者。",
            "Chỉ dùng ngân hàng đã đăng ký hoặc đơn vị chuyển tiền quốc tế nhỏ lẻ được cấp phép.",
        ),
    },
    "tuition-discount": {
        "name": (
            "학비 대납 할인 사기",
            "Tuition 'pay-on-your-behalf' discount scam",
            "代缴学费折扣诈骗",
            "Lừa đảo 'đóng học phí hộ' giảm giá",
        ),
        "signal": (
            "'학비를 대신 내주고 수수료만 받겠다'는 개인·유학원 제안",
            "An individual or agency offering to pay your tuition for you and take only a fee",
            "个人或留学中介提出「替你缴学费，只收手续费」",
            "Cá nhân hoặc trung tâm du học đề nghị đóng học phí hộ và chỉ lấy phí dịch vụ",
        ),
        "why": (
            "선입금만 받고 잠적하거나, 도난 자금이 학교로 흘러가 학생이 조사 대상이 된다.",
            "They may take your money and disappear, or pay with stolen funds — in which case the "
            "student ends up under investigation.",
            "对方可能收钱后失联，或用赃款代缴，导致学生成为调查对象。",
            "Họ có thể nhận tiền rồi biến mất, hoặc đóng bằng tiền phạm pháp — khiến sinh viên trở "
            "thành đối tượng bị điều tra.",
        ),
        "action": (
            "학비는 반드시 학교 공식 고지서의 가상계좌로만 납부한다.",
            "Pay tuition only into the virtual account printed on your university's official "
            "invoice.",
            "学费必须只汇入学校正式缴费通知单上的虚拟账户。",
            "Chỉ đóng học phí vào tài khoản ảo ghi trên giấy báo chính thức của trường.",
        ),
    },
}

_CONFIDENCE = {
    "high": ("높음", "high", "高", "cao"),
    "medium": ("보통", "medium", "中", "trung bình"),
    "low": ("낮음", "low", "低", "thấp"),
}

_SEVERITY = {
    "critical": ("매우 위험", "critical", "极危险", "rất nguy hiểm"),
    "high": ("위험", "high", "危险", "nguy hiểm"),
    "medium": ("주의", "medium", "注意", "cần lưu ý"),
}

RULES = {k: {f: _d(v) for f, v in fields.items()} for k, fields in _RULES.items()}
SCAMS = {k: {f: _d(v) for f, v in fields.items()} for k, fields in _SCAMS.items()}
CONFIDENCE = {k: _d(v) for k, v in _CONFIDENCE.items()}
SEVERITY = {k: _d(v) for k, v in _SEVERITY.items()}


def rule(entry: dict, field: str, lang: str) -> str:
    """kb.ACCOUNT_RULES 항목의 번역된 필드. 없으면 한국어 원문."""
    return RULES.get(entry.get("id"), {}).get(field, {}).get(lang) or entry.get(field, "")


def scam(entry: dict, field: str, lang: str) -> str:
    """kb.SCAM_PATTERNS 항목의 번역된 필드.

    field: name | signal | why | action
    """
    fallback = {"name": "name_ko", "why": "why_dangerous"}.get(field, field)
    return SCAMS.get(entry.get("id"), {}).get(field, {}).get(lang) or entry.get(fallback, "")


def confidence(value: str, lang: str) -> str:
    return CONFIDENCE.get(value, {}).get(lang) or value


def severity(value: str, lang: str) -> str:
    return SEVERITY.get(value, {}).get(lang) or value
