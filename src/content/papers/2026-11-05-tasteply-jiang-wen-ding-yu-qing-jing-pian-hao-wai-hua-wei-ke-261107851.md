---
title: 'Tasteply: Externalizing Stable and Situational Preference as Manipulable Spatial
  Objects'
title_zh: Tasteply：将稳定与情境偏好外化为可操控空间对象
authors:
- DaEun Choi
- Daniel Lee
affiliations:
- KAIST
- Salesforce AI Research
arxiv_id: '2611.07851'
url: https://arxiv.org/abs/2611.07851
pdf_url: https://arxiv.org/pdf/2611.07851
published: '2026-11-05'
collected: '2026-11-06'
category: RecSys
direction: 可交互推荐 · 偏好分层与用户调控
tags:
- Interactive_RecSys
- Preference_Modeling
- Situational_Preference
- User_Control
- Spatial_Interaction
one_liner: 提出分层偏好的空间化表达方案，支持用户直接调控推荐结果
practical_value: '- 可将现有多兴趣召回的兴趣向量映射为可视化空间吸引子，给用户开放兴趣混合度调控入口，解决单一兴趣选择过于生硬的问题

  - 稳定偏好可作为全局权重因子引入排序公式，既满足用户场景化兴趣需求，又避免推荐结果偏离用户长期口味过多

  - 用户行为反馈可按当前各吸引子的贡献度分别更新对应兴趣向量，解决临时场景兴趣污染长期用户画像的业务痛点

  - 模糊探索场景下开放连续空间调控，精准目标场景下保留离散兴趣选择，适配不同用户使用需求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐系统普遍将用户偏好视为单一隐式信号优化，未区分跨场景不变的稳定偏好和随上下文激活的情境偏好，用户只能通过被动点击反馈调整推荐，缺乏对偏好的直接操控能力，临时场景兴趣还容易污染长期画像，导致推荐结果不符合预期。

### 方法关键点
- 偏好拆分：将用户偏好拆分为情境偏好吸引子和稳定偏好全局场两类空间对象，每个吸引子对应一类场景化兴趣的归一化嵌入均值，全局场为所有未被吸引子覆盖的偏好残差的归一化均值
- 空间操控：用户可在2D偏好空间移动光标，通过各向同性高斯核计算不同吸引子的权重，加权混合得到查询向量，同时支持通过滑块调整全局场权重γ
- 排序公式：候选内容的最终得分为`cos(v_query, post) × cos(v_global, post)^γ`，可实时更新推荐结果

### 关键实验
招募5名有2-7年HCI研究经验、常用社交平台的受试者，基于Bluesky历史交互数据构建偏好空间，进行15分钟自由探索加25分钟半结构化访谈。结果显示100%受试者可快速理解分层偏好结构并自主调整吸引子分组，80%受试者认可连续空间调控在模糊探索场景下的价值，20%有明确目标的受试者更偏好离散吸引子选择模式。

### 核心结论
区分稳定与情境偏好并开放直接操控入口，能大幅提升用户对推荐结果的满意度与可控感
