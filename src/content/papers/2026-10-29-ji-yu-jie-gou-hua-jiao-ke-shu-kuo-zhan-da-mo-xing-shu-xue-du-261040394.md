---
title: Scaling Mathematical Proof Supervision from Structured Textbooks
title_zh: 基于结构化教科书扩展大模型数学证明监督数据
authors:
- Youqing Fang
- Zhouqi Hua
- Yinhao Tang
- Yuzhe Gu
- Lingkai Kong
- Bin Liu
- Weiming Zhang
- Kai Chen
- Yanan Sun
- Wenwei Zhang
affiliations:
- University of Science and Technology of China
- Fudan University
- Shanghai AI Laboratory
- Shanghai Jiao Tong University
arxiv_id: '2610.40394'
url: https://arxiv.org/abs/2610.40394
pdf_url: https://arxiv.org/pdf/2610.40394
published: '2026-10-29'
collected: '2026-10-31'
category: Reasoning
direction: 大模型数学推理 · 结构化训练语料
tags:
- Mathematical Reasoning
- Structured Corpus
- Curriculum Learning
- SFT
- Scaling Law
one_liner: 构建保留教材层级结构的38万条数学证明监督语料，大幅提升大模型数学推理性能
practical_value: '- 领域结构化语料构建可复用层级保留思路：电商类目/商品知识体系做SFT数据时，保留类目从属、属性关联、知识点依赖关系，避免拆为孤立QA损失结构信息

  - 可借鉴课程学习训练范式：训练推荐/Agent领域技能时，按从易到难的知识点顺序投喂数据，相比随机混合数据可获得更高下游性能提升

  - 语料scaling规律可迁移：业务做领域SFT时，可参考本文分析框架量化不同量级、来源语料的边际收益，优化数据制作/采购成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有大模型数学监督数据普遍被拆分为孤立的问题-答案对，丢失原始教材的课程组织逻辑、证明依赖关系等结构信息，限制了大模型数学推理能力的提升。
### 方法关键点
1. 构建TOME-Math结构化语料库，覆盖2118本大学数学核心教材、29个学科，提取380292条结构化证明监督记录，完整保留章节顺序、命题-证明关联、依赖引用、来源溯源信息；
2. 基于语料结构信号，探索跨多数学学科的课程学习训练范式，分析监督数据规模、来源广度的scaling规律。
### 关键结果
全量TOME-Math微调后，大模型在自构建留出测试集和公开基准上的平均得分比基线模型高16.7个百分点，整体性能优于3个公开指令数据基线。
