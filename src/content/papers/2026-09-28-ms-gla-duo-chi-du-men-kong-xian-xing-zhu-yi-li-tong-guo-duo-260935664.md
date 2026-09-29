---
title: 'MS-GLA: Multi-Scale Gated Linear Attention for Addressing Representational
  Bottlenecks via Multi-Temporal Resolution'
title_zh: MS-GLA：多尺度门控线性注意力通过多时间分辨率解决表示瓶颈
authors:
- Prasoon Dev
- Anirudh Sankar
- Vasudeva Varma
affiliations:
- Language Technologies Research Center
- International Institute of Information Technology Hyderabad
arxiv_id: '2609.35664'
url: https://arxiv.org/abs/2609.35664
pdf_url: https://arxiv.org/pdf/2609.35664
published: '2026-09-28'
collected: '2026-09-29'
category: LLM
direction: 高效长序列建模 · 门控线性注意力优化
tags:
- Gated Linear Attention
- Multi-Scale Modeling
- Long-Context Modeling
- Linear Transformer
- Sequence Modeling
one_liner: 将GLA注意力头分配到多时间分辨率分支，无参数新增下提升长序列建模与召回性能
practical_value: '- 长上下文用户行为建模场景下，可将现有线性注意力/SSM模块拆分为多时间分辨率分支，无需新增参数即可提升长短期行为融合效果，比如细分支处理近7天点击、粗分支处理近3个月浏览行为

  - 输入依赖的动态路由融合机制可直接复用在多源特征融合模块（如用户特征+商品特征+场景特征的动态加权），效果优于固定权重融合

  - MS-GLA是GLA的drop-in替换组件，现有基于GLA/RetNet的生成式推荐基座可直接替换，仅增加14%内存即可获得9.5%的perplexity下降与18.9%的召回类任务提升

  - 长序列召回场景必须保留至少1个原生分辨率分支，全粗粒度分支会大幅降低token级特征（如Semantic ID、商品ID）的匹配精度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Gated Linear Attention（GLA）作为线性时间复杂度的Transformer变体，兼顾硬件效率与基线性能，但所有注意力头均在单一时间分辨率下处理序列，固定容量的记忆矩阵需同时编码局部句法细节与长程语义结构，存在固有表示瓶颈，仅靠门控机制无法彻底解决。
### 方法关键点
- 无需新增总参数量与头数，将原有GLA头分配到多个时间分辨率分支，每个分支对输入执行不同窗口的非重叠因果平均池化，细分支保留原分辨率处理局部特征，粗分支处理池化后序列专攻长程依赖
- 各分支独立训练无参数共享，输出经因果上采样对齐到原序列长度
- 引入输入依赖的可学习融合层，动态加权不同分支的输出，无需人工干预权重分配
- 完全兼容GLA原生chunkwise并行训练机制，额外计算开销可控
### 关键实验
340M参数量、7B token训练预算下对比GLA基线：语言建模任务平均perplexity降低9.5%，召回密集型任务平均F1提升18.9%，长上下文泛化可支持15倍训练窗口（30720 token）的稳定推理；最优配置{1,2,4}仅损失8%训练吞吐量，内存占用仅提升14%。
> 最值得记住的一句话：多时间分辨率拆分是线性注意力模型突破表示瓶颈、兼顾效率与长程建模能力的低成本有效路径，保留原生分辨率分支是效果不下降的核心前提。
