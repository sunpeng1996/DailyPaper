---
title: Robust Soft Skill Adaptation via Behavioral Localization in Tool-Using Agents
title_zh: 基于行为定位的工具使用Agent软技能鲁棒适配方法
authors:
- Zijian Jiang
- Xilu Wang
affiliations:
- University of Surrey
arxiv_id: '2610.30041'
url: https://arxiv.org/abs/2610.30041
pdf_url: https://arxiv.org/pdf/2610.30041
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: Agent 软技能适配与软提示优化
tags:
- Soft Prompt
- Agent Skill
- Tool-using Agent
- Behavioral Localization
- Prompt Tuning
one_liner: 定位Agent轨迹中技能生效的稀疏关键位置，用其监督软提示训练实现更鲁棒的软技能适配
practical_value: '- 电商导购/客服/工具类Agent做软技能适配时，无需全轨迹训练，仅筛选10%左右技能生效的关键位置做监督，可降低90%训练成本同时提升适配效果

  - 训练业务场景专属Soft Prompt/LoRA时，可复用「正增益+分布偏移」的定位分数筛选关键样本/位置，避免无效更新导致的原有能力退化

  - 任务专属Agent技能落地时，优先采用该稀疏监督方案，效果可超过全量文本技能基线，同时减少KV cache占用，降低推理成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
工具Agent跨任务适配时，长文本技能提示会占用大量上下文、推高推理成本；基于全成功轨迹训练Soft Prompt的方案易引入不必要的行为漂移，甚至损害基座Agent原有能力。研究发现技能的生效效果高度集中在轨迹的极少部分位置，无需全量训练即可实现有效适配。

### 方法关键点
- 计算三类next token分布：添加文本技能、无技能、添加待训练Soft Prompt条件下的输出分布
- 定义两个核心度量：正增益G（加技能后成功token的对数概率提升幅度）、分布偏移J（加/不加技能的输出分布对称KL散度）
- 用G*J作为定位分数，选取top k%轨迹位置作为核心监督位，其余位置要求Soft Prompt输出对齐无技能的基座分布，避免行为漂移
- 核心位训练目标为最小化Soft Prompt输出与文本技能输出的KL散度

### 关键实验
数据集为SpreadsheetBench，基座采用冻结的Qwen3.6-35B-A3B Agent，对比基线包括全文本技能、全轨迹训练的SoftSkill、在线蒸馏的OPCD。核心结果：10%的轨迹位置即可捕获96.12%的技能正增益；共享软提示场景下，top10%位置训练的成功率达36.79%，较全轨迹SoftSkill的30.36%提升6.43pct；任务专属场景下，top10%位置训练成功率达57.38%，超过全文本技能的52.46%和OPCD的49.18%。

### 核心结论
Agent技能带来的行为改变高度稀疏，仅需关注10%左右的关键决策点做适配，就能实现比全量训练更好的效果，同时大幅降低训练和推理成本。
