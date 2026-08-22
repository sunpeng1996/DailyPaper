---
title: Finite-Horizon Input-Output Dynamics of Minibatch Perturbations in AdamW
title_zh: AdamW中微批次扰动的有限时域输入输出动态特性研究
authors:
- Kang Liu
- Suyan Li
affiliations:
- 西安交通大学未来技术学院
- 新加坡国立大学电气与计算机工程系
arxiv_id: '2608.19762'
url: https://arxiv.org/abs/2608.19762
pdf_url: https://arxiv.org/pdf/2608.19762
published: '2026-08-20'
collected: '2026-08-22'
category: Training
direction: 深度学习训练 · AdamW优化器动态分析
tags:
- AdamW
- Training Dynamics
- Optimization
- Gradient Perturbation
- Model Training
one_liner: 将AdamW建模为有限时域ISO系统，量化单微批次扰动对训练损失的延迟效应
practical_value: '- 训练推荐/搜索/广告大模型时可借鉴该扰动分析方法定位loss spike来源，尤其是AdamW优化器导致的延迟异常波动

  - 可基于ISO响应算子设计梯度扰动检测逻辑，在训练过程中提前拦截会引发后续loss恶化的异常微批次

  - 多步误差分解结论可用于优化LoRA微调策略，针对性调整梯度裁剪阈值适配AdamW的梯度记忆效应'
score: 5
source: arxiv-stat.ML
depth: abstract
---

### 动机
AdamW存储历史梯度的一二阶矩信息，单微批次的影响不会局限于当前更新步，会产生延迟效应，现有研究缺乏对该效应的量化建模，难以定位训练过程中loss spike等不稳定问题的根源。
### 方法关键点
1. 构造仅单步梯度更新存在差异、后续训练序列完全一致的配对轨迹，隔离单微批次扰动的延迟影响；
2. 将AdamW建模为状态包含模型参数、一二阶矩估计的有限时域输入-状态-输出（ISO）系统，通过联合动态线性化得到符号响应算子，可映射局部梯度扰动对未来损失的影响；
3. 推导精确多步误差分解，证明局部平滑和激活切换受控条件下的一阶有限时域精度。
### 关键结果
实验验证了优化器状态引发的延迟响应机制，ISO近似可部分恢复扰动延迟影响的预期结构，显著提升训练波动的可解释性。
