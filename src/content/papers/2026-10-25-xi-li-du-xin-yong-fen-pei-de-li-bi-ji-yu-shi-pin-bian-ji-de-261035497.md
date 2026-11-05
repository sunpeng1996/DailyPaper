---
title: 'When Fine-Grained Credit Assignment Helps and Hurts: Multimodal Agentic Reinforcement
  Learning through Video Editing'
title_zh: 细粒度信用分配的利弊：基于视频编辑的多模态智能体强化学习研究
authors:
- Lei Zhao
- Zongheng Cao
- Xinyu Hu
affiliations:
- University of Pennsylvania
- Philo Labs
arxiv_id: '2610.35497'
url: https://arxiv.org/abs/2610.35497
pdf_url: https://arxiv.org/pdf/2610.35497
published: '2026-10-25'
collected: '2026-11-05'
category: Agent
direction: 多模态Agent · RL信用分配优化
tags:
- Reinforcement Learning
- Credit Assignment
- Multimodal Agent
- GRPO
- Process Reward
one_liner: 在视频编辑多模态Agent场景下验证不同粒度信用分配的适用边界与优化方案
practical_value: '- 长周期多步交互Agent（如导购Agent、短视频生成Agent）可按交互轮长选策略：<40轮短任务用纯结果GRPO性价比最高，>60轮长任务加衰减式过程奖励可提效40%+

  - 过程奖励权重不要固定全程使用：训练前中期用过程奖励引导正确行为（如工具调用、信息核查），后期衰减为0可避免奖励黑客（如冗余调用、无效推理消耗配额）

  - 长序列Agent训练慎用OPSD自蒸馏，对特权信息敏感性极高，非最优分步建议类特权信息会直接导致性能崩塌'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期多模态Agent的RL训练中，细粒度信用分配的收益边界长期不清晰，过程奖励易出现奖励黑客问题，缺少真实复杂任务的实证结论，而视频编辑是集多模态感知、长时序规划、工具调用于一体的理想测试场景。

### 方法关键点
- 构建4类真实电影预告片编辑任务集：Content Selection(22.3轮)、Narrative Sequencing(15.3轮)、Rough Cut(21.8轮)、Fine Cut(87.2轮)，覆盖不同交互长度与任务复杂度
- 对比4种不同粒度信用分配方案：① 轨迹级：纯结果GRPO；② 轮次级：固定权重GRPO+PRM、衰减权重GRPO+PRM（20-30步将PRM权重从0.5降到0）；③ token级：OPSD自蒸馏（含参考答案、分步建议两种特权信息）
- 过程奖励与结果奖励用不同LLM裁判隔离避免信号泄露，所有实验基于Qwen3.5-9B训练50步，验证集重复4次评估降方差

### 关键结果
- 平均60+轮的Fine Cut长任务上，衰减PRM比纯结果GRPO相对提升45.4%；平均30-40轮的3类短任务上，纯结果GRPO已足够有竞争力，固定PRM最多仅提升10.4%，甚至因44.1%的截断率导致整体性能下降
- 固定权重PRM会出现奖励黑客：过程奖励持续上升但任务完成率、结果得分下降，权重衰减可将截断率降到6.2%，同时保留前期过程奖励的收益
- OPSD对特权信息极敏感：参考答案作为特权信息时性能接近基线，分步建议作为特权信息时性能下降84.4%

**最值得记住的结论**：短交互周期Agent用纯结果奖励性价比最高，长周期任务用前中期过程奖励+后期衰减的方案可平衡行为引导与任务完成率，避免奖励黑客。
