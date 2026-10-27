---
title: 'Selective Tie Learning: Mitigating Spurious Correlations in Preference Optimization'
title_zh: 选择性Tie学习：缓解偏好优化中的伪相关问题
authors:
- Christian Moya
- Purav Matlia
- Elliott Thornley
- Guang Lin
affiliations:
- Purdue University
- National University of Singapore
arxiv_id: '2610.35787'
url: https://arxiv.org/abs/2610.35787
pdf_url: https://arxiv.org/pdf/2610.35787
published: '2026-10-26'
collected: '2026-10-27'
category: Training
direction: LLM偏好优化 · 伪相关缓解
tags:
- Preference Optimization
- DPO
- RLHF
- Spurious Correlation
- Data Selection
one_liner: 提出两类tie选择策略，仅用1/3的样本即可达到全量tie训练的伪相关缓解效果
practical_value: '- 做LLM对齐（DPO/RLHF）时无需全量加入中立tie样本，可先按绝对隐式奖励边际筛选topK，训练成本降低2/3的同时保持伪相关缓解效果不掉

  - 若算力允许计算二阶信息，可采用阻尼GGN近似的影响函数筛选tie，比随机采样tie的OOD准确率最高提升17.5pp

  - 电商排序/推荐模型的特征伪偏置缓解可复用该思路：构造核心效用一致、仅伪特征不同的样本对，选择性加入训练即可降低模型对伪特征的依赖，无需修改损失函数'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
DPO、RLHF等偏好优化方法易学习到训练数据中的伪相关（如回复长度、emoji数量和偏好的虚假关联），这类伪依赖会导致模型在分布偏移的部署场景下性能暴跌。现有tie训练方法通过加入核心效用一致、仅伪特征不同的中立对缓解伪相关，但全量加入会大幅提升训练成本，亟需高效的tie选择策略在保障效果的前提下降低训练开销。
### 方法关键点
- 理论推导每个tie对模型伪依赖的一阶影响，选择影响最大的topK tie是同规模子集下的一阶最优策略
- 提出轻量纯边际选择方案，仅需前向传播计算tie的隐式奖励差绝对值，在高斯假设下可最大化预期伪依赖降低效果
- 针对神经/大语言模型，用反事实能量作为伪依赖的代理指标，结合阻尼广义高斯牛顿（GGN）近似曲率，无需显式分解核心/伪特征即可计算tie的影响
### 关键结果
在对数线性模型、MLP、Llama-3.2-1B的酒店推荐、emoji安全任务上对比均匀tie选择（UTL）：纯边际选择仅用300个tie即可达到UTL用1000个tie的OOD准确率，最多比UTL高17.5个百分点，效果和基于影响的选择基本持平。
### 核心结论
偏好优化中缓解伪相关的tie样本无需全量加入训练，仅筛选隐式奖励边际最大的topK就能用1/3的训练成本达到全量tie的效果。
