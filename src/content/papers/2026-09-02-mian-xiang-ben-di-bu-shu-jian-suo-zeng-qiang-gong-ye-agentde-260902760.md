---
title: Measurement-Driven Sub-Network Selection for On-Premise Retrieval-Augmented
  Factory Agents
title_zh: 面向本地部署检索增强工业Agent的测量驱动子网络选择方法
authors:
- Vasileios Rizeakos
- Georgios Paisios
- Alexandros Machairas
- Michael Birbas
- Athanasios Bachoumis
affiliations:
- AI lab of enakronIC PC
- Electrical & Computer Engineering, University of Patras
arxiv_id: '2609.02760'
url: https://arxiv.org/abs/2609.02760
pdf_url: https://arxiv.org/pdf/2609.02760
published: '2026-09-02'
collected: '2026-09-03'
category: Agent
direction: 边缘Agent部署 · LLM压缩与RAG适配
tags:
- RAG
- LLM Compression
- Edge AI
- Knowledge Distillation
- Supernetwork
one_liner: 通过超网络蒸馏与后适配测量选择子网络，实现工业边缘RAG Agent低资源高可用部署
practical_value: '- 做边缘端RAG/Agent部署时，不要仅靠参数量选模型，可在RAG适配后基于实测质量+吞吐量+通用能力阈值做帕累托最优选择，避免单纯压体积损失业务效果

  - 超网络+三明治原位蒸馏+LoRA检索适配的流水线可复用：先训权重共享超网络得到多尺度子网络，再统一做领域RAG蒸馏，一次训练适配多档异构硬件，降低部署成本

  - 检索蒸馏阶段可加入RAFT干扰项，让小模型学会忽略低相关上下文，实测能把压缩后的RAG质量损失从13.7%收窄到4.6%，该trick可直接迁移到电商/客服RAG小模型优化

  - 新硬件适配不用全量跑分，仅测3个锚点参数的子网络就能预测所有候选的吞吐量，误差仅2.5-3.1%，大幅降低多硬件部署的测试成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
工业场景RAG Agent要求数据不出厂，只能在边缘硬件部署，但现有大模型内存占用高，传统剪枝压缩会大幅降低通用能力，且参数量无法准确预测RAG适配后的业务质量，单纯按大小/速度选模型会牺牲效果或效率。

### 方法关键点
- 训练权重共享超网络：基于Llama3.2-3B/1B做弹性剪枝，形成11个参数量档位的候选子网络，用三明治原位蒸馏，每次迭代同时训全量模型+3个采样子网络，用全量模型输出做教师做知识蒸馏，保证小子网络效果
- 检索适配：所有子网络统一用LoRA做领域RAG蒸馏，训练数据加入RAFT干扰上下文，让模型学会忽略低相关片段，对齐大模型的RAG回答效果
- 硬件感知选择：先设置通用能力阈值（ARC-Easy得分≥原模型80%）+内存上限，再基于实测的RAG回答质量+设备吞吐量做帕累托最优选择，仅需测3个锚点模型就能预测所有候选的吞吐量，降低测试成本

### 关键结果数字
基于187页工厂操作手册构建686训练/633测试QA对，对比未剪枝大模型基线：压缩后的子网络RAG质量初始损失13.7%，经过检索蒸馏后损失收窄到4.6%，挽回2/3的效果损失；可适配3档异构边缘硬件，待机功耗仅1.3-5W，吞吐量损失小于14%；单纯按大小/速度选模型的方案仅能保留原模型69-74%的通用能力，比所提方案低9-14个百分点。

### 核心结论
领域适配会打破参数量与业务效果的相关性，边缘LLM部署的模型选择必须在领域适配后基于实测数据做，不要盲目相信参数量proxy。
