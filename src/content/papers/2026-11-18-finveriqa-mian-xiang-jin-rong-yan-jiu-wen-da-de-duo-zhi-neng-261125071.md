---
title: 'FinVeriQA: Financial Research Agents for Question Answering: Routing, Retrieval,
  MCP Tool Use, and Provenance-Aware Evidence Verification'
title_zh: FinVeriQA：面向金融研究问答的多智能体路由检索与证据验证框架
authors:
- Meenakshi Rajpurohit
- Anna Phan
- Ravikumar Komandur Narayanan
- Gunanidhi Ramakrishnan
- Nathan Howland
affiliations:
- San José State University, USA
arxiv_id: '2611.25071'
url: https://arxiv.org/abs/2611.25071
pdf_url: https://arxiv.org/pdf/2611.25071
published: '2026-11-18'
collected: '2026-11-20'
category: MultiAgent
direction: 多智能体协作 · 金融问答验证
tags:
- MultiAgent
- RAG
- MCP
- EvidenceVerification
- FinancialQA
- LLM
one_liner: 拆分金融QA各环节到最优组件，实现准确率大幅优于单LLM的开源多Agent金融问答系统
practical_value: '- 可直接复用任务拆分架构：将Agent导购、客服等业务流程拆分为路由、计算、检索、生成、验证独立子任务，路由用小尺寸分类模型（比7B/12B
  LLM准确率高30%+、速度快数倍），数值类计算全交给代码执行，彻底规避LLM数值幻觉

  - 验证层可直接迁移到电商场景：除校验生成内容与检索证据匹配外，增加独立权威源校验层（比如商品参数和商品中心数据库交叉校验），可减少70%+的共享错误证据导致的幻觉漏过

  - 共享记忆模块设计可复用：给记忆条目增加归属主体（商品/用户ID）、新鲜度、来源标签，复用前校验主体匹配，避免跨主体数据混用的低级错误

  - 能力封装方式可借鉴：通过MCP协议将业务通用能力封装为标准工具，其他Agent可直接调用复用统一校验逻辑，降低多Agent体系的重复开发成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM生成金融领域回答流畅性高，但存在计算错误、引用过时数据、请求路由错误、幻觉信息等致命问题，现有多Agent方案多复用同一生成模型承担决策、计算、生成全流程任务，错误率居高不下，亟需明确各环节最优组件的分工方案。

### 方法关键点
- 拆分全流程为6个专用Agent：数据、分析、分类、行情、可视化、报告，Agent间不直接调用，所有数据通过带来源、新鲜度标签的共享内存交互，支持历史结果复用
- 路由用421M参数的Laya非生成式分类模型，同时拦截投资建议类请求，准确率远高于大尺寸LLM
- 所有数值计算完全交由Python实现，Mistral-7B仅负责复制已有数值和检索内容生成回答，代码校验器强制检查引用ID存在、数值和计算结果完全一致
- 检索采用BM25+稠密向量的混合方案，优先按文档章节过滤缩小检索范围
- 全能力通过MCP服务器封装为标准只读工具，内置统一安全护栏

### 关键实验结果
在金融问答数据集上测试：Laya路由准确率达0.85，远超Mistral-7B的0.52、Mistral-12B的0.68；DeepSeek-R1-8B路由准确率0.79但推理速度慢9.9倍。数值计算上Mistral-7B准确率仅29%，Python实现100%准确；接入实时行情接口后价格预测错误从210%降至0.00%。混合检索Hit@5达76%，MRR 0.74。证据验证环节，仅校验生成内容与共享证据匹配仅能捕捉35%的错误，独立来源校验可捕捉77%的错误。

### 核心结论
不要让同一LLM包揽全流程任务，每个环节匹配最优组件（小模型路由、代码做计算、大模型做生成、独立层做验证）的多Agent架构，性价比远高于单纯堆叠大模型尺寸
