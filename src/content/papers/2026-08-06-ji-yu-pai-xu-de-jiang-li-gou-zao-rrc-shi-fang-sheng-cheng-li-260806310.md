---
title: 'RRC: Unlocking Generative Reward Models in LLM Reinforcement Learning via
  Ranking-Based Reward Construction'
title_zh: 基于排序的奖励构造RRC：释放生成式奖励模型在LLM RL中的潜力
authors:
- Chenglong Wang
- Ziming Zhu
- Yifu Huo
- Bei Li
- Qiaozhi He
- Yan Ding
- Xiaoyang Hao
- Yuxin Gao
- Tianhua Zhou
- Xiaojia Chang
affiliations:
- Northeastern University
- NiuTrans Research
- Chinese Academy of Sciences
- Kunming University of Science and Technology
- Independent Researcher
arxiv_id: '2608.06310'
url: https://arxiv.org/abs/2608.06310
pdf_url: https://arxiv.org/pdf/2608.06310
published: '2026-08-06'
collected: '2026-08-07'
category: Training
direction: LLM训练 · 生成式奖励模型RL优化
tags:
- Generative Reward Model
- RLHF
- Ranking-based Reward
- Reinforcement Learning
- LLM Alignment
one_liner: 提出排序导向奖励构造方法RRC，解决生成式奖励模型与RL标量范式适配问题，提升LLM RL性能
practical_value: '- 做Agent/生成式推荐的RLHF对齐时，生成式奖励模型不要强行输出标量得分，改用两两排序转相对奖励的方式，可避免概率塌陷、提升对齐效果

  - 大规模RL训练优先选锚点引导排序（AGR）策略，用少量固定锚点做对比，把生成式奖励模型调用复杂度从O(m²)降到O(mn)，平衡效果与算力成本

  - 偏好判断噪声大的场景（如电商文案/推荐结果的用户偏好打分），可复用多数投票+冲突感知排序调整方案，提升偏好排序鲁棒性

  - 生成式奖励模型的推理算力投入可线性换效果，8次投票/8个锚点就能拿到大部分收益，可根据业务算力预算灵活配置'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
生成式奖励模型（GRM）在响应排序任务上效果远超判别式奖励模型，但应用到RL时优势大幅衰减，核心原因是GRM的比较式优化目标和现有RL要求的标量奖励范式不匹配，直接用偏好token概率作为奖励会存在概率塌陷、置信度与真实偏好不对齐等问题，无法充分释放GRM的能力。

### 方法关键点
- 提出排序导向的奖励构造（RRC）框架，不用GRM输出标量得分，直接从相对偏好排序转换得到符合RL要求的奖励，满足顺序保持、间隔感知两个核心要求
- 自竞争排序（SCR）：对同一输入的多个采样响应做两两比较，用胜出次数作为奖励；加入多数投票降噪、Kemeny规则解决循环偏好冲突，保证排序一致性
- 锚点引导排序（AGR）：引入少量固定参考策略生成的锚点响应，仅需把采样响应和锚点做对比，用胜出锚点的数量作为奖励，把GRM调用复杂度从O(m log m)降到O(mn)，适配大规模RL训练

### 关键实验
用HelpSteer3数据集训练3B/8B规模的GRM，在GRPO算法下做RL训练，对比概率基奖励构造（PRC）、判别式RM、DPO/SimPO等基线，在6个基准上均取得一致提升：8B GRM搭配RRC+8次投票，在AlpacaEval2上从35.8%提升到41.3%，ArenaHardV2从8.0%提升到11.2%，MMLU-Redux从52.9%提升到57.3%；投票次数、锚点数量与效果呈正相关，8个锚点即可拿到大部分收益，边际收益随规模提升递减。

> 最值得记住的一句话：生成式奖励模型的核心优势是比较排序能力，强行要求其输出标量奖励属于削足适履，基于相对排序转换奖励的方案更能释放其性能潜力。
