---
title: 'AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning'
title_zh: AgentOPSD：面向智能体强化学习的递归自蒸馏方法
authors:
- Zi-Han Wang
- Zhengxi Lu
- Zhiyuan Yao
- Jinyang Wu
- Jie Wu
- Zhengzhou Cai
- Yueqing Sun
- Ziang Ye
- Linji Hao
- Qi Gu
affiliations:
- Tsinghua University
- Zhejiang University
- Meituan
arxiv_id: '2608.05987'
url: https://arxiv.org/abs/2608.05987
pdf_url: https://arxiv.org/pdf/2608.05987
published: '2026-08-05'
collected: '2026-08-07'
category: Agent
direction: 长horizon智能体RL信用分配优化
tags:
- Agent
- Reinforcement Learning
- Credit Assignment
- Self-Distillation
- GRPO
one_liner: 无需critic的递归轮次信用分配方法，将稀疏最终奖励转化为精准轮次监督，提升长horizon智能体性能
practical_value: '- 做多轮交互Agent（如电商导购Agent、搜索多轮query引导Agent）训练时，可直接复用AgentOPSD的信用分配方案替代GRPO全局奖励广播，解决长轮次下稀疏最终奖励无法区分关键决策的问题，尤其适合路径长、决策多的交互场景

  - 工程上可复用其自蒸馏实现逻辑：仅需在原有GRPO训练流程上增加单路特权信息（如业务沉淀的优质决策skill库）的teacher前向，无需额外rollout、无需训练critic，额外计算开销极低，可快速接入现有RL训练管线

  - 做多轮推荐/搜索序列优化时，可借鉴其递归贝叶斯信念更新思路，将用户行为序列的每一步交互信号转化为对最终转化的贡献权重，替代现有均匀加权或简单衰减加权的序列建模方案，提升长序列用户建模精度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于GRPO的Agent RL方法仅将轨迹级稀疏奖励广播到所有轮次，无法区分长交互序列中的关键决策和冗余操作，长horizon场景下性能衰减严重；现有自蒸馏方法的token级信号与Agent轮次交互的边界不匹配，且孤立计算每轮信号未考虑历史累积证据，无法生成可靠的序列级信用。

### 方法关键点
- 聚合token级师生对数概率差为轮次级证据，将其作为贝叶斯信念更新的输入，在对数几率空间递归更新轨迹最终成功概率的信念状态
- 以连续两轮信念的差值作为当前轮次的信用，结合最终轨迹奖励的符号对齐优化方向，对GRPO的序列级优势做轮次维度的加权重塑，整个过程无需额外rollout、无需学习critic
- 引入权重λ控制重塑强度，对加权系数做截断保证优化稳定性，完全兼容现有GRPO训练流程

### 关键实验
在ALFWorld、WebShop（电商交互环境）、Search-QA三个基准测试，对比GRPO、SDAR、StepOPSD等10+基线：Qwen2.5-7B在ALFWorld成功率达89.1%，比GRPO高7.9个百分点；长horizon下每增加一轮交互，成功率仅下降0.54个百分点，远低于GRPO的2.91个百分点；WebShop场景下得分达90.2，比基线SDAR高0.8个百分点。

最值得记住的一句话：长序列交互场景下的轮次信用，不应该由单轮局部信号孤立决定，而应该由该信号对最终成功概率信念的修正幅度决定。
