---
title: 'Feedback Manipulation Regularization: Enabling Offline Agent Alignment for
  Imitation Learning'
title_zh: 反馈操纵正则化：实现模仿学习场景下的离线Agent对齐
authors:
- Benjamin Poole
- Minwoo Lee
affiliations:
- University of North Carolina at Charlotte
arxiv_id: '2607.07859'
url: https://arxiv.org/abs/2607.07859
pdf_url: https://arxiv.org/pdf/2607.07859
published: '2026-07-08'
collected: '2026-07-10'
category: Agent
direction: Agent 模仿学习离线对齐优化
tags:
- Imitation Learning
- Agent Alignment
- Regularization
- Offline Training
- Feedback Learning
one_liner: 提出模型无关的反馈操纵正则化FMR，利用评估反馈校正模仿学习策略，大幅降低Agent对齐误差
practical_value: '- 可直接将FMR作为正则项叠加在现有基于模仿学习的电商导购Agent、内容分发Agent训练损失中，无需修改基础算法架构，即可降低违规行为（如推违禁品、跳过必要咨询流程）的出现概率

  - 正负反馈驱动的逐动作温度缩放思路可迁移到GenRec场景：对用户点击的正向item降低生成温度提概率，对举报/跳过的负向item升高温度降概率，校准效果比单纯加权损失更稳定

  - 低质量演示数据占比高的业务场景可参考「少量专家演示+噪声数据标注少量反馈」的训练范式，无需全量重标专家数据，即可大幅提升策略合规性，降低标注成本

  - 对齐评估可借鉴misalignment计算思路：给业务违规行为定义量化cost（如推违规品罚1、路径错误罚0.5），直接用违规步数占比作为对齐效果的离线评估指标，比纯业务指标更精准'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有Agent对齐方法多依赖多阶段RLHF/偏好学习pipeline，要么需要在线环境交互，要么偏好反馈的相对属性无法保证绝对对齐，且很少支持全序列决策场景下的单阶段离线训练；同时噪声演示数据占比高的场景下，基线模仿学习算法的对齐错误率会急剧上升，无法满足业务对Agent行为合规性的强要求。

### 方法关键点
- 提出模型无关的FMR正则项，可直接叠加在任意模仿学习损失函数上，通过超参数α控制对齐强度
- 基于状态-动作对层面的三级评估反馈（正/负/无）生成逐动作温度系数：负反馈对应温度>1（降低该动作概率），正反馈对应非选中动作温度>1（等价提升选中动作概率），无反馈温度为1
- 用温度缩放校正策略输出的动作概率分布，通过最小化校正后分布与原策略的反向KL散度构造正则项，本质是用反馈自适应调节策略熵，抑制不符合要求的行为

### 关键实验
测试环境为Safety Gymnasium的3D导航、3类速度约束locomotion任务，用cost违规率作为misalignment对齐指标；对比BC、IQL、DemoDICE、ReCOIL四类主流模仿学习算法，以及将反馈当奖励的DVL、基于偏好学习的CPL两类反馈利用方案。核心结果：FMR可适配所有基线算法，最多降低98%的misalignment，且在专家/噪声数据比仅1:5的小数据场景下仍保持鲁棒，效果显著优于其他反馈利用方案。

**最值得记住的一句话**：对于需要严格对齐业务规则的序列决策Agent，用动作级评估反馈做概率空间的温度缩放正则，比传统加权损失、偏好学习更高效，且几乎不需要修改原有训练流程。
