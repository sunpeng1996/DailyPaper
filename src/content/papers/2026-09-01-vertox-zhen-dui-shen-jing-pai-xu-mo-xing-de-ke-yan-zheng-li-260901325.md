---
title: 'VerTox: Verifiable Reward-Guided Corpus Poisoning Against Neural Ranking Models'
title_zh: VerTox：针对神经排序模型的可验证奖励引导语料投毒框架
authors:
- Zhiqi Huang
- Vivek Datla
- Zhichao Xu
- Puxuan Yu
- Vivek Srikumar
- Alfy Samuel
affiliations:
- Capital One
- University of Utah
- Snowflake Inc.
arxiv_id: '2609.01325'
url: https://arxiv.org/abs/2609.01325
pdf_url: https://arxiv.org/pdf/2609.01325
published: '2026-09-01'
collected: '2026-09-02'
category: RecSys
direction: 排序模型鲁棒性 · 语料投毒攻击
tags:
- Corpus Poisoning
- Neural Ranking
- RLVR
- GRPO
- RAG Security
- Adversarial Attack
one_liner: 用带可验证奖励的RL微调小LLM生成高隐蔽强迁移的语料投毒文档攻击排序与RAG系统
practical_value: '- 做RAG/检索系统防御时，可复用VerTox的对抗生成逻辑构造样本做adversarial training，同时新增双向NLI事实一致性校验、查询重复度检测规则，拦截投毒文档

  - 开放检索场景（电商商品搜索、内容社区搜索）可在索引入库环节增加低PPL高语义相似但事实不一致的文档检测逻辑，降低被投毒风险

  - 需黑盒攻击排序模型的场景（如合规性测试、竞品排名优化验证）可复用GRPO+多维度可验证奖励的小LLM微调框架，无需目标模型梯度即可生成高迁移性样本

  - 小LLM做特定目标生成任务时，可参考这种多信号组合的RL reward设计，比单纯prompting的任务达标率高30%以上'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
神经排序模型是搜索、推荐、RAG系统的核心组件，但LLM大幅降低了批量生成流畅伪造内容的门槛，现有语料投毒方法普遍存在生成内容可读性差易被过滤、攻击迁移性弱、无法同时实现排名提升与事实篡改的问题，需要更隐蔽高效的攻击框架暴露现有系统的脆弱性，为防御提供依据。
### 方法关键点
1. 将语料投毒建模为可验证奖励引导的RL（RLVR）问题，采用GRPO算法对<1B参数量的小LLM做LoRA微调生成对抗文档，训练仅需本地代理排序模型的反馈，无需目标黑盒排序系统的内部权限；
2. 设计三维可验证奖励：排名扭曲奖励基于本地代理排序模型的得分差做正向激励，归一化处理保证跨查询训练信号稳定；事实篡改奖励采用双向NLI幻觉检测器，奖励和原Top1文档事实不一致的生成，避免无意义paraphrase；查询重复惩罚限制生成内容与查询的编辑距离超过原Top1文档的部分，避免query stuffing这类易被检测的作弊手段；额外增加长度正则项，保证生成文档长度和原文档接近。
### 关键结果
白盒攻击场景下ASR接近100%，Top@1最高达0.84，比8B LLM prompting基线高30pct，生成文档PPL仅12-32，和原生LLM内容无明显差异，难以通过perplexity、可读性过滤检测；黑盒攻击场景下跨BGE、Cohere商用嵌入、SPLADE稀疏检索、RankLLaMA重排等所有主流排序架构，Top@1最高达0.89，迁移性极强；投毒后RAG系统回答准确率从0.7直接跌到0.3，仅需投毒Top2以内的文档即可大幅破坏检索质量。
### 核心结论
仅用弱代理排序模型微调的小LLM生成的投毒文档，可以无差别攻击所有主流开源/商用排序模型，是开放检索环境下真实存在的高隐蔽性威胁。
