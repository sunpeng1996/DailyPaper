---
title: 'UniVR: Thinking in Visual Space for Unified Visual Reasoning'
title_zh: UniVR：基于视觉空间思考的统一视觉推理框架
authors:
- Zhongwei Ren
- Yunchao Wei
- Yao Zhao
- Weibo Gong
- Xiao Liu
- Anran Wang
- Xiangtai Li
- Xiaojie Jin
affiliations:
- Beijing Jiaotong University
- ByteDance
arxiv_id: '2607.12800'
url: https://arxiv.org/abs/2607.12800
pdf_url: https://arxiv.org/pdf/2607.12800
published: '2026-07-14'
collected: '2026-07-16'
category: Reasoning
direction: 多模态·纯视觉统一推理
tags:
- Vision Reasoning
- Reinforcement Learning
- Multimodal
- Benchmark
- GRPO
one_liner: 提出纯视觉输入的统一推理框架UniVR，配套VR-GRPO范式与VR-X基准，性能最高提升25%
practical_value: '- 电商多模态推荐场景可复用VR-GRPO的全局+步骤级奖励设计，优化纯视觉商品理解、搭配推理的逻辑一致性

  - Agent视觉交互任务（如直播选品、实体机器人导购）可直接复用UniVR的纯视觉推理架构，无需依赖图文对预训练数据

  - 多模态内容检索排序场景可引入UniVR的视觉空间推理能力，提升商品/内容的语义匹配精度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有AI推理多基于文本空间展开，无法覆盖真实世界的视觉复杂动态、空间关系、底层物理规律，纯视觉输入的统一推理能力存在明确空白。

### 方法关键点
1. 推出UniVR框架，首次实现从纯视觉演示中同时学习复杂推理、细粒度物理动态和长程规划
2. 核心采用VR-GRPO强化学习范式，搭配互补的全局+步骤级奖励，无需任务特定启发式规则或图文对数据，即可保障推理过程的逻辑连贯与物理一致性
3. 构建大规模基准VR-X，覆盖16个来源的long-horizon操作、空间谜题、物理推理任务，是首个纯视觉协议下的异构能力评估套件

### 关键结果数字
在VR-X基准上性能最高提升25%，同时在多类多模态理解基准上也获得显著性能提升，全量代码、数据、模型已开源
