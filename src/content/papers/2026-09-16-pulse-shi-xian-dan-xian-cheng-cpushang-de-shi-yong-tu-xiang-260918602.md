---
title: 'PULSE: Unlocking Practical Image Compression on Single-Thread CPU'
title_zh: PULSE：实现单线程CPU上的实用图像压缩
authors:
- Zhaoyang Jia
- Tianyu Zhang
- Zihan Zheng
- Wenxuan Xie
- Jiahao Li
- Bin Li
- Houqiang Li
- Yan Lu
affiliations:
- University of Science and Technology of China
- Microsoft Research Asia
- Independent Researcher
arxiv_id: '2609.18602'
url: https://arxiv.org/abs/2609.18602
pdf_url: https://arxiv.org/pdf/2609.18602
published: '2026-09-16'
collected: '2026-09-17'
category: Other
direction: 低资源硬件 · 图像压缩编码优化
tags:
- Image Compression
- CPU Optimization
- Human-LLM Collaboration
- Low Latency
- Codec
one_liner: 提出低复杂度PULSE图像编解码器，单线程CPU解码1080p仅126ms，性能对标专业编解码器HM
practical_value: '- 电商商品图/短视频素材存储分发场景可复用PULSE低延迟解码能力，降低CDN与端侧加载成本

  - 人-LLM协作迭代优化模型架构的思路可迁移到搜推低资源端模型（如端侧推荐模型）的压缩迭代

  - 整数线性CDF预测+元先验的熵编码方案可复用在搜推系统海量特征/行为数据的压缩存储场景'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有学习式图像压缩方法在CPU等资源受限硬件上计算开销过高，难以落地到实际业务场景。
### 方法关键点
1. 设计仅5.2 kMAC/pixel的超低复杂度神经接收器，支持多硬件平台低延迟解码；
2. 采用整数线性CDF预测器+元先验实现高效比特精确熵编码；
3. 提出启发式探针引导的智能进化流程，通过人-LLM协作迭代优化架构，在低复杂度约束下保障压缩性能。
### 关键结果
单CPU线程解码1080p图像仅需126ms，压缩性能与专业编解码器HM相当；感知优化版本可对标MS-ILLM等更大规模感知编解码器，支持手机、笔记本、服务器多平台比特精确熵编码。
