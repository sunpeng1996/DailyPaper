---
title: Ranking-Preserving Coreset Selection for Efficient Evolutionary Hyperparameter
  Optimization
title_zh: 面向高效进化超参数优化的排序保持核心集选择方法
authors:
- Mamoona Tasadduq
- Maryam Bashir
affiliations:
- National University of Computer and Emerging Sciences (FAST-NUCES)
arxiv_id: '2611.27959'
url: https://arxiv.org/abs/2611.27959
pdf_url: https://arxiv.org/pdf/2611.27959
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: 进化HPO加速 · 排序保持核心集选择
tags:
- Hyperparameter Optimization
- Coreset Selection
- Evolutionary Algorithm
- Training Efficiency
- Ranking Preservation
one_liner: 提出排序保持核心集选择框架，大幅降低进化类超参数优化的计算成本
practical_value: '- 推荐/广告排序模型大规模调参时，可复用排序保持核心集思路，用小核心集替代全量数据跑HPO，大幅降低调参算力成本

  - 构建核心集时优先对齐超参配置的相对排序，比单纯随机采样/保精度的核心集更适配调参场景，可直接嵌入现有HPO pipeline

  - 同类型模型需多次跑HPO的业务场景（如多行业垂类模型调参），可一次构建核心集多次复用，摊销一次性构建成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
大规模数据集下进化类HPO需反复在全量数据上训练候选配置，计算成本过高，现有核心集选择方法多聚焦保留模型预测精度，无法保证超参配置的相对排序一致性，不适配调参场景。
### 方法关键点
1. 提出排序保持核心集（RPC）选择框架，将核心集构建建模为进化优化问题，目标为最大化全量数据与子集下超参配置的Spearman秩相关系数，同时惩罚子集大小；
2. 生成的核心集可直接适配GA、CHC、PSO三类主流进化HPO算法。
### 关键结果
11个基准数据集（7表格+2文本+2图像）测试：HPO阶段提速1.14x~8.80x，测试精度与全量数据HPO持平；8/11数据集上RPC的超参排序相关性优于同规模随机采样（Wilcoxon检验p=0.014）；核心集一次性构建成本可通过多次复用摊销。
