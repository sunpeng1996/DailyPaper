---
title: Hierarchical and Permutation-Invariant Feature Transformation Learning via
  Policy-Guided Embedding Search
title_zh: 基于策略引导嵌入搜索的分层置换不变特征变换学习方法
authors:
- Rui Liu
- Tao Zhe
- Yanyong Huang
- Sankha Narayan Guria
- Xiao Luo
- Wei Fan
- Yanjie Fu
- Dongjie Wang
affiliations:
- University of Kansas
- Southwest University of Finance and Economics
- University of Wisconsin–Madison
- University of Auckland
- Arizona State University
arxiv_id: '2609.10225'
url: https://arxiv.org/abs/2609.10225
pdf_url: https://arxiv.org/pdf/2609.10225
published: '2026-09-09'
collected: '2026-09-10'
category: Training
direction: 特征变换 · RL引导嵌入搜索优化
tags:
- Feature Transformation
- Reinforcement Learning
- Permutation Invariance
- Embedding Search
- Tabular Learning
one_liner: 提出融合分层置换不变模块与策略引导RL的特征变换框架，解决现有生成式方法三类核心缺陷
practical_value: '- 电商/广告CTR/CVR预估的特征工程环节可复用置换不变分层模块，解决特征组合顺序敏感导致的embedding偏移问题，提升模型预估稳定性

  - 多目标RL引导的嵌入搜索策略可直接迁移到特征组合探索场景，从经验强种子初始化能大幅降低非凸空间搜索成本，兼顾效果与运算效率

  - 自注意力池化映射语义等价结构到一致embedding的思路，可用于用户行为序列/物品属性组合的特征编码，减少冗余特征计算开销'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有生成式特征变换方法将变换知识编码到连续嵌入空间以提升候选策略探索效率，但存在三大核心局限：1）忽略低层特征、操作与高层抽象的层级关系；2）对天然置换不变的变换序列强制使用顺序敏感embedding，引入系统偏差；3）依赖梯度搜索不适配非凸变换空间。
### 方法关键点
提出双组件框架：1）置换不变分层模块捕捉跨特征、操作、抽象层的交互，通过自注意力池化将语义等价结构映射到与下游性能对齐的一致embedding；2）策略引导多目标强化学习策略，从经验强种子初始化搜索，联合优化预测精度与变换效率。
### 关键结果
在多个公开tabular基准数据集上实验，效果与鲁棒性均显著优于各类SOTA基线，代码已开源。
