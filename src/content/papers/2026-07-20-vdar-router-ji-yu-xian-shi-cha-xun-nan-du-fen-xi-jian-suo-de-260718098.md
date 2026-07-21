---
title: 'VDAR-Router: Adaptive LLMs Routing via Verbalized Query Difficulty Analysis
  Retrieval'
title_zh: VDAR-Router：基于显式查询难度分析检索的自适应LLM路由
authors:
- Yu-Chien Tang
- Jun-Chen Hung
- Wen-Chih Peng
- An-Zi Yen
affiliations:
- National Yang Ming Chiao Tung University
arxiv_id: '2607.18098'
url: https://arxiv.org/abs/2607.18098
pdf_url: https://arxiv.org/pdf/2607.18098
published: '2026-07-20'
collected: '2026-07-21'
category: LLM
direction: LLM部署 · 自适应路由成本优化
tags:
- LLM Routing
- Cost Optimization
- Training-free
- Retrieval Augmented
- Query Difficulty
one_liner: 无需额外训练的LLM路由框架，基于查询难度相似度检索历史样例平衡性能与成本
practical_value: '- 可直接复用难度分析+检索匹配的思路优化Agent工作流的模型路由：电商场景下，简单query（如商品属性查询、订单状态查询）路由给小模型降本，复杂推理query（如活动满减计算、个性化推荐理由生成、售后纠纷处理）路由给大模型保效果

  - reward加权的排序逻辑可直接迁移到多模型服务的调度策略：根据业务对精度/成本的容忍度调整α/β权重，大促期间调大α保障响应质量，平峰期调大β控制推理成本

  - 预设的7维能力难度分析prompt模板可直接复用：无需重新设计评估维度，即可快速适配到业务query分层、多模型调度场景，路由决策的可解释性远高于黑盒训练的路由模型'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM路由方法大多依赖输入query的表层语义或嵌入相似度做模型分配，忽略query本身的难度特征，容易出现语义相似但难度差异大的query路由错误：要么简单query调用大模型浪费成本，要么复杂query调用小模型效果不达标；此外多数路由方案需要额外训练专属路由模型，部署成本高、可解释性差，难以适配业务快速迭代的需求。

### 方法关键点
- 设计Difficulty Analyst模块，基于推理、理解、指令遵循、Agent能力、知识检索、编码、多语言7个预设能力维度，对每个query生成显式的难度分析文本，替代原始query作为路由特征
- 离线将所有历史query的难度分析编码后构建检索库，在线推理时先对新query生成难度分析，再检索Top-K个难度特征相似的历史样例
- 基于检索样例对应的各候选LLM历史性能、推理成本，通过加权奖励函数（α控制性能权重、β控制成本权重，α+β=1）计算综合得分，选择得分最高的模型
- 全流程无需额外训练，为即插即用的插件式框架

### 关键实验
在RouterBench、LLMRouterBench、ArenaExpert5K三个公开数据集上对比KNN、RouteLLM、RouterDC、ICL-Router等7个基线方案：
- RouterBench数据集α=0.8（优先保性能）场景下，奖励得分达48.61，比最高基线ICL-Router的42.15提升15.3%，同时推理成本比ICL-Router降低42.4%
- ArenaExpert5K数据集上，两两偏好预测准确率达60.28%，Spearman相关性达0.5137，均显著优于所有基线
- 用2B参数小模型作为Difficulty Analyst时效果几乎无下降，进一步降低了路由本身的推理开销

### 核心结论
对LLM路由决策而言，query的难度特征相似度远高于表层语义相似度的参考价值，基于难度匹配的检索式路由能以极低的训练部署成本实现远超基线的性价比。
