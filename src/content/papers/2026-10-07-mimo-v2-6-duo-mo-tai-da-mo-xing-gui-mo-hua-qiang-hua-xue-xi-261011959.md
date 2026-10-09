---
title: 'MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement'
title_zh: MiMo-V2.6 多模态大模型：规模化强化学习实现能力自提升
authors:
- Core Team
- Zongming Qiao
- Ziyue Hua
- Zirui Ou
- Zihao Yue
- Zihan Jiang
- Zhuo Huang
- Zhiyang Chen
- Zhixian Zheng
- Zhipeng Xu
affiliations:
- Xiaomi LLM Core Team
arxiv_id: '2610.11959'
url: https://arxiv.org/abs/2610.11959
pdf_url: https://arxiv.org/pdf/2610.11959
published: '2026-10-07'
collected: '2026-10-09'
category: Agent
direction: Agent 规模化强化学习自提升
tags:
- RL
- MoE
- Multimodal
- Agent
- Self-Improvement
one_liner: 基于MoE混合注意力架构，从计算、环境、打分三维度规模化RL，实现多模态Agent能力自提升
practical_value: '- 做Agent RL训练时可复用groupwise agentic grading机制：同query下输出分组对比打分，重分配优势权重，避免奖励黑客同时引导输出更短、更高质量的解决方案，适配电商导购Agent、商品文案生成的RL调优场景

  - 规模化多任务RL训练时，可采用冻结MoE路由层+多层奖励黑客防御的方案，稳定训练过程，避免训练崩溃，适合电商多场景（推荐、搜索、客服）联合RL调优

  - 多场景Agent训练可复用多mini-harness思路：解耦系统提示、工具调用、上下文管理模块，避免模型过度耦合单场景实现逻辑，提升跨场景泛化能力

  - 长上下文RL训练可采用异步训练+partial rollout+KV cache预填充的工程方案，分摊重计算成本，支撑百万级上下文的大批次训练，适配长用户行为序列的推荐Agent训练'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前大模型向自提升演进的核心路径是强化学习（RL），但规模化Agent RL面临两大核心挑战：一是需要适配的模型架构和足够的Agent任务探索空间，二是需要配套的基础设施、多样化环境和精准的打分机制，现有方案难以支撑万亿级MoE模型的大规模RL训练。

### 方法关键点
- 架构：基于混合滑动窗口注意力（SWA）+全局注意力（GA）的稀疏MoE Transformer backbone，配套轻量化视觉、音频编码器，支持1M上下文，推出两个规格：1.02T总参/42B激活参的Pro版、310B总参/15B激活参的Flash版
- RL三维度扩展：①计算层：异步训练每步处理1568个样本、2.7~3.7B tokens，用partial rollout提升GPU利用率；②环境层：覆盖代码、通用工作流、视觉、网络安全四大领域的多样化环境，多mini-harness训练提升跨场景泛化；③打分层：分组Agent打分（GRS离线构造任务rubric、GAR在线重分配优势），输出细粒度奖励信号，引导更高效的解决方案
- 稳定性优化：冻结MoE路由层，多层防御奖励黑客，统一轨迹表示，解耦控制/数据平面，对齐训练推理一致性

### 关键结果数字
RL训练后，DeepSWE v1.1基准上Pro版得分从58.4提升至72.6，Flash版从48.7提升至65.7；训练过程中确认的奖励黑客轨迹占比低于2%；Pro版RL训练总投入260万美元，训练、rollout、打分成本分别占43.5%、43.8%、12.7%。

### 核心结论
规模化RL的性能提升与计算投入呈正相关，稳定训练的核心是在计算、环境、打分三个维度同步扩展，同时做好奖励黑客防御和训练推理一致性对齐。
