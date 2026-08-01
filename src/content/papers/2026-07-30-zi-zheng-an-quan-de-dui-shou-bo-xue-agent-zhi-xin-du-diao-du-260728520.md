---
title: 'Agents That Certify Their Own Exploits: Confidence-Scheduled Restricted Responses
  for Safe Opponent Exploitation'
title_zh: 自证安全的对手剥削Agent：置信度调度受限响应算法CS-RNR
authors:
- Boning Li
- Longbo Huang
affiliations:
- Institute for Interdisciplinary Information Sciences, Tsinghua University
arxiv_id: '2607.28520'
url: https://arxiv.org/abs/2607.28520
pdf_url: https://arxiv.org/pdf/2607.28520
published: '2026-07-30'
collected: '2026-08-01'
category: Agent
direction: Agent安全博弈·自证式策略部署
tags:
- Safe Agent
- Opponent Exploitation
- Game Theory
- Confidence Sequence
- Restricted Response
- Imperfect Information Game
one_liner: 提出首个可自证部署策略安全性的对手剥削算法，收益达基线6.2倍且不超安全预算
practical_value: '- 电商流量博弈/广告竞价场景可借鉴「先证后用」安全机制：新策略上线前先做全局最坏case评估，将损失严格限制在预设预算内，避免策略迭代的不可控风险

  - 对抗场景（反作弊、恶意流量识别）可复用anytime-valid confidence sequences做持续偏差检测，低误报识别对手非均衡行为，避免过早响应的反剥削风险

  - 动态策略调度可参考pin level网格搜索+预算校验逻辑：在基准策略和最优响应间插值，每步校验风险边界，平衡收益和安全性，无需依赖固定超参数'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
双人零和不完美信息博弈中，纳什均衡策略可保证保底收益但无法剥削对手非均衡漏洞；现有剥削方法要么证据不足无法启动，要么对不完备对手模型的最优响应易被反剥削，尤其是对手偏差分散在多决策点时，传统二元放行规则和连续响应都无法兼顾收益与安全。

### 方法关键点
- 检测层：用anytime-valid置信序列统计对手动作频率，仅当频率区间与纳什基准区间完全分离时才确认偏差，构建保守对手模型，保证检测的时间均匀错误控制
- 响应层：在不同pin level（0到1的插值系数）下求解受限响应策略，在纳什基准和模型最优响应间做平滑插值，避免极端策略
- 认证层：对每个候选策略做全局全树最优响应评估，计算其可被剥削的最大损失（安全证书），仅当证书低于用户预设安全预算时才部署，否则回退到更低风险策略

### 关键结果
在Leduc扑克、说谎者骰子、5阶Leduc扑克三类博弈上测试，对比纳什策略、二元放行门、固定混合策略等6个基线；CS-RNR在Leduc上稳态收益是二元门的6.2倍，说谎者骰子上是5.8倍，36000次审计对局全部符合安全证书约束，无预算超限；固定混合策略用相同估计器但无认证，剥削性超出预算13.6倍。

**最值得记住的结论：安全是部署策略本身的属性，而非生成策略的模型的属性，上线前对完整策略做最坏情况校验，比优化模型可信度更能有效控制风险。**
