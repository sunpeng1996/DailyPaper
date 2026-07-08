---
title: 'RSF-GLLM: Bridging the Semantic Gap in Multi-Hop Knowledge Graph QA via Recurrent
  Soft-Flow and Decoupled LLM Generation'
title_zh: RSF-GLLM：基于循环软流与解耦LLM生成的多跳KGQA语义鸿沟填补
authors:
- Sambaran Bandyopadhyay
- Ananth Muppidi
affiliations:
- Adobe Research
- Adobe Systems
arxiv_id: '2607.06527'
url: https://arxiv.org/abs/2607.06527
pdf_url: https://arxiv.org/pdf/2607.06527
published: '2026-07-07'
collected: '2026-07-08'
category: Reasoning
direction: 多跳知识图谱推理 · 推理与LLM生成解耦
tags:
- KGQA
- Multi-hop Reasoning
- Differentiable Graph Reasoning
- LLM Grounding
- GNN
one_liner: 通过解耦可微图推理与LLM生成，解决多跳知识图谱问答的语义鸿沟与推理效率问题
practical_value: '- 多跳路径检索场景可复用RSF动态门控机制，自适应切换结构拓扑/语义匹配权重，解决中间节点无语义重叠的路径召回问题，适配电商「买了A的用户还买过谁代言的B」类多跳关系查询

  - 推理与生成解耦架构可直接迁移到高准确性要求的Agent场景，用轻量可微模块做结构化推理，仅需1次LLM调用生成结果，相比Agentic多轮调用推理 latency
  降低1个数量级

  - 熵驱动流稀疏正则化trick可直接复用在可微图遍历任务中，避免概率分布弥散，保证推理路径可解释可回溯，适配合规要求高的电商/广告场景归因需求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统多跳知识图谱问答（KGQA）的retrieve-then-read架构中，离散节点选择破坏端到端可微性，无法对齐召回与下游生成目标，且中间桥接节点与查询无词汇重叠时（即语义鸿沟）召回失效；LLM原生多跳推理则存在幻觉率高、多轮调用成本过高的问题，无法落地高事实准确性要求的业务场景。
### 方法关键点
- 两阶段完全解耦架构：第一阶段用轻量可微Recurrent Soft-Flow（RSF）模块完成图推理路径召回，第二阶段仅用1次LLM调用完成路径到答案的生成，梯度完全隔离，避免生成噪声干扰图推理模块的稳定学习
- RSF模块核心设计：GRU引导的查询意图动态更新机制，动态门控自适应调节结构传播/语义匹配权重，语义信号失效时完全依赖拓扑遍历桥接节点；加入熵驱动的流稀疏正则化，强制连续概率分布收敛到离散可解释路径，理论上保证路径的结构有效性
- 路径生成对齐：贪心回溯从最终节点分布反推完整推理路径，模板化转成自然语言后作为LLM输入，保证生成结果完全基于KG事实，从架构层面杜绝幻觉
### 关键实验
在WebQSP、CWQ两个标准多跳KGQA数据集上测试：WebQSP Hit@1达90.45%，超过需50+次LLM调用的agentic基线FD-PORT（89.2%），单query推理 latency仅0.25s，推理速度是同性能基线的21倍；相比纯GNN检索基线，CWQ Hit@10提升6.1个百分点，相比RoG等LLM生成路径基线，参数量缩小38倍。
### 核心洞察
结构化推理任务中，专用轻量可微模块的效率和准确率上限远高于通用LLM的agentic多轮调用，解耦推理与生成是兼顾性能、成本、可解释性的可行路径
