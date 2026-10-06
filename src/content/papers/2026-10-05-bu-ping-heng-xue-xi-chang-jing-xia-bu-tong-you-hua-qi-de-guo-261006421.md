---
title: On the Comparison of Optimizers for Imbalanced Learning
title_zh: 《不平衡学习场景下不同优化器的效果对比研究》
authors:
- Cl{é}ment Lezane
- Fran{\c c}ois Bachoc
- J{é}r{ô}me Bolte
- Jean-Michel Loubes
affiliations:
- Université de Toulouse
- Toulouse School of Economics
- ANITI
- University of Lille
- INRIA
arxiv_id: '2610.06421'
url: https://arxiv.org/abs/2610.06421
pdf_url: https://arxiv.org/pdf/2610.06421
published: '2026-10-05'
collected: '2026-10-06'
category: Training
direction: 深度学习训练 · 不平衡数据优化
tags:
- Optimizer
- Imbalanced Learning
- SGD
- AdamW
- Deep Learning
one_liner: 理论结合实验验证AdamW等优化器在隐式不平衡训练中对少数群体的拟合速度优于SGD
practical_value: '- 处理推荐场景长尾用户/小众商品这类隐式不平衡训练任务时，优先选择AdamW/Muon替代SGD，可加快少数群体特征的拟合速度，无需额外做样本重采样/重加权

  - 训练长尾分类、罕见行为预测模型时，不需要提前识别少数群体标签，仅通过更换优化器即可降低多数样本主导训练的偏差

  - 训练调参时，若模型对小众/稀有样本的拟合效果差，可先尝试更换优化器，再考虑调整采样策略，降低数据处理成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
机器学习任务普遍存在隐式数据不平衡问题（如推荐场景长尾商品/用户、语言模型罕见词），多数场景下少数群体标签不可观测，无法通过常规重采样/重加权方法缓解训练偏差，现有研究缺乏不同优化器在该场景下表现的系统性理论支撑。
### 方法关键点
基于连续时间的理想优化器几何模型模拟深度学习小步长训练流程，假设优化器仅能获取聚合训练损失、无法区分多数/少数群体的损失贡献，推导优化器跳出「仅优化多数群体损失」区域的时间边界公式，对比不同优化器的时间边界对少数群体振幅的依赖度。
### 关键结果
理论推导显示sign、谱下降、牛顿下降法跳出多数优先区域的时间对少数样本振幅的依赖度远低于欧式梯度下降；实验验证AdamW、Muon在语言、表格、图像三类不平衡任务上的少数样本拟合效果较SGD提升15%~42%，跳出多数主导训练区间的耗时降低65%以上。
