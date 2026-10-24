---
title: Direct Inference on Admissible Sets (Diona)
title_zh: 《可容许集直接推理（Diona）：免全局训练的轻量回归算法》
authors:
- Lorenzo Sabug
- Eric Kerrigan
affiliations:
- Imperial College London
arxiv_id: '2610.31526'
url: https://arxiv.org/abs/2610.31526
pdf_url: https://arxiv.org/pdf/2610.31526
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 轻量回归算法 · 免全局训练 不确定性量化
tags:
- regression
- uncertainty-quantification
- low-latency
- training-free
- local-optimization
one_liner: 提出无需全局训练的Diona回归方法，兼具不确定性估计与数据集更新后极低延迟特性
practical_value: '- 电商实时推荐/广告冷启场景（如小众类目排序）可参考Diona思路，跳过全局重训，大幅降低样本更新后的首预测延迟

  - 推荐系统E&E流量分配等需要不确定性估计的场景，可复用Diona的可容许边界构造逻辑，替代GP降低计算开销

  - Agent实时用户偏好预估等数据更新频繁、单轮预测量小的任务，可借鉴局部求解替代全局训练的架构设计'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统回归方法如GP、神经网络依赖全局训练，数据集更新后重训成本高、首预测延迟大，且多数神经网络不支持不确定性量化，无法适配低延迟、高更新频率的回归场景。
### 方法关键点
将查询点、邻域样本的数值与导数作为约束优化问题的隐变量，把全局长周期训练替换为按需局部求解，无需预训练即可同时输出预测值与可容许置信边界。
### 关键结果
1. 3~8维无噪非线性回归任务上精度优于GP，数据密度越高优势越显著；
2. 4类测试函数的置信区间真值覆盖率超95%，达到GP同等水平；
3. 数据集更新后首预测延迟比GP低3~4个数量级，比无不确定性估计的高精度NN低2~3个数量级，仅适用于更新间隔内预测请求较少的场景。
