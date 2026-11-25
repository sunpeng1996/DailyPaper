---
title: Reinforcement Learning Can Be Recovered From Its Own Rollouts
title_zh: 仅用训练过程生成的rollout数据即可还原强化学习的完整训练效果
authors:
- Jiayi Sheng
- Jingwen Gu
- Guanning Zeng
- Zhaoyi Zhou
- Stefano Viel
- Qianqian Wang
- Fahim Tajwar
- Andrea Zanette
affiliations:
- Carnegie Mellon University
- University of Illinois Urbana-Champaign
- Tufa Labs
- Harvard University
arxiv_id: '2611.33102'
url: https://arxiv.org/abs/2611.33102
pdf_url: https://arxiv.org/pdf/2611.33102
published: '2026-11-24'
collected: '2026-11-25'
category: Training
direction: 强化学习训练 · rollout数据复用
tags:
- Reinforcement Learning
- SFT
- Rollout Reuse
- RLHF
- Training Optimization
one_liner: 通过按时间顺序SFT回放RL训练存档的rollout，无需奖励即可还原在线RL的全轨迹与最终性能
practical_value: '- 做LLM对齐/推荐系统RL排序训练时，无需丢弃每轮生成的rollout，按时间顺序做SFT回放即可复现RL训练效果，省掉重新采样rollout的高昂推理/探索成本

  - 多任务specialist模型合并无需做权重融合，直接按时间混合各模型的历史rollout做SFT，效果优于权重算术、TIES等常用合并方法，适合电商多品类推荐Agent合并场景

  - 大模型蒸馏时无需专门调用最终大模型生成蒸馏样本，复用RL训练最后几轮的rollout做SFT即可达到和标准蒸馏相近的效果，显著降低小模型蒸馏成本，适合端侧低延迟推荐Agent的蒸馏

  - 不要尝试用离线RL回放历史rollout，会出现灾难性崩溃，加重要性采样仅能延迟崩溃，直接用SFT更稳定'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
在线RL尤其是LLM的RLHF训练中，每轮生成的rollout采样成本极高，但常规训练后都会直接丢弃，知识仅存在于模型权重中；尝试用离线RL回放存档rollout还原训练会出现灾难性崩溃，缺乏稳定的rollout复用方案。

### 方法关键点
- 放弃离线RL的梯度更新方式，改用最大似然的SFT目标，直接拟合每轮rollout的生成分布，避免偏差累积
- 按rollout生成的时间顺序回放，每批rollout做一次SFT更新，无需奖励信号，也无需区分正确/错误响应
- 若只需还原最终性能，仅需回放最后几轮RL的rollout反复做SFT即可，无需全量历史数据
- 多模型合并场景下，按时间顺序混合回放各specialist的rollout做SFT，即可得到多能力模型

### 关键结果数字
- 在MATH-500、GSM8K等推理任务上，按时间顺序SFT回放的轨迹误差低于0.01，最终性能和在线RL的差距小于1%
- 仅用最后1轮RL的rollout做SFT，就能恢复99%以上的在线RL最终性能，最多仅需50轮的rollout就能完全对齐
- 多specialist合并场景下，该方法比权重合并（任务算术、TIES、权重平均）的任务性能损失低30%以上
- 跨模型蒸馏场景下，复用源模型rollout的SFT效果和标准蒸馏的性能差距小于2%

**最值得记住的一句话**：RL训练的大部分算力投入是用于发现更优的采样分布，而非从样本中学习该分布，存档的rollout本身就是极高价值的训练资产。
