---
title: 'EpiCon: Collective Agent Learning through Co-Evolving Multimodal Memory'
title_zh: EpiCon：基于多模态记忆协同演化的多Agent集体学习框架
authors:
- Ziyun Zeng
- Hang Hua
- Shaden Alshammari
- Rogerio Feris
- William T. Freeman
- Jiebo Luo
affiliations:
- MIT-IBM Computing Research Lab
- University of Rochester
- Massachusetts Institute of Technology
arxiv_id: '2609.37923'
url: https://arxiv.org/abs/2609.37923
pdf_url: https://arxiv.org/pdf/2609.37923
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: Agent 多模态共享记忆优化
tags:
- MultiAgent
- Multimodal Memory
- Collective Learning
- External Memory
- Experience Reuse
one_liner: 提出无需更新宿主参数的共享多模态记忆框架，支持跨Agent系统的经验复用与集体学习
practical_value: '- 架构层面：可复用轻量2B小模型做记忆控制与组织的设计，无需改动大模型参数即可提升多Agent系统性能，适合业务侧大模型冻结的场景

  - 记忆管理：文本+视觉多模态记忆协同演化+自适应注入的trick，可迁移至多模态商品理解、多模态搜索推荐的Agent流程优化

  - 经验复用：树形分层组织跨系统经验的方案，可用于搭建跨业务线的Agent经验共享库，降低不同场景的重复开发成本

  - 性能优化：小模型替换大模型做记忆操作可降低67%以上的记忆处理耗时，兼顾效果与成本，适合高并发的业务部署'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多Agent系统无法跨不同框架、不同backbone复用经验，且多模态场景下文本与视觉经验难以协同迭代，更新宿主大模型参数的学习方案成本高、灵活性差，亟需低侵入、可跨系统复用的集体学习方案。

### 方法关键点
- 两个独立训练的2B轻量模型组成核心模块：Memory Controller负责单问题内文本指导与视觉证据的协同迭代，自适应决定是否注入视觉记忆；Tree Self-Organizer负责跨问题的经验分层组织、合并、抽象与检索，无需改动宿主Agent的模型参数
- 共享多模态经验库独立于宿主MAS，支持跨框架、跨backbone的经验读写，集体学习通过经验库的积累迭代完成
- 训练数据来自3类多模态任务的Agent执行轨迹，经大模型教师生成标注再通过重放验证筛选，共25K记忆更新样本、6.5K树操作样本

### 关键结果
在11个多模态基准（覆盖文档理解、视觉转代码、视觉数学、通用VL推理）测试，对比Mem0、Cognee等5个基线：
- 2B模型版本比无记忆方案平均提分1.7~4.9分，记忆操作耗时比用大模型做记忆的方案降低67%~74%
- 跨backbone/跨框架的经验迁移可分别带来3.2、4.2分的平均提分，跨框架协同演化经验库可再提升2.1~3.2分

最值得记住的一句话：无需更新大模型参数，通过轻量模型管理的共享多模态记忆即可实现跨系统的Agent集体学习，兼顾效果、成本与灵活性。
