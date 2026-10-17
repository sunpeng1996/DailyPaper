---
title: Speculative Sampling in Interactive Video Generation
title_zh: 交互式视频生成中的投机采样策略
authors:
- Yubo Huang
- Yuxuan Zhang
- Jiaming Liu
- Sirui Zhao
- Enhong Chen
affiliations:
- University of Science and Technology of China
- The Chinese University of Hong Kong
- Independent Researcher
arxiv_id: '2610.20556'
url: https://arxiv.org/abs/2610.20556
pdf_url: https://arxiv.org/pdf/2610.20556
published: '2026-10-14'
collected: '2026-10-17'
category: Multimodal
direction: 多模态生成 · 推理采样延迟优化
tags:
- Speculative Sampling
- Interactive Video Generation
- Latency Optimization
- Bidirectional Window
- GPU Parallelism
one_liner: 提出交互式视频生成投机采样策略，兼顾大窗口建模质量与低交互延迟，无需流式后训练
practical_value: '- 电商实时AI导购内容生成、直播实时特效等交互类生成服务，可复用大窗口预计算+增量交付思路，平衡生成质量与响应延迟

  - 条件不变时缓存预计算结果的设计，可迁移到RAG、生成式推荐流式响应场景，降低重复计算开销

  - 打破chunk越小延迟越低的固有认知，可在推荐多阶段并行计算、LLM流式推理场景参考，平衡窗口大小与GPU利用率'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
交互式视频生成普遍采用小双向chunk降低响应延迟，但预实验证实更大chunk可显著提升视频质量、提高GPU并行利用率，仅小幅增加采样时间，此前低交互延迟必须牺牲建模窗口大小的约束存在优化空间。
### 方法关键点
1. 以噪声隐变量作为填充扩展建模窗口，融合大窗口的建模能力与小窗口的低延迟交互优势
2. 当输入条件不变时缓存预测结果复用，采用增量方式交付预测内容，未提交的未来内容可随时被新条件替换
### 关键结果
消除了chunk边界带来的等待时间下界，将优化重心从缩小chunk size转向加速单chunk采样，双向窗口大小可作为联合优化画质与采样时间的可调变量，无需复杂流式后训练即可在交互式流媒体系统部署大双向模型。
