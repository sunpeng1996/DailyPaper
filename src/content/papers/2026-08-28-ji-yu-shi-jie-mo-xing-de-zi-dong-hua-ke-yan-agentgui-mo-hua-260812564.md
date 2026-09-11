---
title: Scaling Automatic Research Agents via World Models
title_zh: 基于世界模型的自动化科研Agent规模化训练方法
authors:
- Xiyuan Yang
- Sheikh Sarwar
- Jingru Cheng
- Zhan Shi
- Duanshun Li
- Huiyuan Chen
- Haiyang Zhang
- Xing Fan
- Chenlei Guo
- Jingrui He
affiliations:
- University of Illinois Urbana-Champaign
- Amazon
arxiv_id: '2608.12564'
url: https://arxiv.org/abs/2608.12564
pdf_url: https://arxiv.org/pdf/2608.12564
published: '2026-08-28'
collected: '2026-09-11'
category: Agent
direction: Agent 训练 · 世界模型 RL 优化
tags:
- World Model
- Reinforcement Learning
- GRPO
- Debiasing
- Agent Training
one_liner: 用世界模型替代RL训练中昂贵的环境执行，搭配去偏去噪机制实现3-4倍训练加速且效果优于基线
practical_value: '- 做Agent RL训练时，若真实环境采样成本高（如电商投放策略优化、推荐系统策略迭代），可复用WMRL范式：用轻量世界模型替代90%的真实环境调用，仅留10%样本做锚点，训练成本降70%+的同时保证效果不跌

  - 世界模型输出的矫正方案可直接迁移：Online Debiasing（保序回归在线校准）适配LLM judge、RAG召回打分等场景的系统偏差修正；逆方差加权融合适配多源异构奖励信号的融合场景

  - 推荐/广告场景的RL迭代中，可将离线预估模型作为世界模型，用小流量真实A/B数据做锚点矫正，大幅加快策略迭代速度，降低线上实验风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
AutoResearch Agent的RL训练依赖大量真实环境执行轨迹，生成侧可通过批处理大幅分摊计算成本，而执行侧每个样本需独占独立沙箱、GPU等资源，成本随训练规模线性增长，成为规模化训练的核心瓶颈。纯用世界模型替代真实环境会引入固有偏差和噪声，导致训练收敛性、最终效果大幅下降，需在效率和效果间找到平衡方案。

### 方法关键点
- 核心框架WMRL：用与Agent同架构的世界模型预测执行结果，替代真实环境执行，让执行侧也可通过批处理分摊计算，从根源消除执行瓶颈
- 10%比例锚点样本设计：小部分样本同时走真实环境执行和世界模型打分，作为矫正信号源，不会显著增加额外成本
- 两套无参矫正机制：Online Debiasing用保序回归拟合真实与模拟分数的单调映射，在线消除系统偏差；Inverse-Variance Denoising按两类信号的梯度方差逆权重融合，自动调整真实/模拟信号的贡献占比，抑制噪声影响

### 关键实验结果
- 测试数据集：AutoResearch任务用MLE-Dojo、DSBench，VLA落地场景用LIBERO-Long
- 对比基线：原生基座LLM、48B/120B大参数开源Agent、真实环境GRPO、无矫正纯世界模型RL
- 核心数字：AutoResearch任务训练速度提升3-4倍，4B模型效果超过48B开源Agent，9B模型超过120B开源Agent，最终表现比真实环境GRPO高1-3个百分点；VLA任务整体成功率比真实GRPO高2.9个点

只要任务的奖励获取成本高、可通过Agent产出物预测，且能获取小流量真实信号做锚点，WMRL范式即可通用，解决RL训练中执行而非生成的瓶颈问题。
