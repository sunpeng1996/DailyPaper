---
title: How Anthropomorphic Attitudes Toward Agents Divide User Behavior, and How Design
  Should Change
title_zh: 拟人化Agent态度对用户行为的分化影响及设计优化方案
authors:
- Tingyu Cao
- Yan Tang
- Keer Hu
- Bomingxuan Zhu
- Ruyi Zou
- Huaze Tang
- Yuanbo Tang
- Shao-Lun Huang
- Yang Li
affiliations:
- Tsinghua University
- Tiantong Storm Technology Co. Ltd.
- Shenzhen MSU-BIT University
- Shenzhen University
- The Chinese University of Hong Kong (Shenzhen)
arxiv_id: '2610.13156'
url: https://arxiv.org/abs/2610.13156
pdf_url: https://arxiv.org/pdf/2610.13156
published: '2026-10-09'
collected: '2026-10-13'
category: Agent
direction: 对话Agent 用户分群与交互设计优化
tags:
- Conversational Agent
- User Segmentation
- Anthropomorphic Design
- Field Study
- Human-Agent Interaction
one_liner: 通过田野实验发现拟人化Agent命名用户的行为差异，提出分群差异化回复策略
practical_value: '- 搭建电商导购/客服Agent时，可将用户是否给Agent自定义命名作为核心分群标签，差异化配置回复策略

  - 对自定义命名的拟人态度用户，优先回复带情绪共情的内容再承接任务；对默认名的任务导向用户直接输出执行结果

  - 可复用128-unit sparse-autoencoder codebook做用户交互行为无监督聚类，降低用户分群的标注成本

  - 验证交互策略时优先用小流量真人AB测替代纯实验室调研，结论更贴合业务实际'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
过往对话Agent研究多依赖访谈、问卷或实验室任务，拟人化命名是否会分化用户行为模式、对应交互策略如何调整缺乏真实场景证据

### 方法关键点
1. 开展桌面助手田野实验（2026年5-8月，n=257），将是否给Agent自定义拟人化命名作为分群标识
2. 用128单元稀疏自编码器码本、身份标签、开场白词表量化用户行为差异
3. 基于分群特征设计差异化回复策略，通过1744次用户成对偏好判断验证效果

### 关键结果数字
- 两群用户行为排序相关性仅0.249，远低于空值均值0.382（p=0.0419），差异显著
- 重命名用户更偏好共情优先的回复，偏好度达60.1%，较默认名用户高22.1个百分点
- 差异化回复不会对两类用户的任务完成效率产生负向影响
