---
title: 'Balancing Memory Pathways: Analyzing and Improving Memory Utilization in Hybrid
  LMs'
title_zh: 循环-注意力混合语言模型的内存路径利用分析与优化
authors:
- Hyunji Lee
- Joykirat Singh
- Zaid Khan
- Justin Chih-Yao Chen
- Elias Stengel-Eskin
- Alessandro Sordoni
- Arman Cohan
- Mohit Bansal
affiliations:
- UNC Chapel Hill
- The University of Texas at Austin
- Mila
- Yale University
arxiv_id: '2610.06750'
url: https://arxiv.org/abs/2610.06750
pdf_url: https://arxiv.org/pdf/2610.06750
published: '2026-10-05'
collected: '2026-10-06'
category: Training
direction: 混合LM · 内存路径平衡优化
tags:
- Hybrid-LM
- Memory-Pathway
- Auxiliary-Loss
- Long-Context
- Agent
- LoRA
one_liner: 通过辅助损失平衡混合LM的注意力与循环内存路径，提升长上下文与Agent任务表现
practical_value: '- 训练Mamba/Transformer混合架构的生成式推荐/电商Agent时，可添加限制注意力访问历史上下文的辅助损失，提升长会话用户行为聚合、多商品关联推荐等任务性能

  - 对同时使用RAG文本记忆 + KV latent记忆的多通路推荐系统，可针对利用率低的通路设计专属辅助损失，避免主流通路压制其他通路的互补能力

  - 长上下文商品检索、多轮会话推荐场景下，优先强化循环/latent记忆通路的利用率，可在不增加KV cache开销的前提下提升多步推理准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
循环-注意力混合LM（如Qwen3.5、Nemotron-H）结合了注意力的精准召回能力和循环层的长上下文聚合效率，是当前大模型降本提效的主流架构，但标准SFT训练会让模型过度依赖注意力通路，循环通路能力被严重压制，无法发挥双通路互补优势，在长上下文推理、Agent长轨迹决策等场景下性能瓶颈明显。

### 方法关键点
- 设计通路利用度评估机制：通过分段掩码分别阻断注意力跨段访问、循环状态跨段传播，量化双通路实际贡献占比
- 提出轻量辅助损失$L_{rec}$：辅助前向传播中完全掩码注意力对历史上下文的访问，强制模型仅通过循环状态传递历史信息，与标准SFT损失加权联合训练，权重λ取0.25时效果最优
- 训练时使用LoRA微调全层，控制总计算量与标准SFT对齐，无额外推理开销

### 关键实验结果
在Qwen3.5-4B、Nemotron-H-4B两个主流混合LM上验证：
- 长上下文QA任务：6个数据集平均准确率分别提升3.9%、5.2%，其中长上下文数据集增益达8.0%，短上下文仅0.2%
- Agent任务：TextWorld任务平均成功率提升3.5%~9.3%，BabyAI长轨迹任务最高提升22.0%
- 错误恢复能力：多轮重试场景下QA累计恢复率提升16.6%，Agent任务提升19.2%

### 核心结论
仅为模型提供多内存通路无法保证其有效利用，必须通过针对性的监督信号引导通路间的能力协同，才能充分发挥混合架构的优势。
