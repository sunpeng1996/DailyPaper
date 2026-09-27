---
title: 'Seek: Self-Evaluative Exploration for Knowledge Retrieval'
title_zh: Seek：面向知识检索的自评估探索框架
authors:
- Amin Bigdeli
- Radin Hamidi Rad
- Negar Arabzadeh
- Sajad Ebrahimi
- Hai Son Le
- Charles L. A. Clarke
- Ebrahim Bagheri
affiliations:
- University of Waterloo
- Mila – Quebec AI Institute
- University of California, Berkeley
- University of Toronto
- Toronto Metropolitan University
arxiv_id: '2609.28980'
url: https://arxiv.org/abs/2609.28980
pdf_url: https://arxiv.org/pdf/2609.28980
published: '2026-09-24'
collected: '2026-09-27'
category: RAG
direction: RAG检索优化 · 迭代式召回
tags:
- Iterative Retrieval
- Relevance Feedback
- Query Expansion
- Training Free
- RAG Retriever
one_liner: 无需训练的迭代检索框架，结合伪文生成与相关性评估突破单轮检索召回上限
practical_value: '- 电商搜索长尾/复杂query场景可复用迭代检索逻辑：无需额外训练，基于历史召回结果的正负反馈生成伪文扩展query，弥补单轮BM25/稠密检索的词汇语义
  mismatch问题，提升召回率

  - 推荐系统冷门内容召回可借鉴自适应终止策略：配置召回质量/覆盖度饱和双触发条件，在效果达标时提前终止迭代，平衡计算成本与召回收益

  - Agent的知识库检索模块可直接集成Seek框架：替换原有单轮检索链路，在推理密集型任务下能获得远高于训练后重排器的nDCG收益，且对底层召回器无强依赖，兼容BM25、稠密检索等多种底座

  - 小模型落地检索场景可复用伪文生成+分级评估的范式：7B级小模型即可获得优于同基座训练后重排器的效果，降低训练成本与部署门槛'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM驱动的检索、重排系统均采用单轮语料交互范式，一旦初始召回漏判相关文档，后续重排阶段无法恢复；尤其在推理密集型复杂query场景下，词汇不匹配、隐含约束多等问题会导致单轮召回天花板极低，亟需可动态调整的检索机制突破该限制。
### 方法关键点
- 全程无任务特定训练，测试阶段运行3阶迭代循环：基于原始query与历史反馈池生成伪扩展文档，结合原始query构造扩展召回请求发起新一轮检索
- 新增LLM相关性评估模块：对新召回的未见过文档按原始query打0-3分级标签，正负反馈同步进入反馈池指导下一轮伪文生成，避免检索漂移
- 自适应终止逻辑：满足top-K全为最高相关（质量饱和）或连续两轮top-K完全一致（覆盖饱和）时提前停止，最多迭代5轮
- 最终排序采用双层规则：评估过的文档按相关性得分降序，同得分按召回最高分排序，未评估文档按召回最高分排序
### 关键实验
在TREC DL 2019/2020、推理密集型BRIGHT基准测试，对比BM25、同基座训练后的稠密检索器、重排器：
- TREC DL场景：Seek搭配Qwen2.5-7B nDCG@10达71.6/65.1，与同基座训练后重排器效果持平，Recall@100显著优于单轮BM25
- BRIGHT场景：Seek搭配Qwen2.5-7B nDCG@10平均达30.9，较BM25相对提升82%，超过所有同基座训练基线；搭配GPT-4.1平均nDCG@10达37.4，超最强基线37%；搭配BM25的效果接近搭配训练后稠密检索器ReasonIR的效果

迭代式检索结合显式相关性反馈的无训练范式，可突破单轮检索的召回天花板，在复杂query场景下效果远优于需要大量训练的重排方案
