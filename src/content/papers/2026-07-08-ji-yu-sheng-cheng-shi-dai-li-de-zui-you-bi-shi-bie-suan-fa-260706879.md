---
title: Best-Arm Identification with Generative Proxy
title_zh: 基于生成式代理的最优臂识别算法
authors:
- Tianyi Ma
- Hanzhang Qin
- Ruihao Zhu
- Jierui Zuo
affiliations:
- School of Operations Research and Information Engineering, Cornell University
- Department of Industrial Systems Engineering and Management, National University
  of Singapore
- SC Johnson College of Business, Cornell University
- Michael G. Foster School of Business, University of Washington
arxiv_id: '2607.06879'
url: https://arxiv.org/abs/2607.06879
pdf_url: https://arxiv.org/pdf/2607.06879
published: '2026-07-08'
collected: '2026-07-09'
category: Other
direction: 在线学习 · 最优臂识别样本效率优化
tags:
- Best-Arm-Identification
- Online-Learning
- Control-Variates
- Sample-Efficiency
- PAC-Learning
one_liner: 提出PROBE分阶段消除算法，利用低成本生成代理得分降低最优臂识别所需高成本真实样本量
practical_value: '- 电商广告出价、选品冷启动等高成本试错场景，可引入LLM/离线ML输出的低成本代理得分，用控制变量法降低真实采样量

  - 做在线探索时，不要直接用离线估计的残差方差作为采样阈值，可复用PROBE的上界证书方法保证PAC正确性，避免过度乐观导致效果损失

  - 无需提前离线校准代理得分与真实奖励的相关系数，算法可在线自适应学习，降低落地时的离线预处理成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
最优臂识别是数据驱动决策的经典模型，但真实奖励采样成本极高（如电商定价试错、广告投放效果观测），现有LLM/ML模型可生成低成本、与真实奖励相关的代理得分，如何利用这类代理降低采样成本是核心痛点，且代理与真实奖励的相关系数通常未知，离线估计误差会影响识别正确性。
### 方法关键点
1. 用控制变量调整将代理得分引入最优臂识别框架，将问题转化为异方差识别问题，理论上样本复杂度可按1-ρ²（ρ为代理与真实奖励的相关系数）比例降低
2. 提出PROBE分阶段消除算法，用普通最小二乘拟合直接维护残差方差的上界证书，基于卡方分布保证证书有效性，无需提前已知相关系数
### 关键结果
- 理论证明PROBE满足δ-PAC保证，采样复杂度与已知相关系数的最优Oracle仅差常数乘子和固定校准成本
- 车贷定价仿真实验中，采样节省比例与代理-奖励相关系数正相关，当ρ=0.9时采样量可降低约80%
