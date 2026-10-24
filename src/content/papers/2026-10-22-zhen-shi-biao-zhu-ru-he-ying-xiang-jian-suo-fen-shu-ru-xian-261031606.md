---
title: 'How Ground Truth Shapes Retrieval Scores: Evidence-Aware Evaluation of a Retrieval-Augmented
  Generation System for Breast Lesions'
title_zh: 真实标注如何影响检索分数：乳腺病变RAG系统的证据感知评估
authors:
- Miguel Mochizuki Silva
- Samuel Ismael
- Mateus C. Dias
- Thaís Gaudêncio
- Yuri Malheiros
- Barufaldi
affiliations:
- Universidade Federal da Paraíba (UFPB)
- Perelman School of Medicine, University of Pennsylvania
arxiv_id: '2610.31606'
url: https://arxiv.org/abs/2610.31606
pdf_url: https://arxiv.org/pdf/2610.31606
published: '2026-10-22'
collected: '2026-10-24'
category: Eval
direction: RAG系统评估 · 标注优化
tags:
- RAG
- Retrieval Evaluation
- Cross-Encoder
- Chunking Strategy
- LLM Judge
one_liner: 提出证据感知RAG检索评估协议，验证标注扩展不改变检索排序结果
practical_value: '- 构建RAG评测集时可采用证据跨度映射法，所有包含目标信息的chunk均标为正例，避免因chunk切分/标注不全误判检索效果，适合电商商品知识库、用户咨询问答库的RAG评测

  - 通用知识库RAG可直接复用384token chunk+20%重叠的切分策略，搭配BM25+稠密向量+cross-encoder重排的混合检索架构，性价比最优

  - 迭代RAG评测标注时，仅扩展同证据的正例chunk无需重新跑检索排序实验，可大幅降低评测集迭代的工程成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有RAG检索评估默认以单标注chunk为正例，指标数值受标注覆盖度干扰，无法客观衡量检索能力，高风险场景下易出现评估偏差。
### 方法关键点
1. 提出证据感知评估协议：将问题对应的证据跨度映射到所有包含该内容的chunk，所有含等价证据的重叠chunk均标记为正例，避免chunk切分规则干扰评估结果；
2. 对比4种检索配置（混合BM25、稠密向量、cross-encoder重排），遍历128~1024token chunk大小、0~20%重叠率的参数组合；
3. 检索用Recall@K、MRR、nDCG等指标，生成效果采用DeepEval claim级指标+DeepSeek-v4-pro LLM judge评估。
### 关键结果
最优配置为384token chunk+20%重叠的混合检索器，17/18的查询前3返回命中目标证据，Recall@3、R-Precision、MRR@3、nDCG@3均达0.94；扩展标注将证据跨度从25增至37、正例chunk从36增至51，完全不改变检索排序结果。
