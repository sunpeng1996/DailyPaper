---
title: Geometric Mean Pooling for Equal-Weight Multiplicative Coarse-Graining
title_zh: 面向等权乘法粗粒度聚合的几何均值池化算子设计
authors:
- Ang-Kun Wu
- Fangdi Wen
- Jingtao Zhang
affiliations:
- University of Tennessee, Knoxville
- Rutgers University
- Google
arxiv_id: '2609.21876'
url: https://arxiv.org/abs/2609.21876
pdf_url: https://arxiv.org/pdf/2609.21876
published: '2026-09-18'
collected: '2026-09-21'
category: Training
direction: 深度学习基础算子 · 池化优化
tags:
- Pooling
- Geometric Mean
- Feature Aggregation
- Inductive Bias
- CNN
one_liner: 提出无参数带符号几何均值池化GMP，缓解平均/最大池化的加性与极值偏差，适配乘法特征组合场景
practical_value: '- 在用户行为序列特征聚合场景，若特征为乘法相关（如点击率×转化率类复合信号），可替换平均/最大池化测试GMP效果，无额外参数开销

  - 面对带乘性噪声的输入特征（如埋点噪声、异构数据源对齐偏差），可尝试GMP提升特征聚合的鲁棒性

  - 无需盲目替换现有池化，仅在特征符合等权乘法组合假设的子任务（如多模态特征融合、多渠道转化信号聚合）中做AB验证即可'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
平均池化存在加性偏差、最大池化存在极值偏差，现有池化算子大多无法适配乘法特征组合场景，部分改进方案引入额外可学习参数抬高训练成本。

### 方法关键点
提出无参数带符号几何均值池化（GMP），将特征符号的乘积与特征幅值的几何均值结合，灵感来自量子多体物理的局部到全局组合规则；非重叠分层GMP可保留全局乘法统计信息，无额外训练参数。

### 关键结果
合成序列任务上，GMP恢复乘积类信号的准确率显著高于平均/最大池化，在测试的乘性输入噪声水平下可稳定保持预测性能；但在图像、分子回归任务上效果依赖特征表示、目标参数化及池化放置位置，仅为乘法组合场景的补充归纳偏置，而非通用池化替换方案。
