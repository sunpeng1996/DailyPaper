---
title: 'Role-Break in Attention Heads: Understanding and Detecting Hallucinations
  in VLMs'
title_zh: 注意力头角色断裂：多模态大模型幻觉的理解与检测
authors:
- Mingyu Wang
- Weilin Jin
- Wenbo Li
- Haoyang Huang
- Nan Duan
- Tong Jia
- Chaoran Luo
- Ying Li
affiliations:
- Peking University
- Joy Future Academy
arxiv_id: '2607.29412'
url: https://arxiv.org/abs/2607.29412
pdf_url: https://arxiv.org/pdf/2607.29412
published: '2026-07-31'
collected: '2026-08-03'
category: Multimodal
direction: 多模态大模型 · 幻觉检测
tags:
- VLM
- Hallucination Detection
- Attention Head
- Lightweight Detector
- Zero Fine-tuning
one_liner: 基于注意力头角色断裂现象构建无需微调的轻量VLM幻觉检测器，跨多基准平均AUROC达93.23%
practical_value: '- 多模态商品理解场景可复用Role-Break信号，无需微调VLM即可快速检测生成内容的幻觉，降低商品文案生成、直播内容审核的错误率

  - 轻量线性检测器架构（特征维度<5000）可直接部署在多模态生成链路后，额外推理开销极低，适合高并发业务场景

  - 关注attention head行为模式偏差的思路可迁移到纯文本LLM幻觉检测场景，用于RAG、Agent生成内容的合规校验'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有VLM幻觉检测方法多围绕单一幻觉模式设计，而真实场景下幻觉由多种模式混合产生，单模式绑定的信号跨模型、跨任务稳定性差，难以落地。
### 方法关键点
从注意力头层级统一分析幻觉成因，发现幻觉发生时注意力头会偏离其固有上下文行为模式（命名为Role-Break现象）；该偏差在注意力头、上下文来源、偏差方向上存在系统性规律，保留头身份的前提下信号可线性读取；基于此构建轻量线性检测器，无需微调VLM，特征维度低于5000。
### 关键结果
在6种VLM、4个基准测试集上平均AUROC达93.23%，检测到的幻觉token可直接用于判别式干预场景。
