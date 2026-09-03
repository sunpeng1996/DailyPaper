---
title: 'Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers'
title_zh: Trace as State：将推理轨迹作为长上下文Transformer的条件状态
authors:
- Xu Zou
- Jie Tang
affiliations:
- Z.ai
- Tsinghua University
arxiv_id: '2609.02702'
url: https://arxiv.org/abs/2609.02702
pdf_url: https://arxiv.org/pdf/2609.02702
published: '2026-09-02'
collected: '2026-09-03'
category: Reasoning
direction: 长上下文推理 · 推理轨迹复用优化
tags:
- Long-Context LLM
- Reasoning Trace
- Causal Attention
- Inference Optimization
one_liner: 将首遍推理轨迹作为状态前置到长上下文前二次推理，无需改模型即可大幅提升长任务效果
practical_value: '- 电商/推荐Agent处理超长用户行为序列、全量商品库检索等长任务时，可直接复用该方法：先让LLM首遍推理生成中间轨迹，将轨迹前置到原始上下文前二次推理，无需微调即可大幅提升长序列信息提取准确率

  - RAG系统处理超长商品评价、活动规则等文档的复杂查询时，将首遍检索+推理的中间轨迹前置，效果远好于将轨迹追加到上下文后的常规方案，可直接作为RAG长文档处理的优化trick

  - 长任务Prompt工程通用准则：将任务相关的先验条件、中间状态放在长上下文最前面，符合因果Transformer的处理逻辑，可显著降低模型记忆负担，提升推理效果'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有长上下文Transformer受因果注意力约束，后续输入的信息无法修改前面token的表征，处理长任务时关键任务状态往往要读完整个上下文才能得到，此时模型需要保留所有潜在状态的可能性，最坏情况下内存开销是状态前置场景的指数倍；现有常规方案是将推理轨迹追加到上下文后，无法让轨迹指导上下文重读过程，长上下文推理准确率低。
### 方法关键点
- 提出**TRACE AS STATE**推理方法，无需修改模型结构、无需微调，仅调整输入顺序即可生效；
- 首遍推理让LLM处理任务，生成1~5条推理轨迹，序列化后作为任务状态的文本代理；
- 二次推理时将轨迹前置到长上下文和问题之前，让轨迹中记录的任务状态全程指导上下文重读过程；对照组**TRACE APPEND**采用常规方案，将轨迹放在上下文之后、问题之前。
### 关键实验结果
在GraphWalks 256K、MRCRv2 8-needle 256K/512K、NUB-1M三个长上下文基准数据集上，测试DeepSeek V4 Pro、Qwen 3.7 Max、GLM-5.2三个主流大模型，27组模型-任务-指标组合中TRACE AS STATE赢了26组；在GraphWalks Parents任务上，DeepSeek V4 Pro的Exact Match从首遍的29.2%、TRACE APPEND的43.0%提升到81.8%，GLM-5.2更是直接提升到100%。
### 核心结论
因果Transformer处理长任务时，任何任务相关的先验/中间状态放在上下文前面的收益远高于放在后面，这是符合底层内存开销逻辑的通用规律。
