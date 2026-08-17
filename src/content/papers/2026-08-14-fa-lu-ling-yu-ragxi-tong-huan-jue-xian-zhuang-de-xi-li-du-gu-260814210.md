---
title: How Much Do Legal RAG Systems Still Hallucinate?
title_zh: 法律领域RAG系统幻觉现状的细粒度量化评估研究
authors:
- Souvick Das
- Sallam Abualhaija
- Domenico Bianculli
affiliations:
- SnT, University of Luxembourg
arxiv_id: '2608.14210'
url: https://arxiv.org/abs/2608.14210
pdf_url: https://arxiv.org/pdf/2608.14210
published: '2026-08-14'
collected: '2026-08-17'
category: RAG
direction: 垂直领域RAG · 幻觉评估
tags:
- RAG
- Hallucination
- Evaluation
- VerticalAI
- LegalAI
one_liner: 针对8款法律RAG系统开展细粒度幻觉分析，量化不同场景下的幻觉密度与严重程度
practical_value: '- 垂直领域RAG（如电商客服、合规审核Agent）可复用claim-level+answer-level双层评估框架，细粒度定位幻觉来源，替代粗粒度整体准确率评估，提升迭代效率

  - 业务侧RAG/Agent需新增false-premise query检测模块，电商场景下用户常提带错误假设的问题，提前识别纠正可大幅降低幻觉率

  - 高风险垂直场景RAG上线前，可参考该研究的测试范式，用领域专家标注的专属测试集做预上线校验，避免严重幻觉引发客诉、合规风险'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
垂直领域RAG落地时幻觉会引发严重业务风险，法律领域错误回答甚至会影响司法决策，当前缺乏对高风险场景RAG幻觉的细粒度量化分析结论。
### 方法关键点
覆盖8款主流法律RAG系统，跨英文GDPR、法语本国民法两个语料库；采用claim级+answer级双层评估维度，结合问题类型、用户persona多维度分析幻觉特征；最终用142道法律专家编写的独立问题集验证结论通用性。
### 关键结果
幻觉问题在法律RAG中普遍存在，最优系统幻觉率低于10%，最差系统幻觉率接近50%；包含错误假设的假前提问题幻觉率显著更高，是幻觉高发的高风险场景。
