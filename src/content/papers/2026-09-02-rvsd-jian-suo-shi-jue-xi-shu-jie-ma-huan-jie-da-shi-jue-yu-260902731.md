---
title: 'RVSD: Retrieval Vision Sparse Decoding for Mitigating Visual Hallucinations
  in Large Vision-Language Models'
title_zh: RVSD：检索视觉稀疏解码缓解大视觉语言模型视觉幻觉
authors:
- Canjie Liu
- Jiawen Kang
- Jinbo Wen
- Zishao Zhong
affiliations:
- Guangdong University of Technology
- City University of Hong Kong
- Guangzhou University of Chinese Medicine
arxiv_id: '2609.02731'
url: https://arxiv.org/abs/2609.02731
pdf_url: https://arxiv.org/pdf/2609.02731
published: '2026-09-02'
collected: '2026-09-04'
category: Multimodal
direction: 多模态大模型 · 视觉幻觉缓解
tags:
- LVLM
- Visual Hallucination
- Sparse Decoding
- Semantic Retrieval
- Training-Free
one_liner: 提出免训练即插即用的RVSD解码框架，统一token稀疏化与语义空间视觉检索缓解LVLM视觉幻觉
practical_value: '- 多模态商品理解场景可复用语义导向token选择策略，在保留商品核心视觉特征的前提下降低冗余token的计算开销，提升推理速度

  - 电商多模态Agent（如智能导购、图文审核）可直接集成RVSD即插即用框架，无需额外训练即可降低视觉幻觉，避免对商品属性、外观的错误描述

  - 语义空间跨模态检索（SSVR）机制可迁移至多模态召回场景，在共享语义空间做按需检索，降低传统跨模态检索的资源消耗'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
大视觉语言模型（LVLM）在图文问答、多模态推理等任务表现优异，但普遍存在视觉幻觉问题，生成内容与实际视觉信息不符，严重影响落地可靠性；现有解决方案依赖标注数据集、额外训练或多轮解码，计算开销高，落地门槛高。
### 方法关键点
提出免训练即插即用的RVSD解码框架，单次解码pass内统一两个核心模块：1）语义导向token选择策略，选择性稀疏化冗余token，保留关键视觉信息，降低无效计算；2）语义空间视觉检索（SSVR）机制，将视觉补偿重构为共享语义空间内的按需跨模态检索流程，无需额外训练或标注数据。
### 关键结果
实验达到SOTA的视觉幻觉缓解效果，在长上下文生成场景下仍保持稳定的幻觉抑制能力，推理开销远低于现有重训或多轮解码方案。
