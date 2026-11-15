---
title: Towards a Theory of Learnability via Debate
title_zh: 面向辩论驱动可学习性的理论框架研究
authors:
- Tosca Lechner
- Vinayak Pathak
- Sivan Sabato
- Ruth Urner
affiliations:
- Vector Institute
- Computational Rational Agents Laboratory (CORAL)
- McMaster University
- York University
arxiv_id: '2611.17303'
url: https://arxiv.org/abs/2611.17303
pdf_url: https://arxiv.org/pdf/2611.17303
published: '2026-11-12'
collected: '2026-11-15'
category: MultiAgent
direction: 多智体辩论训练可学习性理论研究
tags:
- Learning_via_Debate
- Online_Learning
- Multi_Agent
- Scalable_Oversight
- AI_Alignment
one_liner: 首次将AI辩论协议建模为在线学习问题，刻画可学习性边界并对比合作与对抗辩论的效果差异
practical_value: '- 落地多Agent辩论训练（如RLHF、内容审核对齐、推荐结果对齐）时，优先选择合作辩论框架而非纯对抗设置，同等条件下可将错误数从T/2降至最多DLdim次

  - 对抗辩论训练中，将双方优化目标从最小化单步损失改为最小化regret，可大幅降低预测错误率，如论文示例中错误期望从T/4降至1.5

  - 辩论训练的评委（人类/自动打分模型）反馈噪声控制优先级远高于常规在线学习，k次噪声会带来Ω(k·DLdim)的错误放大，落地需提前做噪声校验'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有AI辩论研究仅聚焦固定已知评委下的博弈均衡分析，完全忽略了辩论作为训练协议的核心可学习性问题，无法回答如何通过辩论让模型学到符合人类偏好的复杂目标函数，也未考虑人类评委不可避免的判断错误对学习效果的影响，是可扩展监督与AI对齐领域的关键理论空白。
### 方法关键点
- 将辩论协议形式化为在线学习问题，首次提出辩论学习维度（DLdim），其刻画了合作辩论模式下的最优错误边界：DLdim有限等价于对应假设类可通过合作辩论被有限错误学习，且最优错误上界等于DLdim。
- 对比两类辩论设置：对抗辩论（双方分别优化自身损失/regret）、合作辩论（双方共同优化目标为最小化预测错误）。
- 分析含评委错误的不可实现场景，推导噪声下的错误上下界。
### 关键结果数字
- 合作辩论场景：DLdim=1的示例中最多仅1次预测错误，远优于对抗辩论的最高50%错误率。
- 对抗辩论场景：采用损失优化目标时错误期望可达T/4，改为regret优化后错误期望降至1.5。
- 噪声场景：k次评委错误会导致Ω(k·DLdim)量级的总错误，敏感度远高于常规在线学习；随机合作策略可实现16kd的错误上界。
### 核心结论
纯对抗辩论训练的学习效果远不如合作辩论，且辩论协议对评委噪声的敏感度远高于常规在线学习，落地需严格控制噪声。
