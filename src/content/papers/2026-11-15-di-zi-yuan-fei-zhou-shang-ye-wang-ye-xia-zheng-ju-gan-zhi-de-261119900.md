---
title: 'Attribute or Abstain: Evaluating Evidence-Grounded Retrieval on the Low-Resource
  African Business Web'
title_zh: 低资源非洲商业网页下证据感知检索的归因与拒答能力评估
authors:
- Bakary Gibba
- Muhammad Abba Mandara
- Karim Ismail Abd-Ellah Mohamed
affiliations:
- Albukhary International University, Malaysia
arxiv_id: '2611.19900'
url: https://arxiv.org/abs/2611.19900
pdf_url: https://arxiv.org/pdf/2611.19900
published: '2026-11-15'
collected: '2026-11-17'
category: Eval
direction: RAG/Agent 事实归因与拒答能力评估
tags:
- RAG
- Fact Attribution
- Abstention
- Low Resource NLP
- Agent Evaluation
one_liner: 构建多语言非洲商业检索基准AfriBizClaims，验证单步RAG比多步Agent归因精度更高
practical_value: '- 业务RAG/Agent可复用「先做实体对齐校验再做事实归因」的评估逻辑，避免用户查询某商家时返回其他商家信息的实体错误，这类错误即使内容正确也属于严重业务故障

  - 低资源/长尾场景下无需盲目堆叠多步Agent流程，单步检索+严格引述提示词即可做到98%的归因精度，成本仅为多步Agent的1/10

  - 高风险场景（如商家资质核验、商品合规查询）可优先上线拒答逻辑，错误输出的业务代价比不输出高得多，优先保证输出100%有证据支撑

  - 大规模RAG效果验收可复用双AI法官+人工抽检的标注流程，大幅降低标注成本的同时保证标注一致性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
低资源商业场景下公开信息稀疏，现有RAG/Agent检索系统易输出无证据支撑的错误信息，而商业决策场景下错误信息的代价比不输出高得多；现有归因基准多基于高资源维基类文本，不匹配多语言、信息稀疏的商业网页场景，缺乏对拒答能力和实体对齐的评估。

### 方法关键点
- 构建AfriBizClaims基准：包含6个非洲市场、英法葡三语的150条企业查询，其中24条为虚构企业查询，要求系统正确拒答，覆盖8类企业核心字段
- 标注流程：采用双AI法官（GPT-6.1-sol + Claude Sonnet 5-5）做事实校验，区分支持、部分支持、不支持、实体错误四类标签，配套人工校验规则
- 对比三组同基座（DeepSeek-V4.1-Flash）系统：固定语料BM25检索、单步Web RAG、多步Agent流水线Konexium V1，评估维度覆盖精度、覆盖率、拒答能力、成本、稳定性

### 关键结果
- 单步BM25和Web RAG的每查询归因精度达98%，100%正确拒答所有虚构企业查询，Web RAG对可回答字段的覆盖率达78%
- 多步Agent流水线的每查询归因精度仅68%，指定企业查询全部返回其他企业信息，5/24的虚构企业查询错误输出内容，成本是Web RAG的10倍，两次运行结果Jaccard相似度仅0.36

### 核心结论
在低资源信息检索场景下，盲目堆叠多步Agent流程反而会降低事实准确性，严格的实体对齐校验和引述约束比复杂的流程设计更重要
