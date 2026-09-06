---
title: Can LLMs Design Video Coding Tools? A Case Study on Planar Mode
title_zh: 大语言模型能否设计视频编码工具？基于Planar模式的案例研究
authors:
- Yingwen Zhang
- Meng Wang
- Liqiang He
- Shiqi Wang
affiliations:
- Department of Computer Science, City University of Hong Kong
- School of Data Science, Lingnan University
arxiv_id: '2609.01535'
url: https://arxiv.org/abs/2609.01535
pdf_url: https://arxiv.org/pdf/2609.01535
published: '2026-09-01'
collected: '2026-09-06'
category: Other
direction: LLM驱动的自动算法设计优化
tags:
- LLM
- Automatic Algorithm Design
- Video Coding
- Iterative Optimization
- Intra Prediction
one_liner: 采用生成-评估迭代框架用LLM优化视频编码Planar预测工具，实现比特率节省
practical_value: '- 可复用「生成-评估-反馈迭代」框架，用于推荐系统排序策略、召回规则的自动优化，降低人工调参成本

  - 两种LLM能力集成思路（直接替换原有模块/新增独立模块+适配逻辑）可迁移到业务系统落地，控制上线风险

  - 先在轻量基准上验证优化效果、再迁移到复杂系统的迭代流程，可复用在算法迭代的小流量验证环节'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
视频编码工具设计存在算法耦合度高、人工迭代优化成本高的痛点，LLM在该垂直领域自动算法设计的可行性尚未得到验证。
### 方法关键点
以视频编码标准通用的Planar帧内预测工具为案例，搭建生成-评估迭代闭环：LLM生成新的Planar预测器实现，编码器实测编码性能后将结果反馈给LLM，指导其迭代优化方案；分别在VVenC快速预设、Enhanced Compression Model（ECM）两种环境下验证两种集成策略：直接替换原有Planar模式、新增LLM生成模式作为独立候选项。
### 关键结果
- VVenC轻量工具集下，LLM生成模式优于传统方案，实现0.18%比特率节省，仅带来0.4%复杂度开销
- 低分辨率约束下，两种集成策略在ECM上均获得编码增益
