---
title: 'CoRA-NAS: Coarse Ranking and Anchor-Residual Refinement for Neural Architecture
  Search'
title_zh: CoRA-NAS：基于粗排序与锚点残差精炼的神经网络结构搜索方法
authors:
- Yifan Yang
- Zhaoyan Wang
- Zheng Gao
- Xiaoyu Li
- Jiaojiao Jiang
affiliations:
- University of New South Wales
- Korea Advanced Institute of Science and Technology
arxiv_id: '2609.11884'
url: https://arxiv.org/abs/2609.11884
pdf_url: https://arxiv.org/pdf/2609.11884
published: '2026-09-10'
collected: '2026-09-12'
category: Training
direction: 神经网络结构搜索 · 低算力架构选型
tags:
- Neural Architecture Search
- Zero-Cost Proxy
- Low Training Cost
- Model Selection
- Robust Ranking
one_liner: 提出无全训标注的两阶段NAS框架，跨空间鲁棒性最优，仅消耗1%全训练成本
practical_value: '- 低算力下模型选型可参考「零成本静态先验+少量训练动态残差修正」两阶段框架，大幅降低候选模型排序的算力开销

  - 多个弱排序信号融合可采用等权对数秩共识策略，无需标注就能适配不同业务场景，避免单指标排序的鲁棒性问题

  - 少量训练步长的学习曲线外推+残差校正思路，可复用到推荐模型超参搜索场景，降低调参算力成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
零成本proxy的NAS排序可靠性在不同搜索空间波动大，单proxy效果甚至不如参数量/FLOPs朴素基线，全训候选架构的成本过高难以落地。
### 方法关键点
1. 两阶段无标注框架，仅需适配空间专属架构编码，无需全训精度标签训练排序器
2. 第一阶段粗排序：聚合容量与初始化结构proxy，通过等权对数秩共识和无目标共识门生成稳定粗排序结果
3. 第二阶段精炼：采样粗排序锚点架构，用约1%全训成本拟合早期验证曲线，通过ExtraTrees模型传播残差校正粗排序
### 关键结果数字
跨4个基准测试集Spearman相关系数分别为0.946、0.715、0.786、0.894，最低值0.715为所有对比方法最高；NAS-Bench-201/CIFAR-100上选出的架构精度73.32%，接近真值最优的73.37%
