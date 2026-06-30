---
title: 'AB-RAG: Adaptive Budgeted Retrieval-Augmented Generation for Reliable Question
  Answering'
title_zh: AB-RAG：面向可靠问答的自适应预算检索增强生成
authors:
- Ansh Kamthan
affiliations:
- Manipal University Jaipur
arxiv_id: '2606.29090'
url: https://arxiv.org/abs/2606.29090
pdf_url: https://arxiv.org/pdf/2606.29090
published: '2026-06-27'
collected: '2026-06-30'
category: RAG
direction: RAG · 自适应检索 · 置信度估计
tags:
- RAG
- Adaptive Retrieval
- Confidence Estimation
- Self-consistency
- LLM
one_liner: 训练免调适配开闭源模型的自适应预算RAG，基于多信号置信度决定是否追加检索
practical_value: '- 落地RAG做成本控制时，可直接复用该自适应预算框架：简单query提前停止检索，节省context窗口和API成本，复杂query才追加检索，平衡成本与效果

  - 闭源API场景做RAG时，可用self-consistency作为模型置信度的代理，不需要访问模型内部token概率就能得到可靠置信度信号，适配商业API落地

  - 短输出/短回答场景做置信度设计时，不要复用答案-全文余弦相似度做一致性信号，长度不匹配会导致该信号完全失效，可替换为字符串匹配或NLI验证

  - 多信号融合设计时，必须逐个做 ablation 验证信号有效性，本文原检索方差信号符号设计错误，实测后才修正，这个工程思路值得借鉴'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有主流RAG对所有查询都固定检索段落数量，简单问题过度检索浪费计算资源、context空间和API成本，难问题又检索不足导致效果差；现有自适应RAG方法要么需要训练无法适配闭源API，要么没有明确的检索预算约束，缺一个能适配所有模型、带成本边界的自适应检索方案，在当前大量QA系统基于商业API落地的背景下，这个问题有明确实用价值。

### 方法关键点
- 训练免调、与 backbone 无关，同时支持开放权重模型和闭源商业API
- 三信号融合置信度估计：开放模型用生成token平均概率做S1（模型自身置信度），闭源API用self-consistency（多次采样的答案一致率）做S1代理；S2为答案与证据的嵌入相似度；S3为重排序得分的方差（高方差代表重排序能清晰区分相关/无关，为正向信号），加权融合得到总置信度
- 自适应循环机制：从少量检索开始生成答案，置信度超过阈值则停止，否则追加检索，直到达到预设预算，单阈值即可调节成本-准确率 tradeoff

### 关键实验
在HotpotQA（多跳问答）、TriviaQA（事实类问答）两个数据集，测试Qwen2.5-1.5B、Llama3.2-3B、Claude Haiku三个backbone，对比固定检索RAG：Llama3.2-3B在HotpotQA的Exact Match从39.5%提升到45%，Claude Haiku在TriviaQA从35.5%提升到40%；置信度拆分后，TriviaQA高置信答案Exact Match为57.6%，低置信答案为0%，分离效果极强；ablation验证仅S1（模型自身置信度）是强预测信号，S2对短回答完全无效。

### 核心结论
对落地RAG来说，可靠的置信度对错分离比单纯的平均准确率提升更有实用价值。
