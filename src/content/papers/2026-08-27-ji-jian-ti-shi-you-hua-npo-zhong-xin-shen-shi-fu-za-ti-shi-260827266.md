---
title: 'Naive Prompt Optimization: Rethinking the Need for Complex Prompt Search'
title_zh: 极简提示优化NPO：重新审视复杂提示搜索的必要性
authors:
- Yuan Chang
- Xiaoqi Chen
affiliations:
- Purdue University
arxiv_id: '2608.27266'
url: https://arxiv.org/abs/2608.27266
pdf_url: https://arxiv.org/pdf/2608.27266
published: '2026-08-27'
collected: '2026-08-28'
category: Agent
direction: Agent 轻量提示优化
tags:
- Prompt Optimization
- LLM Agent
- Model Transfer
- Rollout Efficiency
- Lightweight Tuning
one_liner: 提出单谱系轻量提示优化方法NPO，用更少rollout达到比肩复杂方案的性能
practical_value: '- 业务侧Agent（如导购、客服、内容生成Agent）的prompt调优可直接复用NPO方案，无需搭建复杂的多候选prompt搜索框架，省算力且迭代速度提升30%以上

  - 小参数模型上优化得到的prompt可直接迁移到同系列大模型，无需针对大模型重新优化，大幅降低大模型适配业务的prompt tuning成本

  - 做prompt优化/RL方法效果对比时，复用论文提出的共享随机种子+约束解码方案，可排除环境随机噪声和输出格式误差，大幅提升评估结果可信度

  - 资源有限时优先提升教师模型能力，比优化prompt搜索策略的ROI更高，如用GPT-4o级模型当教师优化端侧小模型prompt，性价比远高于复杂搜索方案'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前自动提示优化方案普遍采用多候选池搜索、贝叶斯优化等复杂机制，算力开销大、落地门槛高，而提示优化本身具备远低于权重微调的部署与适配成本，是Agent快速适配业务场景的核心技术，亟需兼顾效果与效率的轻量方案。

### 方法关键点
- 单谱系迭代：仅维护一条prompt迭代链路，无需维护多候选池，无复杂搜索逻辑
- 滑动窗口反馈：每次迭代输入最近W轮的prompt、完整rollout轨迹与对应奖励，而非仅输入历史prompt和标量分数
- 纯LLM驱动：直接由教师模型基于反馈生成下一轮prompt，无额外规则或优化器模块

### 关键结果
在IFBench指令跟随、HotpotQA多跳问答、22个TextArena交互游戏上对比GEPA（复杂提示优化）、GRPO（权重微调）基线：
- 用GPT-5.5作为教师时，NPO在HotpotQA上用比GEPA少10%的rollout达到0.68准确率，领先GEPA 8个百分点；IFBench上达到0.88准确率，领先GEPA7个百分点
- 优化后的prompt同家族模型迁移保留90%以上性能增益，跨家族迁移也能获得平均0.1+的提升
- 22个交互游戏中NPO与GEPA效果基本持平，GRPO仅在部分不适合提示优化的任务上占优

### 核心结论
强教师模型的推理能力+完整轨迹反馈，可完全替代复杂的提示侧搜索机制，轻量方案在多数业务场景下ROI更高
