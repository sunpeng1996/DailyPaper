---
title: 'H^2SD: Hybrid Hindsight Self-Distillation'
title_zh: H²SD：面向LLM推理优化的混合后验自蒸馏方法
authors:
- Qiye Cai
- Yichuan Ma
- Linyang Li
- Peiji Li
- Yongkang Chen
- Qipeng Guo
- Yicheng Zou
- Tao Gui
- Xiaocheng Feng
- Bing Qin
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Harbin Institute of Technology
- Fudan University
- The Chinese University of Hong Kong
arxiv_id: '2607.18955'
url: https://arxiv.org/abs/2607.18955
pdf_url: https://arxiv.org/pdf/2607.18955
published: '2026-07-20'
collected: '2026-07-22'
category: Training
direction: LLM训练 · RLVR自蒸馏优化
tags:
- Self-Distillation
- RLVR
- GRPO
- LLM Training
- Reasoning
one_liner: 按轨迹正确性匹配差异化自蒸馏策略，兼顾RLVR训练稳定性与推理性能提升
practical_value: '- 做Agent推理/工具调用的RL微调时，可直接复用分轨迹的蒸馏策略：成功轨迹仅调整token更新幅度避免信息泄露，失败轨迹用带中间步骤的hint做反向KL蒸馏实现明确纠错，比纯GRPO/RLSD效果更稳定

  - 自蒸馏场景下无需准备同词表的大模型教师，仅用外部大模型生成自然语言hint作为特权信息即可，大幅降低工程依赖与部署成本

  - 成功轨迹的教师端加入重述指令的trick可直接复用，能显著提升token级信用分配的准确性，避免过拟合到特权信息

  - 电商场景的query理解、商品文案生成、客服回复的RL微调任务，都可套用该混合蒸馏框架，在不降低推理效率的前提下提升生成质量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有RLVR方法仅用轨迹级标量奖励优化，存在token级信用分配稀疏的瓶颈；OPD依赖额外同词表的强教师模型，适用性受限；OPSD直接匹配特权信息下的教师分布易引发信息泄露、训练不稳定；RLSD仅用教师信号调整更新幅度，在轨迹推理失败时无法提供明确纠错方向，亟需兼顾训练稳定性与性能的自蒸馏方案。
### 方法关键点
- 轨迹正确性路由：对验证成功的轨迹，沿用RLSD思路，教师端输入正确的学生回复+重述指令，仅用教师输出的token概率调整更新幅度，不改变奖励确定的优化方向，避免信息泄露
- 失败轨迹纠错：对推理失败的轨迹，教师端输入包含关键推理步骤与验证答案的参考hint，最小化学生到教师的反向KL散度，提供明确的分布级纠错信号
- 特权信息轻量化：仅需外部大模型生成自然语言hint作为特权信息，无需教师与学生同词表，降低部署门槛
### 关键结果
在数独、Calcudoku、Arrow Maze三类逻辑推理基准上对比GRPO、RLSD、OPSD、SRPO等基线，H2SD整体准确率达50.49%，较次优基线RLSD的24.85%提升超100%；同时单问题平均生成token数最少，推理效率最高；消融实验显示带中间推理步骤的hint比仅用最终答案的提升幅度超180%。

最值得记住的结论：自蒸馏的最优策略完全依赖轨迹的正确性，成功轨迹优先保障训练稳定、失败轨迹优先做强分布纠错，是兼顾训练稳定性与性能提升的核心。
