---
title: 'S3AC: Stabilized, Selective, and Scalable Actor-Critic for LLM Reasoning'
title_zh: S3AC：面向大模型推理的稳定、可选择、可扩展Actor-Critic框架
authors:
- Shuo Shen
- Guangran Cheng
- Chengqi Lyu
- Xiangsen Wang
- Yanan Sun
- Wenwei Zhang
affiliations:
- Shanghai AI Laboratory
- Independent Researcher
arxiv_id: '2610.35518'
url: https://arxiv.org/abs/2610.35518
pdf_url: https://arxiv.org/pdf/2610.35518
published: '2026-10-25'
collected: '2026-10-27'
category: Training
direction: LLM RL训练 · Actor-Critic优化
tags:
- RLHF
- Actor-Critic
- GRPO
- CoT Reasoning
- Curriculum Learning
one_liner: 提出适配长CoT推理的Actor-Critic训练方案，支持1.5B-397B模型，性能超GRPO-X
practical_value: '- 做LLM驱动的Agent决策/生成式推荐RL优化时，可直接复用S3AC的Critic训练trick：多策略轨迹预训练扩大覆盖、小标准差初始化value
  head、critic梯度裁剪阈值设为10，避免早期梯度被value head主导，解决长序列RL训练不稳定问题

  - 做训练样本选择/推荐系统curriculum learning时，可复用DAPS设计：复用现有critic的prompt初始价值估计结合历史成功率，优先选择中等难度样本训练，无需额外单独训练难度预估模型，降低无效rollout开销

  - 单rollout RL训练场景（如大规模生成式推荐/Agent推理低成本训练）可直接复用S3AC框架，35B规模下比无critic的REINFORCE++平均准确率高10.5个点，且避免训练后期性能崩溃'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前长链CoT推理的RLVR训练主流采用无critic方案（如GRPO），无法实现token级信用分配，且依赖分组rollout获取prompt特定基线，单rollout场景下批量统计基线无法适配prompt难度差异；引入critic又面临长轨迹覆盖不足、初始化value head主导早期梯度的痛点，亟需稳定可扩展的Actor-Critic方案。

### 方法关键点
- Critic训练配方：用不同强度策略的轨迹混合预训练critic，扩大长短、正误轨迹覆盖；value head用1/(H+1)小标准差初始化，critic梯度裁剪阈值设为10，避免骨干网络梯度被过度压缩；critic学习率设为actor的5倍，每轮rollout训练2个epoch
- 提出DAPS难度感知prompt采样：复用critic的初始状态价值估计结合历史成功记录，计算prompt的预估成功率，优先选择中等难度样本，无需离线难度初始化，减少分组rollout的无效丢弃
- 优势计算：用GAE生成token级优势，actor采用长度自适应λ值，critic直接回归蒙特卡洛回报

### 关键实验
在1.5B到397B的稠密和MoE模型上验证：分组rollout场景下S3AC在35B模型7个benchmark平均准确率比GRPO-X高4.1个点，397B模型5个benchmark平均高2.2个点；单rollout场景下35B模型S3AC平均准确率80.9，比最优无critic基线REINFORCE++高10.5个点，且避免后者训练后期性能崩溃的问题；DAPS相比均匀采样，分组rollout场景下35B模型准确率提升1.45个点，减少约30%的无效丢弃轨迹。

**最值得记住的一句话**：长序列RL训练中，用好critic不仅能实现更细粒度的信用分配，还能复用为难度预估模块，同时兼顾性能提升与训练效率优化。
