---
title: 'RIT-RAG: Navigating Document Corpora with Retrieval-Induced Trees'
title_zh: RIT-RAG：基于检索诱导树的多文档知识库导航框架
authors:
- Meghanadh Pulivarthi
- Swaraj Kumar Biswal
- Kushagra Bhushan
- Yatin Nandwani
- Sachindra Joshi
- Dinesh Raghu
affiliations:
- IBM
- IIT Kharagpur
arxiv_id: '2610.11370'
url: https://arxiv.org/abs/2610.11370
pdf_url: https://arxiv.org/pdf/2610.11370
published: '2026-10-08'
collected: '2026-10-09'
category: RAG
direction: RAG · 结构感知检索优化
tags:
- RAG
- Agentic RAG
- Hierarchical Navigation
- Information Retrieval
- Question Answering
one_liner: 融合内容检索与结构感知导航，平衡RAG精度召回 trade-off，提升多场景问答准确率
practical_value: '- 可复用「粗召chunk→生成查询专属子结构→Agent选择性读取」的架构，优化电商客服、商品知识库问答类RAG系统，解决现有Agentic
  RAG召回杂、精度低的问题

  - 离线处理可复用节点对齐的chunking方案：chunk不跨文档节点，每个chunk绑定所属节点、祖先节点元数据，无需额外大规模图构造，成本远低于GraphRAG类方案，适合大规模电商商品/帮助中心文档库

  - 可借鉴子树构建逻辑：用召回chunk的最高得分排序节点，保留节点到根的祖先路径，既保留结构上下文又控制给LLM的结构输入长度，避免全量结构无法入上下文的问题

  - 结论复用：当知识库存在天然层级结构（如电商帮助中心、商品类目、站点地图）时，优先利用原生结构比额外构造语义树/知识图的成本更低、效果更稳定'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agentic RAG仅基于离散chunk检索，缺乏文档结构感知，召回精度低，大量无关内容占用上下文；结构感知RAG（如PageIndex）需要提前锁定单文档，易出现早期决策错误无法挽回，召回率低，两者存在精度-召回的权衡矛盾，难以适配大规模多文档知识库问答场景。

### 方法关键点
- 离线阶段：为每个文档基于目录/站点地图构建层级树，每个节点对应文档的章节/页面，chunk按节点拆分不跨节点，每个chunk绑定所属节点ID、节点标题、祖先节点元数据存入检索索引
- 在线查询阶段：首先召回Top-k'个chunk，按chunk最高得分取Top-n个节点，拼接每个节点到根的所有祖先节点生成查询专属子森林，无需加载全量文档结构
- Agent迭代流程：Agent可调用GetToC工具获取子森林结构，自主选择要读取的节点内容，若未找到答案可重新生成查询触发新的召回和子森林生成，无需锁定单文档

### 关键实验
在WixQA（客服场景）、QASPER（论文问答）、FinanceBench（金融文档）3个公开数据集上，RIT-RAG相对同算力Agentic RAG精度提升2.4~10.5个点，相对PageIndex提升5.0~18.6个点；在包含284万页企业文档的新基准EntQABench上，相对最优基线精度提升6.8~11.4个点，同时在读取内容的F1值上全面领先基线，平衡了精度与召回。

### 核心结论
检索负责锚定潜在相关区域，Agent负责基于结构做精准读取，结合原生文档结构的检索诱导方案比额外构建语义结构的成本更低、可扩展性更强。
