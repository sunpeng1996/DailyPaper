---
title: Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning
title_zh: 面向智能体强化学习的单轨迹异步优化算法SAO
authors:
- Zhenyu Hou
- Yujiang Li
- Jie Tang
- Yuxiao Dong
affiliations:
- Tsinghua University
- Z.AI
arxiv_id: '2607.07508'
url: https://arxiv.org/abs/2607.07508
pdf_url: https://arxiv.org/pdf/2607.07508
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: 智能体强化学习 · 异步训练优化
tags:
- Reinforcement Learning
- Asynchronous Training
- GRPO
- Agentic LLM
- LLM Post-training
one_liner: 提出单轨迹异步RL优化框架SAO，解决异步训练稳定性与异策略漂移问题，性能显著优于GRPO
practical_value: '- 电商导购/内容推荐类LLM Agent做RLHF微调时，可直接替换GRPO的组采样为SAO的单轨迹异步训练，消除长轨迹拖尾导致的GPU
  idle，预计可提升集群利用率30%以上

  - 异步RL的异策略修正可复用双端token级裁剪+掩码策略，直接复用rollout阶段的log概率计算重要性权重，无需维护多版本旧策略快照，大幅降低工程实现复杂度

  - 单轨迹RL的高方差问题可借鉴两个trick：价值模型更新频率设为策略的2倍、冻结价值模型的Attention层仅优化MoE层，可有效降低价值估计噪声，避免训练崩溃

  - 实时适配用户偏好的在线学习场景（如动态风格的商品文案生成Agent），SAO天然适配单轨迹反馈的生产环境，比滑动窗口均值基线的偏好适配速度快30%+，收敛效果更优'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM RL pipeline多为同步架构，在长轨迹智能体任务（多轮交互、代码、推理）中，轨迹长度差异大导致短轨迹需等待慢轨迹返回才能开始训练，GPU idle率高；异步RL虽能提升利用率，但存在异策略漂移、训练不稳定问题，且主流GRPO的组采样需要等待同组所有样本返回，与异步架构不兼容，也无法适配仅能获得单轨迹反馈的在线学习场景。
### 方法关键点
- 双端token级重要性采样裁剪：直接使用rollout阶段生成的log概率计算重要性权重，超出[1-εl, 1+εh]区间的token直接掩码不参与梯度计算，无需维护旧策略快照，大幅降低异策略噪声
- 单轨迹采样替代组采样：每个prompt仅生成1条轨迹，完成后立即送入训练，消除组采样的同步等待开销；通过三类设计解决单轨迹梯度方差高问题：1）价值模型更新频率为策略的2倍，快速适配策略变化；2）冻结价值模型的Attention层，仅优化MoE层，提升价值模型训练稳定性；3）提出跳过观测token的GAE估计，仅在模型生成的动作token间计算优势，避免环境反馈引入噪声
### 关键结果
在4个数学推理基准（AIME2025、BeyondAIME、HMMT Nov2025、IMOAnswerBench）和1个代码基准SWE-Bench Verified上测试，SAO稳定训练1000步无崩溃，AIME2025准确率达97.3%，较GRPO提升13.1pp；SWE-Bench Verified准确率29.8%，较GRPO提升2.8pp；模拟在线偏好切换场景下，较滑动窗口均值基线的适配速度快40%，稳定奖励高20%。

**最值得记住的一句话**：单轨迹异步RL配合优化后的价值模型设计，不仅能解决GRPO组采样与异步训练、在线学习的适配问题，还能实现比GRPO更优的性能和训练稳定性。
