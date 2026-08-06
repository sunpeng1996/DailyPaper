---
title: 'GDPevo: Evaluating Agent Self-Evolution on Real Business Tasks'
title_zh: GDPevo：面向真实商业任务的Agent自进化评估基准
authors:
- Leijun Zhou
- Zhihao Liu
- Xiang Qu
- Chenxu Liu
- Yifei Liu
- Yanke Yu
- Jingzhe Xu
- Xuejun Wu
- Buyue Qian
- Xi Chen
affiliations:
- PrismShadow
- New York University
arxiv_id: '2608.03764'
url: https://arxiv.org/abs/2608.03764
pdf_url: https://arxiv.org/pdf/2608.03764
published: '2026-08-03'
collected: '2026-08-06'
category: Agent
direction: Agent自进化 · 能力评估基准
tags:
- Agent
- Self-Evolution
- Benchmark
- Rule Hybridization
- Business Task
one_liner: 提出首个覆盖6大高价值商业域的Agent自进化基准，通过规则杂交确保测试增益可归因
practical_value: '- 业务域Agent评测可复用规则杂交方法：将电商/广告业务流程拆解为原子规则，训练任务放规则子集、测试任务重组，可准确衡量Agent对业务规则的迁移学习能力，避免评测增益不可归因

  - 自进化监督策略选型参考：固定业务域优化选fewshot（类SFT），同域准确率最高可提升16.44pp；需跨业务域复用的Agent选reflect（类RL），跨域迁移更鲁棒，基本无负迁移

  - 减少自进化模块的无效投入：无需过度设计skill creator，极简的经验总结prompt效果甚至优于复杂内置实现，自进化性能瓶颈核心在底层大模型能力

  - 抗污染评测集搭建可复用全自动生成管线：快速批量生成新的业务评测任务，避免模型刷榜导致内部评测集失效'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent自进化基准存在三大缺陷：高价值商业场景（金融、法律、医疗等）覆盖不足；训练测试拆分无逻辑对应，性能增益无法归因于习得能力；静态公开数据集易受数据污染快速失效，缺乏适配真实企业业务的可信赖评测方案。
### 方法关键点
- 核心设计**规则杂交**机制：将每个业务流程拆解为独立的原子业务规则，训练任务仅暴露规则子集，测试任务重组规则，确保测试阶段的性能提升完全来自Agent从训练中习得的可迁移规则
- 全自动3阶段任务生成管线：种子场景挖掘→任务组生成→校准审核，2天即可将基准从120个任务扩展到240个，可快速迭代有效对抗数据污染
- 多维度确定性评测：采用规则化代码grader替代LLM评判，结果可复现可归因；同时将token消耗、调用轮次、monetary cost作为一等指标，兼顾效果和落地效率
### 关键结果
在覆盖CRM/ERP/金融/医疗/法律/数据处理6大领域的240个任务上测试4类Agent+4种监督类型：所有自进化方案相对无进化base均有提升，最高提升16.44pp；fewshot监督同域效果最优但跨域易出现负迁移，reflect监督跨域迁移更鲁棒；最优进化后Agent准确率仍远低于91.6%的全知oracle上限，当前Agent自进化能力还有极大提升空间。

> 值得记住的结论：Agent自进化的性能瓶颈主要来自底层大模型的基础能力，而非复杂的进化策略设计，极简经验提炼就能拿到不错的提升效果
