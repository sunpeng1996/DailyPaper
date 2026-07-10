---
title: Can Dialects Be Steered Like Languages? Sparse Neurons and Distributed Directions
  in Arabic LLMs
title_zh: 阿拉伯语大模型的方言调控：稀疏神经元与分布式表征方向
authors:
- Kareem Elozeiri
- Mervat Abassy
- Omar Kallas
- Fahim Dalvi
- Preslav Nakov
- Kentaro Inui
- Nadir Durrani
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Qatar Computing Research Institute, Hamad Bin Khalifa University
- Tohoku University
- RIKEN
arxiv_id: '2607.03936'
url: https://arxiv.org/abs/2607.03936
pdf_url: https://arxiv.org/pdf/2607.03936
published: '2026-07-03'
collected: '2026-07-10'
category: LLM
direction: 大模型推理控制 · 内部表征干预
tags:
- LLM Steering
- Inference-time Control
- Sparse Neuron
- Representation Engineering
- Dialect NLP
one_liner: 提出两种推理时无微调方法，可精准调控阿拉伯语大模型输出目标方言
practical_value: '- 针对小语种/方言场景的生成式文案生成，可直接复用推理时神经元调控+向量注入的无微调方案，无需收集大量方言数据做LoRA微调，大幅降低冷启动成本

  - 生成式推荐/广告的地域化、圈层化风格控制场景，可先识别对应风格的稀疏神经元群体，通过推理时激活系数调整快速切换输出风格，稳定性远高于prompt工程

  - 多风格/多语言LLM服务部署时，可预计算各风格/语言的表征方向向量，推理时直接注入，无额外推理延迟，也无需维护多个LoRA权重，降低部署成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
阿拉伯语LLM预训练数据以现代标准阿拉伯语（MSA）为主，方言数据稀缺，导致模型生成默认倾向MSA，方言输出准确率低；现有优化方案依赖微调，数据成本与训练成本高。
### 方法关键点
1. 神经元级分析识别编码方言专属特征的稀疏神经元群体，推理时通过放大/抑制对应神经元调控输出方言；
2. 针对单神经元特征纠缠问题，提取方言专属激活方向向量，推理时注入实现更精准的控制，两种方案均无需微调。
### 关键结果
两种方法均能有效将模型输出从MSA转向目标方言，无额外训练成本，同时可解释性远高于prompt工程与微调方案。
