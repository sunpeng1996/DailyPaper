---
title: Selecting Diverse SFT Traces Improves Post-RL Generalization
title_zh: 选择多样化SFT推理轨迹可提升RL后模型泛化能力
authors:
- Dylan Zhang
- Mingyuan Wu
- Jinning Li
affiliations:
- University of Illinois Urbana-Champaign
- Google
arxiv_id: '2609.33780'
url: https://arxiv.org/abs/2609.33780
pdf_url: https://arxiv.org/pdf/2609.33780
published: '2026-09-26'
collected: '2026-09-30'
category: Training
direction: SFT数据选择 · RL训练优化
tags:
- SFT
- Reinforcement Learning
- Data Selection
- Reasoning LLM
- Diversity
one_liner: 提出轻量规则指纹筛选多样化SFT推理轨迹，无需模型调用即可大幅提升RL后泛化能力
practical_value: '- 做电商Agent推理、搜推query理解类LLM微调时，SFT阶段不要仅筛选准确率最高的样本，优先保留同问题下的多样化推理路径，可提升后续RLHF/GRPO后的OOD泛化效果

  - 可复用文中的轻量规则指纹方法，仅用CPU即可完成SFT样本多样性筛选，无需GPU或大模型调用，成本极低，适合业务快速落地

  - 训练商品文案生成、营销话术优化类模型时，同query下的多样化SFT轨迹能让后续RL阶段获得更多混合奖励信号，避免陷入局部最优，提升输出多样性和效果

  - 评估SFT数据质量不要唯准确率论，可将混合奖励样本占比作为SFT到RL过渡的核心诊断指标，提前预判RL后最终效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM推理训练主流采用「SFT+RL」两阶段流程，传统SFT数据选择仅关注正确性、长度等指标，忽略推理路径多样性，过高的SFT准确率反而会限制后续RL的学习空间与泛化能力，低代价的SFT筛选方案是业界迫切需求。

### 方法关键点
- 定义推理路径为问题求解的步骤序列，用规则生成固定长度指纹表征路径结构，仅需文本规则+随机投影，无需模型调用、梯度计算，可在CPU上高效运行
- 基于指纹做多样性选择：聚类后按簇大小分配配额，每簇内选距离已选样本最远的样本构建多样化SFT集，对比组选指纹空间最密集的相似样本集
- 核心逻辑：多样化SFT能让RL前的初始策略在更多问题上产生混合（既有正确也有错误）的rollout结果，为GRPO等group-relative类RL算法提供更多有效学习信号

### 关键实验
实验覆盖RLVE合成谜题、10个数学竞赛基准、3个开源推理语料，对比随机选择、梯度多样性、embedding筛选等基线：
1. OLMo3-7B在SFT未见过的环境上pass@8提升16.9个点
2. 单模型生成SFT候选池场景下，Qwen3-4B在10个数学基准上pass@8最高提升6.2个点
3. 210万样本池筛选仅需3小时单CPU，成本比embedding类方法低2个数量级，所有场景下效果均优于基线

### 核心结论
SFT的目标不只是训练出准确率更高的初始模型，更是要给后续RL阶段留下足够的学习信号和探索空间，多样化推理路径比单一高正确率更有价值
