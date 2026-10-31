---
title: 'After One-Click Video: The Inflow of Service-Type Content, the Failure of
  the Recommendation Pool Mechanism, and the BoLe System'
title_zh: 一键视频普及后服务类内容涌入、推荐池失效与BoLe系统方案
authors:
- Bo Zou
- Chao Xu
arxiv_id: '2610.37695'
url: https://arxiv.org/abs/2610.37695
pdf_url: https://arxiv.org/pdf/2610.37695
published: '2026-10-23'
collected: '2026-10-31'
category: RecSys
direction: 内容推荐机制 · 内容分层治理
tags:
- Content Recommendation
- Recommendation Pool
- AIGC
- Content Governance
- UGC
one_liner: 分析AI生成服务类内容泛滥导致传统推荐池失效，提出分品类审核的BoLe优化方案
practical_value: '- 可复用服务类/作品类内容的二元分类框架，对UGC/AIGC先做品类拆分再设计不同召回准入规则，避免优质内容被稀释

  - 当平台AI生成内容供给爆发时，可参考阈值模型判断传统推荐池的失效临界点，提前迭代推荐架构

  - 服务类内容（如电商导购短视屏）可先靠机器规则做准入过滤，品质类内容引入专业评审池，平衡效率和质量'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
2026年大模型驱动的一键生成视频大规模普及，平台服务类AIGC供给爆发，传统基于用户试看分层流转的推荐池机制面临失效，优质作品类内容被低质服务内容稀释，用户注意力被无意义消耗。
### 方法关键点
1. 将平台内容划分为服务类（用户为满足特定需求观看，生产门槛极低）、作品类（用户为内容本身消费，生产受创作者能力约束）两类，明确两类内容供给失衡的核心逻辑；
2. 搭建简化数学模型量化新增内容规模与推荐池有效性的关联，证明当内容供给超过特定阈值后传统推荐池必然失效；
3. 提出BoLe系统，服务类内容由机器规则做准入过滤，作品类内容由可信人群做质量评审，分赛道治理。
### 关键结果
数学模型验证当服务类内容供给占比突破阈值后，传统推荐池的优质内容分发效率下降超50%，BoLe系统可将优质作品类内容曝光占比提升至原有水平的2倍以上。
