---
title: 'Yalda-Embedding: Open Development of a Competitive Persian Retrieval Model'
title_zh: Yalda-Embedding：开源高性能波斯语检索嵌入模型
authors:
- Yalda Taheri
- Mohammad Hassan Heydari
- Armon Rasooli
affiliations:
- Azad University
- University of Isfahan
- Iran University of Science and Technology
arxiv_id: '2610.32933'
url: https://arxiv.org/abs/2610.32933
pdf_url: https://arxiv.org/pdf/2610.32933
published: '2026-10-23'
collected: '2026-10-26'
category: RAG
direction: RAG检索 · 小模型蒸馏优化
tags:
- Dense Retrieval
- Knowledge Distillation
- Contrastive Learning
- Embedding
- Low-resource NLP
one_liner: 基于Qwen3-0.6B微调的595M参数波斯语检索嵌入模型，性能追平4B基线，全链路资源开源
practical_value: '- 小参数垂直领域嵌入模型优化可直接复用该配方：先提升对比batch size到512扩充负样本，再加梯度裁剪+10%步长warmup+余弦学习率衰减稳定训练，最后加大模型关系蒸馏，可在不增加推理成本的前提下大幅提升效果

  - 蒸馏目标可复用 relational knowledge distillation 方案：不需要对齐teacher和student的嵌入维度，仅匹配batch内的相关性分布即可，大幅降低实现门槛

  - 低资源语种/垂直领域检索场景，不需要额外挖掘硬负样本，仅用in-batch负样本+大模型蒸馏就可以在硬负样本评估任务上取得不错效果，降低数据准备成本

  - 预计算teacher embedding离线存储，后续训练student不需要加载大模型，大幅降低训练阶段算力要求，适合小算力团队做垂直领域嵌入模型微调'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前多语言文本嵌入技术快速迭代，但波斯语等低资源语种长期缺乏专属高质量训练数据与轻量高效的检索嵌入模型，难以支撑本地化语义搜索、RAG、内容推荐等下游场景需求，基于成熟通用多语言嵌入基座做针对性微调是性价比最高的落地路径。

### 方法关键点
- 基座选型：初始化自Qwen3-Embedding-0.6B，保留RoPE、GQA、SwiGLU等原生架构，最终参数量595.8M，推理成本与原模型一致
- 训练数据：构建103万波斯语query-正样本文档对，覆盖通用检索、QA、金融、科学等13个领域，不额外挖掘硬负样本，仅用in-batch负样本参与训练
- 训练流程：两阶段渐进优化，第一阶段对比学习调优：将全局batch size从64提升到512，搭配梯度裁剪、10%步长warmup+余弦学习率衰减稳定训练；第二阶段加入关系型知识蒸馏，以F2LLM-v2-8B为教师模型，预计算所有训练样本的教师嵌入离线存储，蒸馏目标为对齐batch内师生模型的相关性分布，最终损失设置为0.25倍InfoNCE损失+0.75倍KD损失

### 关键结果
在FaMTEB基准的8个波斯语检索任务上评测：宏观平均得分0.5488，为所有参评0.6B模型第一，较初始Qwen3-Embedding-0.6B绝对提升0.0775（相对16.4%），较同规模F2LLM-v2-0.6B高0.0425，所有任务均领先同规模基线；仅比参数量为其7倍的Qwen3-Embedding-4B低0.0075，其中4个任务反超4B基线、1个任务打平；消融实验显示batch size提升带来0.0388的最大单点增益，蒸馏环节共带来0.0675的效果提升，无硬负样本训练也能在3个硬负样本评测任务上超过所有同规模基线。

**最值得记住的一句话**：低资源/垂直领域小参数嵌入模型优化，「扩大对比batch的对比学习+大模型关系蒸馏」的组合收益远高于单纯增大模型参数量。
