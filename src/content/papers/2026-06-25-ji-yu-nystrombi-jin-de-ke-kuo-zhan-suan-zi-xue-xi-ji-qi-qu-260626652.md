---
title: Scalable Operator Learning via Nyström Approximation With Denoising Applications
title_zh: 基于Nyström逼近的可扩展算子学习及其去噪应用
authors:
- Naveen Gupta
- Vaibhav Silmana
- S. Sivananthan
affiliations:
- Pennsylvania State University
- Indian Institute of Technology Delhi
arxiv_id: '2606.26652'
url: https://arxiv.org/abs/2606.26652
pdf_url: https://arxiv.org/pdf/2606.26652
published: '2026-06-25'
collected: '2026-06-27'
category: Other
direction: 算子学习 · 核方法效率优化
tags:
- Kernel Methods
- Nyström Approximation
- Operator Learning
- Denoising
- Scalable Learning
one_liner: 提出基于Nyström子采样的可扩展算子学习算法，性能比肩全核方法同时大幅降低计算开销
practical_value: '- 推荐召回/排序模块的核方法特征建模环节，可引入Nyström子采样优化大核矩阵计算开销，适配亿级用户/商品规模数据集

  - 用户行为序列、商品图文/音视频内容信号去噪场景，可复用通用算子学习框架，无需针对特定噪声模型定制专属方案

  - 端侧推荐低资源推理场景，可借鉴该方法压缩核方法计算量，在精度损失可接受范围内大幅提升推理速度'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统核方法需构建、反转大型核矩阵，计算成本极高，无法适配大规模数据集；现有去噪方法多针对特定信号表征或噪声模型定制，通用性差。
### 方法关键点
1. 提出基于Nyström子采样的高效算子学习算法，支持函数输出
2. 在索引函数表征的通用源条件下（覆盖经典Hölder型和算子单调框架），证明估计器达到极小极大最优收敛率
3. 将去噪问题统一纳入通用算子学习框架，无需绑定特定噪声模型
### 关键结果
在信号去噪、实时音频去噪、图像去噪、逆Radon变换重建、能效预测等任务上，性能与全核方法持平，计算成本大幅降低。
