---
title: Advancing Omnimodal Embodied Agents from Isolated Skills to Everyday Physical
  Autonomy
title_zh: Advancing Omnimodal Embodied Agents from Isolated
authors:
- Junhao Shi
- Zezheng Huai
- Siyin Wang
- Jia Chen
- Yubang Wang
- Zhaoye Fei
- Hechang Chen
- Jingjing Gong
- Xipeng Qiu
- Yu-Gang Jiang
arxiv_id: '2606.27251'
url: https://arxiv.org/abs/2606.27251
pdf_url: https://arxiv.org/pdf/2606.27251
published: '2026-06-25'
collected: '2026-06-27'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: Building persistent embodied agents in unstructured environments demands
  unified orchestration...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 摘要

Building persistent embodied agents in unstructured environments demands unified orchestration of heterogeneous tools spanning both cyber (APIs, IoT) and physical (manipulation, navigation) domains, coupled with autonomous recovery from physical failures that inevitably arise over extended operation. Existing systems treat these as separate problems: VLM-based planners lack a unified cyber-physical action space, agent frameworks accumulate unbounded context that degrades temporal coherence, and VLA policies execute open-loop without detecting their own failures. We argue that persistent autonomy requires not a monolithic model but a hierarchical asynchronous architecture with explicit separation of planning, memory, and verification. To this end, we present OmniAct, a framework integrating a multimodal semantic planner for skill routing across unified action spaces, an adaptive hierarchical memory with event-boundary-driven compression for sub-linear context growth, and an asynchronous visual preemption engine that closes the semantic loop during physical execution. Across 40 real-world long-horizon tasks on two robotic platforms coordinating four IoT devices, OmniAct achieves consistent improvements in end-to-end success across all complexity levels, maintains near-flat token consumption over under 100k+ accumulated interaction tokens, and elevates mid-scale open-weight models to proprietary-level performance.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
