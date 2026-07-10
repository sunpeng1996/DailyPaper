---
title: 'ProjAgent: Procedural Similarity Retrieval for Repository-Level Code Generation'
title_zh: ProjAgent：面向仓库级代码生成的流程相似性检索方法
authors:
- QiHong Chen
- Aaron Imani
- Iftekhar Ahmed
affiliations:
- University of California, Irvine
arxiv_id: '2607.08691'
url: https://arxiv.org/abs/2607.08691
pdf_url: https://arxiv.org/pdf/2607.08691
published: '2026-07-09'
collected: '2026-07-10'
category: Agent
direction: Agent 驱动的代码生成检索优化
tags:
- Agent
- RAG
- Similarity Retrieval
- Code Generation
- Static Analysis
one_liner: 引入流程相似性作为检索信号，结合Agent工作流与静态分析反馈提升仓库级代码生成效果
practical_value: '- 跨域相似召回场景可新增「流程/逻辑步骤相似性」作为独立召回维度，补足语义/词汇匹配漏召回的同逻辑异表述资源，可适配电商营销文案生成、多场景推荐策略生成的案例召回

  - 复杂生成类Agent工作流可将任务拆解为中间推理步骤，逐步骤匹配对应参考上下文后拼接全链路输入，降低大模型推理难度同时提升输出一致性

  - 生成任务后可接入轻量规则化反馈环（如业务规则校验、格式检查）做迭代修复，无需重跑全生成流程，降低推理成本同时提升输出合规性，可复用在商品文案合规校验、活动规则生成等场景'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
仓库级代码生成需兼顾跨文件依赖与项目特有规范，现有检索方案仅依赖词汇、结构、语义相似性，易遗漏标识符、应用域不同但核心执行逻辑高度相似的仓库函数，无法提供充足有效上下文支撑生成符合要求的代码。
### 方法关键点
1. 新增流程相似性作为独立检索信号，将目标生成任务拆解为多步中间推理步骤，通过Agent工作流逐步骤匹配具备相似流程行为的仓库函数
2. 融合流程相似性检索结果与传统语义检索结果，构建更全面的仓库上下文输入
3. 接入保守静态分析反馈环，基于编译器、静态检查结果迭代修复生成代码
### 关键结果
在REPOCOD基准测试集上Pass@1达41.14%，显著优于所有现有检索类基线，验证了流程相似性作为检索维度的有效性。
