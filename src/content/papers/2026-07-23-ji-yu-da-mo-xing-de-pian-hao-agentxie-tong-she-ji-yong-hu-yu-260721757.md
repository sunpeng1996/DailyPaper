---
title: 'Co-design of LLM-based preference agents: participation may drive overtrust'
title_zh: 基于大模型的偏好Agent协同设计：用户参与或引发过度信任
authors:
- Michael J. Fell
affiliations:
- University College London
arxiv_id: '2607.21757'
url: https://arxiv.org/abs/2607.21757
pdf_url: https://arxiv.org/pdf/2607.21757
published: '2026-07-23'
collected: '2026-07-27'
category: Agent
direction: 偏好Agent协同设计与信任机制研究
tags:
- LLM Agent
- Preference Alignment
- Co-design
- Overtrust
- Human-Agent Interaction
one_liner: 实证发现用户参与偏好Agent协同设计会催生过度信任，掩盖与真实偏好的系统性偏差
practical_value: '- 做电商/服务类个性化偏好Agent时，不能仅依靠用户自评估的对齐度判定效果，必须增加跨场景的独立离线对齐校验，避免用户因参与设计产生过度信任，在未覆盖场景出现偏好偏差

  - 偏好收集流程中要警惕Barnum效应、IKEA效应导致的虚假对齐，不要将用户对自行参与构建的Agent的高满意度直接等同于偏好对齐效果，避免上线后出现大规模集体偏好趋同于模型默认值的问题

  - 偏好Agent落地初期优先定位为辅助建议工具而非自动决策工具，向用户明确告知Agent能力边界，同时保留用户随时干预、修正偏好的入口，降低过度信任带来的业务投诉风险'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
LLM 偏好 Agent 已被广泛用于代用户决策、用户调研等场景，行业普遍认为引入用户协同设计可提升偏好对齐度、减少代表性偏差，但该流程是否会掩盖真实对齐问题、催生用户过度信任，尚未得到实证验证，尤其在用户无稳定明确偏好的陌生决策领域（如能源、小众消费品选择）风险不明。
### 方法关键点
- 招募12名覆盖不同年龄、AI使用频率、家庭能源设备拥有情况的英国用户作为研究样本
- 核心流程：背景调查收集用户价值观、人格、能源偏好 → 基于GPT-5生成初始个性化Agent描述 → 1小时协同设计访谈，由用户修正Agent描述、测试场景响应并迭代优化 → 独立验证阶段，用户与Agent分别回答5个未见过的能源场景问题，对比双向响应差异
- 采用定性主题编码+定量响应统计的混合分析方法，区分用户感知对齐度与独立验证对齐度
### 关键结果
- 协同设计后10/12的用户强烈认同Agent很好代表了自身偏好，所有用户均认可参与过程体验
- 独立验证显示对齐度参差不齐：Agent100%输出明确倾向，从未选择中立选项，响应同质化程度远高于人类；在用户观点分歧较大的场景对齐度显著下降，出现系统性偏差（如EV充电限速场景所有Agent均支持该政策，而持反对意见的人类用户的Agent全部输出错误结果）
- 不同用户的Agent对齐度差异极大，从完全对齐到几乎完全错位均存在
### 核心结论
用户参与的偏好Agent协同设计本质是「对齐的构建过程」而非「对齐的验证过程」，过度信任会让用户接受甚至主动认同Agent输出的与自身初始偏好不符的结果，规模化落地时会导致全量用户偏好被模型默认值同质化，却被个体用户认为是符合自身需求的
