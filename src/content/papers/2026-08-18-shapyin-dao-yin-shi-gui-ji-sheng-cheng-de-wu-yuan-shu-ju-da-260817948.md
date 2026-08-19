---
title: 'SIGMA: SHAP-Guided Implicit-Trajectory Generation for Metadata-Free LLM-Based
  AutoFE'
title_zh: SHAP引导隐式轨迹生成的无元数据大模型自动化特征工程
authors:
- Xuan Zheng
- Kento Uchida
- Shinichi Shirakawa
affiliations:
- Yokohama National University
arxiv_id: '2608.17948'
url: https://arxiv.org/abs/2608.17948
pdf_url: https://arxiv.org/pdf/2608.17948
published: '2026-08-18'
collected: '2026-08-19'
category: Training
direction: 大模型自动化特征工程 · 无元数据优化
tags:
- AutoFE
- SHAP
- LLM
- Implicit Trajectory
- Tabular Data
one_liner: 提出无元数据依赖的SHAP引导隐式轨迹大模型AutoFE框架，恒定prompt下性能追平SOTA
practical_value: '- 电商/推荐场景的隐私合规特征挖掘可复用SHAP分组方案，无需特征语义元数据即可完成特征交互迭代，适配用户敏感数据、匿名业务数据的特征优化需求

  - EXIT隐式轨迹机制可直接迁移到长周期LLM生成任务（如生成式推荐prompt优化、广告文案迭代），避免上下文窗口溢出的同时将生成重复率从37%降至6.8%

  - 小样本表场景优先用小尺寸LLM做AutoFE，大模型容易过拟合验证集；大样本场景可选用代码能力强的MoE模型提升生成准确率

  - 特征生成的组内深挖+跨组融合策略可直接复用在推荐排序的特征交互挖掘流程，平衡高重要特征增益与弱信号挖掘效率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM驱动的AutoFE依赖特征语义元数据，隐私受限场景（如电商用户敏感特征、金融风控数据）无法落地；同时迭代过程中显式记录轨迹会持续膨胀prompt长度，容易溢出上下文窗口，无轨迹又会导致生成重复率高、易陷入局部最优，亟需轻量无语义依赖的优化方案。

### 方法关键点
- 引入SHAP值做特征重要性打分，新增高斯噪声特征作为阈值，将特征划分为top/ useful/ weak三组，无需语义元数据即可给LLM提供任务感知的生成引导
- 每轮要求LLM生成1个组内特征（深挖同组特征交互）+1个跨组特征（强弱特征融合提效），仅保留增益最高的特征加入特征集
- 提出EXIT隐式轨迹机制：每轮使用过的特征按重要性设置2/4/8步的屏蔽期，无需在prompt中显式记录历史轨迹，仅通过动态调整暴露的特征集合隐式传递历史信息，同时跟踪失败操作屏蔽高频无效操作

### 关键实验
在16个公开表分类数据集上对比，LLM基线选CAAFE、OCTree，传统AutoFE基线选DFS、OpenFE、AutoFeat，核心结果：
1. 性能和语义依赖的SOTA CAAFE持平，平均F1 79.80%，排名2.06优于所有LLM基线
2. prompt长度全程恒定在1739token，峰值仅为CAAFE的1/9，支持长周期迭代
3. 生成特征重复率从37.2%降到6.8%，平均仅需5.4个有效特征即可追平传统AutoFE用数百个特征达到的性能，特征利用率提升超130倍

### 核心结论
LLM生成类迭代任务不一定需要显式记录历史轨迹，通过动态调整输入空间的可访问范围即可隐式传递迭代信息，同时大幅降低上下文开销
