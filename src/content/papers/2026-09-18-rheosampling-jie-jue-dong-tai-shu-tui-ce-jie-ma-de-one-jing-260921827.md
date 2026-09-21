---
title: 'RheoSampling: Resolving the One-Hot Dilemma in Stochastic Dynamic-Tree Speculative
  Decoding'
title_zh: RheoSampling：解决动态树推测解码的One-Hot困境
authors:
- Qiao Hu
- Yepeng Weng
- Bo Zhang
- Takehisa Yairi
affiliations:
- Chinese Academy of Sciences
- The University of Tokyo
- Lenovo AI Technology Center
- University of Chinese Academy of Sciences
arxiv_id: '2609.21827'
url: https://arxiv.org/abs/2609.21827
pdf_url: https://arxiv.org/pdf/2609.21827
published: '2026-09-18'
collected: '2026-09-21'
category: LLM
direction: LLM推理加速 · 动态树推测解码
tags:
- Speculative Decoding
- Dynamic Tree
- LLM Inference
- Optimal Transport
- Lossless Sampling
one_liner: 通过双身份概率解耦实现首个支持无损随机采样的动态树推测解码框架
practical_value: '- 业务中使用LLM做商品文案生成、Agent客服问答等高吞吐场景时，可直接基于现有EAGLE-3推理栈集成RheoSampling，在无精度损失前提下获得3%左右的端到端提速

  - 双身份解耦思路可迁移到生成式推荐候选生成模块：构造「top-K确定性热门候选+长尾随机采样候选」的混合池，对两类候选采用不同的排序规则用于召回筛选和最终排序，兼顾头部效率与长尾探索

  - 稀疏采样trick可直接复用：LLM推理/生成式推荐的token采样阶段，将logit截断到top-128后再做softmax，可大幅降低采样计算开销，且几乎不会影响最终效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有动态树推测解码方案（如EAGLE-3）在贪心解码下效率优异，但随机解码（温度T>0）场景下会将候选分布坍缩为one-hot，导致接受率大幅下降，陷入「动态树保上下文拓扑就丢失随机性、静态树保随机性就丢失上下文感知」的两难，根源是树构建和token验证两个任务共用同一套概率分布，耦合度过高。
### 方法关键点
- 双身份概率解耦：给随机采样的长尾token分配两个独立概率，树构建阶段用固定proxy概率与确定性top-K候选竞争扩展、剪枝资格，验证阶段用真实采样概率计算接受率，保证输出无损
- 混合候选池设计：每步扩展时分配K个候选槽位，分别填充top-m个高概率确定性候选、1个长尾随机采样候选、剩余填充候选，通过调整m（rheostat参数）平衡随机探索强度和树结构质量，默认m=1为最优配置
- 工程优化：基于最优运输（OT）设计验证逻辑提升接受率，截断logit到top-128做稀疏采样，大幅降低大vocab下的采样计算开销
### 关键实验
在Alpaca、GSM8K、HumanEval等6个跨领域benchmark、3个主流LLM（Vicuna-13B、Llama-3.1-8B、DeepSeek-R1-Distill-8B）上对比EAGLE-3基线，平均接受长度提升0.14~0.22，端到端推理速度提升3%左右，在T=1.0随机解码场景下收益最显著。
### 核心洞察
将原本耦合的「结构构建用概率」和「效果验证用概率」解耦，是兼顾效率、效果、无损性的核心思路
