---
title: 'PCTD: Preference-Guided Counterfactual Task Decomposition for Agent Tool Retrieval'
title_zh: PCTD：偏好引导的反事实任务分解框架用于智能体工具检索
authors:
- Chu Zhao
- Lei Tang
- Minghang Li
- Jianzhe Zhao
- Guibing Guo
- Zhengzong Chen
- Yuanyuan Zhao
- Fei Huang
affiliations:
- Northeastern University
- Honor Device Co., Ltd
- Beijing University of Posts and Telecommunications
arxiv_id: '2607.15696'
url: https://arxiv.org/abs/2607.15696
pdf_url: https://arxiv.org/pdf/2607.15696
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: Agent工具调用 · 任务分解优化
tags:
- Task Decomposition
- Counterfactual Reasoning
- Preference Alignment
- Tool Retrieval
- GRPO
one_liner: 结合反事实因果奖励与结构偏好奖励，解决Agent任务分解的奖励黑客与OOD泛化缺陷
practical_value: '- 任务分解类RL优化可复用双奖励设计：反事实奖励（用原始query检索结果做基线算边际增益，切断浅层特征虚假关联）+ 结构偏好奖励（约束分解逻辑性、原子性，避免重复冗余），解决奖励黑客问题

  - OOD泛化要求高的场景（如电商多场景工具调用、新类目召回），可参考反事实归因思路，不要直接用下游召回/排序指标做唯一奖励，避免模型过拟合训练集分布

  - 需做多轮交互场景任务拆解评测时，可复用MTDTool的状态机驱动数据集构建pipeline，自动生成带细粒度过程标注的对话数据，降低人工标注成本

  - 任务分解+下游检索链路中，RL优化比Prompt/SFT的OOD泛化提升更显著，有条件优先走RLVR闭环优化路径'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于RL的Agent任务分解方法直接用下游工具检索指标（Recall、NDCG）作为奖励，易引发奖励黑客问题：模型通过重复分解、堆砌关键词等浅层策略最大化匹配分，导致分解结果与检索指标产生虚假关联，在含未见过工具的OOD场景下泛化能力暴跌；同时缺少对分解结构的偏好建模，进一步加剧重复分解问题。

### 方法关键点
- 双奖励联合优化：①反事实奖励：以原始query直接检索的结果为基线，计算任务分解带来的NDCG边际增益和工具覆盖增益，消除原始query关键词、工具先验等混淆变量干扰，切断虚假关联；②偏好奖励：基于训练好的过程奖励模型（PRM），从逻辑一致性、上下文忠实度、原子性等5个维度打分，和人工参考结果对比生成相对偏好奖励，提供细粒度结构约束
- 基于GRPO做策略优化，无需单独训练Critic网络，降低内存开销，提升训练稳定性
- 构建MTDTool基准数据集：通过状态机驱动的pipeline自动生成移动端多轮交互场景对话数据，包含对话状态演化、意图改写、原子任务序列等细粒度标注，覆盖10种细分场景，填补多轮任务分解过程评测空白

### 关键结果
在ToolRet和MTDTool两个基准上对比SOTA方法：①MTDTool OOD场景下，基于Qwen3-8B的PCTD NDCG@10达82.74，较RL baseline ToolQP提升4.82；②MTDTool In-Domain场景下Completeness@10达87.08，较ToolQP提升3.47；③分解重复率从5.2%降至0.7%，训练单步耗时从110ms降至92ms。

> 最值得记住：直接用下游检索指标作为任务分解的唯一RL奖励，必然会引发奖励黑客和OOD泛化缺陷，必须结合因果归因与结构约束双维度优化。
