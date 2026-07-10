---
title: 'CausalDS: Benchmarking Causal Reasoning in Data-Science Agents'
title_zh: CausalDS：面向数据科学Agent的因果推理能力评测基准
authors:
- Andrej Leban
- Yuekai Sun
affiliations:
- University of Michigan
arxiv_id: '2607.08093'
url: https://arxiv.org/abs/2607.08093
pdf_url: https://arxiv.org/pdf/2607.08093
published: '2026-07-08'
collected: '2026-07-10'
category: Agent
direction: Agent 因果推理能力基准构建
tags:
- Causal Reasoning
- Agent Benchmark
- SCM
- Pearl Hierarchy
- Tool Use
one_liner: 首个整合SCM合成、真实叙事、工具调用、弃权评估的因果数据科学Agent基准
practical_value: '- 构建电商归因/运营分析Agent时，可复用其弃权评估逻辑：将因果效应可识别性判断作为前置gate，无法识别时强制Agent输出弃权而非幻觉结果，降低业务决策风险

  - 搭建业务端Agent能力评测集时，可参考SCM+真实场景叙事+噪声观测层的合成范式，避免训练数据污染导致的“因果鹦鹉”问题，准确衡量真实推理能力

  - 电商广告/推荐因果归因的工程实现中，可参考分层设计：先完成因果结构识别→判断目标效应可识别性→再执行估计，有效减少无效计算和错误输出'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有因果推理基准存在明显割裂：纯符号因果基准无真实数据分析流程，数据科学Agent基准无结构化因果生成逻辑，且多数基于公开数据集构建易存在训练数据污染，导致模型靠记忆而非推理回答（“因果鹦鹉”问题），无法完整评估Agent结合叙事理解、工具调用、因果推理、不确定性判断的综合能力。
### 方法关键点
- 基于结构因果模型（SCM）合成基准场景，可锚定真实数据集的变量类型、图结构等分布，同时完全合成避免数据污染
- 设计独立观测层，可在不改变因果结构和效应可识别性的前提下，引入噪声观测、缺失变量等，灵活调整数据分析难度
- 任务覆盖Pearl因果三层级（关联、干预、反事实），首次将非可识别问题的弃权作为核心评估指标
- 支持工具调用/代码执行的评估范式，Agent需在沙箱环境中读取数据、运行分析、输出结果，贴合真实数据科学工作流
### 关键结果
在953个合成场景组成的100场景真实测试集上评估6款主流模型：Claude Opus 4.8表现最优，CausalDS得分0.278，Pass Rate 82.4%；所有模型标称95%的ATE置信区间实际覆盖率仅20%~71.4%，普遍存在过度自信；开源模型与闭源模型在成本-质量平面上线性可分，闭源模型单任务token消耗低1~2个数量级，弃权准确率领先15%~50%。
### 核心洞察
因果数据科学Agent的能力差距不在符号因果推理或点估计精度，而在「知道何时应该弃权」的认知能力和不确定性校准水平。
