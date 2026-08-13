---
title: 'MOON: Multi-Objective OrthoNormalized Updates for Multitask Learning'
title_zh: MOON：面向多任务学习的多目标正交归一化更新算法
authors:
- Shiji Zhou
- Kunlin Lyu
- Lei Zhang
- Ruodong Wang
- Yifan Sun
affiliations:
- 北京航空航天大学
- 北京人工智能研究院(BAAI)
- 中国人民大学
arxiv_id: '2608.11749'
url: https://arxiv.org/abs/2608.11749
pdf_url: https://arxiv.org/pdf/2608.11749
published: '2026-08-12'
collected: '2026-08-13'
category: Training
direction: 多任务训练 · 多目标梯度优化
tags:
- Multi-Task Learning
- Multi-Objective Optimization
- Gradient Manipulation
- Transformer Training
- Optimizer
one_liner: 针对含矩阵参数的深度学习架构，提出基于谱-核范数几何的多任务多目标优化框架MOON，收敛更快性能更优
practical_value: '- 电商多任务推荐（CTR/CVR/GMV等多目标）场景采用Transformer/MLP架构时，可直接用MOON替换现有PCGrad/CAGrad等欧氏空间MOO方法，适配矩阵参数结构，提升多目标均衡效果

  - 工程实现可复用论文给出的三个低开销组件：梯度动量稳定权重、牛顿-舒尔茨迭代近似极因子、单步在线更新任务权重，算力增量控制在10%以内

  - 生成式推荐/LLM多目标对齐（如有用性/无害性/相关性）场景，MOON可匹配大模型矩阵参数特性，比传统MOO方法降低30%左右训练步数'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有多目标优化（MOO）方法均将模型参数展平为向量，在欧氏空间执行梯度操作，完全忽略Transformer等主流架构中大量矩阵参数的固有结构，既无法获得矩阵几何下的最速下降方向，与Muon等矩阵感知优化器结合时还存在几何假设 mismatch，严重限制多任务训练效率与最终性能。
### 方法关键点
1. 基于矩阵参数的谱范数光滑上界，将多目标共同下降方向求解转化为谱范数正则化极小极大问题，通过谱-核范数对偶求解任务权重，最小化加权聚合梯度的核范数，取聚合梯度的极因子作为更新方向
2. 工程落地采用三个低开销优化：梯度动量稳定聚合梯度波动、牛顿-舒尔茨迭代近似极因子避免高开销SVD、单步在线更新跟踪对偶任务权重省去内循环优化
3. 理论证明光滑非凸目标下，确定性梯度收敛率为O(T⁻¹/₂)，随机梯度收敛率为O(T⁻¹/₄)
### 关键实验结果
在MultiMNIST、NYU-v2、CityScapes、QM9、CelebA 5个多任务基准上对比12种MOO基线：MultiMNIST双任务分类平均准确率达95.65%，比SOTA FAMO高0.26pct；CityScapes双任务场景理解相对STL的平均性能下降仅1.54%，比FAMO低5.39pct；QM9 11任务回归平均性能下降49.9%，比FAMO低7.4pct，同时收敛速度比基线快30%以上。
### 最值得记住的一句话
针对含大量矩阵参数的现代深度学习架构，多目标优化不能盲目展平参数，适配矩阵几何的梯度操作可同时提升收敛效率和多任务均衡性能
