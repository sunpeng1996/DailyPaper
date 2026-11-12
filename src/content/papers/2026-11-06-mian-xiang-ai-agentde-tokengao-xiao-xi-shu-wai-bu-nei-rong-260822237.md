---
title: 'Read Less, Solve More: Token-Efficient Sparse Reading of External Content
  for AI Agents'
title_zh: 面向AI Agent的Token高效稀疏外部内容读取框架SparseRead
authors:
- Zedong Liu
- Jiaan Wu
- Xinyang Ma
- Le Xu
- Kai Wang
- Yuanchao Hu
- Dingwen Tao
- Guangming Tan
affiliations:
- University of Chinese Academy of Sciences
- Institute of Computing Technology, CAS
- Songshan Lake Materials Laboratory
arxiv_id: '2608.22237'
url: https://arxiv.org/abs/2608.22237
pdf_url: https://arxiv.org/pdf/2608.22237
published: '2026-11-06'
collected: '2026-11-12'
category: Agent
direction: AI Agent 外部内容读取效率优化
tags:
- LLM Agent
- Token Efficiency
- Sparse Reading
- Context Management
- RAG
one_liner: 无需修改Agent模型的可复用读取控制层，最高降92.9%Token、89%时延且保任务效果
practical_value: '- 电商导购Agent、商品详情页问答Agent可直接复用SparseRead架构，对商品详情、评价、规则等大文本做稀疏读取，降低大模型调用成本同时避免无关内容干扰回答准确率

  - 可借鉴Read Intent Protocol设计，在RAG召回阶段结合用户当前Query意图+历史会话意图做分槽位证据覆盖度追踪，减少重复召回、冗余片段进入上下文

  - Budgeted Read Gate的2L最坏开销绑定机制可直接复用，避免稀疏读取迭代开销超过直接全量读取的成本，平衡性能与最坏case风险

  - 多Reader Backend适配不同资源类型的设计，可迁移到多模态商品内容（文本/表格/JSON规格）的信息提取场景，针对不同资源选最优召回/计算方式'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
AI Agent执行任务时会大量读取网页、文档、工具返回等外部内容，现有方案通常全量加载，导致Token开销、时延上升，还会稀释有效证据引发错误；传统RAG、上下文压缩等方案没有统一的读取意图追踪、覆盖度管理和成本fallback机制，无法适配异构资源和动态变化的Agent信息需求。

### 方法关键点
- 设计Read Intent Protocol，追踪会话级+当前访问级双重读取意图，记录证据覆盖度和资源版本，避免重复读取和无效验证
- 实现Adaptive Reader Backends，统一异构资源（文本/PDF/表格/JSON/代码库）的读取接口，根据资源类型、意图自动选择最优证据定位方法（BM25/混合检索/列查询/键路径查找等）和暴露形式
- 新增Budgeted Read Gate，按单资源全量读取长度L设置累计曝光预算，稀疏读取累计开销超过L时自动fallback到全量视图，保证单资源最坏曝光不超过2L

### 关键实验
覆盖6个大模型（包括Claude Opus 5、DeepSeek系列、Qwen等）、5类场景（长文档QA、多文件审计、结构化分析、Web深度搜索、科学计算），对比原生Agent、静态RAG、Agentic RAG、ACON等基线：SparseRead最高降低92.9%总Token、89.0%端到端时延，97%场景下任务效果持平或提升；Web深度搜索场景降31.0~43.0%Token、23.0~37.0%任务耗时，同时效果提升5~14个百分点。

### 核心结论
更多的上下文输入不会自动带来更好的任务效果，通过受控的稀疏读取可以同时实现成本下降和效果提升。
