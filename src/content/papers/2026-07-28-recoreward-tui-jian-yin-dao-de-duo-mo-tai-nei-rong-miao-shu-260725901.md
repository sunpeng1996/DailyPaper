---
title: 'RecoReward: Recommender-Guided Multimodal Description Generation for Recommendation'
title_zh: RecoReward：推荐引导的多模态内容描述生成方法 适配下游推荐任务
authors:
- Guohong Mu
- Yueyang Liu
- Jiangxia Cao
- Changxin Lao
- Zijie Zhuang
- Yuhui Zhang
- Jiaqi Feng
- Ruochen Yang
- Shuang Yang
- Zhaojie Liu
affiliations:
- Nankai University
- Kuaishou Technology
- Institute of Information Engineering, CAS
- University of Chinese Academy of Sciences
arxiv_id: '2607.25901'
url: https://arxiv.org/abs/2607.25901
pdf_url: https://arxiv.org/pdf/2607.25901
published: '2026-07-28'
collected: '2026-07-29'
category: GenRec
direction: 生成式推荐 · 多模态语义特征优化
tags:
- MLLM
- Reinforcement Learning
- Two-Tower
- Multimodal Recommendation
- Reward Design
one_liner: 训练阶段通过推荐器衍生的RAS奖励优化MLLM 推理仅需内容输入即可产出提升推荐效果的共享描述
practical_value: '- 可复用RAS奖励设计思路：针对商品/短视频/直播内容，用历史交互用户与非交互用户的embedding均值差作为RL奖励，优化MLLM生成描述的推荐适配性，推理无需用户信息可直接缓存复用，大幅降低推理成本

  - 可复用训练-推理边界设计：训练阶段仅用冻结的双塔推荐器给MLLM提供奖励信号，MLLM侧无需感知用户特征，避免推理时依赖用户数据导致的架构复杂度提升，兼容现有召回链路

  - 超参数初始值可直接参考论文结论：直播/短视频推荐场景下，非目标用户惩罚系数λ取2、单样本rollout数取12、奖励计算用户采样数取25时效果最优'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有MLLM生成多模态内容描述用于推荐时存在两类问题：仅基于内容生成的方法未结合下游用户交互信号，描述语义与推荐目标匹配度低；用户条件生成方法推理时依赖用户历史信息，需要为每个用户单独生成无法缓存复用，推理成本极高，无法适配大规模工业推荐场景。

### 方法关键点
- 提出Recommender Affinity Score (RAS)奖励：将历史交互用户embedding均值减去非交互用户embedding均值乘以系数λ，再与生成描述的embedding做内积作为语义奖励，叠加格式校验奖励保证输出可解析
- 训练边界隔离：冻结双塔推荐器仅在训练阶段提供奖励信号，MLLM训练时不接收任何用户特征输入，推理仅需多模态内容即可生成共享描述，可直接缓存用于全量用户的召回匹配
- 采用GRPO组相对策略优化，无需额外critic网络，降低训练复杂度

### 关键实验
数据集为快手1周直播行为数据，包含6.99万条直播、739万条交互，对比基线覆盖DSSM、LightGCN等传统推荐模型，Qwen3.5、InternVL3.5等开源MLLM，及GPT-5、Gemini 3.1 Pro等商用模型。RecoReward-9B在7个召回指标上相对Qwen3.5-9B提升31.7%~40.4%，超过所有对比基线；在线A/B测试核心页面有效用户渗透率提升0.265%，外流曝光提升0.791%，外流用户提升0.74%。

### 核心结论
下游推荐的用户交互信号可以通过训练阶段的奖励注入MLLM，在不增加推理复杂度的前提下大幅提升生成语义特征的推荐适配性
