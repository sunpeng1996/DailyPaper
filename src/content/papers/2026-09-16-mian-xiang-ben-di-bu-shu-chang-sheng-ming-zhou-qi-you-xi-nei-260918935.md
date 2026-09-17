---
title: 'Long-Lived Characters, Local Inference: Incremental Memory Maintenance for
  Game NPCs'
title_zh: 面向本地部署长生命周期游戏NPC的增量内存维护方法
authors:
- Zimu Xu
affiliations:
- University of Bern
arxiv_id: '2609.18935'
url: https://arxiv.org/abs/2609.18935
pdf_url: https://arxiv.org/pdf/2609.18935
published: '2026-09-16'
collected: '2026-09-17'
category: Agent
direction: Agent 长生命周期内存增量维护
tags:
- Agent
- KV cache
- Memory Maintenance
- Local Inference
- LLM Serving
one_liner: 针对本地部署的混合结构LLM游戏NPC，提出无需重训的增量内存维护方法，大幅降低上下文更新开销同时保留语义一致性
practical_value: '- 电商导购/客服Agent、长会话用户建模等场景可直接复用增量KV维护思路：无需每次重建全量上下文，仅更新变更的记忆片段，可大幅降低长上下文推理开销，提升多Agent并发调度能力

  - 混合循环-注意力结构的模型内存更新优先采用true-tail策略，不要强制将新KV插回旧记录位置，可避免RoPE位置依赖导致的实体、时序语义绑定错误，适用于用户兴趣更新、订单状态变更等强事实绑定的推荐/Agent场景

  - 不要仅依赖注意力分布相似度作为记忆正确性的评估指标，必须结合业务事实校验（如商品库存、订单状态、用户权益绑定），避免小分布偏差引发的业务逻辑错误

  - 内存更新引发的事实绑定错误不一定需要全量重建上下文，可通过prompt编排（如先引导事实回忆再生成输出）快速修正，降低修复成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
本地部署的长生命周期游戏NPC每次对话前重建全量上下文成本极高，少量记忆更新就会导致长前缀KV cache失效，多NPC场景下背景重建会挤占前台对话算力，且容易出现物品归属、事件时序等语义绑定错误，导致游戏规则逻辑出错。
### 方法关键点
- 针对混合循环-注意力结构的量化Qwen模型，将推理状态拆分为可删除的attention KV和持续保留的循环状态，仅移除过期记忆对应的KV条目，新记忆在序列尾部计算并追加，无需修改模型权重
- 采用true-tail更新策略，更新的KV保留实际尾部的RoPE位置编码，不强制回写到旧记录的原始位置，避免位置依赖导致的语义错误
- 记忆更新成本仅与变更的token数挂钩，不变的历史记录完全无需重编码
### 关键结果
在RTX 5090 Laptop GPU上测试27B量化模型：11.9K token上下文初始构建耗时10.2s，8次记忆更新总耗时仅3.48s，相比每次全量重建提速23.5倍；8轮脚本化内存维护后，物品数量、事件参与方等关键语义绑定效果与全量重建相当；独立分块编码会导致目标记忆注意力占比从57.4%降至21.5%，出现时序绑定错误。
### 核心结论
Agent的推理状态是需要持续维护的历史依赖资源，而非仅作为最新记忆文本的一次性编码
