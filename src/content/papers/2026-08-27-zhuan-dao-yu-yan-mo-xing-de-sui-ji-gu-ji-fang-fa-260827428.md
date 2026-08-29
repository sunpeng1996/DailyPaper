---
title: Stochastic Estimation of Transduced Language Models
title_zh: 转导语言模型的随机估计方法
authors:
- Vésteinn Snæbjarnarson
- Samuel Kiegeland
- Manuel de Prada Corral
- Ryan Cotterell
- Tim Vieira
affiliations:
- ETH Zürich
- University of Copenhagen
- CHI-FRO
arxiv_id: '2608.27428'
url: https://arxiv.org/abs/2608.27428
pdf_url: https://arxiv.org/pdf/2608.27428
published: '2026-08-27'
collected: '2026-08-29'
category: LLM
direction: 转导语言模型 · 无偏概率估计
tags:
- Transduced-LM
- Probability-Estimation
- Beam-Search
- Unbiased-Sampling
- Prefix-Probability
one_liner: 提出转导语言模型前缀概率无偏估计算法，相比阈值剪枝beam search大幅降低长序列计算开销
practical_value: '- 搜索/推荐场景下的序列生成beam search可替换阈值剪枝为无放回采样+逆概率加权，在可控方差下降低计算开销，适配长query/长内容生成场景

  - 涉及字符串转导的业务场景（比如多语言文案生成、query改写、语义对齐转码）可复用该无偏估计算法，解决长序列概率求和的指数级计算问题

  - 大模型推理时的prefix概率计算场景（比如内容合规校验、生成结果置信度评估）可借鉴该方法，用更低的计算成本获得无偏的概率估计值'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
转导语言模型（TLM）将预训练源LM与有限状态转导器结合生成目标字符串分布，但目标前缀概率计算需要对所有映射到该前缀的源字符串概率求和，集合规模指数级甚至无限，现有阈值剪枝beam search方法只能得到误差未知的下界，长序列计算效率极低。
### 方法关键点
1. 采用无放回采样源前缀，按被包含概率的倒数重加权，递归校正得到目标前缀概率的无偏估计，同时可量化阈值剪枝丢失的概率质量；
2. 改进beam summing算法，动态采样保留前缀，随累计概率质量提升减少保留前缀数量，保证算法以概率1终止。
### 关键结果
文本场景下实现更优的计算-方差权衡；DNA任务相同粒子数下误差更低；DNA转氨基酸场景相比阈值剪枝beam summing runtime降低数个数量级，长目标序列前缀概率估计成为可能；阅读时间分析任务替换剪枝方法后语料惊讶度估计显著降低但原有结论保持一致。
