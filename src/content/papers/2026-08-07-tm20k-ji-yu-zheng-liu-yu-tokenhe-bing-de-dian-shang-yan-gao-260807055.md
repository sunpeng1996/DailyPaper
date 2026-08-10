---
title: 'Teacher Retains Full Tokens, Student Merges Efficiently: TM20K for E-Commerce
  Sequence Modeling in Ad Recommendation'
title_zh: TM20K：基于蒸馏与Token合并的电商广告20K超长序列建模
authors:
- Xinchun Li
- Duoru Zheng
- Wenlin Zhao
- Ziyi Zhou
- Jingxuan Tan
- Huizhi Yang
- Linlan Chen
- Dongjian Wang
- Dongyue Wang
- Xiaosong Li
affiliations:
- ByteDance
arxiv_id: '2608.07055'
url: https://arxiv.org/abs/2608.07055
pdf_url: https://arxiv.org/pdf/2608.07055
published: '2026-08-07'
collected: '2026-08-10'
category: RecSys
direction: 推荐系统 · 超长用户行为序列建模
tags:
- Long Sequence Modeling
- Knowledge Distillation
- Token Merging
- CTR Prediction
- Recommender System
one_liner: 通过教师蒸馏加三类Token合并策略实现20K超长序列建模，电商广告ADSS提1.036%、延迟仅增5.6%
practical_value: '- 可直接复用三类Token合并策略：按ID局部合并、按位置自适应合并、按层金字塔合并，工程实现简单，性能损失可控，适配电商场景下用户重复交互多、近期行为权重高的特点

  - 可参考长序列落地的蒸馏范式：教师仅离线训练一次不在线部署，成本可被大规模业务摊薄，学生能复用约85%的教师性能增益，几乎不增加在线serving开销

  - 工程优化点可直接落地：CPU侧合并原始特征而非Embedding降低CPU-GPU带宽消耗，Stack Sequence重排Batch内有效Token降低10GB左右的GPU显存占用，QK
  Norm解决长序列+蒸馏的训练发散问题'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商广告推荐中，超长用户行为序列可同时捕捉长短期兴趣提升效果，但序列长度从5K扩展到20K时，训练时间增长3.5×、GPU显存多占49G、推理延迟升高6.3×，现有压缩/轻量注意力方案要么丢失细粒度信息，要么序列建模能力不足，亟需兼顾效果与效率的落地方案。

### 方法关键点
- 序列建模选用全注意力（FA）而非目标注意力（TA），实验证明20K序列下FA AUC较TA高0.25%，可充分捕捉序列内依赖关系
- 两阶段知识蒸馏框架：仅训练一次的教师模型使用完整20K无压缩序列，不做在线部署；学生模型通过三类Token合并策略压缩序列，同时蒸馏教师预测logits补全性能
- 三类低开销Token合并策略：① LITM：短窗口内同商品ID的交互合并，去噪同时降长度；② PATM：按位置自适应压缩，近期行为少压缩、历史行为高比例压缩；③ LPTM：Transformer上层采用更大压缩力度，匹配上层注意力更集中的分布规律
- 工程优化：CPU侧合并原始特征而非Embedding降低跨设备带宽，Stack Sequence重排Batch内有效Token减少显存浪费，QK Norm解决长序列+蒸馏的训练不稳定问题

### 关键结果
在字节十亿级电商广告CVR数据集上，对比STCA、LONGER等SOTA长序列方案：教师模型AUC较5K基线高0.26%但吞吐量仅11K；学生模型单独用Token合并后平均序列长度压缩至1.8K，吞吐量达83K（接近5K基线的88K），AUC高0.15%；加蒸馏后AUC高0.22%，恢复教师85%的性能增益。线上A/B测试ADSS提升1.036%，推理延迟仅增5.6%

### 核心结论
超长序列落地不需要追求端到端部署大模型，「一次性重训教师+轻量化学生蒸馏+规则引导的Token合并」范式，可在极低 overhead 下拿到绝大部分长序列的业务收益
