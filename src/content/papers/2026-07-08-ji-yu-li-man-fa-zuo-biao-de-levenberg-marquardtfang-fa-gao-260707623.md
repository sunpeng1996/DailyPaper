---
title: Higher-Order Geometric Updates for Levenberg-Marquardt Method via Riemann Normal
  Coordinates
title_zh: 基于黎曼法坐标的Levenberg-Marquardt方法高阶几何更新
authors:
- Jianing Liu
- Dong H. Zhang
affiliations:
- 中国科学技术大学
- 中国科学院大连化学物理研究所
- 中国科学院大学
- 合肥国家实验室
arxiv_id: '2607.07623'
url: https://arxiv.org/abs/2607.07623
pdf_url: https://arxiv.org/pdf/2607.07623
published: '2026-07-08'
collected: '2026-07-09'
category: Training
direction: 非线性最小二乘优化器性能改进
tags:
- Optimization
- Levenberg-Marquardt
- Riemannian-Geometry
- Nonlinear-Least-Squares
- PINN
one_liner: 提出基于黎曼法坐标的RNC-LM优化器，大幅提升非线性最小二乘任务收敛效率与鲁棒性
practical_value: '- 推荐/广告场景CTR/CVR模型、召回向量的非线性最小二乘拟合任务可替换原有LM优化器，提升曲形损失谷、秩亏场景下的收敛鲁棒性

  - 训练PINN约束的电商销量预测、库存仿真模型时，采用RNC-LM可大幅降低预测误差，避免输出物理无意义的异常结果

  - 大规模模型小批量微调场景可复用RNC-LM的加速逻辑，相比标准LM最高可获34倍训练速度提升，计算开销接近原生LM'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
非线性最小二乘是回归、PINN等任务的核心优化问题，传统LM方法仅在参数空间做切空间直线更新，二阶测地线加速仅能在无限小步长下消除参数效应曲率，有限步长下几何一致性差，收敛效率与鲁棒性不足。
### 方法关键点
提出RNC-LM优化器，重构测地线方程将二阶测地线加速扩展到任意阶校正，构建具备更高重参数一致性的有限步更新；沿RNC曲线做线搜索控制步长，计算开销与标准LM接近；逐阶消除移动切向框架下残差加速度的切向分量，让实际目标下降更贴合LM的线性模型预测。
### 关键结果
经典非线性最小二乘基准上，大幅提升曲谷、秩亏问题的收敛性与鲁棒性；反应扩散PINN基准上相对L2误差降至1e-3量级，输出符合物理意义的解；大规模势能面拟合任务上相对标准LM实现34倍加速。
