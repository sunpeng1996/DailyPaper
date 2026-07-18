---
title: Sharp Stability Threshold and Certification for Designing Stable Residual Architectures
title_zh: 面向稳定残差架构设计的锐化稳定性阈值与验证方法
authors:
- Hyemin Gu
- Michael Tyrrell
- Tuhin Sahai
- Markos A. Katsoulakis
affiliations:
- University of Massachusetts Amherst
- SRI International
arxiv_id: '2607.14576'
url: https://arxiv.org/abs/2607.14576
pdf_url: https://arxiv.org/pdf/2607.14576
published: '2026-07-16'
collected: '2026-07-18'
category: Training
direction: 模型训练 · 残差架构稳定性优化
tags:
- Residual Network
- Training Stability
- Mamba
- Architecture Design
- Stability Certification
one_liner: 提出残差块次线性增长原则，给出q≤1稳定训练充要条件，可高效验证残差架构稳定性
practical_value: '- 优化Mamba、Transformer等序列模型训练稳定性时，可优先校验残差块输入量级指数q是否≤1，替代盲目叠加Norm层的试错方案

  - 自定义用户行为序列建模残差块、Agent记忆模块架构时，可复用论文给出的基础运算q指数运算法则，快速验证稳定性，降低架构迭代成本

  - 端侧轻量推荐/Agent模型部署时，可通过调整残差块将q控制在≤1，去掉冗余Norm层降低推理延迟，同时保证训练收敛性'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
当前残差架构稳定性依赖人工试错添加Norm层，缺乏统一量化判定准则，Mamba等新型序列结构易出现训练发散问题。
### 方法关键点
1. 提出次线性增长原则，定义残差块速度场输入量级指数q，证明q≤1是训练稳定的充要条件，q>1时训练最优解必然发散
2. 给出5种残差块基础运算下的q指数运算法则，可直接在架构原语层面完成稳定性验证，无需训练试错
3. 设计无参数修改方案将原生Mamba块的q从5降至1，无需Norm层即可实现稳定训练
### 关键结果
Mamba、PatchTST的q≤1变种均实现稳定训练，验证稳定性仅由q值决定，与是否存在Norm层无关
