---
title: 'LMEG-Doc: Layout-Grounded Multi-View Evidence Graphs for Multimodal Long-Document
  Retrieval'
title_zh: LMEG-Doc：基于布局的多视图证据图多模态长文档检索框架
authors:
- Changcheng Fu
- Xiao Liu
- Qi Yu
- Yage Wang
- Derek Young
- Giri Iyengar
affiliations:
- Capital One
- University of Southern California
arxiv_id: '2611.18901'
url: https://arxiv.org/abs/2611.18901
pdf_url: https://arxiv.org/pdf/2611.18901
published: '2026-11-13'
collected: '2026-11-17'
category: RAG
direction: 多模态长文档检索 · 图增强RAG
tags:
- Multimodal Retrieval
- Graph RAG
- Long Document
- Cross-Page Relation
- VLM
one_liner: 无需任务特定训练，通过布局证据图+跨页关系建模提升多模态长文档检索及下游QA效果
practical_value: '- 做电商商品详情页、商家资质文档、活动规则长文档RAG时，可复用其元素建模方案，将段落、图片、表格、caption作为节点构建结构关系图，避免孤立匹配漏掉关联证据（比如商品参数表和对应描述段落联动召回）

  - 跨页关联召回可借鉴CRR方案：先用语义/lexical/视觉相似性等规则生成候选对，再用轻量VLM做置信度校验过滤，平衡召回效果和计算成本，适合跨页的活动条款、保修规则等召回场景

  - 多模态检索融合可复用其四视图打分+个性化PageRank传播+RRF融合的流程，无需修改下游LLM即可提升召回准确率，可直接接入现有RAG/Agent问答流水线'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态长文档检索大多基于query与文档元素的独立相似度排序，忽略互补证据间的关联，导致和query直接匹配度低但包含核心信息的图表、跨页关联内容被漏召回，严重影响下游问答准确率。

### 方法关键点
- 先将文档解析为带空间位置、类型属性的结构化元素（段落、标题、图表、caption等），构建初始证据图，包含阅读顺序、图表-caption关联、上下文关联、空间邻近四类边，新增视觉组、section组辅助节点
- 提出Cross-Page Relation Refinement（CRR）模块，通过语义/词汇/视觉相似、文本引用、数值锚点等规则生成跨页候选关联对，再用VLM校验保留高置信度跨页边
- 检索阶段融合BM25、BGE-M3、SigLIP 2、ColPali四视图打分得到初始种子节点，用个性化PageRank沿图传播相关性，再通过RRF融合初始排序和传播后排序，同时输出布局级、页面级两类召回结果

### 关键实验
在MMDocIR、DocScope、FinRAGBench-V三个基准上测试，无需任务特定训练，MMDocIR上布局召回L@10达70.7%，比ColPali高8.7个百分点；下游QA用Qwen3.8-27B时，比基线分别提升7.6%（DocScope）和15.8%（FinRAGBench-V），准确率超过GPT-6.1 Sol等专有模型。

### 核心结论
多模态长文档检索不能仅依赖独立元素相似度，显式建模元素间结构关联和跨页依赖，能以极低侵入性大幅提升召回和下游QA效果。
