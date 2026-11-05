---
title: Alignment Myopia in Generative AI
title_zh: 生成式AI的对齐短视：短期偏好优化的长期风险与范式转向
authors:
- Remi Denton
- Aida Davani
- Cynthia L Bennett
- Michael Madaio
- Roma Patel
- Himabindu Lakkaraju
affiliations:
- Google Research
- Google DeepMind
- Harvard Business School
arxiv_id: '2611.06830'
url: https://arxiv.org/abs/2611.06830
pdf_url: https://arxiv.org/pdf/2611.06830
published: '2026-11-04'
collected: '2026-11-05'
category: LLM
direction: LLM对齐 · 长周期人类福祉优化
tags:
- Alignment
- RLHF
- Long-term Wellbeing
- Generative AI
- LLM
one_liner: 指出LLM对齐的短视缺陷，提出转向兼顾长期人类福祉的长周期对齐范式
practical_value: '- 搭建电商导购Agent、陪伴型推荐系统时，不能仅优化即时点击/会话满意度指标，需补充长期用户行为标签（如自主决策频次、技能使用频率）避免用户过度依赖带来的长期流失与负向口碑

  - 可复用推荐系统从短期点击优化转向长期留存的演进思路，引入surrogate模型预测用户长期价值，作为LLM/Agent对齐阶段的辅助奖励信号

  - 设计多目标对齐框架时，需显性权衡短期体验（如情绪价值、任务完成效率）与长期风险（如认知依赖、自主决策能力退化），避免过度追求用户粘性带来的社会负外部性

  - 针对教育类/职业辅助类AI产品，可添加用户主动参与度权重，要求用户保留对核心任务的控制权，降低心理所有权缺失带来的长期满意度下降'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前生成式AI对齐普遍依赖RLHF等基于短期用户偏好反馈的方法，默认即时满意度等价于长期收益，但随着LLM深度嵌入用户认知、社交、情感与职业生活，短期偏好优化会累积为认知萎缩、社交能力退化、情感依赖、自主性丧失等长期负面效应，现有范式完全无法覆盖这类跨时间尺度的风险，亟需对齐范式的系统性转向。
### 方法关键点
- 从认知能力、社交健康、情感福祉、身份与自主性4个维度，系统梳理了AI短期效用与长期风险的矛盾，明确了现有奖励模型缺失的跨尺度影响因子
- 借鉴推荐系统从短期点击优化转向长期价值的演进经验，指出传统长周期指标（留存、engagement）仍无法覆盖福祉类目标，需构建跨机器学习、社会学、HCI的融合测量框架
- 提出长周期对齐的核心方向：将社会科学的纵向测量方法转化为可扩展的优化目标，构建多时间尺度、多利益相关方的多目标对齐范式，平衡短期效用与长期个体、集体福祉
### 关键实证结论
基于100+余篇认知科学、HCI、社会学、ML领域的实证研究佐证，现有短期对齐范式的风险已被广泛验证：癌症专家使用AI辅助工作1年后专业技能出现明显退化，长期使用AI陪伴的用户人际冲突耐受度降低30%以上，青少年长期通过AI倾诉后生命意义感显著下降。
### 核心警句
生成式AI的终极衡量标准，不仅是当下能否让用户满意，更是持续使用能否促进个体、社区和社会的长期活力
