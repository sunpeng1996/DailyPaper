---
title: Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Reasoning
  and Execution
title_zh: AI Agent能否识别任务简单程度？面向复杂度感知的推理与执行
authors:
- Junjie Yin
- Xinyu Feng
arxiv_id: '2607.13034'
url: https://arxiv.org/abs/2607.13034
pdf_url: https://arxiv.org/pdf/2607.13034
published: '2026-07-14'
collected: '2026-07-15'
category: Agent
direction: Agent 复杂度感知推理与执行优化
tags:
- LLM Agent
- Reasoning Optimization
- Cost Efficiency
- Task Complexity
- Execution Framework
one_liner: 提出复杂度感知的E3 Agent执行框架，保持满成功率的同时大幅削减推理冗余开销
practical_value: '- 所有调用LLM的业务Agent（比如智能客服、商品文案生成、用户意图解析）均可复用E3的「预估复杂度→最小路径执行→失败扩范围」流程，实测降本幅度超过80%，ROI极高

  - 可直接复用Agent Cognitive Redundancy Ratio (ACRR)作为核心观测指标，量化自家LLM应用/Agent的推理冗余度，锚定优化方向

  - RAG/搜索类Agent场景可替换现有全量召回策略，先基于任务复杂度做最小必要召回，验证不通过再扩大检索范围，同时降低latency和召回成本'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM Agent普遍采用最大上下文优先策略，无视任务实际复杂度匹配资源，简单任务也会触发全量上下文检索、重加载已读依赖等冗余操作，带来不必要的token、时间成本浪费。
### 方法关键点
1. 定义最小充分执行规则和Agent Cognitive Redundancy Ratio (ACRR)，量化Agent推理冗余程度
2. 推出E3三段式执行框架：先预估任务复杂度与初始执行边界，走最小可行路径执行，仅验证失败时扩大执行范围
### 关键结果
在MSE-Bench 121个编辑任务上，E3持平最强基线100%成功率，成本降85%，token消耗降91%，检索文件量降92%，性能超出自适应检索基线16%；真实GPT-4o开源库编辑场景下，E3是同等成功率下最轻量、最快的执行策略。
