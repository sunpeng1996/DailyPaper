---
title: Discriminative World Models for Web Agents
title_zh: 面向Web Agent的判别式世界模型
authors:
- Kelvin Li
- Dhruv Pendharkar
- Anish Pahilajani
- Chuyi Shang
- Leon Oks
- Leonid Karlinsky
- Rogerio Feris
- Trevor Darrell
- Roei Herzig
affiliations:
- University of California, Berkeley
- MIT-IBM Watson AI Lab
- Cal Poly San Luis Obispo
- Xero
arxiv_id: '2609.02885'
url: https://arxiv.org/abs/2609.02885
pdf_url: https://arxiv.org/pdf/2609.02885
published: '2026-09-02'
collected: '2026-09-03'
category: Agent
direction: Web Agent 世界模型训练优化
tags:
- WebAgent
- WorldModel
- PRM
- ActionRanking
- GRPO
one_liner: 提出预测状态匹配训练目标，提升Web Agent世界模型的动作结果区分与决策性能
practical_value: '- 做电商导购、运营类Web Agent时，世界模型无需强求生成完整HTML/AXTree，可改用判别式训练目标，仅保留动作相关的核心状态信息，既降低推理token消耗，又提升下游排序效果

  - 现有PRM（过程奖励模型）可直接接入判别式世界模型的输出，无需修改PRM原有训练逻辑，即可低成本提升动作排序准确率，快速升级Agent决策能力

  - 构造多分支对比训练数据时，可复用不同轨迹中重复的状态节点，合并为状态-动作图，无需额外人工标注即可生成多动作-多结果的对比样本，降低数据采集成本

  - 用GRPO做RL训练时，仅需加入轻量化格式奖励（如要求输出符合指定XML标签），无需复杂调参即可稳定提升模型输出的合规性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Web Agent的世界模型普遍采用监督学习训练生成固定格式状态（HTML/AXTree/文本摘要），但该目标与下游PRM/排序器的需求错配：排序器需要能区分不同动作结果差异的表示，而监督生成的表示要么遗漏关键差异，要么包含大量冗余信息，导致动作排序准确率偏低。
### 方法关键点
- 提出**预测状态匹配**训练目标：不要求模型生成固定格式的状态，仅要求其输出的状态表示能让固定判别器将当前动作对应的真实结果与其他动作的结果区分开，是表示无关的训练目标
- 构造分支轨迹数据集：合并WebArena的Go-Browse轨迹中重复的状态节点，生成状态-动作图，每个节点关联多个不同动作及对应结果，共得到30920组对比样本，无需额外标注
- 用GRPO做RL训练，总奖励由两部分组成：判别器判断预测表示匹配真实结果的匹配奖励，输出符合指定格式的格式奖励
- 下游接入简单：直接将世界模型输出的状态表示拼入PRM输入，无需修改PRM原有训练逻辑
### 关键结果
- 预测状态匹配基准准确率达80.8%，比WebDreamer、WebWorld等现有世界模型高6~10个百分点
- 接入WebPRMBench的PRM后，平均Best-of-N准确率达72.7%，比无状态PRM高16.9个百分点，比接入WebWorld的PRM高5个百分点
- WebArena-Lite端到端任务中，用该世界模型增强Best-of-5动作选择，任务成功率达28.48%，比纯ReAct范式高14.5个百分点，比无状态Best-of-5高6.7个百分点

最值得记住的一句话：Web世界模型的核心目标是区分不同动作的效果差异，而非机械复现完整的页面状态。
