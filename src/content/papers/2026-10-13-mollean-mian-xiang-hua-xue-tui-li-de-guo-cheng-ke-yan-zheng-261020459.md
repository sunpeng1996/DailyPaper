---
title: 'MolLean: A Process-Verifiable Language for Chemical Reasoning'
title_zh: MolLean：面向化学推理的过程可验证语言
authors:
- Jiatong Li
- Yatao Bian
affiliations:
- National University of Singapore
arxiv_id: '2610.20459'
url: https://arxiv.org/abs/2610.20459
pdf_url: https://arxiv.org/pdf/2610.20459
published: '2026-10-13'
collected: '2026-10-25'
category: Reasoning
direction: LLM推理 · 过程可验证性优化
tags:
- Chain-of-Thought
- Hallucination Mitigation
- Reasoning Verification
- Stateful Tool
- Formal Verification
one_liner: 提出面向化学推理的过程可验证语言MolLean及配套交互接口，解决化学CoT推理幻觉问题
practical_value: '- Agent决策链路可复用「状态校验+非法操作不更新状态+反馈回传」机制，避免推荐决策、搜索Query改写等场景的幻觉累积

  - 分层校验设计可迁移到商品合规校验场景：原生规则校验（如类目属性匹配）和外部接口校验（如库存、价格有效性）分离，降低维护成本

  - 多推理模式可根据业务选型：全轨迹回溯优化适合多步复杂推荐路径规划，分步交互校验适合规则严格的营销活动选品等场景'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
化学领域Chain-of-Thought推理普遍存在分子结构伪造、属性断言无依据的幻觉问题，自由格式推理无法对中间过程做正确性校验。

### 方法关键点
1. 基于Lean实现分层校验内核，可覆盖从基础分子图编辑到复合变换的所有状态转移、属性断言校验；搭配带类型的见证协议，分离原生结构校验和外部测量数据校验
2. 推出带状态的工具接口MolLean-MCP，生成过程中实时返回校验结果和分子读数，被拒绝的操作不会修改当前状态
3. 支持三种推理模式：单轮轨迹执行、全轨迹回溯优化、MolLean-MCP交互式推理

### 关键结果
在12类分子生成、编辑、优化、反应任务共8800个匹配样本上测试，基于Qwen3.6-27B的全轨迹优化模式在所有12个任务上性能优于直接CoT；搭配MolLean-MCP的分步校验反馈后，反应类任务性能进一步提升
