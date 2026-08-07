---
title: 'MACRO: Markov Chain Routing of Transformer Layers'
title_zh: MACRO：面向Transformer层的马尔可夫链动态路由框架
authors:
- Paweł Batorski
- Abtin Pourhadi
- Akylgali Aitaza
- Przemysław Spurek
- Paul Swoboda
affiliations:
- Heinrich Heine University Düsseldorf
- Jagiellonian University
- IDEAS Research Institute
arxiv_id: '2608.05872'
url: https://arxiv.org/abs/2608.05872
pdf_url: https://arxiv.org/pdf/2608.05872
published: '2026-08-06'
collected: '2026-08-07'
category: LLM
direction: LLM推理优化 · 动态层路由
tags:
- Dynamic Routing
- Transformer
- LLM Inference
- Markov Chain
- Viterbi Decoding
one_liner: 不修改LLM权重，通过马尔可夫链动态层路由提升推理精度，同时降低路由搜索成本9.4倍
practical_value: '- 部署小参数LLM做电商客服/推荐文案生成/商品属性解析时，可直接复用MACRO框架，无需微调权重即可提升任务准确率，小模型收益最高可达12%+

  - MoE推荐/广告模型的专家调度可借鉴其设计：用轻量马尔可夫策略+top-k Viterbi解码替代复杂路由网络，降低调度开销

  - LLM垂直任务优化可复用其任务级路由思路：基于少量验证集反馈迭代全局路由策略，避免逐样本搜索带来的推理延迟'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM固定按层顺序执行，动态层路由可挖掘模型潜力提升推理表现，但现有方案要么需要修改模型权重，要么要逐测试样本做高成本搜索，甚至推理时依赖真值标签，无法低成本落地到垂直任务优化。

### 方法关键点
- 层路由建模为上下文相关的马尔可夫策略，状态包含当前层、计算预算阶段、层位移、操作上下文4个因子，支持层跳过、重复、回退、隐藏态加法、回归标准后缀5类操作
- 基于训练集反馈迭代更新马尔可夫转移分布，用分布估计方法+回放缓冲区保证收敛，无需反向传播修改LLM权重
- 训练完成后用top-k Viterbi算法解码高概率候选路由，再基于验证集选最优单路由全量部署，推理时无额外搜索开销

### 关键结果
在GSM8K、MMLU-Pro、MedQA等13个推理/知识基准上测试Qwen3系列、Llama 3.2、Mixtral 8x7B等开源LLM：平均比无路由基线提升5.0%准确率，比SOTA动态路由方法Dr.LLM提升7.2%，路由搜索时间从14.8小时降至1.6小时，成本降低9.4倍；小模型（如Qwen3-1.7B）收益最高，平均准确率提升12.68个点。

### 核心结论
LLM内部通常已经学到了正确答案的表征，合适的层路由不需要修改权重，只要把被模型后续层抑制的正确信号重新暴露出来即可提升准确率。
