---
title: Token-Level Credit Assignment Optimization for Generative Document Retrieval
title_zh: 面向生成式文档检索的Token级信用分配优化
authors:
- Xinpeng Zhao
- Yang Liu
- Ran Chen
- Xinyu Ma
- Daiting Shi
- Pengjie Ren
- Zhumin Chen
- Zhaochun Ren
- Xin Xin
affiliations:
- Shandong University
- Peking University
- Baidu Inc.
- Leiden University
arxiv_id: '2608.12049'
url: https://arxiv.org/abs/2608.12049
pdf_url: https://arxiv.org/pdf/2608.12049
published: '2026-08-12'
collected: '2026-08-13'
category: GenRec
direction: 生成式检索 · 强化学习优化
tags:
- Generative Retrieval
- Reinforcement Learning
- Credit Assignment
- DocID
- GRPO
- PPO
one_liner: 提出Token级信用分配强化学习框架，提升生成式检索的Top排序准确率
practical_value: '- 生成式检索/生成式推荐的RL优化可复用该Token级奖励设计：用冻结参考模型的金标轨迹与生成轨迹的隐状态余弦相似度做逐Token奖励，无需额外训练奖励模型，大幅降低落地成本

  - 优化Semantic ID/DocID类生成任务时，优先选择GRPO而非PPO作为RL优化器，GRPO的组相对优势估计更适配离散ID空间的序列生成场景，效果更稳定

  - RL训练阶段必须加合法ID前缀约束解码，避免生成无效ID引入噪声；同时根据ID类型调整KL正则系数：语义类ID（如PQ码）关闭KL，词汇类ID（如商品标题+SKU）加小系数KL保留生成模式

  - 做Top推荐/搜索首屏效果优化时，重点提升生成序列前几个Token的准确率，早期Token对应候选空间更大，对最终排序的影响远高于后期Token'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式检索通过自回归生成DocID完成召回，但现有训练范式存在粒度不匹配问题：监督微调仅优化逐Token交叉熵，未对齐最终检索目标；基于RL的优化普遍采用序列级奖励，将文档级相关性反馈平摊到所有Token，无法区分不同位置Token的路由贡献，尤其是影响候选空间范围的早期Token得不到精准反馈，导致Top检索精度提升受限。
### 方法关键点
- 两阶段训练：先通过监督微调（SFT）得到基础Query→DocID生成能力，冻结SFT模型作为参考模型，预缓存金标DocID的逐Token隐状态轨迹
- 无额外奖励模型的Token级奖励设计：生成轨迹逐Token隐状态与同位置金标隐状态的余弦相似度为基础奖励，叠加超长生成惩罚、全序列命中全局奖励
- 两种优化器适配：TCA-GRPO基于同Query多候选的位置级归一化计算逐Token优势，无需值函数，效果更稳定；TCA-PPO基于值函数估计优势，验证奖励设计通用性
- 全程加Trie约束解码，仅生成合法DocID前缀，避免无效轨迹引入噪声
### 关键结果
在MS MARCO、NQ两个公开检索基准上，对比SFT基线、序列级RL基线DDRO/GenRRL等：TCA-GRPO在Title+URL DocID设置下，MS MARCO R@1相对提升3.56%、MRR@10相对提升1.53%；NQ PQ语义ID设置下R@1相对提升3.99%、MRR@10相对提升3.28%，且效果显著优于TCA-PPO实现。

生成式ID类任务的RL优化，监督粒度必须与决策粒度对齐，逐Token细粒度反馈对Top排序精度的提升远大于粗粒度序列级奖励。
