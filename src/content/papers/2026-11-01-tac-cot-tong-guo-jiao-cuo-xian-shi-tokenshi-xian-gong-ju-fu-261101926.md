---
title: 'TAC-CoT: Tool-Empowered Implicit Chain-of-Thought via Interleaving Explicit
  Tokens'
title_zh: TAC-CoT：通过交错显式Token实现工具赋能的隐式思维链
authors:
- Juseon Do
- Sangmin Bae
- Jeesu Jung
- Hwanjun Song
affiliations:
- KAIST
- Cluvion
arxiv_id: '2611.01926'
url: https://arxiv.org/abs/2611.01926
pdf_url: https://arxiv.org/pdf/2611.01926
published: '2026-11-01'
collected: '2026-11-05'
category: Agent
direction: Agent 工具调用推理效率优化
tags:
- CoT
- Implicit Reasoning
- Tool Calling
- LLM Agent
- Inference Efficiency
one_liner: 提出隐式思维片段与显式工具交互交错的框架，兼顾工具使用能力、推理精度与效率
practical_value: '- 可复用「隐式思维链+显式交互」架构，优化电商导购Agent、搜索query理解多跳推理的推理成本，在保证工具调用、RAG检索正确性的前提下降低推理token消耗

  - 可借鉴自适应推理预算分配逻辑，根据用户query复杂度动态调整推理步数，简单查询直接返回结果，复杂多步查询才触发多轮工具调用，降低长尾查询的平均推理延迟

  - 训练侧可复用基于显式CoT轨迹蒸馏隐式推理段的方案，不需要额外构造隐式训练数据，基于现有工具调用的Agent轨迹即可完成训练，适配LoRA微调方案'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有显式CoT推理生成大量中间文本，推理成本高且容易累积错误；而现有隐式CoT用固定长度连续Token承载推理，没有中间交互点，无法支持Agent的工具调用，也不能根据query复杂度动态分配推理资源，不适合需要外部工具、多步交互的Agent场景。

### 方法关键点
- 架构设计：将显式CoT轨迹中的每段推理文本替换为固定长度的连续隐式思维Token，仅保留工具调用、观测结果、最终答案为显式文本，实现隐式推理与显式交互的交错
- 动态路由：每段隐式推理结束后判断是否需要调用工具，是则生成工具调用、插入返回观测后继续下一段隐式推理，否则直接生成最终答案，总推理段数随query复杂度动态调整，实现自适应推理预算
- 训练方案：基于现有显式CoT工具调用轨迹，通过自蒸馏训练，用辅助解码器从隐式Token重建原始推理文本，同时蒸馏显式CoT教师的隐藏态保证推理一致性，推理时丢弃辅助解码器无额外 overhead

### 关键实验
在数学推理、多跳QA、ToolBench三类基准上测试，对比Explicit-CoT、TokenSkip、SIM-CoT等基线，跨Qwen2.5-0.5B、Llama3.2-1B、Qwen3-4B三个backbone：平均数学推理精度提升5.8个百分点，QA EM提升2.4个百分点，模型前向传播次数最多降低6.8倍，单L40S GPU上实测端到端推理速度提升2.3~2.4倍，多工具场景下工具调用胜率比显式CoT高8.6个百分点。

### 核心结论
隐式推理不需要完全屏蔽显式交互，仅压缩纯推理段、保留交互相关显式Token，是兼顾Agent工具能力、推理精度和效率的最优折中
