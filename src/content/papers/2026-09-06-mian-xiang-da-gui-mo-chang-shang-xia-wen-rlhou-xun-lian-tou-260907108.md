---
title: Online Draft Co-Training for Speculative Decoding in Large-Scale, Long-Context
  RL Post-Training
title_zh: 面向大规模长上下文RL后训练投机解码的在线草稿联合训练系统
authors:
- Zili Wang
- Zhaopeng Qiu
- Yuekai Zhang
- Shuang Yu
- Junjie Lai
affiliations:
- NVIDIA
arxiv_id: '2609.07108'
url: https://arxiv.org/abs/2609.07108
pdf_url: https://arxiv.org/pdf/2609.07108
published: '2026-09-06'
collected: '2026-09-09'
category: Training
direction: LLM训练 · 投机解码加速
tags:
- Speculative Decoding
- RL Post-Training
- Context Parallelism
- Pipeline Parallelism
- Long Context LLM
one_liner: 提出适配上下文/流水线并行的在线草稿联合训练方案，实现RL后训练1.16-1.88倍端到端加速
practical_value: '- 做Agent/生成式推荐RL微调时，可复用在线联调投机解码草稿的思路，将rollout生成速度提升1.19-2.23倍，降低大模型微调成本

  - 长上下文分布式训练场景下，可复用打包zigzag环注意力实现分支注意力，相比USP方案延迟降低最多2.9倍，单卡显存占用降低2.7倍

  - 流水线并行下跨阶段取中间特征的场景，可复用TapChannel旁路传输方案，相比主机中转延迟降低4.5-8.5倍，几乎不影响原有流水线调度'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
RL后训练是Agent、大模型能力对齐的核心范式，rollout生成占其总耗时的最大比例，投机解码可显著降低生成耗时，但在线联合训练投机解码草稿以适配动态更新的RL策略时，现有分布式训练的上下文并行（CP）不支持草稿的分支注意力结构，流水线并行（PP）下草稿依赖的目标模型中间特征跨阶段无法获取，无法支撑大规模长上下文大模型的RL后训练需求。
### 方法关键点
- 上下文并行适配：将草稿分支注意力拆分为主序列因果前缀注意力、分支本地注意力两部分，主序列采用打包负载均衡的zigzag环注意力计算，分支部分本地计算后通过在线softmax合并结果，兼容EAGLE-3、DFlash、DSpark三类主流草稿架构。
- 流水线并行适配：提出TapChannel旁路传输机制，为每个输出中间特征的PP阶段在草稿所在的最后阶段预分配缓存槽，通过RDMA/IPC独立于原有流水线调度传输特征，通过序列号同步生产消费关系，不干扰原有流水线调度。
- 联合训练范式：草稿与RL策略共享训练数据，基于目标模型中间特征的梯度截断版本训练，与策略联合更新。
### 关键实验
在8B-122B参数模型、DAPOMath-17K、多轮工具调用任务上验证，对比无投机解码基线：
1. 草稿接受长度达2.28-4.78，rollout速度提升1.19-2.23倍，端到端训练速度提升1.16-1.88倍；
2. 打包zigzag环注意力相比USP方案，latency最高降低2.9倍，单卡显存降低2.7倍，支持256K长上下文训练；
3. TapChannel相比主机中转特征传输延迟降低4.5-8.5倍，仅带来15%以内的PP overhead。
### 核心结论
在线联合训练投机解码草稿是大模型RL后训练降本的有效手段，仅需修改分布式并行适配层即可实现无损加速，无需调整原有RL训练逻辑。
