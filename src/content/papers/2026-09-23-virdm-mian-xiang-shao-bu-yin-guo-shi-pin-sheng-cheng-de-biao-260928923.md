---
title: 'ViRDM: Taming Representation Distribution Matching for Few-Step Causal Video
  Generation'
title_zh: ViRDM：面向少步因果视频生成的表征分布匹配优化方法
authors:
- Zichong Meng
- Chongjian Ge
- Chun-Hao P. Huang
- Yang Zhou
- Huaizu Jiang
affiliations:
- Northeastern University
- Adobe Research
arxiv_id: '2609.28923'
url: https://arxiv.org/abs/2609.28923
pdf_url: https://arxiv.org/pdf/2609.28923
published: '2026-09-23'
collected: '2026-09-25'
category: Multimodal
direction: 多模态生成 · 视频扩散蒸馏优化
tags:
- Video Diffusion
- Distribution Matching
- Knowledge Distillation
- Low-Latency Generation
- Multimodal
one_liner: 提出无教师无判别器的少步因果视频生成后训练方案ViRDM，降本提效同时提升生成质量
practical_value: '- 电商个性化商品短视频、直播片段生成场景可复用该无教师无判别器的蒸馏框架，大幅降低少步扩散模型后训练的资源开销

  - 低延迟生成类场景（如推荐流实时插出生成式视频、Agent实时内容反馈）可借鉴随机截断干净退出监督、轻量化VAE解码器的trick，仅需少量更新即可达标

  - 资源受限的生成类大模型后训练任务，可复用分段向量-雅克比乘积的梯度优化方法，降低显存占用，减少训练所需GPU资源'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
少步自回归视频扩散可实现低延迟流式生成，但现有基于DMD的后训练方法依赖大参数量预训练教师模型与在线判别器，资源开销极高，落地门槛高。
### 方法关键点
将图像领域的表征分布匹配(RDM)迁移至少步因果视频生成，针对三大落地障碍提出优化：1. 结合随机截断干净退出监督、轻量化VAE解码器、分段向量-雅克比乘积，解决多步视频生成的显存瓶颈；2. 引入轻量时序动态正则补偿时序约束缺失，仅需训练生成器，无需教师、判别器网络。
### 关键结果
仅完成20次生成器更新，VBench官方评测得分达84.87，较此前最优少步因果基线高0.36，仅消耗16 A100 GPU小时
