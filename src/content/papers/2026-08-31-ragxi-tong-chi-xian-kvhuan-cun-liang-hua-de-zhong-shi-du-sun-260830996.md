---
title: 'Faithfulness Is Not Free: Auditing Offline KV-Cache Quantization in Retrieval-Augmented
  Generation'
title_zh: RAG系统离线KV缓存量化的忠实度损耗审计研究
authors:
- Atta Ul Asad
- Ahsan Bilal
- Muhammad Ali
- Muhammad Haseeb
- Dean F. Hougen
affiliations:
- Lahore University of Management Sciences
- University of Oklahoma
- Air University
- National University of Sciences and Technology
arxiv_id: '2608.30996'
url: https://arxiv.org/abs/2608.30996
pdf_url: https://arxiv.org/pdf/2608.30996
published: '2026-08-31'
collected: '2026-09-01'
category: RAG
direction: RAG优化 · KV cache 量化保真
tags:
- RAG
- KV-cache
- Quantization
- Faithfulness
- Offline Cache
one_liner: 首次验证离线KV缓存INT4量化会造成RAG回答忠实度的隐藏损耗，准确率指标无法识别
practical_value: '- 线上RAG类业务（电商智能客服、商品问答、检索Agent）如果用离线KV缓存降本，优先选择INT8量化，几乎无准确率和忠实度损失，可直接复用

  - 若要采用INT4量化压缩存储，不能仅评估EM/F1等准确率指标，必须加入HHEM、NLI、LLM judge多维度忠实度校验，避免答案正确但不依赖检索上下文的隐藏风险

  - 检索chunk多、噪声高的场景（如多轮多文档导购Agent）尽量避免使用INT4量化，这类场景下忠实度损耗会被显著放大

  - 离线KV缓存的实际压缩比需计入scale/zero-point元数据开销，INT4实际压缩比约3.6倍而非标称4倍，做存储容量规划时要预留冗余'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RAG系统预计算离线KV缓存可大幅降低查询时的上下文编码开销，低比特量化是压缩缓存存储的主流方案，但现有评估仅关注准确率，未验证量化是否会破坏回答忠实度（即回答是否真实基于检索上下文），存在「答案正确但不依赖检索证据」的隐藏故障风险，此前无相关系统性审计研究。

### 方法关键点
- 控制变量设计：仅修改KV缓存精度，固定检索结果、prompt、解码策略，排除其他变量干扰
- 统一缓存构建：全检索上下文一次性因果预填充生成KV缓存，避免分块缓存拼接的位置mismatch混淆变量
- 多维度评估：除常规准确率（EM、F1）外，引入HHEM幻觉检测、DeBERTa-v3 NLI蕴含、Claude Haiku LLM judge三个互补的忠实度评估信号
- 四组对照：无缓存Oracle、BF16缓存基线、INT8量化、INT4量化

### 关键实验结果
采用Qwen2.5-7B-Instruct在RGB、HotpotQA两个数据集测试，检索chunk数K=1/3/5：
1. INT8量化几乎无损耗，准确率、忠实度均接近BF16基线，实际压缩比约1.9倍
2. INT4量化除准确率下降（EM错误翻转比正确翻转多10倍以上），更严重的是在准确率不变的样本中，超过90%的忠实度变化为负向，准确率指标完全无法识别该损耗
3. INT4忠实度损耗随检索chunk数增加、检索噪声升高放大，K=5时最高出现6%的退化输出（空内容/重复循环），实际压缩比约3.6倍，低于标称4倍

### 核心结论
KV缓存量化不能仅作为存储优化方案，必须作为可靠性决策对待，压缩RAG系统不能仅用EM/F1验证，上线前必须做忠实度审计
