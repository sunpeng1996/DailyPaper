---
title: 'TriGen: A Generative Paradigm for Trigger-Induced Recommendation'
title_zh: TriGen：面向触发诱导推荐场景的生成式推荐范式
authors:
- Muyu Zou
- Haibo Xing
- Shunye Tang
- Liyan Tie
- Lingyu Mu
- Yandong Wang
- Jinxin Hu
affiliations:
- Alibaba International Digital Commerce Group
- Nankai University
- Independent Researcher
arxiv_id: '2611.16395'
url: https://arxiv.org/abs/2611.16395
pdf_url: https://arxiv.org/pdf/2611.16395
published: '2026-11-12'
collected: '2026-11-13'
category: GenRec
direction: 生成式推荐 · 触发诱导场景优化
tags:
- Generative Recommendation
- Trigger-Induced Recommendation
- Semantic ID
- Sequential Recommendation
- E-commerce
one_liner: 针对触发诱导推荐场景提出平衡历史偏好与即时意图的生成式框架TriGen，已全量部署于生产环境
practical_value: '- 触发信号处理可复用Calibrated Tail Injection方案：将触发item重复N次插入行为序列尾部，配合RoPE控制触发信号的影响强度，无需复杂改造即可适配现有生成式推荐骨架，重复次数可根据场景对触发的敏感程度调优

  - 双路径动态门控架构可直接迁移到多信号融合场景：分别建模长期历史偏好和即时触发意图，通过输入依赖的门控动态调整权重，可有效解决误触、用户探索等场景下的触发信号过拟合问题

  - 解码阶段的位置特定引导方案可优化Semantic ID生成效果：针对Semantic ID从粗到细的层级结构，每个解码步骤注入独立的触发条件投影，避免初始引导信号随解码步长衰减，大幅提升生成结果与触发意图的匹配度

  - 工业落地验证该架构额外推理延迟仅10ms左右，完全符合线上实时推荐的serving要求，可直接用于商品详情页关联推荐、点击后feed、相关推荐等典型触发场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐（GenRec）默认基于用户长期行为序列做被动的下一个item预测，未覆盖电商核心的触发诱导推荐（TIR）场景：即用户点击某商品后进入的专属关联feed场景，该场景需同时兼顾用户长期消费偏好和点击动作传递的即时购物意图。传统TIR方案均为判别式CTR模型，无法适配生成式范式的token级生成引导需求；简单将触发信号拼入输入的方案无法平衡偏好连续性和意图跳转的结构性冲突，容易出现过度贴合触发（推荐范围过窄）或完全忽略触发（无法响应用户即时需求）的问题。
### 方法关键点
- 编码层：Calibrated Tail Injection，将触发item的embedding重复N次插入行为序列尾部，配合RoPE建模相对位置，通过调整重复次数精准控制触发信号的影响强度
- 表示层：Adaptive Dual-Path Fusion，分别用触发item引导的查询、可学习默认查询提取即时意图、长期偏好两路独立表征，通过输入依赖的门控模块动态调整两路信号的融合权重
- 解码层：Position-Specific Trigger-PFFN，为每个Semantic ID解码步骤学习独立的条件投影层，将层级化的触发引导信号注入每一步解码输入，适配Semantic ID从粗类别到细属性的生成逻辑
### 关键结果
离线在阿里国际站亿级工业数据集、Amazon公开数据集上，对比DIAN等TIR判别式基线、TIGER/LC-Rec等生成式基线，工业数据集上Recall@5达5.58%，比简单触发注入的GR baseline提升28.3%；线上6个东南亚国家A/B测试，流量加权后Revenue提升3.27%，GMV提升0.90%，额外推理延迟仅10.5ms，已全量上线服务主流量。
最值得记住的结论：生成式推荐在触发场景下的核心优化点不是简单加入触发特征，而是要在编码、融合、解码全链路系统性平衡长期偏好与即时意图的权重
