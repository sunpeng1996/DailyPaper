---
title: 'Selection Is Not Learning: Choosing Model Futures'
title_zh: 选择不等于学习：自进化大模型的更新继承优化框架
authors:
- Haoyi Yang
- Kshitij Mishra
- Nils Lukas
- Salem Lahlou
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2610.22029'
url: https://arxiv.org/abs/2610.22029
pdf_url: https://arxiv.org/pdf/2610.22029
published: '2026-10-14'
collected: '2026-10-19'
category: Training
direction: 自进化LLM · 更新继承优化
tags:
- Self-Evolution
- LLM Training
- Update Gating
- Knowledge Distillation
- LoRA
one_liner: 提出EVOHEIR自进化框架与HEIRCOMMIT更新门控，解决LLM自进化任务合格但更新无效的问题
practical_value: '- 电商推荐/Agent自迭代场景可直接复用HEIRCOMMIT门控逻辑：每次模型更新后，用和训练数据完全隔离的离线新鲜探针集验证效果，仅当收益严格为正才上线，避免负向更新损伤线上业务

  - 可借鉴参数与经验解耦的设计思路：不要因模型整体效果不达标就丢弃其产出的优质样本，将优质交互/推理路径存入通用经验库，供后续所有版本迭代复用，降低样本收集成本

  - 经验恢复的训练trick可落地推荐小步迭代场景：用LoRA做低秩更新，针对当前模型的bad case用经验库样本修复，同时用KL散度约束保留已有正确预测能力，避免迭代中的能力遗忘'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有自进化LLM框架（Agent0、R-Zero等）仅通过任务侧筛选判定学习价值，只要任务符合可学习要求就全量继承模型更新，存在显著的「选择-更新gap」：实验发现62.5%的验证合格任务对应的模型更新没有收益甚至会降低效果，导致自进化过程中性能波动、甚至出现倒退的“自退化”问题。
### 方法关键点
- **HEIRCOMMIT更新门控**：冻结更新后的候选模型，使用与训练、筛选环节完全隔离的新鲜探针集和当前模型做对比，仅当候选模型效果更优才继承参数，否则保留当前版本。
- **EVOHEIR解耦参数与经验继承**：先筛选表现最优的候选作为参数起点，再从当前分支、历史存档的所有经验中区分当前模型的答对/答错样本：答错样本参考经验库的正确答案修复，答对样本用KL散度约束保留原有能力，全程仅更新LoRA参数避免过拟合。
- **经验独立存档**：无论本轮参数是否被继承，所有合格的经验样本都存入归档库，供后续轮次复用。
### 关键结果
- HEIRCOMMIT相比同接受率的随机继承策略，将有害更新占比降低68%~83%；
- 覆盖4个不同大小骨干LLM的10轮自进化实验中，EVOHEIR的数学推理平均得分比最强基线Agent0高5.3%，在45/48的基准-骨干配对中效果领先；
- 80%效果差于当前版本的模型产出的经验，仍能给后续迭代带来正向收益。

**最值得记住的一句话**：自进化系统应该评判最终产生的模型更新效果，而不是只评判选择的任务质量，经验的生命周期远长于产出它的模型。
