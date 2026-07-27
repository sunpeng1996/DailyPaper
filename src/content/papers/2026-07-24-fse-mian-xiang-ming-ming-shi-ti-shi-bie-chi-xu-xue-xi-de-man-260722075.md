---
title: 'FSE: Continual Learning for Named Entity Recognition by Fast-Slow Experts'
title_zh: FSE：面向命名实体识别持续学习的快慢专家方法
authors:
- Yunan Zhang
- Yang Fan
- Heng Li
- Xiangping Wu
- Qingcai Chen
affiliations:
- School of Computer Science and Technology, Harbin Institute of Technology, Shenzhen
arxiv_id: '2607.22075'
url: https://arxiv.org/abs/2607.22075
pdf_url: https://arxiv.org/pdf/2607.22075
published: '2026-07-24'
collected: '2026-07-27'
category: Other
direction: 持续学习 · 快慢专家架构命名实体识别
tags:
- Continual Learning
- Named Entity Recognition
- Expert Mixture
- Negative Sampling
- Catastrophic Forgetting
one_liner: 提出基于快慢双专家架构的持续学习NER方法，解决灾难性遗忘与跨任务信息利用不足问题
practical_value: '- 快慢双专家架构可复用至搜索推荐增量学习场景：用共享通用模块过滤低价值候选，任务专属模块做精细分类，同时兼顾抗遗忘与新任务适配性，降低全量重训成本

  - 长度衰减负采样策略可迁移至召回/排序等任务的样本不平衡优化：针对不同长度/粒度的候选样本动态调整负采样权重，提升训练效率与效果

  - 「跨任务知识共享+降低单任务学习负担」的设计思路，可直接用于多场景多目标广告推荐系统的增量训练，适配业务快速迭代需求'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
CLNER（命名实体识别持续学习）要求模型增量学习新实体类型且不遗忘旧知识，现有方案存在两大痛点：一是易出现灾难性遗忘，二是跨任务共享信息利用不充分，同时span式NER普遍存在候选跨度样本分布不平衡问题。
### 方法关键点
1. 提出快慢双专家增强的span-based CLNER架构FSE：共享fast expert学习token级关联，高效过滤低概率候选span；任务专属slow expert仅对剩余候选做分类，兼顾跨任务知识共享与单任务学习负担降低，稳定训练同时保持模型可塑性。
2. 引入长度衰减负采样策略，针对不同长度span动态调整负采样权重，缓解样本不平衡。
### 关键结果
在OntoNotes、FewNERD合成数据集上取得CLNER任务SOTA性能，各组件有效性均得到验证，相比基线收敛速度更快，双专家功能符合预期。
