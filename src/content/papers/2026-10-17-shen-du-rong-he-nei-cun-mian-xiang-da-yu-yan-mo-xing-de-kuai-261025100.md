---
title: 'Deep Fusion Memory: A Chunk-Level Parametric Memory for Large Language Models'
title_zh: 深度融合内存：面向大语言模型的块级参数化内存架构
authors:
- Rubin Wei
- Siyuan Sun
- Hao Sun
- Yuliang Liu
- Xiang Shi
- Jiarui Wang
- Junming Zhang
- Zhouhan Lin
affiliations:
- 上海交通大学人工智能学院LUMIA Lab
- 上海人工智能实验室
arxiv_id: '2610.25100'
url: https://arxiv.org/abs/2610.25100
pdf_url: https://arxiv.org/pdf/2610.25100
published: '2026-10-17'
collected: '2026-10-23'
category: LLM
direction: 大语言模型 · 参数化内存优化
tags:
- Parametric Memory
- Knowledge Injection
- LLM Adaptation
- Gated Cross-Attention
- Chunk-level Processing
one_liner: 提出块级参数化内存DFM，免在线检索，降训练成本同时提升知识密集任务效果
practical_value: '- 电商Agent/智能客服等场景做领域知识注入时，可借鉴DFM方案替代传统RAG，既降低在线检索延迟，又避免持续预训练的灾难性遗忘问题，适配高实时性业务需求

  - 门控交叉注意力融合设计可直接复用：将垂类知识库的chunk embedding作为监督信号，插入LLM decoder中后层融合，冻结backbone即可快速适配商品问答、法律咨询等垂直场景

  - 训练数据构建阶段改用chunk级而非token级检索目标，可将检索查询量降低32倍、召回条目降低2048倍，大幅降低垂类场景知识注入的离线准备成本，适合资源有限的业务团队'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM知识注入方案存在明显短板：持续预训练/LoRA易引发灾难性遗忘，RAG等非参数检索方案在线推理延迟高，传统参数化内存需要token级检索构建训练数据，离线成本极高且仅做输出层浅融合，知识利用效率低。

### 方法关键点
- 架构分为因果块级内存预测器+门控交叉注意力融合模块，全程冻结LLM backbone训练，推理无需在线检索
- 离线按32token分块，以前序chunk检索得到的Top16邻居embedding作为监督信号，同chunk内所有token共享预测内存，大幅降低检索次数
- 预测内存通过门控交叉注意力插入decoder中后层，每个头可学习独立权重控制内存贡献，直接融合到中间隐层而非仅做输出层插值
- 联合优化目标为LM交叉熵损失+预测内存与目标内存的MSE损失，端到端训练新增模块

### 关键实验
- 6个QA任务：Mistral-7B、Qwen3-8B上效果分别超过最优基线12.71%、11.19%
- 领域适配：代码、数学、法律三个垂类，Qwen3-4B、Qwen3-8B上分别平均提升6.51、4.38个点
- 效率：相比token级参数内存，训练数据构建检索查询量降32倍，检索条目降2048倍，训练时间减少62.5%

**最值得记住的一句话**：块级共享的参数化内存可以在免在线检索、不微调backbone的前提下，以极低的离线成本实现高效的领域知识注入，效果优于主流RAG、LoRA、持续预训练方案。
