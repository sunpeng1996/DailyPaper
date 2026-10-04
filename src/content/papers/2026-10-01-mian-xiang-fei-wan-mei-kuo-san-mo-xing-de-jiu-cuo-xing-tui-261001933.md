---
title: Error-Corrected Inference-Time Scaling for Imperfect Diffusion Models
title_zh: 面向非完美扩散模型的纠错型推理时缩放方法
authors:
- Zuokai Wen
- Louis Grenioux
- Weinan E
- Jiequn Han
affiliations:
- Shanghai Jiao Tong University
- Flatiron Institute
- Peking University
arxiv_id: '2610.01933'
url: https://arxiv.org/abs/2610.01933
pdf_url: https://arxiv.org/pdf/2610.01933
published: '2026-10-01'
collected: '2026-10-04'
category: Other
direction: 扩散模型推理优化 · 采样误差校正
tags:
- Diffusion Model
- Inference Optimization
- Sampling Correction
- Energy-based Model
- Monte Carlo
one_liner: 提出基于能量的Feynman-Kac校正框架，无需额外训练即可修正非完美扩散模型的推理采样误差
practical_value: '- 若使用扩散模型做生成式推荐场景（如商品图、个性化文案生成），可直接复用该推理校正方法，无需重训即可降低预训练模型采样误差，提升生成质量

  - 针对小样本训练的预训练扩散模型固有偏差问题，可借鉴渐进式引入目标能量偏差修正的思路，解决生成结果与业务目标不匹配问题

  - 做生成类任务推理优化时，可复用带方差控制引导的序列蒙特卡洛近似方法，平衡采样效率与生成准确率'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有扩散模型推理时缩放方法默认预训练模型完全精确，实际场景中数据、训练限制会导致模型存在固有缺陷，增加采样粒子仅能降低蒙特卡洛误差，无法消除生成端点与目标不匹配、概率路径跟踪误差问题。
### 方法关键点
提出基于能量的Feynman-Kac校正器（EBFKC）框架：1）推导连续时间群体极限下可精确跟踪预设路径的Feynman-Kac动力学，通过带方差控制引导的序列蒙特卡洛近似实现；2）将预训练能量作为扩散路径代理，渐进融合学习与目标终端能量的偏差，消除端点不匹配，全程无需额外训练。
### 关键结果
在高斯混合模型、粒子系统、丙氨酸二肽/四肽实验中，采样分布匹配度、分子自由能曲线拟合度远优于标准基线，基线存在的显著采样误差基本被消除。
