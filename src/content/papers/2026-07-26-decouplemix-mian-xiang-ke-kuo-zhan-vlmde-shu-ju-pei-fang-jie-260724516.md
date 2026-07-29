---
title: 'DecoupleMix: Decoupled Ratio Search and Convex Allocation for Scalable VLM
  Data Recipes'
title_zh: DecoupleMix：面向可扩展VLM的数据配方解耦比例搜索与凸分配
authors:
- Jiahao Xie
- Zhongbin Guo
- Qianle Wang
- Ruiqi Lu
- Dongling Xiao
- Wanxuan Sun
- Cheng Yang
affiliations:
- ByteDance
arxiv_id: '2607.24516'
url: https://arxiv.org/abs/2607.24516
pdf_url: https://arxiv.org/pdf/2607.24516
published: '2026-07-26'
collected: '2026-07-29'
category: Multimodal
direction: 多模态大模型预训练数据配比优化
tags:
- VLM
- Data Curation
- Convex Optimization
- Pre-training
- Data Mixture
one_liner: 将VLM预训练数据配比优化解耦为跨类单变量搜索与类内凸优化，性能优于启发式方案且小尺度最优比可直接迁移到大模型
practical_value: '- 电商多模态推荐/搜索的训练数据配比可复用解耦思路：先做跨任务大类的单变量比例搜索，再在同任务类内基于质量、难度打分做带约束的凸优化选数据，比直觉调参效率高

  - 小参数量试点得到的最优数据配比可直接迁移到同场景大参数量模型训练，无需重调，大幅降低大模型训练试错成本

  - 新增训练数据源的准入可复用该框架的归因验证逻辑，无需全量AB即可快速评估新数据源的业务价值'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前VLM预训练数据配比多依赖启发式人工设置，缺乏可复现的系统化优化方案，前沿厂商的配比规则未公开，新增数据源无明确可归因的准入标准。
### 方法关键点
将数据混合配比优化拆分为两个正交子问题：
1. 跨能力类别配比：采用单变量迭代搜索确定大类间的分配比例
2. 同类别内数据集配比：先对单数据集做质量、难度多维度打分，再以多样性为目标求解带约束的凸优化问题完成选组
框架同时支持指导后续数据采集方向，实现可归因的数据集验证。
### 关键结果
效果持续优于启发式基线，小尺度代理模型上找到的最优配比无需重调即可无缝迁移到大尺度场景；仅用80B额外多模态继续预训练token，训练出的VLM性能可比肩使用多得多的多模态数据预算训练的开源SOTA模型。
