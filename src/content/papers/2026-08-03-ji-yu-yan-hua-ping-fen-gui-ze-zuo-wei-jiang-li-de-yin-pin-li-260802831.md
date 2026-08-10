---
title: Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning
title_zh: 基于演化评分规则作为奖励的音频推理强化学习框架
authors:
- Fangxu Yu
- Tao Feng
- Dehai Min
- Zinan Lin
- Weijia Xu
- Michael Xu
- Philip S. Yu
- Ge Liu
- Tianyi Zhou
affiliations:
- University of Maryland, College Park
- University of Illinois Urbana-Champaign
- University of Illinois Chicago
- Microsoft Research
- MBZUAI
arxiv_id: '2608.02831'
url: https://arxiv.org/abs/2608.02831
pdf_url: https://arxiv.org/pdf/2608.02831
published: '2026-08-03'
collected: '2026-08-10'
category: Reasoning
direction: 音频推理 · 强化学习动态奖励设计
tags:
- Reinforcement Learning
- Audio Reasoning
- Dynamic Reward
- Rubric Generation
- Process Supervision
one_liner: 提出音频驱动自演化评分规则奖励的强化学习框架，显著提升音频推理任务表现
practical_value: '- 动态评分规则设计思路可迁移到LLM4Rec的RLHF流程中，替代静态人工奖励规则，根据当前模型生成结果的短板动态调整奖励权重，提升推荐理由/话术生成的合理性

  - 单样本定制化奖励生成逻辑可复用在多模态商品检索/语音搜索场景中，基于原始音频/图像特征生成对齐感知证据的细粒度奖励信号，降低人工标注成本

  - 奖励随模型能力迭代演化的机制可用于Agent工具调用能力训练，避免静态规则随模型能力提升出现的奖励饱和问题，持续优化Agent决策合理性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有音频推理RL奖励设计存在两类局限：结果导向奖励仅监督最终答案，无法约束模型关注原始音频输入；过程导向奖励依赖粗粒度人工固定规则，无法适配单样本需求，且随模型策略提升会出现奖励饱和，无法提供持续有效监督。
### 方法关键点
AudioRubrics强化学习框架基于原始音频波形生成单样本专属评分规则，结合模型当前生成的rollout结果，按组动态更新评分规则及对应权重，持续定向优化当前模型短板，奖励信号始终锚定原始声学证据，避免规则静态化导致的监督失效。
### 关键结果
在3个音频推理基准测试中表现大幅优于各类开源及训练类基线；奖励效果随评分规则生成器与判别器的能力提升线性增长；模型推理长度收敛至稳定区间，既无退化坍缩也无无限增长，音频感知能力得到显著提升。
