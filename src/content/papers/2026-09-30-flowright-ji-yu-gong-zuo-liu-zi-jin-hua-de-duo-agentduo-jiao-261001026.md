---
title: It Takes Workflows to Evolve Better Workflows
title_zh: FLOWRIGHT：基于工作流自进化的多Agent多角色协同优化框架
authors:
- Xuehang Guo
- Haoyu Wang
- Haifeng Chen
- Yangyi Chen
- Zhenhailong Wang
- Qingyun Wang
affiliations:
- William & Mary
- NEC Corporation of America
- University of Illinois Urbana-Champaign
arxiv_id: '2610.01026'
url: https://arxiv.org/abs/2610.01026
pdf_url: https://arxiv.org/pdf/2610.01026
published: '2026-09-30'
collected: '2026-10-02'
category: MultiAgent
direction: 多Agent工作流 · 协同进化优化
tags:
- Multi-Agent
- Workflow Optimization
- Co-evolution
- Credit Assignment
- Reinforcement Learning
one_liner: 提出层次化结构感知奖励范式，无需额外标注即可实现多Agent工作流的单/多角色协同进化
practical_value: '- 可复用层次化结构感知奖励设计：电商多Agent导购/售后流程、推荐全链路各模块的优化中，直接从执行轨迹提取角色级故障归因，无需额外训练奖励模型或人工标注，大幅降低多Agent系统训练成本

  - DATAWRIGHT数据硬化方法可直接用于构造业务评测集：将现有单Agent可解决的简单任务组合为贴合真实复杂场景的工作流级难任务，避免无效评测，更精准衡量多Agent/多模块系统的实际效果

  - 多角色协同进化思路可迁移至推荐全链路优化：同时优化召回、排序、文案生成等上下游角色，收益远高于单独优化单个模块，论文验证协同进化比单角色优化整体收益高2.2个百分点

  - 测试时元蒸馏方法可实现业务快速迭代：无需更新模型权重，仅将历史成功工作流蒸馏为few-shot prompt即可获得收益，适合线上多Agent系统的快速灰度迭代'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多Agent工作流优化仅单独训练工作流生成器，负责执行的Agent全程固定，整体性能上限受限；工作流执行结果仅输出全局稀疏分数，无法定位故障角色，现有归因方法需额外引入奖励模型、人工标注或重复执行，成本极高；同时现有评测数据集大多为单Agent即可解决的简单任务，无法真实体现多Agent工作流的价值。
### 方法关键点
- 以工作流为统一载体，同一信号同时用作评测指标、各角色训练优化信号、测试时蒸馏目标
- 层次化结构感知奖励范式：将全局稀疏分数拆分为格式校验、贡献有效性、可执行性、答案正确性、角色级故障归因5个加权项，故障归因直接从执行轨迹提取，无需额外标注、模型或执行
- 支持4种进化模式：单角色自进化、Agent-技能协同进化、上下游协同进化、多Agent协同进化，兼容GRPO、DAPO等任意RL优化算法
- 配套DATAWRIGHT数据硬化方案：通过子任务组合、提升复杂度等策略，将单Agent可解决的数据集转换为多难度等级的工作流级任务
### 关键结果
在文档、幻灯片、图表、代码、数学、金融7个领域的44组测试任务上，未训练的FLOWRIGHT比单Agent基线性能高≥11.39%；多Agent协同进化整体收益达+5.03%，远超单角色自进化的+2.83%，最高单点收益+7.41%；测试时无需更新权重的元蒸馏方案最高可带来+2.58%的额外收益。
### 核心结论
多角色协同进化的收益远高于单独优化单个环节，基于执行轨迹的零额外成本归因是多Agent系统落地的关键可行路径
