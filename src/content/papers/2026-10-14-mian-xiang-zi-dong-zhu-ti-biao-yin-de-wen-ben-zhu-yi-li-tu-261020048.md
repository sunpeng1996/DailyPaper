---
title: 'Reading the Neighborhood: Text-Attentive Graph Reranking for Automated Subject
  Indexing'
title_zh: 面向自动主题标引的文本注意力图重排序方法
authors:
- Lakshmi Rajendram Bashyam
- Ralf Krestel
affiliations:
- ZBW – Leibniz Information Centre for Economics
- Kiel University
arxiv_id: '2610.20048'
url: https://arxiv.org/abs/2610.20048
pdf_url: https://arxiv.org/pdf/2610.20048
published: '2026-10-14'
collected: '2026-10-18'
category: Other
direction: 极端多标签分类 · 图重排序优化
tags:
- Extreme Multi-label Classification
- Graph Reranking
- Heterogeneous GNN
- Retrieve-and-Rerank
- Long-tail Learning
one_liner: 提出融合受控词表邻域语义的异构图重排序模型TAGHN，提升极端多标签主题标引的长尾效果
practical_value: '- 电商商品类目/属性打标场景可复用思路：召回候选标签后引入标签层级邻域语义特征做重排序，提升长尾标签识别准确率

  - 极端多标签分类任务可借鉴打分头设计：将图结构特征与检索语义特征分解后融合，兼顾效果与可解释性

  - 少样本长尾标签优化可参考：利用标签体系的上下位语义关联，减少仅依赖单标签语义匹配带来的误差'
score: 4
source: arxiv-cs.IR
depth: abstract
---

**动机**：自动主题标引属于极端多标签分类任务，存在标签量级大、单标签正样本少、长尾标签占比高的痛点，现有方案将受控词表视为扁平结构，完全忽略词表内置的语义关联信息，长尾标签效果差。
**方法关键点**：提出TAGHN异构图重排序模型，首先为每个文档的召回候选标签引入词表邻域节点构建专属子图；相关性计算同时融合候选标签与文档的语义相似度、候选标签邻域与文档内容的匹配度；打分头将可解释的图衍生特征与检索信号融合输出最终得分。
**关键结果**：在含6198个标签的经济词表STW数据集上，macro F1达0.380，优于微调cross-encoder的0.346与固定词表XMLC分类器的0.278；micro F1超过所有对比重排序模型，与最优固定词表XMLC模型仅差3个百分点。
