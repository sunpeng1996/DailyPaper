---
title: Distributionally Faithful Imputation via Positive Semi-Definite Kernel Density
  Estimation
title_zh: 基于半正定核密度估计的分布保真缺失值插补方法
authors:
- Andrea Basteri
- Carlo Ciliberto
- Alessandro Rudi
affiliations:
- Inria - Ecole Normale Supériore
- Department of Computer Science - UCL
- SDA Bocconi School of Management
arxiv_id: '2607.07767'
url: https://arxiv.org/abs/2607.07767
pdf_url: https://arxiv.org/pdf/2607.07767
published: '2026-07-08'
collected: '2026-07-11'
category: Other
direction: 缺失值插补 · 半正定核密度估计
tags:
- Missing Value Imputation
- Kernel Density Estimation
- Convex Optimization
- Data Preprocessing
- Statistical Consistency
one_liner: 提出基于半正定核密度估计的分布一致性插补方法，MCAR场景下分布准确性优于主流基线
practical_value: '- 电商推荐场景下用户/商品特征、行为序列的MCAR类缺失可直接复用PSD-Impute插补，保留原始数据分布特征避免下游建模偏差

  - 需生成多组插补结果做不确定性评估的任务（如A/B测试样本预处理）可直接调用其多插补能力，无需多次训练模型

  - 高维稀疏特征插补场景可参考其规避维度灾难的核密度估计设计，替换原有均值/众数等启发式插补提升数据质量'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有缺失值插补方法多依赖启发式规则或强参数假设，未对齐原始数据联合分布，易给下游建模任务引入偏差，完全随机缺失（MCAR）场景下缺乏分布保真的高性能插补方案。
### 方法关键点
将MCAR下的插补转化为掩码观测的密度估计问题，要求估计分布的观测边际与原始数据完全匹配；基于半正定核密度构造凸经验风险问题，边际有闭式解，可通过牛顿内点法高效求解；拟合后的PSD-Impute模型同时支持单值/多值插补，具备统计一致性，自适应超额风险收敛速度快，可规避高维场景下的维度灾难。
### 关键结果
在1个合成数据集、11个真实数据集上测试，分布准确性显著优于均值填充、生成式插补等主流基线，具备落地可行性。
