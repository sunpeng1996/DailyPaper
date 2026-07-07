---
title: Hierarchical Variational Kalman Filtering
title_zh: 分层变分卡尔曼滤波算法
authors:
- Shilei Li
- Dawei Shi
- Wei Zheng
- Ling Shi
affiliations:
- Beijing Institute of Technology
- Shenzhen Youjia Innovation Technology Co., Ltd.
- The Hong Kong University of Science and Technology
arxiv_id: '2607.00877'
url: https://arxiv.org/abs/2607.00877
pdf_url: https://arxiv.org/pdf/2607.00877
published: '2026-07-01'
collected: '2026-07-07'
category: Other
direction: 动态系统状态估计 · 卡尔曼滤波优化
tags:
- Kalman Filtering
- Variational Inference
- CAVI
- State Estimation
- Maximum A Posteriori
one_liner: 提出引入过程噪声无关代理变量并重构CAVI为边际MAP问题，提升未知噪声场景下卡尔曼滤波的收敛速度与估计精度
practical_value: '- 可借鉴单步超参数拟合替代多轮CAVI迭代的设计，优化用户实时兴趣漂移估计模块的推理延迟，适配高吞吐在线推荐场景

  - 可复用显式过程噪声统计建模方法，优化电商实时流量、转化等时序特征的漂移检测精度，降低噪声干扰

  - 滑动窗口超参数估计逻辑可直接迁移至多模态时序特征融合的状态估计任务，提升特征时序建模稳定性'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统未知噪声统计的变分卡尔曼滤波存在过程协方差估计不一致、收敛速度慢的问题，限制了其在高实时性动态系统中的落地价值。
### 方法关键点
1. 引入表征无过程噪声状态的代理变量，实现过程噪声统计的显式建模与推理；
2. 将传统坐标上升变分推理(CAVI)重构为边际最大后验(MAP)问题，仅需单步超参数拟合，免去CAVI固有多轮内迭代开销，解耦协方差跟踪滤波器的设计；
3. 支持部署高阶协方差跟踪滤波器、实现滑动窗口超参数估计，当窗口覆盖全量历史数据时，协方差跟踪估计器天然可作为零相位滤波器使用。
### 关键结果
数值仿真验证，该方法相比现有方案收敛速度显著提升，估计精度表现更优。
