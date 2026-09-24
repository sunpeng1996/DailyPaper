---
title: Hunyuan-A13B Technical Report
title_zh: Hunyuan-A13B 开源高效MoE大模型技术报告
authors:
- Tencent Hunyuan Team
- Ao Liu
- Botong Zhou
- Can Xu
- Chayse Zhou
- ChenChen Zhang
- Chengcheng Xu
- Chenhao Wang
- Decheng Wu
- Dengpeng Wu
affiliations:
- Tencent Hunyuan Team
arxiv_id: '2609.27284'
url: https://arxiv.org/abs/2609.27284
pdf_url: https://arxiv.org/pdf/2609.27284
published: '2026-09-22'
collected: '2026-09-24'
category: LLM
direction: 大模型 · 高效MoE架构与双模式推理
tags:
- MoE
- Chain-of-Thought
- RLHF
- Long Context
- Agent Capability
one_liner: 总参80B激活仅13B的开源MoE大模型，兼顾推理能力与部署效率
practical_value: '- 架构选型：可复用「1个共享专家+64个专用专家、单请求激活8个」的MoE配置，在业务侧自建垂域大模型时平衡效果与推理成本，适配高并发的搜索query理解、商品文案生成、Agent工具调用等场景

  - 推理优化：双模式CoT机制可直接迁移到业务LLM服务，简单任务（如关键词提取、短文案生成）用fast模式降本提效，复杂任务（如用户深度意图推理、多步工具调用）用slow模式保障效果

  - 训练流程：先做核心场景SFT+RL、再做全场景微调的两阶段后训练策略，以及重点垂域数据增广的方案，可复用在垂域大模型训练中，优先保障业务核心任务的效果

  - 部署落地：模型兼容vLLM/SGLang等主流推理框架，支持INT8/FP8无损量化，推理吞吐量是同效果稠密模型的2倍以上，适合电商高并发场景低成本落地'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前SOTA大模型普遍参数规模大、推理延迟高、部署成本高昂，难以在latency敏感的电商搜索推荐、Agent交互等业务场景大规模落地，亟需兼顾核心能力与部署效率的开源大模型方案。

### 方法关键点
- 架构：采用MoE稀疏结构，总参数80B，单请求仅激活13B参数（1个永久共享专家+64个专用专家，每次激活8个专用专家），搭配GQA优化KV Cache效率，支持256K上下文窗口。
- 预训练：基于20T严格过滤的高质量语料训练，重点补充250B高标注质量STEM领域数据提升推理能力上限，分基础训练、快速退火、长上下文扩展三阶段完成。
- 后训练：先针对数学、代码、逻辑、科学四大领域做推理导向的SFT+GRPO强化学习，再覆盖全场景任务做通用SFT+RL；同时引入双模式CoT：fast模式`<think>`块为空，低延迟处理简单任务；slow模式输出完整推理链，保障复杂任务效果。

### 关键结果
- 基础能力：12/14项通用、代码、数学基准超越前代混元-Large（激活参数仅为其1/4），7/12项基准超越激活参数22B的Qwen3-A22B。
- Agent能力：慢思考模式下4项主流Agent基准均为同量级最优，BFCL v3得分78.3、ComplexFuncBench得分61.2，大幅领先同类模型。
- 推理效率：A16W16精度下batch=32时吞吐量达1982 tokens/s，适配高并发业务场景。

### 核心结论
通过MoE稀疏激活+双模式推理的组合方案，可在不损失核心能力的前提下，将大模型部署成本降低至同效果稠密模型的1/3-1/2
