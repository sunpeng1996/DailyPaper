---
title: 'Stale but Stable: Staleness-Adaptive Trust Regions for Stabilizing Asynchronous
  Reinforcement Learning'
title_zh: Stale but Stable：面向异步强化学习稳定性的陈旧度自适应信任域
authors:
- Junyao Yang
- Yucheng Shi
- Zongxia Li
- Zhongzhi Li
- Ruhan Wang
- Xiangxin Zhou
- Kishan Panaganti
- Haitao Mi
- Leowei Liang
affiliations:
- Tencent Hy LLM Frontier
- National University of Singapore
- University of Maryland, College Park
- University of Georgia
- Indiana University
arxiv_id: '2607.18722'
url: https://arxiv.org/abs/2607.18722
pdf_url: https://arxiv.org/pdf/2607.18722
published: '2026-07-20'
collected: '2026-07-22'
category: Training
direction: 异步RL · 训练稳定性优化
tags:
- Asynchronous RL
- Trust Region
- PPO
- MoE
- Training Stability
one_liner: 提出陈旧度自适应信任域SAT，作为PPO即插即用替代，提升高延迟异步RL训练稳定性与性能
practical_value: '- 做LLM-based推荐/Agent的RLHF对齐时，如果用异步流水线提升吞吐量，可直接复用SAT作为PPO裁剪的即插即用替代，仅增加少量张量运算即可解决高陈旧度下的训练崩溃问题

  - 适配MoE架构的推荐/大模型训练时，可搭配SAT+R3（路由重放）组合方案，同时解决策略滞后、引擎差异、MoE路由三类不一致导致的训练不稳定问题

  - 对于异步训练的离线策略校正，可复用「用当前批次log-ratio分位数自适应识别高陈旧度样本，仅收紧异常样本裁剪边界」的设计思路，平衡普通样本学习效率和异常样本稳定性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
异步RL通过解耦rollout采样与优化过程大幅提升吞吐量、最大化GPU利用率，是当前大模型RLHF、Agent训练的核心落地范式，但会天然产生由策略滞后、推理/训练引擎实现差异、MoE路由不一致共同导致的训练-推理陈旧度问题。固定裁剪阈值的PPO无法适配单批次内异质性的陈旧度分布：阈值过小会限制大部分低陈旧度样本的学习效率，阈值过大则会放任高陈旧度长尾样本的异常更新，最终导致训练崩溃、性能跳水。

### 方法关键点
- 用无梯度的采样log-ratio作为逐token/逐序列的陈旧度代理指标，无需额外系统埋点或标注
- 基于当前批次的陈旧度分位数自动识别高陈旧度长尾样本，仅对该部分样本按陈旧度收缩PPO裁剪区间的单侧边界（比例偏大则收缩上界，比例偏小则收缩下界），普通样本和拉回行为策略的更新完全不受影响
- 是PPO裁剪的即插即用替代，仅增加少量张量运算，额外计算成本可忽略

### 关键实验结果
基于Qwen3-30B MoE模型，用SGLang做采样引擎、Megatron做训练流水线，在AIME24数学推理任务上对比GRPO、GSPO、DPPO等主流baseline：SAT-GSPO+R3方案在配置lag=1（低陈旧度）时AIME24 avg@8达35.83，lag=8（高陈旧度）时达34.79，相对基线GSPO分别提升3.58、3.33个点，且完全避免高陈旧度场景下的训练崩溃。

最值得记住的一句话：异步训练中配置的延迟只是粗粒度系统指标，真正影响优化的是逐样本的实际陈旧度分布，自适应适配长尾陈旧度的裁剪策略能在不损失学习效率的前提下大幅提升训练稳定性。
