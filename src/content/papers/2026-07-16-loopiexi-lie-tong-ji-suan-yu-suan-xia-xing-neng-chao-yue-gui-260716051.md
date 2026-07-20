---
title: Loop the Loopies!
title_zh: Loopie系列：同计算预算下性能超越常规Transformer的循环MoE大模型
authors:
- Zitian Gao
- Yilong Chen
- Yihao Xiao
- Xinyu Yang
- Ran Tao
- Joey Zhou
- Bryan Dai
affiliations:
- IQuest Research
arxiv_id: '2607.16051'
url: https://arxiv.org/abs/2607.16051
pdf_url: https://arxiv.org/pdf/2607.16051
published: '2026-07-16'
collected: '2026-07-20'
category: LLM
direction: LLM架构 · 循环Transformer优化
tags:
- MoE
- Looped Transformer
- Model Efficiency
- Reasoning LLM
- Training Pipeline
one_liner: 提出层循环架构的MoE大模型Loopie，同训练计算预算下性能优于常规Transformer，推理能力达奥赛金牌水平
practical_value: '- 层循环架构的工程优化思路可复用：通过层内循环减少存储层数，降低激活内存占用，提升大模型微调/推理的微批量大小，在相同GPU资源下可跑更大batch，降低生成式推荐/Agent的LLM部署成本

  - Supervised Pre-Training（SPT）范式可迁移到垂直领域LLM训练：用SFT的损失函数+预训练级别的大批次、长序列、大数据量训练，既提升电商选品、Agent决策等垂直任务能力，又避免常规SFT的灾难性遗忘问题

  - 同计算预算下的模型选型思路可借鉴：无需盲目堆参数，通过循环架构+效率优化，小参数量MoE也能达到更大参数常规Transformer的效果，适合业务侧资源有限的场景快速落地推理型LLM'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统循环Transformer存在核心痛点：相同预训练计算预算下，直接堆叠参数的常规Transformer性能通常优于循环N次的模型，且过往循环Transformer多适配密集模型，未兼容当前主流的MoE架构，无法适配大模型规模化训练场景。

### 方法关键点
- 架构创新：提出**layer-loop（层循环）** 范式，每个Attention/MoE层循环执行2次再传到下一层，相比传统全模型循环（model-loop），数据locality更好、训练效率更高、参数共享逻辑更合理
- 计算匹配缩放规则（Loopie Recipe）：先减半存储层数，用层循环补充有效深度，节省的内存用于翻倍单卡微批量大小，再把效率增益兑换为更多模型容量，保证单步训练耗时和同计算预算的常规Transformer持平
- 训练pipeline创新：新增Supervised Pre-Training（SPT）阶段，用SFT的损失模式+预训练级别的大批次（≥1024）、长序列（≥128K）、2T级token规模训练，兼顾推理能力和通用知识保留，后续再加RL强化推理能力

### 关键结果
- 预训练阶段：20B总参数（2B活跃参数）的Loopie-20B-A2B，相同训练计算预算下性能优于30B总参数（3B活跃参数）的Qwen3-30B基线，训练吞吐量提升37.9%（261.5 TFLOPS/s vs 189.6 TFLOPS/s）
- 推理基准：AIME准确率92.1%、AMC准确率94.21%、OlympiadBench准确率81.2%，无工具情况下达到2025 IMO、IPhO金牌水平

### 核心结论
在固定计算预算下，合理设计的循环架构比盲目堆叠常规Transformer参数能获得更高的模型性能和训练效率
