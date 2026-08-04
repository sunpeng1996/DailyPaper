---
title: 'HindSearch: Trajectory-Level Hindsight Critique for Search-Augmented Reinforcement
  Learning'
title_zh: HindSearch：面向搜索增强强化学习的轨迹级事后批判方法
authors:
- Haowei Liu
- Jiamian Wang
- Hsin-Tai Wu
- Zhiqiang Tao
- Yi Fang
affiliations:
- Santa Clara University
- Rochester Institute of Technology
- Independent Researcher
arxiv_id: '2608.01597'
url: https://arxiv.org/abs/2608.01597
pdf_url: https://arxiv.org/pdf/2608.01597
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: 搜索增强Agent · RL训练优化
tags:
- Search-Augmented Agent
- GRPO
- On-Policy Distillation
- Hindsight Critique
- Multi-hop QA
one_liner: 面向搜索增强强化学习，基于GRPO引入轨迹级事后批判自蒸馏，提升多跳搜索问答EM表现
practical_value: '- 训练电商导购Agent、query改写/推荐Agent时，可复用事后批判逻辑：对失败交互轨迹，用大模型结合已知正确结果生成修正提示做on-policy蒸馏，解决纯稀疏奖励训练不稳定问题

  - 工程上可直接复用GRPO加辅助损失的架构：仅对搜索/query生成类token计算蒸馏损失，不更新回答/导购话术类token，兼顾任务效果和生成稳定性，额外训练开销仅15%

  - 可复用损失设计trick：对蒸馏损失加[0,1]范围clamp避免梯度异常，用学生模型的初始化权重作为冻结教师，避免跨尺寸教师导致的训练崩溃

  - 搜索类Agent训练优化可优先落地黄金答案事后信号，该方法验证其贡献了80%以上的效果提升，是性价比最高的优化点'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前搜索增强LM Agent普遍采用二元精确匹配（EM）作为训练奖励，仅能标识轨迹成败，无法传递失败原因，存在长程信用分配难、训练不稳定的问题；现有过程奖励方法仅能对单步打分，无法给出明确修正方向，也未充分利用训练阶段可直接获取的黄金答案信号，训练效率偏低。
### 方法关键点
- 设计轨迹级事后批判（TLHC）流程：每次GRPO rollout后，将所有失败轨迹连带对应的黄金答案输入冻结Judge大模型，生成1-2句指令性批判，明确指出搜索动作的修正方向
- 新增轻量辅助OPD损失：以学生模型的初始化权重作为冻结教师，将批判作为前缀拼接至每个搜索步骤的上下文，仅对<SEARCH>标签内的搜索动作token计算蒸馏损失，损失加[0,1]范围clamp避免梯度被 outliers 主导
- 总损失为原生GRPO损失加权重为0.01的OPD损失，训练全程Judge和教师模型均冻结，仅更新学生模型参数，推理阶段无需额外组件
### 关键结果
以Qwen2.5-3B-Instruct为骨干，在NQ、TriviaQA、HotpotQA等7个单/多跳QA基准测试，对比Search-R1 GRPO等10+基线，平均EM达39.4%，超出最强基线5.8个百分点；零样本基准和训练域基准的增益几乎一致，无过拟合问题；移除Judge的黄金答案访问权限后，81%的增益消失，验证事后黄金信号是核心贡献来源。
**最值得记住的结论**：训练带工具调用的Agent时，训练阶段可直接获取的黄金结果是性价比最高的监督信号，简单的事后批判蒸馏就能大幅降低稀疏奖励的训练难度。
