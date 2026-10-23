---
title: 'Chunk Recomputation under Real Document Revisions: Measuring Update Cost and
  Retrieval Quality of Fixed, Recursive, and Content-Defined Chunking'
title_zh: 真实文档修订场景下的分块重计算：三类分块的更新成本与检索质量测评
authors:
- Yuning Bian
- Lele Xu
- Yifan Yuan
- Xinyu Yin
- Chengyan Zhan
affiliations:
- Anhui University of Technology
arxiv_id: '2610.31019'
url: https://arxiv.org/abs/2610.31019
pdf_url: https://arxiv.org/pdf/2610.31019
published: '2026-10-22'
collected: '2026-10-23'
category: RAG
direction: RAG 动态知识库分块策略优化
tags:
- RAG
- Chunking
- Incremental Indexing
- Embedding Reuse
- Retrieval Evaluation
one_liner: 实测三种无状态分块在真实文档修订下的更新成本与检索质量，明确固定分块成本最高
practical_value: '- 电商商品详情页、客服知识库、广告规则库这类高频更新的RAG场景，优先弃用无重叠固定大小分块，改用递归分块或CDC，可降低30%-50%的重嵌入计算成本，同时检索质量损失<2%

  - 对于小编辑占比高的业务场景（比如商品参数修改、活动规则局部更新），递归分块的成本优势更明显，小编辑场景下英文语料可将重嵌入占比从46%降到25%

  - CDC分块在无空格的中文长文本场景下存在适配问题，需额外增加分词fallback逻辑，避免分块失败

  - 评估分块策略不能只看静态检索效果，必须增加动态更新下的重计算率指标，尤其是高频迭代的业务知识库'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG分块策略的评估均基于静态语料快照，但业务场景中的知识库（电商商品库、客服规则库、广告素材库等）始终处于持续更新状态，文档局部编辑会引发分块边界漂移，大量未修改文本也需要重新嵌入，这部分动态更新成本长期缺乏系统量化，且成本降低是否会伴随检索质量下降也未有明确结论。
### 方法关键点
- 定义严格的字节级完全匹配复用规则：仅当新分块的完整输入（含模型特殊token）与旧分块完全一致时才复用embedding，重计算率为需重计算的token数占新文档总输入token的比例
- 对比三种无状态分块策略：无重叠固定大小分块、优先段落拆分的递归分块、基于内容指纹的CDC分块
- 构建中英双语维基百科相邻修订对benchmark，共120对修订，标注240个问题的证据跨度，全程使用冻结的BGE-M3 embedding模型，固定2048 token检索预算
### 关键实验
在116篇三种分块均成功的通用样本上测试：
- 中文场景：固定分块重计算率68.4%、递归分块55.7%、CDC 54.0%；英文场景：固定分块57.4%、递归分块37.9%、CDC 42.8%
- 三种分块的证据召回率差距均小于2个百分点，无显著差异
- 小编辑场景（编辑占比≤5%）下递归分块成本优势最突出，英文语料重计算率仅25%，较固定分块低21个百分点
### 核心结论
对于需要持续更新的RAG知识库，分块策略的动态更新成本是比静态检索效果优先级更高的选型指标，无重叠固定分块在所有参数下更新成本均为最高。
