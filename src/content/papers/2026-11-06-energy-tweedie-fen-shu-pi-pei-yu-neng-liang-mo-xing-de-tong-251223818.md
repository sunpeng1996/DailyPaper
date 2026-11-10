---
title: 'Energy-Tweedie: Score meets Score, Energy meets Energy'
title_zh: 《Energy-Tweedie：分数匹配与能量模型的统一理论恒等式》
authors:
- Andrej Leban
affiliations:
- Department of Statistics, University of Michigan, Ann Arbor
arxiv_id: '2512.23818'
url: https://arxiv.org/abs/2512.23818
pdf_url: https://arxiv.org/pdf/2512.23818
published: '2026-11-06'
collected: '2026-11-10'
category: Training
direction: 生成模型训练 · 分数匹配理论
tags:
- Score-Based Diffusion
- Energy-Based Model
- Tweedie Formula
- Generative Model
- Denoising
one_liner: 将Tweedie公式从高斯噪声扩展到广义Gibbs噪声族，提出统一的Energy-Tweedie恒等式
practical_value: '- 落地扩散-based GenRec（生成式推荐）时，可基于该恒等式将默认高斯噪声替换为广义高斯等Gibbs噪声，适配商品/广告的长尾分布特性，提升生成item的匹配精度

  - 扩散推荐模型训练阶段，可采用论文提出的噪声参数估计准则，替代人工网格搜索调参，降低训练调优成本

  - 针对不同品类商品的生成约束，可自定义噪声采样路径，比如高单价商品采样更保守、低单价引流品采样更多样，适配业务差异化需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
经典Tweedie公式是高斯去噪、分数匹配、扩散模型的核心理论基础，但仅支持高斯噪声场景，无法适配非高斯噪声下的生成模型优化需求，限制了扩散类模型的噪声设计空间。
### 方法关键点
将Tweedie公式的适用范围扩展到广义Gibbs（能量基）噪声族，推导得到Energy-Tweedie恒等式，建立了噪声势能定义的核评分规则路径导数与带噪边际分布Stein分数的对应关系，把原有高斯噪声、后验均值、平方损失的单点关联升级为Gibbs噪声、全后验分布、核评分规则的分布级关联。
### 关键结果
1. 提供从后验样本直接估计分数的新路径，降低分数估计成本
2. 给出未知噪声参数的可解释估计准则，无需人工调优
3. 支持自定义噪声参数空间路径的扩散式采样，为基于评分规则的生成模型提供理论支撑
