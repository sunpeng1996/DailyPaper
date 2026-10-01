---
title: 'Routing Should Pay for Itself: Sparse Supervision for Economical LLM Routing'
title_zh: 面向成本自覆盖的稀疏监督LLM路由框架SAVEROUTER
authors:
- Guannan Lai
- Gelin Bian
- Hao-Xuan Ma
- Jun-Peng Jiang
- Long Chen
- Jian-Dong Liu
- Zhi-Hao Tan
- Han-Jia Ye
affiliations:
- Nanjing University
- The Hong Kong University of Science and Technology
- SinapisAI
arxiv_id: '2609.37402'
url: https://arxiv.org/abs/2609.37402
pdf_url: https://arxiv.org/pdf/2609.37402
published: '2026-09-28'
collected: '2026-10-01'
category: LLM
direction: LLM推理优化 · 成本感知路由
tags:
- LLM Routing
- Sparse Supervision
- Cost Optimization
- Inference Efficiency
- ROI Evaluation
one_liner: 通过自适应稀疏反馈采集与分层能力估计降低LLM路由前置成本，大幅缩短回本周期
practical_value: '- 电商/客服等多LLM服务场景可直接复用稀疏监督思路：无需全量标注所有query-模型的效果对，仅采集33%-41%高信息度样本即可训练合格路由，前置标注成本可降60%以上

  - 分层能力估计架构（query分组+组级先验+轻量残差修正）可复用在各类多模型路由场景，比如不同难度的推荐Query改写、商品文案生成任务的模型分发，平衡推理成本与效果

  - 可直接引入SA-BEP、SA-CR指标做路由方案的业务ROI评估，避免只看上线后推理成本忽略前置投入，导致方案长期无法回本

  - 自适应UCB采样策略可复用在新模型冷启动效果评估，无需全量跑通测试集，即可快速得到不同query分组下的模型效果分布，降低评估成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM路由方法仅关注上线后的推理成本优化，完全忽略前置监督的高额投入：训练路由需要全量执行所有候选模型在历史query上的效果，前置成本极高，甚至可能导致路由方案上线后长期无法回本；同时观测到路由质量早在全量标注完成前就已饱和，全量监督属于经济上的过度投入。
### 方法关键点
- 自适应稀疏反馈采集：先对query做语义/任务分组，采用UCB策略结合模型能力估计与不确定性，仅选择高信息度的query-模型对采集反馈，每个训练query仅需评测K个远少于候选总量的模型
- 分层能力估计：用双因素加性模型生成组-模型先验，结合已观测局部证据做收缩估计，再用轻量线性模型修正query级残差，无需重构全量query-模型效果矩阵，仅保证路由决策的正确性
- 新增SA-BEP（回本所需部署query量）、SA-CR（固定部署规模下的摊销成本比）两个指标，将前置监督成本纳入路由方案的经济效果评估
### 关键实验
在LLMRouterBench、Mixinstruct、MMR-Bench、RouterBench 4个基准上对比11个SOTA路由方法，仅用33%-41%的标注量即可达到持平或更优的路由质量；相比最快的全监督基线，回本所需部署query量降低1.9-9.5×，其中Mixinstruct场景下回本阈值从1163万query降至123万。
### 核心结论
LLM路由只需要决策充分性而非信息完备性，额外的监督投入不一定带来更优的经济收益，最小化长期服务成本的监督水平与实现最快回本的监督水平可能存在差异
