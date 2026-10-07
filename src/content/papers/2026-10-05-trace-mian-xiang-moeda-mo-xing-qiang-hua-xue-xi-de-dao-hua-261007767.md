---
title: 'TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning
  of MoE Language Models'
title_zh: TRACE：面向MoE大模型强化学习的Rollout引导FP4量化训练框架
authors:
- Xin Wang
- Hao Yu
- Zhengyang Zhuge
- Bochao Mao
- Zheng Li
- Junda Feng
- Yuyan Luo
- Yi Zhang
- Yizhong Cao
- Mi Zhang
affiliations:
- Alibaba Group
- Ohio State University
arxiv_id: '2610.07767'
url: https://arxiv.org/abs/2610.07767
pdf_url: https://arxiv.org/pdf/2610.07767
published: '2026-10-05'
collected: '2026-10-07'
category: Training
direction: MoE LLM · FP4量化 · RL训练优化
tags:
- MoE
- FP4 Quantization
- RL Training
- QAT
- KV cache
one_liner: 提出对齐训练与rollout路径的FP4量化框架，在MoE RL场景保留BF16性能同时实现5.4倍rollout加速
practical_value: '- 做LLM+Agent的RL对齐时，可复用rollout引导的量化对齐思路，解决FP4低精度推理与训练路径不一致导致的训练不稳定问题，在保持性能的前提下大幅降低推理成本

  - 低精度量化场景下，可借鉴仅缓存深层网络尾数位+scale信息的工程trick，在仅增加7.4%训练overhead的前提下，将FP4 rollout的存储通信开销降低6倍

  - 业务场景需要部署低精度MoE模型时，优先在RL训练阶段引入FP4量化对齐（而非训练后量化），可获得更高的最终低精度模型性能，比PTQ方案平均高3.9个百分点'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
MoE大模型RL后训练需反复生成长轨迹rollout，计算内存开销极高，FP4低精度量化可大幅降低rollout成本，但现有方案独立优化训练与rollout路径的量化精度，未直接对齐两条路径的量化结果，会导致策略失配、训练崩溃，尤其MoE的路由机制会进一步放大数值差异的负面影响。
### 方法关键点
- Rollout引导的量化感知训练：用rollout侧的FP4量化结果指导训练侧的FP4舍入决策，直接降低两条路径的量化差异，避免小数值差异被舍入边界放大
- 高效量化信息缓存：仅保留模型后半部分深层的量化尾数位与scale信息，大幅降低rollout引导带来的存储通信开销
### 关键结果
在4款不同规模Qwen MoE模型（最大2.4T参数）的推理、编码、长序列RL任务上验证，对比QAT、QaRL、QUADS等基线及post-hoc量化方案：
1. 联合FP4权重/激活/KV cache的rollout场景下，性能与BF16 rollout持平，平均比QUADS高6.5个百分点
2. 128K输出长度下rollout解码吞吐量比BF16高5.4倍，端到端RL训练仅比原生FP4 rollout增加7.4% overhead
3. 最终FP4模型性能比BF16训练后再做PTQ的方案平均高3.9个百分点

只要控制好训练与rollout的量化路径差异，RL过程中模型可以自主适配FP4低精度执行环境，最终性能甚至超过BF16训练后量化的结果
