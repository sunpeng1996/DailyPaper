---
title: 'Cybernetic and Epistemic: A Missing Vocabulary for Trustworthy Agentic Delegation'
title_zh: 控制论与认知视角：可信智能体任务委托的缺失术语体系
authors:
- Jérémie Lumbroso
affiliations:
- University of Pennsylvania
arxiv_id: '2610.00961'
url: https://arxiv.org/abs/2610.00961
pdf_url: https://arxiv.org/pdf/2610.00961
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: 可信智能体 · 任务委托治理
tags:
- Agent Trustworthiness
- Delegation Governance
- Human-in-the-loop
- ORRCF
- Epistemic Audit
one_liner: 区分智能体委托通道两类语言功能，提出ORRCF记录规范与可测试的可信治理标准
practical_value: '- 电商/广告推荐的AI生成策略（如文案、选品规则、流量分配规则）落地时，可复用ORRCF规范记录每个决策的可选方案、推荐理由、置信度、反向触发条件，避免只有审批没有可追溯依据，大幅降低线上事故排查与合规审计成本

  - 涉及人在环路的Agent工作流（如智能运营Agent、内容审核Agent、选品Agent），需区分cybernetic指令（直接要求做什么）和epistemic说明（为什么做、什么条件下调整），可大幅提升Agent执行灵活性，减少对齐偏差

  - 现有AI决策的解释性指标不能只看是否有解释文本，需补充「反向触发条件可测试性」校验，避免解释文本仅用于过审、不具备实际参考价值，减少虚假解释导致的合规风险'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前智能体任务委托领域的「人类 oversight」设计仅要求对输出做审批，未区分委托通道中语言的两类核心功能，大量解释类输出被校准为仅用于通过审批而非传递真实决策依据，导致人在环路监督沦为橡皮图章，无法追溯决策逻辑、定位系统性偏差。尤其在电商推荐、广告投放场景，若AI选品、文案生成、流量分配决策缺乏可审计的理由记录，出现歧视性推荐、不合规内容时无法定位根因，合规风险极高。
### 方法关键点
- 明确区分委托通道两类语言功能：cybernetic语言用于协调行动，成功标准为现实匹配指令；epistemic语言用于协调认知，成功标准为表述符合现实且可被第三方验证
- 提出可信委托核心治理准则：所有重大决策必须附带第三方可测试的反向触发条件（即何种场景下决策会变更），无该条件的决策从记录层面无法与橡皮图章区分
- 提出可落地的决策记录规范ORRCF：每条决策必填5个字段：可选方案（Options）、推荐结果（Recommendation）、决策理由（Rationale）、置信度（Confidence）、反向触发条件（Falsifier）
- 设计两层重构测试校验记录有效性：① 未参与决策的第三方仅根据记录预测某一扰动下决策是否变更；② 用实际扰动重新请求智能体，校验预测与实际结果的匹配度
### 关键结果
论文引用已发表的计量研究结果：弗吉尼亚州重罪量刑场景中，风险评估工具的推荐仅为控制论类勾选框，无决策理由记录要求，相同风险得分下黑人被告的刑期比白人被告长12~24%，且现有仅核查输出是否通过的监督机制完全无法发现该类系统性偏差。论文通过3个实操案例验证了ORRCF规范可在不影响工作效率的前提下实现决策可审计。
### 核心结论
一个没有可测试反向触发条件的决策，从记录层面无法和橡皮图章区分开。
