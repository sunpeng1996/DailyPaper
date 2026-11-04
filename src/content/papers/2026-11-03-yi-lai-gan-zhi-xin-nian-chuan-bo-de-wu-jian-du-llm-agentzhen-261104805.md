---
title: Where Is the Truth When AI Agents Disagree? Dependence-Aware Belief Propagation
  for Unsupervised Truth Discovery (Extended Version)
title_zh: 依赖感知信念传播的无监督LLM Agent真值发现方法
authors:
- Laure Berti-Equille
affiliations:
- IRD, ESPACE-DEV, Montpellier, France
arxiv_id: '2611.04805'
url: https://arxiv.org/abs/2611.04805
pdf_url: https://arxiv.org/pdf/2611.04805
published: '2026-11-03'
collected: '2026-11-04'
category: Agent
direction: 多Agent协作 · 无监督真值发现
tags:
- Truth Discovery
- LLM Agent
- Belief Propagation
- Unsupervised Learning
- Ensemble Learning
one_liner: 提出无监督BP-TD算法，解决同基座LLM Agent错误相关导致的真值发现失效问题
practical_value: '- 多Agent结果聚合场景（如多Agent生成电商商品文案、审核违规内容、回复用户咨询）若存在大量同基座变体Agent，可直接复用family权重（1/同基座Agent数）做加权投票，无需标注即可压制弱基座群体的多数错误

  - 无标签场景下需要识别低质Agent做下线/优化，可复用BP-TD的软去相关权重+迭代可靠性估计逻辑，比经典Dawid-Skene方法更能避免将高错误率的同基座群体误判为高可靠

  - 标注预算≥20条时，直接筛选最优单Agent的效果优于所有无监督多Agent聚合方法，无需投入复杂的聚合逻辑开发

  - 若已知最强基座的衍生Agent占群体多数，不要盲目添加去相关权重，否则会抵消强基座的性能优势'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
经典真值发现方法假设来源条件独立，但实际部署的LLM Agent多为同基座的变体（不同prompt、RAG封装、自一致性样本等），错误高度相关，导致传统方法会奖励同基座的错误共识，效果甚至不如多数投票；同时大规模标注真值成本过高，亟需无监督的多Agent真值聚合方法。
### 方法关键点
- 提出BP-TD，在单硬币Dawid–Skene模型的均值场变分推理中加入每个Agent的去相关权重`w_a`，同基座/高答案共现的Agent组总权重约等于1，避免同组多票绑架结果
- 支持三种无标签去相关权重计算：`family`（按基座来源分组，`w_a=1/组大小`，仅需 provenance 信息，无额外成本）、`cooccur`（按答案共现阈值分组，无需真值）、`shared error`（按共同错误分组，依赖当前真值估计，易出现循环偏差）
- 首次迭代等价于`w_a`加权投票，后续迭代更新每个Agent的可靠性得分，时间复杂度线性随问题数增长，仅Agent数维度为平方级，适合小规模Agent池
### 关键结果
- 实验基于MMLU、SciQ、TruthfulQA、ARC四个基准，13个基于5个基座的本地Agent，覆盖160题到10000题规模，对比多数投票、经典Dawid-Skene、TruthFinder等10+基线
- 无标签BP-TD在MMLU 160题上准确率0.716，较多数投票的0.624提升9.2pp；10000题规模下准确率0.707，较多数投票的0.674提升3.3pp
- Agent可靠性排名与真实准确率的斯皮尔曼相关系数达0.94，远优于经典Dawid-Skene的-0.62；仅需20条标注，选最优单Agent的效果就超过所有无监督聚合方法

> 最值得记住的结论：去相关权重仅在最大相关Agent群体的准确率低于其他群体时有效，反之会降低效果，目前无无标签统计量可区分这两种场景。
