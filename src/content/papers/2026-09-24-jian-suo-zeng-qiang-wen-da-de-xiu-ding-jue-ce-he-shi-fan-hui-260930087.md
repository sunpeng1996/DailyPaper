---
title: Return or Revise? Learning When Revision Helps Retrieval-Augmented QA
title_zh: 检索增强问答的修订决策：何时返回草稿何时执行修订
authors:
- Nicholas Kashani Motlagh
- Tim Anderson
- Jeremy Gwinnup
- Grant Erdmann
affiliations:
- DCS Corp
- Air Force Research Laboratory
arxiv_id: '2609.30087'
url: https://arxiv.org/abs/2609.30087
pdf_url: https://arxiv.org/pdf/2609.30087
published: '2026-09-24'
collected: '2026-09-25'
category: RAG
direction: RAG问答 · 动态修订决策优化
tags:
- RAG
- Question Answering
- Decision Making
- LoRA
- Adaptive Generation
one_liner: 基于成对标注训练可恢复性预测器优化RAG问答返回/修订决策，效果优于草稿置信度方案
practical_value: '- 电商商品问答、客服应答场景可复用成对标注范式，离线同时标注直接返回、修订后的答案效果，训练决策模型规避把正确的商品参数、售后规则改坏的有害修订

  - 落地自适应RAG系统时优先采用「生成草稿+标准RAG生成」二选一的路由架构，比先打草稿再基于检索结果修订的方案收益高2个百分点左右，还能降低不必要的修订推理成本

  - 训练决策模型时优先用LoRA微调全量输入（用户query、草稿答案、检索上下文），比仅依赖草稿置信度、冻结特征分类器的效果提升更显著'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有RAG修订系统仅基于草稿置信度决策是否修订，既无法预估修订的实际收益，还常出现把正确草稿改坏的情况，而单纯的整体准确率指标无法区分「低风险全量修订」和「高风险选择性修订」两类场景，缺乏可落地的精细化决策方案。

### 方法关键点
- 提出可恢复性（recoverability）指标：定义为修订修复错误的概率减去损坏正确答案的概率，离线阶段同时标注每个样本的草稿、修订后答案的正确性，生成四分类（保留正确、修复错误、损坏正确、未修复错误）的成对标签
- 决策模型采用LoRA微调Llama 3.1 8B，输入覆盖query、草稿、检索到的全部证据，预测可恢复性并设定阈值，超过阈值才触发修订
- 对比基线包括仅预测草稿正确性的模型、基于检索效用的工程特征基线，以及固定全量修订、固定返回草稿的策略

### 关键结果
在NQ-Open、TriviaQA、PopQA共25870个测试样本上验证，三个检索配置（DPR、BM25、BM25+MonoT5重排）下，可恢复性预测策略比全量修订准确率提升1.10-1.33个百分点，比仅用草稿置信度的方案高0.23-0.68个百分点，平均闭合35.9%-41.4%的最优oracle gap。但如果加入无草稿的标准RAG答案作为可选项，「草稿/标准RAG」二选一的策略比「草稿/修订」二选一高2个点左右，加入修订作为第三选项无显著增益。

### 核心结论
修订的价值完全取决于可选的替代方案，离线成对标注所有可选路径的效果是优化决策的基础。
