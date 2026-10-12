---
title: 'CAST: Credit Alignment for Cross-Tokenizer On-Policy Distillation'
title_zh: CAST：面向跨分词器在线蒸馏的信用对齐框架
authors:
- Jingru Yang
- Jinhang Wu
- Minjing Shi
- Shengfeng He
- Xuyan Li
- Man Tan
- Biye Li
affiliations:
- Taobao & Tmall Group of Alibaba
- Singapore Management University
arxiv_id: '2610.13257'
url: https://arxiv.org/abs/2610.13257
pdf_url: https://arxiv.org/pdf/2610.13257
published: '2026-10-09'
collected: '2026-10-12'
category: Training
direction: 跨分词器LLM在线蒸馏优化
tags:
- Knowledge Distillation
- On-Policy Distillation
- Cross-Tokenizer
- LLM Training
- Credit Assignment
one_liner: 提出shift-or-stay跨分词器在线蒸馏框架，解决块对齐后信用分配与无对齐位置漂移问题
practical_value: '- 电商/推荐场景常需将大语言模型蒸馏为小规格模型部署在实时推理链路，CAST的跨分词器蒸馏能力可直接复用，无需统一师生模型分词器，降低跨模型族能力迁移的适配成本

  - 对齐块内梯度分配trick可迁移至生成式推荐的SFT/RLHF微调流程：用学生预测不确定性+教师信号局部平滑度加权分配梯度，相比均匀分配可提升蒸馏效果、降低训练崩溃概率

  - 选择性KL锚定机制可复用至所有跨模型蒸馏场景：仅对无教师监督的token位置施加初始SFT模型的KL约束，避免无监督区域漂移的同时不干扰有效知识的迁移'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
跨分词器On-Policy Distillation（OPD）是大模型小规格化、跨模型族能力迁移的核心技术，可解决蒸馏训练的推理分布偏移问题。但现有方法仅实现师生序列的块级文本对齐，两个核心瓶颈未解决：一是块级优势信号无法直接转化为合理的token级更新，均匀分配梯度会浪费学习机会、降低训练效率；二是无教师对齐的token位置无监督信号，易受参数共享影响发生漂移，导致蒸馏效果下降、训练崩溃。
### 方法关键点
- Shift模块：对齐块内按「学生预测不确定性 × 教师信号局部平滑度」加权分配块级优势，保留块总优势不变，让梯度集中在学生不确定且教师信号稳定的token上，兼顾学习效率与训练稳定性
- Stay模块：仅对无教师对齐的位置施加SFT初始模型的KL惩罚，约束无监督区域漂移的同时，不干扰有教师信号位置的知识迁移
- 兼容共享分词器场景，支持固定长度、标点分割的块定义，适用范围不局限于跨分词器蒸馏
### 关键结果
在数学、科学、代码6个基准上测试：跨分词器场景从Qwen3-8B蒸馏到Mistral-7B、Llama-3.1-8B，比最强基线分别高2.45、1.32个点；共享分词器场景蒸馏到Qwen3-1.7B，比最强基线高2.10个点；同时梯度信噪比提升1倍以上，训练崩溃率显著低于基线。
### 最值得记住的一句话
跨模型蒸馏的核心不只是建立师生信号的对齐关系，更要合理分配梯度信用，做到有监督区域充分学习、无监督区域不随意漂移。
