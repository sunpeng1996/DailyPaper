---
title: 'RAGuard: A Layered Defense Framework for Retrieval-Augmented Generation Systems
  Against Data Poisoning'
title_zh: RAGuard：对抗检索增强生成系统数据投毒的分层防御框架
authors:
- Pushkal Kumar
- Tucker Nielson
- Tanish Kolhe
- Shubham Zala
- Vincent Li
arxiv_id: '2607.26339'
url: https://arxiv.org/abs/2607.26339
pdf_url: https://arxiv.org/pdf/2607.26339
published: '2026-07-28'
collected: '2026-07-30'
category: RAG
direction: RAG安全 · 数据投毒防御
tags:
- RAG
- Data Poisoning
- Adversarial Training
- Black-box Defense
- Counterfactual Inference
one_liner: 提出两层RAG投毒防御框架，无标注黑盒ZKIP层将攻击成功率降至0
practical_value: '- 业务中用RAG做商品咨询、客服问答的场景，可直接复用ZKIP的留一法反事实校验逻辑，无需标注投毒样本就能过滤恶意篡改的商品介绍、虚假评价等投毒内容，保障回答准确性

  - 做语义召回的场景，可借鉴对抗训练思路，用构造的虚假样本（如错配的商品属性、伪造的用户意图样本）微调dense retriever，提升召回阶段对恶意样本的抗干扰能力

  - 对高优query（如大额商品咨询、合规相关问题）可选择性开启ZKIP，配合批量化留一解码、早停等优化手段平衡防御效果和推理延迟，避免全量开启的6倍overhead'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG系统依赖外部语料实现事实性回答，是电商客服、商品咨询、检索问答等业务的核心组件，但语料投毒攻击（如恶意注入虚假商品信息、伪造评价、矛盾事实）会直接误导输出，给业务带来合规、用户信任风险。现有防御方案要么依赖标注的投毒样本泛化性差，要么仅针对检索/生成单阶段优化存在漏洞，无法覆盖全链路风险。
### 方法关键点
- 第一层防御：对抗微调dense retriever，构造伪造事实、矛盾内容、推理陷阱三类合成投毒样本，用三元组损失做对比训练，让检索器主动降低恶意段落的排序权重，在检索阶段减少投毒样本漏过
- 第二层防御：Zero-Knowledge Inference Patch（ZKIP）黑盒过滤，对top-k召回结果执行留一解码，通过移除单篇文档后的回答语义偏移、输出熵变化两个维度计算异常分，过滤高风险文档，全程无需投毒标注、真值答案或访问模型内部
### 关键实验
在投毒比例5%-30%的Natural Questions（NQ）数据集上测试，对比无防御基线：仅用对抗训练可将攻击成功率（ASR）降至0.072，叠加ZKIP后所有配置下ASR降至0.000，同时Recall@5仅比干净语料基线低最多0.03；默认k=5时ZKIP推理开销为6倍生成调用，批量化优化后可降至约2倍。
### 核心结论
针对RAG投毒的防御不能只依赖检索端的对抗训练，生成端的反事实自校验是无需标注、能应对未知攻击的高可靠补充手段
