---
title: 'HPD-Parsing: Hierarchical Parallel Document Parsing'
title_zh: HPD-Parsing：分层并行文档解析
authors:
- Shu Wei
- Jingjing Wu
- Lingshu Zhang
- Qunyi Xie
- Hao Zou
- Le Xiang
- Xu Fan
- Yangliu Xu
- Manhui Lin
- Xiaolong Ma
affiliations:
- Baidu
- PaddlePaddle
arxiv_id: '2607.18839'
url: https://arxiv.org/abs/2607.18839
pdf_url: https://arxiv.org/pdf/2607.18839
published: '2026-07-20'
collected: '2026-07-22'
category: Multimodal
direction: 多模态文档解析 · 并行解码效率优化
tags:
- VLM
- Document Parsing
- Parallel Decoding
- Throughput Optimization
- Multi-token Prediction
one_liner: 提出分层并行文档解析范式HPD-Parsing，吞吐量较自回归基线提3倍且精度持平
practical_value: '- 电商场景解析商品详情页、商家资质、用户评价等多模态文档时，可复用分层并行解码思路，全局布局分析后并行解码各内容块，大幅提升解析吞吐量

  - 大模型推理链路优化可借鉴P-MTP渐进式多Token预测trick，在不损失效果的前提下减少单分支解码步数，降低推理延迟

  - Agent系统的多模态信息摄入模块可直接集成开源HPD-Parsing模型，替代现有自回归文档解析组件，提升整体链路效率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有基于VLM的统一文档解析器采用全页逐Token自回归生成逻辑，存在随文档长度线性增长的序列瓶颈，且忽略了「布局需全局分析、块内容可并行解析」的核心文档特性。

### 方法关键点
1. 采用分层并行解码范式替代全页自回归生成，设置主布局分支统筹全局文档结构，动态分配块级内容解码任务到并发分支
2. 引入渐进式多Token预测（P-MTP）机制，进一步压缩单分支内的解码步骤

### 关键结果
公开基准测试中TPS达4752，吞吐量是现有最快文档解析模型的2.62倍、原生自回归基线的3.06倍，同时保持有竞争力的解析精度。
