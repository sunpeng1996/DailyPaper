---
title: 'PaDoc: Layout-Grounded Parallel Decoding for Document Parsing'
title_zh: PaDoc：基于布局锚定的并行解码文档解析方法
authors:
- Hao Yu
- Jiabo Zhan
- Kang Liu
- Linnan Zhao
- Dongxu Yue
- Rui Chen
- Jinglin Wang
- Chong Sun
- Chen Li
- Jing Lyu
affiliations:
- Tsinghua University
- Wechat Vision, Tencent
arxiv_id: '2608.06146'
url: https://arxiv.org/abs/2608.06146
pdf_url: https://arxiv.org/pdf/2608.06146
published: '2026-08-05'
collected: '2026-08-07'
category: Multimodal
direction: 多模态大模型 · 文档解析并行解码优化
tags:
- MLLM
- Parallel Decoding
- Document Parsing
- vLLM
- KV Cache Reuse
one_liner: 提出基于布局分支结构的MLLM并行解码文档解析方案，兼顾全页上下文与高吞吐低延迟
practical_value: '- 电商商品详情页、广告物料结构化等多模态内容理解场景，可复用该并行解码架构，在保留全页上下文的同时大幅提升吞吐、降低延迟

  - vLLM共享前缀KV cache复用技巧可直接迁移到同批次多分支生成任务（如同一用户多候选文案/内容并行生成），降低推理成本

  - 分支式注意力掩码设计可用于解决多任务并行生成的依赖可见性问题，适配标准next-token训练范式，无需额外修改训练逻辑'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
端到端文档解析的自回归序列化解码路径随内容长度线性增长，延迟高；分块两阶段解析存在重复视觉预填充、上下文碎片化问题，无法兼顾全页上下文与推理效率。
### 方法关键点
1. 将预测布局作为共享页面表征的分支结构，基于区域充足假设推导前缀条件因式分解，让布局流与各区域内容分支并行解码，解码深度降至最长布局-内容路径长度；
2. 单MLLM内实现：打包变长祖先注意力保证标准next-token训练下的可见性，掩码并行解码结合vLLM共享前缀KV cache复用实现多分支并发推理。
### 关键结果
OmniDocBench Full上布局F1达91.1，端到端解析总得分94.24，文本编辑误差0.038、公式CDM95.59均为最优；单A800上384页测试集吞吐较同骨干序列SFT基线提升67.4%~118%，P95延迟降低39.2%~54.9%。
