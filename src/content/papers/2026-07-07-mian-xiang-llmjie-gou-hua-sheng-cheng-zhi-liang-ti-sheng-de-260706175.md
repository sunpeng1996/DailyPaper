---
title: 'Improving LLM-Generated Process Model Quality Through Reinforcement Learning:
  The Role of Reward Function Design'
title_zh: 面向LLM结构化生成质量提升的强化学习奖励函数设计研究
authors:
- Alexander Rombach
- Chantale Lauer
- Nijat Mehdiyev
affiliations:
- German Research Center for Artificial Intelligence (DFKI)
- Saarland University
arxiv_id: '2607.06175'
url: https://arxiv.org/abs/2607.06175
pdf_url: https://arxiv.org/pdf/2607.06175
published: '2026-07-07'
collected: '2026-07-08'
category: Training
direction: LLM强化学习训练 · 多维度奖励设计
tags:
- Reinforcement Learning
- Reward Function
- Structured Generation
- GSPO
- LoRA
one_liner: 系统探究多维度结构化生成场景下RL奖励设计规则，给出通用落地指南
practical_value: '- 多维度结构化生成任务（电商规则生成、推荐结构化理由、Agent工具调用参数生成等）的RL奖励优先采用等权重分配，刻意加权单个维度不仅无法提升该维度效果，还可能导致模型崩溃到低质量输出模式

  - RL训练前是否做SFT需匹配基座能力：小参数模型（如8B级）必须用SFT初始化保证RL训练效果，中参数模型（如14B级）可跳过SFT直接做RL，避免语义质量下降

  - 结构化生成场景的无效输出惩罚项需匹配基座初始生成合法率：基座合法率低时加惩罚可快速提升有效性，基座合法率高时加惩罚可作为隐式正则减少模板收敛

  - 多指标奖励的RL训练优先选择GSPO/GRPO这类序列级组内归一化算法，对奖励校准要求更低，训练更稳定，无需额外训练critic网络'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM面向结构化输出任务时，SFT只能拟合训练数据的分布上限，无法突破现有标注质量的天花板；RL可通过外部可验证的质量指标优化，但多维度质量要求下的奖励函数设计缺乏系统性指导，奖励权重、惩罚项、初始化策略的效果及交互影响尚未明确。
### 方法关键点
- 采用GSPO序列级RL算法，基于同prompt下多候选的组内相对奖励更新策略，无需单独训练critic网络，天然适配整体输出质量评估的场景
- 基于横跨语法、语用、语义3个维度的38个自动化评估指标构建奖励，测试6种奖励配置（等权重、单维度加权、有无无效输出惩罚）
- 覆盖Llama3.1 8B、Qwen2.5 14B两个开源基座，对比SFT初始化/直接RL两种策略，全程采用LoRA实现参数高效微调
### 关键结果
- 对比SFT基线，RL训练后语法、语用质量显著提升，输出波动率降低6倍以上，语义保真度基本无损失
- 等权重奖励效果全面优于定向加权，刻意加重某维度权重不仅不会提升该维度效果，反而可能导致模型模式崩溃
- 无效输出惩罚的作用与基座强相关：对Qwen2.5 14B是隐式多样性正则，可减少模板收敛，对Llama3.1 8B无明显效果
- SFT初始化的必要性与基座强相关：Llama3.1 8B必须用SFT初始化才能有效RL，Qwen2.5 14B跳过SFT直接RL效果更好，可避免语义质量下降

多维度结构化生成场景下，奖励函数设计带来的效果差异，和是否采用RL优化本身的效果差异相当，没有通用默认配置，需结合基座能力做小范围验证。
