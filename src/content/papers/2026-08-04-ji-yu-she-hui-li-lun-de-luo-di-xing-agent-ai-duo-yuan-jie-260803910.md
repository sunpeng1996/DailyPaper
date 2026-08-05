---
title: 'Socially Grounded Agentic AI: Coordinating Plural Perspectives through Social
  Theory'
title_zh: 基于社会理论的落地型Agent AI：多元价值视角协调框架
authors:
- Matt Ratto
- Abhishek Moturu
- Daniel Silver
affiliations:
- University of Toronto
- Vector Institute for Artificial Intelligence
- Schwartz Reisman Institute for Technology and Society
- Temerty Centre for Artificial Intelligence Education and Research In Medicine
arxiv_id: '2608.03910'
url: https://arxiv.org/abs/2608.03910
pdf_url: https://arxiv.org/pdf/2608.03910
published: '2026-08-04'
collected: '2026-08-05'
category: Agent
direction: Agent 多元价值对齐架构设计
tags:
- Pluralistic Alignment
- Multi-Agent Coordination
- Agent Governance
- LLM Alignment
- Social Theory
one_liner: 引入社会学核心理论重构Agent多元对齐范式，将其从输出多样化转化为可审计的社会协调问题
practical_value: '- 多角色Agent设计可直接复用：电商客服、商品合规审核、平台治理场景可将用户、运营、合规、商家等角色结构化编码，明确各角色权责、证据来源、决策优先级，替代传统单一角色prompt，大幅提升复杂诉求处理合理性

  - 公平性优化可落地：做个性化推荐的群体公平性治理时，可引入场域加权聚合逻辑，不直接拟合历史用户行为分布，而是基于专家规则、弱势群体诉求、平台治理目标等不同立场加权，避免放大马太效应和偏见

  - 可审计性设计参考：Agent系统无需仅输出最终结果，可留存角色激活、协商轨迹、加权规则等全链路日志，既满足监管合规要求，也便于bad case快速根因定位

  - 评估体系升级：不要只评估Agent最终输出的准确率/满意率，新增轨迹层面的评估指标，比如角色匹配度、诉求覆盖度、升级触发合理性，提升复杂场景下Agent的鲁棒性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM与Agent系统落地场景日益多元，传统单一价值对齐范式无法适配不同文化、身份、角色、立场主体的诉求，现有多元对齐方法仅关注输出层面的多样性，缺乏对价值的社会属性、权力结构、协作规则的建模，容易出现视角边界模糊、公平性缺失、决策不可解释等问题，在电商治理、客服、公共服务等高利害场景下缺陷尤为突出。

### 方法关键点
- 重构三类主流多元对齐范式：基于米德「generalized other」理论，将Overton多元主义从枚举随机视角改造为**角色索引化表示**，每个角色明确定义权责、证据准入范围、与其他角色的关系、升级触发条件；基于哈贝马斯交往行动理论，将可控多元主义从单向prompt控制改造为**结构化多Agent协商流程**，设计「主张-证据-反驳-修正」的交互协议，明确投票、仲裁、人工升级等收敛规则；基于布迪厄场域理论，将分布多元主义从拟合全量群体行为分布改造为**场域感知加权聚合**，区分不同立场的权威性、公平性权重，避免直接复刻现有社会权力不平等。
- 提出可落地技术管线：角色索引化表示 → 结构化多Agent协商 → 溯源敏感的加权聚合 → 全交互轨迹审计，所有环节的决策规则均可配置、可追溯。
- 升级评估体系：从仅评估最终输出准确率，升级为轨迹层面的6维度评估：角色保真度、视角覆盖度、协商质量、溯源透明度、场域敏感度、升级合理性。

### 关键实验
本文为ICML 2026多元对齐Workshop的概念框架类论文，暂无公开落地实验数据，后续计划在医疗协调、公共服务、面向公众的AI服务等场景验证效果。

### 最值得记住的一句话
多元对齐的核心不是输出多样化，而是可审计、可问责的社会协调。
