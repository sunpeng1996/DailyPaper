---
title: 'Correcting to Predict: Pseudo-Value Correction for Multimodal Attribute Value
  Extraction'
title_zh: 面向多模态商品属性值提取的伪值校正C2P框架
authors:
- Junhao Zhang
- Feiran Hu
- Xiao Hu
- Baoliang Cui
- Xiaoyi Zeng
affiliations:
- Alibaba International Digital Commerce Group
arxiv_id: '2609.34383'
url: https://arxiv.org/abs/2609.34383
pdf_url: https://arxiv.org/pdf/2609.34383
published: '2026-09-28'
collected: '2026-09-29'
category: RecSys
direction: 多模态大模型 · 电商属性值提取
tags:
- Multimodal LLM
- Attribute Value Extraction
- E-commerce
- LoRA
- Fine-tuning
- Industrial Deployment
one_liner: 将多模态属性值提取重构为伪值校正任务，兼顾低推理开销与歧义属性抽取精度
practical_value: '- 可直接复用C2P伪值校正范式改造现有属性抽取流程：训练阶段随机注入占位符/相似商品检索伪值，让模型学习基于图文证据校正初始假设，推理仅需替换prompt中固定占位符，无需改造推理链路即可提升歧义属性抽取精度

  - 可迁移SCR策略优化垂域MLLM效果：通过不同伪值输入筛选预测不稳定的难例，混合50%原训练数据微调，针对性解决模型依赖输入先验、忽略任务证据的问题，仅需额外两轮少量数据微调即可获得显著增益

  - 工业部署可参考C2P的效率设计：相比RAG类属性抽取方案，C2P无在线检索开销，单L20 GPU QPS达4.77，仅比直接生成低7.9%，精度更优，适合千万级商品的大规模属性补全场景'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商商品属性是分面过滤、搜索推荐、供应链运营的核心基础特征，但大量商品因卖家非结构化录入导致属性缺失/错误，传统文本-only方法无法处理需跨模态推理的隐含属性，MLLM直接生成易依赖语言先验、忽略细粒度多模态证据，常混淆语义相似的属性值；现有自校正、多Agent辩论等方法依赖初始生成结果，错误易传导，RAG类方案又带来额外检索开销，推理效率低无法适配大规模工业场景。
### 方法关键点
- 重构任务范式：将属性值抽取从直接生成改为伪值校正任务，训练阶段注入两类伪值：无信息占位符（如invalid）、相似商品检索得到的合理伪值，让模型学习基于商品图文证据判断保留/校正伪值，输出符合平台规范的标准化属性值
- 二阶SCR训练：对基模型输入不同伪值，筛选预测结果不一致的难例，混合50%原训练数据微调，降低模型对伪值的敏感度，强化依赖多模态证据的决策逻辑
- 推理优化：无需在线检索或多步迭代，仅输入固定占位符（默认选类目-属性对下最少出现的属性值leastV）即可触发校正逻辑，实现单步高效推理
### 关键结果
基于Qwen2.5-VL-7B做LoRA微调，在公开ImplicitAVE基准和AliExpress工业数据集上，C2P-SCR相比直接SFT基线，整体Micro-F1分别提升1.68、3.27个点，难属性分别提升3.03、9.92个点；推理单L20 GPU QPS达4.77，仅比直接生成低7.9%，远高于RAG-top3的1.45；线上A/B测试显示，可部署属性对提升22.6%，过滤会话CTR提升3.3%，全量商品卡片CTR提升0.94%。
### 核心结论
对垂域多模态预测任务，将生成重构为「基于证据校正初始假设」的范式，可在不增加推理开销的前提下显著提升难例效果。
