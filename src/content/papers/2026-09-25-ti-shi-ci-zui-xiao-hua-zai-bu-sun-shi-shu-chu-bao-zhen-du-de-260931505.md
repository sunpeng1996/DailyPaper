---
title: 'Prompt Minimization: Reducing Input Redundancy Without Sacrificing Output
  Fidelity'
title_zh: 提示词最小化：在不损失输出保真度的前提下消除输入冗余
authors:
- Marius F. R. Juston
- Kevin A. Karim
- Jonathan Gao
- Kevin C. Li
- Rudhi Bashambu
affiliations:
- University of Illinois Urbana-Champaign
- KTH Royal Institute of Technology
arxiv_id: '2609.31505'
url: https://arxiv.org/abs/2609.31505
pdf_url: https://arxiv.org/pdf/2609.31505
published: '2026-09-25'
collected: '2026-09-28'
category: LLM
direction: LLM 提示优化 · Prompt Compression
tags:
- Prompt Minimization
- Prompt Compression
- LLM Efficiency
- LoRA
- PPO
- BERTScore
one_liner: 提出零样本、上下文学习、RL微调三种提示压缩框架，在保输出保真前提下大幅压缩提示长度
practical_value: '- 业务中高频调用的固定prompt（如RAG系统提示、推荐文案生成prompt）可先用零样本压缩方案迭代2-3轮，能压缩70%+长度且不影响输出效果，直接降低token成本和推理延迟

  - 提示词压缩的评估可复用BERTScore+压缩率的加权目标函数，业务侧可根据对输出精度的要求调整权重，生成适配自身场景的帕累托最优prompt

  - 小参数模型（如7B级）的提示压缩效果优于大参数模型，业务侧可选择轻量模型做前置prompt压缩模块，进一步降低全链路推理成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM提示词普遍存在冗余，长prompt不仅提升token成本、增加推理延迟，还会引入无关信息干扰LLM推理，降低输出准确性；同时冗余提示也不利于理解LLM对输入信息的依赖逻辑，阻碍提示工程的可解释性优化。

### 方法关键点
- 零样本压缩框架：直接调用LLM迭代压缩prompt，每轮用BERTScore对比压缩前后prompt的输出语义相似度，结合压缩率评估，迭代到阈值停止
- 上下文学习进化压缩框架：将压缩转为离散优化问题，维护候选prompt队列，基于逆适应度加权采样父prompt，通过变异生成新候选，每轮保留TOP N最优prompt避免局部最优
- RL微调压缩框架：用PPO算法仅微调LoRA参数训练专用压缩模型，reward函数结合输出BERTScore和压缩率，动态调整压缩约束避免语义丢失

### 关键结果数字
基于跨领域60条长prompt的测试集，上下文学习方案在Llama-3.1-8B上可实现96%的prompt压缩率（仅保留4%长度），同时输出BERTScore保持0.89，几乎不损失语义；零样本方案也可实现92%压缩率，BERTScore达0.88；小模型Llama-3.1-8B的压缩效果显著优于Qwen2.5-32B大模型，同等语义下压缩率高出1倍以上。

典型prompt中存在大量冗余，仅需2-3轮轻量迭代即可获得大幅压缩收益，投入产出比极高。
