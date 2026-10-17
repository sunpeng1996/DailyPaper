---
title: 'Beyond Pairwise Repulsion: Collective Diversity via Determinant Maximization
  in Diffusion Sampling'
title_zh: 超越成对排斥：扩散采样下基于行列式最大化的集体多样性优化
authors:
- Kwanyoung Lee
- SeungJu Cha
- Yebin Ahn
- Sungho Koh
- Dong-Jin Kim
affiliations:
- Hanyang University, South Korea
arxiv_id: '2610.22267'
url: https://arxiv.org/abs/2610.22267
pdf_url: https://arxiv.org/pdf/2610.22267
published: '2026-10-15'
collected: '2026-10-17'
category: Multimodal
direction: 多模态生成 · 扩散模型采样多样性优化
tags:
- Diffusion Model
- Diversity Optimization
- Determinant Maximization
- Synthetic Data Generation
- Sampling Strategy
one_liner: 提出无需训练或修改采样器的DetNO方法，通过行列式最大化提升扩散模型生成批次的集体多样性
practical_value: '- 电商广告/商品素材生成场景可直接复用DetNO的批次级多样性优化逻辑，无需微调现有扩散模型，仅在采样阶段添加单超参数λ控制质量-多样性trade-off，解决同prompt生成素材同质化问题

  - 用合成数据做小样本分类（如商品细分类目打标、违规内容识别）时，优先选用log-determinant作为批次多样性优化目标，效果优于InfoNCE等成对约束，batch越大提升越显著

  - 生成式推荐生成候选item集时，可借鉴RKHS体积最大化思路设计候选集多样性指标，替代传统成对相似度计算，避免候选集落入低维语义子空间，提升覆盖度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
T2I扩散模型强引导会使采样向条件分布高密度模式收敛，同prompt独立采样结果高度同质化，现有成对排斥优化无法解决批次落入低维子空间的高阶问题，限制合成数据增强等需多样性场景的效果。
### 方法关键点
提出DetNO，将多样性生成转化为初始噪声的RKHS体积最大化问题，优化单步Tweedie预测的RBF Gram矩阵对数行列式，搭配锚点保真项约束噪声在合理区间，仅需单超参数λ平衡多样性与质量，无需训练或修改采样器。
### 关键结果
在SD1.5、SDXL、SD3三个骨干上，VendiScore、平均自相似性指标达批次多样性SOTA；下游小样本分类实验中，低样本量下合成数据增强带来统计显著的精度提升，log-determinant目标比InfoNCE的下游精度更优，batch越大优势越明显
