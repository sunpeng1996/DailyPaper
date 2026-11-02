---
title: 'CRoS: Causality Reward on Scrambled CoTs Improves Accuracy and Reasoning Faithfulness'
title_zh: CRoS：基于打乱CoT的因果奖励提升推理准确率与忠实度
authors:
- Xiao Yu
- Justin Chih-Yao Chen
- Zaid Khan
- Hyunji Lee
- Mohit Bansal
affiliations:
- UNC Chapel Hill
arxiv_id: '2610.42054'
url: https://arxiv.org/abs/2610.42054
pdf_url: https://arxiv.org/pdf/2610.42054
published: '2026-10-30'
collected: '2026-11-02'
category: Reasoning
direction: LLM推理优化 · CoT因果奖励设计
tags:
- CoT
- Causality
- RLVR
- Reasoning
- Faithfulness
one_liner: 基于CoT步骤顺序打乱的无内容扰动设计因果奖励，提升LLM推理准确率与忠实度
practical_value: '- 电商导购Agent、营销规则计算等多步推理场景，可引入CRoS作为RL辅助奖励，强化CoT与最终决策的因果关联，避免无意义推理步骤，提升决策可解释性与可信度

  - 生成式推荐的理由生成、用户需求多步拆解场景，可复用CRoS的扰动思路：不修改推理内容仅打乱步骤顺序，快速评估推理与输出的因果性，筛选高忠实度的生成结果

  - 做LLM推理类RL训练时，避免使用截断/插错类因果奖励（会导致模型生成短推理、减少自我修正），优先选用CRoS的顺序扰动奖励，同时提升OOD泛化能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有基于可验证奖励的强化学习（RLVR）训练LLM推理时仅依赖结果正确性，无法保证思维链（CoT）与最终答案的因果关联，容易出现CoT仅为事后合理化、模型靠捷径答题的问题。现有CoT因果度量方法通过截断步骤、注入错误扰动CoT，会改变推理内容，混淆「真实因果性」和「对内容变化的敏感度」，用作训练奖励时还会导致模型生成低信息量CoT、减少探索与自我修正的副作用。
### 方法关键点
- 提出CRoS因果奖励，仅打乱CoT的步骤顺序不修改每步内容，避免内容扰动带来的混淆效应，保留所有推理信息
- 计算原始CoT与M个打乱顺序CoT下，原始答案的对数概率差作为因果得分，差值越大说明CoT对最终答案的因果影响越强
- 作为辅助奖励与结果奖励结合，仅对回答正确的样本按因果得分排名分配相对奖励，消除跨问题的得分尺度差异
### 关键实验结果
基于Gemma-3-4B在Reasoning Gym的2个数据集训练，在5个未见过的逻辑/游戏数据集上做OOD测试，对比仅结果奖励、4种现有因果奖励基线：
- OOD平均准确率46.8%，比最强基线高3.0pp，比纯结果奖励高5.0pp，问题难度越高优势越显著
- CoT-Pass@K平均43.4%，比基线高2.0pp，推理过程正确性更高
- CoT忠实度（hint影响答案时的明确承认率）34.0%，比最强基线高13.8pp

> 最值得记住的一句话：评估CoT因果性时，仅改变步骤顺序不修改内容的扰动，比截断/插错类扰动更可靠，用作训练奖励能同时提升推理准确率和CoT忠实度
