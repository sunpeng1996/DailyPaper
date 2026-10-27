---
title: 'EnvLunch: The Environment as a Free Lunch for Learning to Interact'
title_zh: EnvLunch：利用可执行环境无标注训练交互Agent
authors:
- Wei Liu
- Min Gao
- Yali Du
- Yulan He
affiliations:
- King's College London
- Chongqing University
- The Alan Turing Institute
arxiv_id: '2610.33817'
url: https://arxiv.org/abs/2610.33817
pdf_url: https://arxiv.org/pdf/2610.33817
published: '2026-10-24'
collected: '2026-10-27'
category: Agent
direction: Agent 无标注交互能力预热优化
tags:
- Agent Training
- Label Efficiency
- Reinforcement Learning
- Zero Annotation
- Environment Supervision
one_liner: 提出无标注环境驱动的Agent预热方法，大幅降低下游任务标注需求
practical_value: '- 可复用环境自监督预热思路：电商导购Agent、SQL查询类Agent上线前，可直接用业务已有的可执行环境（商品库、用户数据库、开放API）生成无标注交互任务做预热，大幅降低下游标注成本

  - 反奖励作弊机制可迁移：用多份扰动副本环境验证Agent输出有效性的设计，可直接用到广告投放Agent、推荐系统自动调参Agent的RL训练中，解决Agent刷奖励的问题

  - 低标注冷启动适配：新垂类导购Agent、新场景搜索意图理解Agent等标注数据不足的场景，优先做环境驱动预热，可实现8~32倍的标注效率提升，快速完成冷启动'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前训练具备可执行环境交互能力的Agent需依赖大量人工标注任务或大模型蒸馏轨迹，标注/数据制作成本极高；但可执行环境（如数据库、API系统）本身自带丰富的交互结构与可验证执行结果，这类免费信号长期未被充分利用。
### 方法关键点
- 无标注预热流程：随机组合环境合法动作生成可执行轨迹，执行得到最终观测，训练Agent仅根据最终观测还原功能等价的交互轨迹，无需任何人工/模型编写的任务描述
- 反奖励作弊机制：构造多个扰动副本环境（删除30%行、数值列随机缩放），仅当还原轨迹在所有副本的执行结果与原轨迹一致时发放全额奖励，同时加入交互轮次的简洁性奖励权重
- 训练流程：预热阶段用GRPO做RL优化，预热后的模型直接接入下游带标注的Agent RL训练流程
### 关键结果
在Qwen3.5-4B/9B两个模型规模、13个跨领域Agent benchmark（含数据分析、text2SQL、具身交互、应用操作等）上验证：
- 全训练预算下平均准确率比基线高9%以上，小样本场景下基线需要8~32倍的标注样本才能达到EnvLunch最低标注量下的准确率
- 1600个预热任务仅需20分钟CPU即可生成，远低于模型合成任务所需的4小时
- 即使预热环境与下游任务完全无重叠，仍可有效提升下游标注效率

**最值得记住的一句话**：可执行环境本身就是免费的训练信号源，无需显式构造任务描述就能有效提升Agent的交互能力与下游标注效率。
