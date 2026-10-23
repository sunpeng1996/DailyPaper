---
title: 'Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation'
title_zh: 因果思维链：通过上下文隔离缓解注意力泄漏问题
authors:
- Gabriele Dominici
- Teague McMillan
- Fazl Barez
- Marc Langheinrich
- Martin Gjoreski
affiliations:
- Università della Svizzera Italiana
- ETH Zurich
- University of Oxford
arxiv_id: '2610.31639'
url: https://arxiv.org/abs/2610.31639
pdf_url: https://arxiv.org/pdf/2610.31639
published: '2026-10-22'
collected: '2026-10-23'
category: Reasoning
direction: 思维链优化 · 推理忠实度提升
tags:
- Chain-of-Thought
- Causal Reasoning
- Attention Leakage
- Faithfulness
- LLM Inference
one_liner: 提出基于DAG与上下文隔离的CausalCoT推理框架，大幅提升LLM推理忠实度且精度损失极小
practical_value: '- 电商导购/客服Agent、多步推荐推理场景可复用DAG拆分+上下文隔离方案，强制LLM严格按逻辑链推导，避免跳过中间规则直接输出错误结果，提升推理可解释性

  - 高stakes场景（如信贷推荐、医疗导购）可借鉴上下文隔离执行机制，支持人工干预中间推理节点，修正错误后仅重算下游依赖节点，高效降低bad case率

  - 做LLM推理忠实度评估时，可复用Predictable Change度量，相比单纯的步骤扰动翻转率，能更准确区分真正的逻辑依赖和扰动导致的随机输出'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
标准CoT的全局注意力机制存在严重注意力泄漏问题，LLM可直接从原始输入提取信息生成答案，输出的分步推理只是事后合理化的伪解释，忠实度极低，无法支撑高可信场景的推理需求。

### 方法关键点
- 两阶段推理：第一阶段让LLM作为规划器，将复杂问题拆分为子问题构成的DAG，明确各节点的依赖关系；第二阶段按拓扑顺序执行每个节点，仅传入当前子问题和其直接父节点的答案，完全隔离无关上下文，切断注意力泄漏路径
- 提出Predictable Change度量，不仅统计中间步骤扰动后的答案翻转率，还判断输出结果是否符合扰动后的逻辑推导，区分真正的逻辑依赖和扰动导致的随机输出
- 原生支持测试时干预，可人工修改DAG结构或中间节点结果，仅重算下游依赖节点，推理路径可控可追溯

### 关键结果数字
在GPQA、MedQA、反事实模拟套件3类数据集上测试，对比标准CoT、Factored Decomposition基线：平均中间步骤因果敏感度提升12p.p.，最高达21p.p.；精度仅比最优基线低1.05~6.38p.p.，3次采样的Pass@3指标优于标准CoT；3次人工干预后精度可追平甚至超过标准CoT。

### 核心结论
LLM的CoT推理忠实度问题本质是注意力泄漏导致的事后合理化，仅靠prompt优化无法解决，必须通过结构层面的上下文隔离强制推理步骤的因果依赖。
