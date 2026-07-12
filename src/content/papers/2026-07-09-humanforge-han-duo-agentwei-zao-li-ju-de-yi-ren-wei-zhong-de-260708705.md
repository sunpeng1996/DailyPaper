---
title: 'HumanForge: A Human-Centric Deepfake Video Benchmark with Multi-Agent Forgery
  Rationales'
title_zh: HumanForge：含多Agent伪造理据的以人为中心的深度伪造视频基准
authors:
- Wenbo Xu
- Zhimin Chen
- Xiaojie Liang
- Hengrui Liu
- Wei Lu
affiliations:
- School of Computer Science and Engineering, Sun Yat-sen University
arxiv_id: '2607.08705'
url: https://arxiv.org/abs/2607.08705
pdf_url: https://arxiv.org/pdf/2607.08705
published: '2026-07-09'
collected: '2026-07-12'
category: Agent
direction: 多Agent协作 · 数据集自动构建与标注
tags:
- Multi-Agent
- LangGraph
- Deepfake
- Dataset Construction
- MoE
one_liner: 基于LangGraph多Agent管线生成18K+深度伪造视频数据集，配套全维度标注填补现有基准的交互与多模态对齐维度空白
practical_value: '- 可复用基于LangGraph的模块化多Agent协作管线，替代人工完成大规模内容生成、标注、校验的闭环工作流，降低内容治理类业务的人力成本

  - MoE分模块负责不同环节的多Agent分工思路可迁移到电商内容审核、生成式内容质检场景，提升复杂多模态内容的处理精度

  - 结构化对比标注的设计逻辑可复用在推荐系统的负样本构造、用户反馈标注环节，提升模型训练的样本质量'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
视频扩散模型与时序编辑工具快速迭代，高拟真以人为中心的生成视频大幅降低深度伪造门槛，现有深度伪造基准仅聚焦换脸或全局文生视频场景，缺失人-物/人-人交互、多模态对齐等关键检测维度，同时大规模标注存在人工成本高、单Prompt生成易出现幻觉的问题。
### 方法关键点
构建HumanForge大规模多范式以人为中心深度伪造数据集，提出基于LangGraph的Gen2Anno模块化主动多Agent管线，协调6个专业化Agent（覆盖源特征分析、MoE参考分析、闭环取证校验等环节），自动完成样本生成与标注。
### 关键结果
生成超18K高保真视频片段，产出包含二分类标签、细粒度artifact类别、时空定位的结构化对比全维度标注；测试显示现有SOTA传统检测器与LMM在该数据集上的零样本泛化、细粒度推理性能均表现不佳，检测难度远高于现有基准。
