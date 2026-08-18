---
title: 'ClawGym II: Exploring Black-Box RL on Agent Harness'
title_zh: ClawGym II：面向Agent Harness的黑盒强化学习框架探索
authors:
- Huatong Song
- Fei Bai
- Ming Yang
- Renyuan Li
- Jia Deng
- Jujie He
- Zhange Zhang
- Daixuan Cheng
- Yan Xing
- Qi Yun
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- IQuest Research
arxiv_id: '2608.16798'
url: https://arxiv.org/abs/2608.16798
pdf_url: https://arxiv.org/pdf/2608.16798
published: '2026-08-16'
collected: '2026-08-18'
category: Agent
direction: Agent黑盒强化学习训练优化
tags:
- Black-Box RL
- Agent Harness
- PPO
- GRPO
- Multi-Harness Training
one_liner: 提出统一黑盒RL框架，支持异构Agent Harness下通用Agent的稳定可扩展优化
practical_value: '- 做Agent业务时可复用沙箱隔离+服务代理的架构，不用修改现有Harness逻辑就能接入RL训练，大幅降低业务Agent的迭代成本

  - 从黑盒Harness的零散调用中构建前缀树恢复多轮轨迹的方法，可直接复用到复杂业务Agent的训练数据构造环节，解决轨迹碎片化问题

  - 混合Harness训练的思路可用于跨场景Agent优化，比如让电商导购Agent同时在多端交互框架下联合训练，提升跨场景泛化性

  - token-in-token-out机制+token级重要性采样校正的方案，可直接解决RL训练推理一致性问题，大幅降低训练波动'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent Harness已经成为长周期任务的核心运行层，集成了工具编排、上下文管理、故障恢复等能力，可大幅提升Agent性能，但现有RL训练无法适配复杂不透明的Harness，面临三大核心问题：大规模并发rollout的基础设施不稳定、黑盒Harness输出的碎片化轨迹难以直接用于训练、难以适配异构Harness的统一训练，导致Harness的性能潜力无法被底层模型充分利用。

### 方法关键点
- 基础设施层：用临时沙箱隔离每个任务的环境和Harness，支持大规模并发rollout，在模型服务边界加代理拦截所有模型调用，无需修改Harness原生逻辑
- 轨迹恢复与优化：将拦截到的零散模型调用组织成前缀树，过滤无效叶子节点后适配PPO、GRPO算法在树结构上做优化，通过token-in-token-out机制、token级重要性采样校正保证训练推理一致性
- 混合Harness训练：将任务和不同Harness组成训练实例，同一批次混合异构Harness的rollout数据，按任务-Harness对做优势归一化，实现单模型跨Harness联合优化

### 关键结果
基于Qwen3-30A3B backbone，在ClawGym-Bench上，通过OpenClaw和Claude Code训练的模型Pass@1分别提升9.98、14.81个点，在PinchBench上分别提升11.71、17.28个点，训练在200-400步内保持稳定；混合Harness训练的模型性能不输单Harness训练的版本，在JobBench、OfficeQA等更难的任务上也能获得稳定提升。

### 核心结论
复杂生产级Agent Harness可以直接作为训练接口，无需改造就能用来优化运行在其上的通用Agent模型。
