---
title: On the Reliability of Majority-Vote Pseudo-Labels in Test-Time Reinforcement
  Learning
title_zh: 测试时强化学习中多数投票伪标签的可靠性分析与优化
authors:
- Haoyu Wang
- Ru Wang
- Yuanyuan Wang
- Jiaxian Guo
- Mingming Gong
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- The University of Melbourne
- The University of Tokyo
arxiv_id: '2611.09872'
url: https://arxiv.org/abs/2611.09872
pdf_url: https://arxiv.org/pdf/2611.09872
published: '2026-11-06'
collected: '2026-11-09'
category: Training
direction: LLM对齐 · 测试时强化学习DPO优化
tags:
- DPO
- Test-Time RL
- Pseudo-Label
- Distributional Robustness
- LLM Alignment
one_liner: 分解多数投票伪标签两类误差，提出带缓存的prompt条件鲁棒DPO，24/30场景优于SOTA基线
practical_value: '- 做电商垂域LLM/生成式推荐/Agent自对齐时，多数投票生成伪标签无需盲目增加采样数：群体多数偏倚无法通过加采样消除，优先投入资源缓解有限采样波动即可

  - 在线DPO做领域适配（如新品类推荐理由生成、客服Agent对齐）时，可复用prompt级动态温度机制：按投票一致度设置权重，低一致度prompt做更保守更新，避免噪声带偏模型

  - 在线迭代更新LLM/Agent时，可加入缓存回放机制：存储之前输出高度一致的prompt样本，后续同prompt伪标签冲突时回放缓存样本，大幅缓解自监督遗忘'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
测试时强化学习（TTRL）可让预训练LLM在无标注目标域自适应，无需外部标注，适配电商新类目、垂域Agent等缺标注场景，但现有基于多数投票的伪标签可靠性缺乏系统分析，噪声易导致模型更新退化甚至崩溃。
### 方法关键点
- 理论拆解多数投票伪标签两类误差：群体多数偏倚（行为策略的群体模态答案本身错误，无外部监督无法修正）、有限采样波动（采样多数与群体模态不一致，可缓解）
- 提出PC-Dr.DPO：按每个prompt的投票一致度动态设置鲁棒重加权温度，一致度越低温度越小，更新越保守，降低采样敏感样本的影响
- 新增缓存机制：首次出现输出全一致的prompt时缓存样本，后续同prompt新伪标签与缓存冲突时直接回放缓存监督，缓解自监督遗忘
- 用轨迹隐式DPO分数替代单纯频次投票，优化伪标签构造
### 关键结果
在6个数学/知识推理基准、5个不同规模/家族的LLM骨干上测试，对比RENT、TTRL、Co-Reward三个SOTA TTRL基线，PC-Dr.DPO在24/30的模型-基准组合上打平或超过最优基线；缓存机制可提升Llama-3.2-3B在MATH500上的准确率2.1个百分点。
### 核心结论
多数投票伪标签的群体偏倚无法通过增加采样数消除，实际业务中优先通过prompt级动态加权和缓存缓解可优化的采样波动，避免盲目堆采样量浪费算力。
