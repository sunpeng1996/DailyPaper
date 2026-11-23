---
title: Enhancing Attention with Higher-Order Attention
title_zh: 利用高阶注意力增强大语言模型的注意力机制
authors:
- R. I. Cukier
affiliations:
- Michigan State University
arxiv_id: '2611.27764'
url: https://arxiv.org/abs/2611.27764
pdf_url: https://arxiv.org/pdf/2611.27764
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: 大语言模型 · 注意力机制优化
tags:
- Attention
- LLM
- MutualInformation
- MarkovChain
- ContrastiveDecoding
one_liner: 从信息论与马尔可夫链出发提出三类高阶注意力，增强大模型自回归推理的信息密度
practical_value: '- 做生成式推荐的LLM微调时，可引入2-3阶的邻接key关联注意力，仅增加少量参数就能提升长序列用户行为的建模精度，适配电商用户跨session行为序列建模场景

  - 对比解码场景下，可将高阶注意力的输出作为专家模型、标准注意力作为反专家模型，降低推荐文案、Agent回复的重复率与幻觉，适合电商客服Agent、商品文案生成

  - 长序列推理时，可复用论文提出的最小概率阈值候选集裁剪方法，仅保留top-K高概率token，将高阶注意力的推理复杂度压缩到和标准注意力相当的水平'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有decoder架构大语言模型的标准自注意力本质为伪自回归，其对value向量的线性加权组合无法严格匹配自回归负对数似然（NLL）损失的概率分解形式，缺少多token间的高阶关联建模，限制了生成序列的信息密度与逻辑一致性。
### 方法关键点
- 基于条件互信息（CMI）分解，设计依赖双query token的注意力机制，建模key与间隔较远的query对的关联，引入长程序列依赖
- 基于局部马尔可夫链，设计关联相邻key token的高阶注意力，支持乘法、加法两种参数化形式，2阶版本仅增加1个可学习矩阵，计算复杂度可控
- 基于广义最大熵原理（GMEP），训练完成后通过拉格朗日乘子优化，将2阶注意力学到的token对概率扩展到τ长度的序列级概率，无需全模型重训
- 提出基于最小条件概率阈值的候选词表裁剪方法，仅保留高概率token参与计算，大幅降低高阶注意力的推理开销
### 关键结果
该工作为纯理论推导，未提供公开数据集上的量化实验结果，核心结论均来自信息论与概率公式的严格证明：高阶注意力的条件概率分布比标准注意力有更大的极差，最小概率更低、最大概率更高，对token的区分度更强；自回归程度越低，模型困惑度越高，验证了高阶关联建模对提升生成确定性的作用。

标准自注意力的线性组合形式与自回归NLL损失存在本质不匹配，引入多token高阶关联的注意力机制可以系统性提升生成序列的信息密度。
