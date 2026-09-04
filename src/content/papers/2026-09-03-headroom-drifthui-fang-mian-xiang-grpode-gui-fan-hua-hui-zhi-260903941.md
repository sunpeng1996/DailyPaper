---
title: 'Headroom-Drift Replay: A Primitive for Principled Replay Control in GRPO'
title_zh: Headroom-Drift回放：面向GRPO的规范化回放控制原语
authors:
- Hyun Bin Park
- Du-Seong Chang
affiliations:
- Sogang University, Republic of Korea
arxiv_id: '2609.03941'
url: https://arxiv.org/abs/2609.03941
pdf_url: https://arxiv.org/pdf/2609.03941
published: '2026-09-03'
collected: '2026-09-04'
category: Training
direction: LLM训练·GRPO回放优化
tags:
- GRPO
- Replay Buffer
- Reinforcement Learning
- LLM Post-training
- Policy Optimization
one_liner: 提出学习价值排序+策略漂移门控的GRPO组级回放控制原语，无额外辅助模块，多任务效果超朴素回放对齐复杂方案
practical_value: '- 训练电商导购Agent、搜索推荐交互Agent时，可直接复用该双维度回放机制：用Headroom排序筛选高学习价值轨迹，Drift门控过滤过旧样本，无需额外轨迹生成模块，可大幅降低环境交互带来的训练成本

  - GRPO训练架构改造成本极低：保留原生GRPO的组级训练逻辑和新鲜样本流，仅新增回放筛选逻辑即可上线，无需修改原有训练管道

  - 策略漂移阈值无需全量训练调参：可通过短周期对数间隔扫描快速校准，不同参数规模（3B/7B）的同类任务可复用阈值，适配生成式推荐、Agent等多场景模型训练'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：GRPO是当前LLM推理、Agent训练的主流RL后训练范式，但反复生成新轨迹成本极高，尤其是需要和外部环境交互的Agent场景（如电商多轮导购、搜索交互决策），朴素回放复用旧轨迹易导致训练不稳定，现有回放方法均绑定额外探索、混合策略优化等模块，难以单独评估回放本身的增益，亟需低开销的纯回放控制机制。

**方法关键点**
- 双维度解耦回放决策：Headroom维度衡量存储轨迹组的剩余学习价值，对正优势样本计算1-当前token概率、负优势样本计算当前token概率，组平均后作为排序分数；Drift维度衡量当前策略与轨迹生成策略的差异，用token级对数概率差的平方平均值作为门控指标，仅低于阈值的组可进入回放
- 回放单元为完整GRPO组，保留原生组内优势对比结构，不修改原有新鲜样本生成流，仅将筛选后的回放组混入训练批次，无额外辅助生成、训练模块
- 工程优化：回放筛选时单次前向传播同时计算Drift和刷新Headroom，满回放预算即停止扫描，缓冲区采用固定容量FIFO队列，计算开销极低

**关键实验结果**：覆盖数学推理、多模态推理、Agent搜索三类任务，对比朴素GRPO、朴素回放、ExGRPO、BAPO等基线：数学推理任务上Avg Mean@32达0.3533，超过所有基线；Agent搜索任务仅用匹配基线的新鲜样本量，Avg Mean@32达0.3577，较1.5倍新鲜样本量的GRPO高11.4%，单步训练耗时低15.7%，实现帕累托优化；多模态推理上Avg Mean@32达0.4137，优于所有对比方案。

最值得记住的一句话：回放优化不需要绑定复杂辅助模块，仅通过学习价值排序+兼容性门控的双维度纯控制机制，就能在低改造成本、低计算开销前提下实现效果和训练效率的双重提升。
