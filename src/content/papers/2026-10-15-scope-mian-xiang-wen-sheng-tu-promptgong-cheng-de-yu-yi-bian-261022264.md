---
title: 'SCOPE: Semantic Bounded Credit Optimization for Prompt Engineering in Text-to-image
  Generation'
title_zh: SCOPE：面向文生图Prompt工程的语义边界信用优化
authors:
- Yufei Jiao
- Jinfa Huang
- Zeyue Xue
- Tianyu Xie
- Yuexiao Ma
- Rongrong Ji
- Xiawu Zheng
- Jiebo Luo
affiliations:
- Xiamen University
- University of Rochester
- Nanyang Technological University
- The University of Hong Kong
arxiv_id: '2610.22264'
url: https://arxiv.org/abs/2610.22264
pdf_url: https://arxiv.org/pdf/2610.22264
published: '2026-10-15'
collected: '2026-10-17'
category: LLM
direction: LLM Prompt优化 · RL对齐
tags:
- Prompt Engineering
- Reinforcement Learning
- GRPO
- Text-to-Image
- Semantic Span
one_liner: 提出基于语义跨度池化的GRPO变体，零额外开销提升文生图Prompt优化效果
practical_value: '- 电商文生图广告、商品素材生成的Prompt自动优化场景，可复用语义跨度池化的RL损失设计，无需额外标注即可提升Prompt与需求的对齐效果

  - 做RLHF、RL对齐类任务时，可引入语义结构作为归纳偏置，同语义段内token共享损失系数，降低梯度噪声、提升训练稳定性

  - 电商商品文案改写、搜索Query改写的RL优化场景，可借鉴语义分段+组内池化的策略更新逻辑，降低标注/采样成本'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有基于RL的文生图Prompt优化方法直接将全局图像奖励分配到单个subword token，未考虑对象、属性、关系等连贯语义跨度的结构特性，梯度噪声大、优化效率低。
### 方法关键点
1. 基于Group Relative Policy Optimization (GRPO) 设计SCOPE优化目标，Prompt重写器同时生成增强Prompt和对应的语义分区；
2. 对每个语义跨度内的策略log概率偏移做池化，给跨度内所有token的损失分配共享系数，仅保留全局单优势信号；
3. 无需单独的跨度级奖励，也不需要额外生成图像，训练开销与原生GRPO一致。
### 关键结果
在Qwen-Image、SD3、FLUX.1-dev三个文生图底座上，相比原生GRPO，GenEval指标平均相对提升9.48%，T2I-CompBench指标平均相对提升7.62%，消融验证语义边界和跨度内池化均贡献增益。
