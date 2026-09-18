---
title: Q&A on Any Spreadsheet Requires Interpreting Its Grid Structure
title_zh: 基于网格结构解析的任意电子表格RAG问答方法
authors:
- Zofia Smoleń
affiliations:
- Systems Research Institute, Polish Academy of Sciences
arxiv_id: '2609.20732'
url: https://arxiv.org/abs/2609.20732
pdf_url: https://arxiv.org/pdf/2609.20732
published: '2026-09-17'
collected: '2026-09-18'
category: RAG
direction: RAG表格解析 · 结构感知分块
tags:
- RAG
- Chunking
- Table Understanding
- Spreadsheet
- GNN
one_liner: 提出基于单元格角色标注的网格感知分块框架，大幅提升电子表格RAG问答质量
practical_value: '- 处理电商运营报表（销售、库存、财务）的RAG场景，可复用Row分块策略：为每个数值拼接完整表头层级路径，提升LLM数值理解准确率

  - 复杂嵌套表格解析优先选用GAT/DualModalityGNN做单元格角色标注，比固定表头规则在嵌套表头场景得分提升1.01分，适配商家多维度报表

  - 表格分块优化的收益核心在生成阶段而非检索阶段，无需为提升召回率修改分块语义，重点保障生成上下文完整性即可

  - 简单平表场景无需引入复杂模型，固定第一行表头的规则即可达到和复杂模型相当的效果，可分场景降级控制成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前工业界电子表格RAG分块普遍丢失表头上下文，59%的从业者反馈分块时的上下文丢失是最常见失败模式，现有STC、SpreadsheetLLM等方法仅适配固定结构表格，无法处理嵌套表头、多表共存等真实复杂表格，导致生成答案准确率低。

### 方法关键点
- 标注13类细粒度单元格角色（含3级行/列表头、聚合值、元数据等），训练6款单元格角色分类模型（3款节点分类器、3款图学习器），支持任意表格结构的角色识别
- 设计3种分块组装策略，其中Row策略为每行数据拼接完整的表头层级路径、表名等上下文，不跨表分块
- 端到端RAG pipeline融合BM25+稠密向量召回，取top5块送入Gemini 2.5 Flash生成答案

### 关键实验结果
在480个问答样本、382张表格的测试集上，对比Unstructured、STC等5个基线：最优GAT模型的人类评分达3.88，比SOTA STC的3.43高0.45分（p=1.5×10^-6）；即便用人类标注的完美角色，得分天花板仅4.01，说明固定角色分类方法存在瓶颈；收益集中在嵌套表头场景，比基线高1.15分，平表场景无显著收益。

### 核心结论
表格结构感知分块的收益不来自检索准确率提升，而来自让LLM能正确理解检索到的数值的业务含义。
