---
title: Numerical Integration on Bounded Domains via Learned Reflected Diffusions
title_zh: 基于学习反射扩散的有界域数值积分方法
authors:
- Kirill Korolev
- Artur Goldman
- Timofei Gritsaev
- Tigran Ramazyan
- Nikita Morozov
affiliations:
- HSE University
- ETH Zürich
- Constructor University
arxiv_id: '2610.40499'
url: https://arxiv.org/abs/2610.40499
pdf_url: https://arxiv.org/pdf/2610.40499
published: '2026-10-29'
collected: '2026-11-01'
category: Other
direction: 高维数值积分 · 扩散采样优化
tags:
- Diffusion Model
- Numerical Integration
- Importance Sampling
- Score Matching
- REINFORCE
one_liner: 提出基于学习反射扩散的有界域高维积分方法，解决传统采样不满足约束、非光滑被积函数梯度失效问题
practical_value: '- 生成式推荐中需要生成满足价格、品类、库存等硬约束的商品时，可借鉴反射扩散思路保证生成结果落在合法域内，无需额外后处理过滤

  - 非光滑目标（如电商场景下带截断的收益函数、广告竞价的阶梯式扣费函数）的梯度估计场景，可复用反射前高斯分布的REINFORCE梯度估计技巧，避免求导失效

  - 高维积分类业务需求（如用户期望LTV预估、多变量因果效应计算、策略预期收益估计），该方法相比传统蒙特卡洛有更好的维度扩展性，采样效率更高'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
高维有界凸域积分是多领域计算瓶颈，传统准蒙特卡洛无法根据被积函数的分布自适应调整采样点，现有基于扩散的采样方法仅支持全空间采样，无法满足域约束，且非光滑被积函数下重参数化梯度容易失效或无意义。
### 方法关键点
1. 构建天然保持在约束域内的反射扩散过程，正向将目标分布逐步转换为域上均匀分布，训练神经得分模型反转该过程得到适配被积函数的提议分布；
2. 基于反射扩散的测度变换公式推导无额外边界项的训练目标，以及积分值的无偏重要性采样估计器；
3. 非光滑场景下，基于反射前的高斯提议密度推导REINFORCE梯度估计器，无需计算反射转移密度或对被积函数求导。
### 关键结果
在多个合成任务与真实场景验证性能超越基线方法，随问题维度、蒙特卡洛采样点数量的扩展表现优异。
