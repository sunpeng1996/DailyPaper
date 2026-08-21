---
title: Robust Incomplete Multimodal Sentiment Analysis via Iterative Proxy Correction
title_zh: 基于迭代代理校正的鲁棒不完整多模态情感分析
authors:
- Zhifa Geng
- Subin Huang
- Hao Guo
- Junjie Chen
- Sanmin Liu
- Chao Kong
affiliations:
- School of Computer and Information, Anhui Polytechnic University
arxiv_id: '2608.19971'
url: https://arxiv.org/abs/2608.19971
pdf_url: https://arxiv.org/pdf/2608.19971
published: '2026-08-20'
collected: '2026-08-21'
category: Multimodal
direction: 多模态情感分析 · 缺失模态鲁棒性优化
tags:
- Multimodal Sentiment Analysis
- Proxy Correction
- Missing Modality
- Multimodal Fusion
- Robust Learning
one_liner: 提出迭代代理校正框架，解决不完整多模态输入下情感分析性能退化问题
practical_value: '- 电商多模态用户评论/直播内容的情感分析场景经常遇到模态缺失问题，可借鉴迭代代理校正思路补全缺失模态的语义表示，提升情感识别准确率

  - 多模态特征融合时可复用「模态可靠性评分+自适应加权融合」的trick，动态降低模糊图像、杂音音频等低质量模态的权重，避免带偏预测结果

  - 训练阶段用完整模态作为语义锚约束补全过程的思路，可迁移到多模态召回排序场景的缺失特征补全任务，减少补全误差传播'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
多模态情感分析需融合文本、视觉、声学多维度信号，但实际场景中输入常存在模态缺失/损坏，现有基于单步代理构建的补全方法初始代理质量差，误差向后续推理传播，导致预测精度下降。
### 方法关键点
1. 从非语言模态构建语言导向的代理，通过门控残差校正迭代优化代理表示
2. 基于估计的语言模态可靠性评分，将校正后的代理与观测到的语言表示自适应融合，平衡补全信息与真实可信信息的权重
3. 训练阶段引入分阶段隐式校正目标，用完整语言表示作为语义锚稳定代理优化轨迹
### 关键结果
在MOSI、MOSEI、SIMS三个公开数据集的多种模态缺失设置下，性能一致优于现有SOTA基线，实现不完整输入下的鲁棒情感预测。
