---
title: 'ScAn-Bench: Evaluating Scaling Analysis Methodology'
title_zh: ScAn-Bench：大模型缩放分析方法评估基准
authors:
- Artin Sermaxhaj
- Nastaran Alipour
- Donat Sinani
- Johannes Hog
- Neeratyoy Mallik
- Jenia Jitsev
- Danny Stoll
affiliations:
- University of Freiburg
- Zuse School ELIZA
- Juelich Supercomputing Center
arxiv_id: '2609.35707'
url: https://arxiv.org/abs/2609.35707
pdf_url: https://arxiv.org/pdf/2609.35707
published: '2026-09-28'
collected: '2026-09-29'
category: Training
direction: 大模型训练 · 缩放规律评估基准
tags:
- Scaling Law
- Benchmark
- LLM
- VLM
- Surrogate Model
- Hyperparameter Optimization
one_liner: 构建LLM/VLM专属缩放分析代理基准，实现不同缩放方法的低成本可复现评估
practical_value: '- 训练业务专属LLM/VLM（如电商商品理解模型、多模态匹配模型）时，可直接复用文中对比的4种数据采集+3种外推策略组合，避免凭经验选缩放配置，降低试错成本

  - 计算资源有限的团队可参考文中TabPFN构建训练效果代理模型，用少量小尺度训练结果外推大尺度最优配置，节省GPU算力

  - 跨模态推荐、生成式推荐场景训练非标准架构模型时，优先选择无参数假设的Power-Law拟合做缩放外推，鲁棒性远高于Chinchilla参数法'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大模型训练成本极高，缩放分析（ScAn）是预测最优训练配置、降低成本的核心手段，但现有缩放方法的评估缺乏统一基准，不同模态、架构下的方法性能差异大，结论难以复现，甚至存在大量方法论偏差，亟需标准化的评估工具。

### 方法关键点
1. 构建两个代理基准ScAn-Bench-LLM和ScAn-Bench-VLM，分别基于4524个LLM（16M~1B参数量）、8024个VLM（2M~357M参数量）训练checkpoint构建，覆盖缩放参数、优化超参数的全搜索空间
2. 对比TabPFN、AutoGluon、XGB等多个代理模型，最终选择Spearman相关性最高的TabPFN作为默认预测器，单100次查询仅需17~29 CPU秒，比真实GPU训练快4个数量级以上
3. 统一将缩放分析拆解为数据采集、外推两个阶段，评估了Random Search、Chinchilla A1/A2、CARBS 4种采集策略，以及Kaplan幂律、Chinchilla参数拟合、Power-Law拟合3种外推方法

### 关键结果
1. 数据采集阶段存在明确的探索-利用权衡：CARBS早期收敛最快，但Iso-Parameter（Chinchilla A1）的空间覆盖度最高，Random Search在预算充足时表现最优
2. 外推阶段无通用最优组合：Chinchilla参数法在LLM下表现好，但在VLM下因架构假设失效预测失败，纯经验Power-Law拟合跨模态鲁棒性最高
3. 全参数外推场景下，Random Search采集数据的效果比CARBS好，0.5倍目标预算下即可将预测配置的损失接近最优值的90%

**最值得记住的一句话**：缩放规律的有效性高度依赖数据采集阶段对帕累托前沿的覆盖，盲目复用已有架构的缩放经验会带来极大的配置偏差
