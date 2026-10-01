---
title: Semifactual Credit-Augmented Policy Optimization
title_zh: 半事实信用增强策略优化（SCAPO）
authors:
- Junshu Pan
- Zhizhang Fu
- Shulin Huang
- Yiran Ding
- Zifan Cheng
- Wenqi Shao
- Qiaosheng Zhang
- Yue Zhang
affiliations:
- 浙江大学
- 西湖大学
- 上海创新研究院
- 上海人工智能实验室
arxiv_id: '2609.40360'
url: https://arxiv.org/abs/2609.40360
pdf_url: https://arxiv.org/pdf/2609.40360
published: '2026-09-30'
collected: '2026-10-01'
category: Training
direction: RLVR策略优化 · Token级信用分配
tags:
- RLVR
- GRPO
- Credit Assignment
- LLM Reasoning
- Semifactual Intervention
one_liner: 基于半事实扰动的token级信用分配优化GRPO，提升LLM推理精度与泛化能力
practical_value: '- 电商/导购Agent场景可复用半事实扰动方法，构造不改变用户需求的query变体，解码时过滤高漂移token，无需更新权重即可提升query理解、推荐理由生成的鲁棒性

  - 用RL做推荐文案生成、query改写微调时，可借鉴SCAPO的token级信用分配思路，仅降低不稳定无关token的优势，无需额外引入奖励模型即可提升细粒度训练效果

  - 半事实扰动的四类构造方法（改写/拼写错误/无关场景/无关上下文）可直接用于搜索推荐系统的鲁棒性测试，低成本构造大量分布外测试用例'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RLVR（带可验证奖励的强化学习）是当前提升LLM推理能力的主流方案，但代表方法GRPO给同一条回复的所有token分配相同的全局优势，会强化模型对prompt无关特征的虚假依赖，导致推理结果对输入扰动敏感、泛化性差。
### 方法关键点
- 构造4类半事实prompt扰动：自然语言改写、轻微拼写错误、无关场景包装、追加无关上下文，保证问题核心和答案不变，仅调整无关特征
- 用teacher-forcing计算固定回复下每个token在原prompt和扰动prompt下的概率漂移，作为token级虚假依赖的度量
- 仅对组内相对不稳定的token降低GRPO全局优势，不给稳定token额外奖励，避免将稳定性等同于正确性
- 仅在训练早期加信用增强，后续用标准GRPO训练，额外计算开销仅占总训练时长的1.8%
### 关键实验
在DAPO-Math-17K数据集上训练Qwen3-4B和1.7B Base模型，对比GRPO、FIPO、CF-GRPO等主流RLVR方法；SCAPO在AIME 2024-2026数据集上准确率分别比GRPO高5.63和4.17个百分点，收敛速度快1倍以上，在所有分布外推理基准上均取得最优效果。
### 核心结论
仅降低不稳定token的信用、不额外奖励稳定性的半事实信号，是提升RL训练的LLM推理鲁棒性的低成本有效手段。
