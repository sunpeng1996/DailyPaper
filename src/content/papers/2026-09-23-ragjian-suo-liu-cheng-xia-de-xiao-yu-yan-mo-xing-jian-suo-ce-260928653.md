---
title: 'The Fellowship of the Query: Learning Retrieval Actions'
title_zh: RAG检索流程下的小语言模型检索动作决策学习方法
authors:
- Mohammed Al-Maamari
- Saber Zerhoudi
- Michael Granitzer
- Jelena Mitrović
affiliations:
- University of Passau
arxiv_id: '2609.28653'
url: https://arxiv.org/abs/2609.28653
pdf_url: https://arxiv.org/pdf/2609.28653
published: '2026-09-23'
collected: '2026-09-27'
category: Agent
direction: Agent 检索动作控制优化
tags:
- LoRA
- SLM
- RAG
- Action Prediction
- Trajectory Fine-tuning
one_liner: 基于优质教师轨迹LoRA微调SLM，实现RAG七类检索动作的精准决策
practical_value: '- 搭建电商客服/商品多跳问答RAG Agent时，可复用7类检索动作框架（分解/搜索/改写/提取/合成/校验/终止），解决小模型乱调用工具、提前终止等问题

  - 小模型做动作控制器优先选择多分类LoRA SFT方案，仅需3000条左右优质标注轨迹即可达到接近全量数据的效果，大幅降低标注成本

  - 端到端RAG pipeline可让同一款微调后的SLM同时承担控制器与生成器角色，既降低部署资源消耗，还能提升证据提取率和最终问答准确率

  - 若需保留模型通用能力，可采用适配器插拔设计，检索控制时加载动作LoRA权重，生成任务时切换回基础模型，兼顾效果与通用性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多跳RAG问答需动态决策检索流程动作，小模型零样本工具调用普遍存在重复搜索、漏提证据、无法正确终止等问题，现有方案依赖大模型成本高，缺乏结构化动作监督的低资源落地方案。

### 方法关键点
- 基于Qwen 3-Next 80B生成的优质检索轨迹，过滤后得到1490条有效轨迹、16488个动作样本，动作空间包含7类：decompose、search、reformulate、extract、synthesize、verify、finish。
- 对比多类SLM/xSLM的训练方案：LoRA SFT、LoRA序列分类、TF-IDF逻辑回归、零样本，LoRA固定参数r=16、α=32，仅微调注意力投影层。
- 设计控制器/生成器swap实验，测试4种角色组合的端到端效果，采用Exact Match、token F1、证据提取率作为评估指标。

### 关键结果
- 动作预测任务：Granite 4.1 3B LoRA SFT在1646条测试集上macro-F1达0.6536，较同模型零样本提升3倍，较TF-IDF基线提升21%；仅3000条训练样本即可达到0.6489的macro-F1，接近全量数据效果。
- 端到端问答：微调模型同时承担控制器和生成器时，Exact Match从0.7530提升至0.7946，token F1从0.7783提升至0.8295，证据提取率从1.2%提升至63.9%。

### 核心结论
3000条优质教师轨迹加轻量LoRA微调，即可让小模型达到可用的检索动作控制效果，大幅降低RAG Agent的落地成本。
