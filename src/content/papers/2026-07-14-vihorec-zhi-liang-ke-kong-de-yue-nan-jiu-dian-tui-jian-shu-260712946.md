---
title: 'ViHoRec: A Quality-Controlled Vietnamese Hotel Recommendation Dataset and
  Cold-Start Benchmark'
title_zh: ViHoRec：质量可控的越南酒店推荐数据集与冷启动基准
authors:
- Minh Hoang Nguyen
arxiv_id: '2607.12946'
url: https://arxiv.org/abs/2607.12946
pdf_url: https://arxiv.org/pdf/2607.12946
published: '2026-07-14'
collected: '2026-07-15'
category: RecSys
direction: 低资源推荐 · 冷启动基准数据集
tags:
- Dataset
- Cold-Start
- Hotel Recommendation
- Low-Resource RecSys
- Benchmark
one_liner: 发布质量可控的越南酒店推荐公开数据集ViHoRec，配套可复现冷启动基准
practical_value: '- 小语种/垂类低资源推荐场景构建自有数据集时，可直接复用其跨平台实体对齐、量化质量管控、HMAC隐私匿名的全流程方案

  - 稀疏冷启动推荐场景选型可参考其结论：用户交互历史极短的场景下，传统UserKNN效果优于BPR-MF等基于学习的协同过滤模型

  - 搭建内部推荐算法基准时，可借鉴其时间序留一划分、数据驱动消融、无依赖基线的评估框架，提升benchmark的可靠性和可复现性'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
越南语垂类推荐领域长期缺乏公开、文档完善的酒店交互数据集，现有构建方案存在三大痛点：跨平台酒店实体未对齐导致交互不可比、无标准化可复现的质量审计流程、公开版本无法同时满足隐私保护与真实冷启动benchmark要求。
### 方法关键点
1. 爬取Booking.com、Traveloka、Ivivu三大平台的18267条交互数据，覆盖6832位用户、560家酒店；
2. 落地可复现的构建pipeline，包含跨平台实体消解、量化质量控制模块；
3. 采用HMAC假名实现隐私脱敏，配套时间序留一划分的冷启动基准、数据-centric ablation、无依赖baseline。
### 关键结果
短历史用户场景下学习类模型效果骤降，BPR-MF Recall@10仅0.065，为长历史用户表现的54%，UserKNN整体表现最优，验证该数据集是典型的稀疏、冷启动主导的低资源推荐测试床。
