---
title: 'PageRecall: Measuring Page Selection in Literature-Grounded Question Answering'
title_zh: PageRecall：文献支撑问答场景下的页面选择效果度量
authors:
- Aaditya Chauhan
affiliations:
- Independent Researcher
- Everest Team
arxiv_id: '2609.18154'
url: https://arxiv.org/abs/2609.18154
pdf_url: https://arxiv.org/pdf/2609.18154
published: '2026-09-16'
collected: '2026-09-17'
category: RAG
direction: RAG 文献问答检索瓶颈优化
tags:
- RAG
- GroundedQA
- QuestionAnswering
- PageRanking
- Evaluation
one_liner: 发现文献问答证据定位瓶颈为页面召回而非模型阅读，提出跳过页选送全文档的优化方案
practical_value: '- RAG 落地可优先验证检索环节瓶颈，若单篇召回内容长度符合上下文窗口限制，可跳过细粒度段/页排序直接喂全内容，避免召回漏检导致的静默错误

  - 针对按位置指代的查询（如商品详情第3条规格、评价第2条），优先做结构化解析而非语义检索，大幅提升准确率

  - 对外输出依赖闭源模型的系统时，可配套可复现的验证工具集，基于固化工件校验核心效果指标'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
文献支撑问答需要同时完成论文召回、证据位置定位、按格式输出答案，过往无法区分证据定位错误来自召回环节还是模型阅读环节，缺乏对页面选择步骤的量化评估。
### 方法关键点
1. 拆分 pipeline 为页面选择器、证据定位模型两个独立模块，分别度量各环节精度；
2. 当单篇召回论文长度适配 LLM 上下文窗口时，跳过页面排序步骤直接传入全文档，仅对超长文档保留页排序作为降级方案；
3. 针对按位置指代的查询，提前解析结构化内容为可寻址列表，替代语义检索链路。
### 关键结果
原页面选择器金页召回率仅 52.6%，给定正确页面后证据定位准确率达 94%；优化后金页召回率在可解析论文上达 100%，最终系统测试集 paper F1=0.762、evidence F1=0.441、多选准确率 0.920。
