---
title: 'EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under
  Missing Evidence'
title_zh: EpiSEM-Bench：缺失证据场景下LLM Agent安全性与证据恢复评测基准
authors:
- Qijin Zhang
- Hanzhen Wang
- Yuehan Zhao
- Haoyu Dai
- Yao Shu
- Zhongxiang Dai
- Shuang Qiu
affiliations:
- City University of Hong Kong
- The Hong Kong University of Science and Technology (Guangzhou)
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2610.31650'
url: https://arxiv.org/abs/2610.31650
pdf_url: https://arxiv.org/pdf/2610.31650
published: '2026-10-22'
collected: '2026-10-23'
category: Eval
direction: Agent安全评测 · 证据缺失场景
tags:
- LLM Agent
- Safety Evaluation
- Missing Evidence
- Benchmark
- Evidence Recovery
one_liner: 推出含6个领域300对任务的可执行基准，评测证据缺失下LLM Agent的安全与证据恢复能力
practical_value: '- 电商高风险Agent（代客下单、自动退款、优惠券发放）可复用基准的核心设计：将安全规则与可见证据解耦，增加证据缺失校验逻辑，避免因工具返回信息不全导致超额退款、错发权益等违规操作

  - 关键操作流程可新增独立证据恢复审计工具入口，要求Agent在执行高风险动作前主动校验缺失的核心规则字段，实测可降低90%以上的证据缺失类误操作

  - 可复用配对任务评测范式：构造同请求、不同安全状态的配对任务，同时衡量Agent合规率与合法任务完成率，避免因过度收紧安全规则导致的用户体验下降'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM Agent评测多聚焦工具使用能力、对抗样本鲁棒性，未覆盖工具返回无虚假信息但缺失关键安全事实的场景——这类场景无攻击者介入，却极易导致Agent执行违规操作，且无法通过单纯的任务完成率/安全拒答率衡量真实表现，需要专门的评测基准区分滥用、过度拒答、合理校验三类行为。

### 方法关键点
- 构造6个领域（含金融支付、电商履约等）共300对配对任务，每对任务共享用户请求、工具接口，仅底层安全状态不同（对应操作允许/禁止两种场景），共覆盖944条关键安全事实、419条无关事实
- 设计三层评测范式：1）全证据基准，测基础任务完成率与违规率；2）证据压制场景，系统隐藏关键安全事实，测安全边界阈值；3）可恢复证据场景，提供独立审计工具入口，测Agent主动恢复证据并正确决策的能力
- 提出6个联合度量指标，区分任务完成率、违规执行率、证据恢复有效率，避免单一指标的误导（比如全拒答可获得极低违规率但无实用价值）

### 关键结果
在10款主流LLM上测试：1）高任务完成率的模型普遍违规率更高，Qwen3-14B全证据下任务完成率达92%，但违规率高达77.3%；2）所有模型在增加证据恢复入口后违规率均下降，DeepSeek-V4.1-Flash的证据恢复后有效配对决策率达58.4%，为所有模型最高；3）抗证据缺失能力与有效恢复能力无强相关性，GPT-6-Luna安全边界最高但有效恢复率仅30.5%。

**最值得记住的一句话**：LLM Agent的安全能力不能仅看单一的违规率或任务完成率，必须同时验证其在证据不全时主动获取关键信息、并根据真实安全状态区分操作的能力。
