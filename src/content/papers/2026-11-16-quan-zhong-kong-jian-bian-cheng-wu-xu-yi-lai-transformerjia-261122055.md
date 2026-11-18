---
title: Weight-Space Programming Doesn't Need Transformers
title_zh: 权重空间编程无需依赖Transformer架构
authors:
- Hyunjong Ok
- Jaeho Lee
affiliations:
- Pohang University of Science and Technology (POSTECH)
arxiv_id: '2611.22055'
url: https://arxiv.org/abs/2611.22055
pdf_url: https://arxiv.org/pdf/2611.22055
published: '2026-11-16'
collected: '2026-11-18'
category: LLM
direction: LLM 无梯度权重空间编程
tags:
- Weight-Space-Programming
- Associative-Memory
- Sparse-Table
- No-Gradient-Training
- LLM
- Inference-Optimization
one_liner: 发现LLM做权重空间编程时自发选择稀疏查表结构，比同规模Transformer小680×快17×
practical_value: '- 垂类小模型（如电商商品FAQ、售后问答）场景可复用该稀疏查表架构，仅需10级别的标注样本即可快速生成可用模型，远低于梯度训练的标注需求

  - 推荐系统冷启动阶段，可通过WSP将领域规则、运营经验直接写入稀疏表模型，快速拿到基线效果，解决新品/新场景缺标注数据的问题

  - Agent的事实记忆模块可借鉴概念对哈希查表设计，实现可解释、可单行编辑的记忆能力，推理延迟远低于基于Transformer注意力的记忆检索

  - 低流量边缘端部署场景可选用优化后的关联记忆模型，同准确率下参数量最多小1800×，推理速度最快快17×，大幅降低部署成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Transformer的设计初衷是适配梯度下降训练和GPU密集矩阵计算，在权重空间编程（WSP）范式下，LLM直接手写目标模型权重、无需梯度训练与数据拟合，原有的Transformer架构优势不再成立，需要探索更适配WSP的模型结构。
### 方法关键点
- 给3款前沿LLM（Claude Opus 5.5、GPT-6.1 Sol、GPT-6 Astra）仅提供10个标注样本与运行沙箱，对比固定架构权重编写、自由设计架构两种模式的表现
- 自由设计模式下，所有LLM均自发选择「稀疏事实表+固定查询流程」的结构，无需注意力、MLP、稠密嵌入，单条事实对应表中单行，支持预测溯源、单行局部编辑
- 优化得到关联记忆架构，通过概念对哈希直接寻址查表，单查询仅读取120行数据，推理成本与事实总量无关
### 关键结果
- 实验基于ARC科学多选题数据集（共3530道题），对比基线包括同规模Transformer、全量样本梯度训练的小模型、BM25检索等
- LLM设计的稀疏表模型比同准确率的手写权重Transformer参数量少1800×，优化后的关联记忆模型推理速度比同规模Transformer快17×，ARC准确率最高达54.4%
- 仅用10个标注样本的WSP模型效果，超过用全量3358个样本梯度训练的同规模小模型
### 核心结论
无需梯度训练的场景下，可溯源、可局部编辑的稀疏查表结构，比为梯度优化设计的Transformer更适配LLM手写权重的需求
