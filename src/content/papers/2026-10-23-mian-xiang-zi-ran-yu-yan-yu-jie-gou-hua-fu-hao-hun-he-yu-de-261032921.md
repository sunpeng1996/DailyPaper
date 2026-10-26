---
title: Adaptive Frequency Threshold Byte Pair Encoding for Mixed Natural Language
  and Structured Symbolic Corpora
title_zh: 面向自然语言与结构化符号混合语料的自适应阈值BPE分词
authors:
- Pietro Di Nicco
- Lucio La Cava
- Andrea Tagarelli
affiliations:
- DIMES Department, University of Calabria, Italy
arxiv_id: '2610.32921'
url: https://arxiv.org/abs/2610.32921
pdf_url: https://arxiv.org/pdf/2610.32921
published: '2026-10-23'
collected: '2026-10-26'
category: LLM
direction: LLM分词 · 自适应阈值BPE优化
tags:
- BPE
- Tokenization
- AdaBPE
- Supertoken
- LLM
one_liner: 提出自适应频率阈值的AdaBPE分词，兼顾通用文本和低占比结构化符号的编码效率
practical_value: '- 针对电商/广告领域的结构化符号（如商品ID、规格参数标识、活动编码），可复用AdaBPE的类型区分阈值逻辑，给领域专属符号设置更低的合并阈值，在不增大整体词表的前提下提升结构化内容的编码效率，降低KV
  cache开销

  - 多词短语（如爆款商品名、常见搜索query组合）的分词优化可参考自适应长度阈值逻辑：越长的候选短语阈值越低，鼓励把高频长语义单元合并为单个supertoken，提升LLM生成/理解电商文案、搜索query的语义一致性

  - 超参设置可复用论文的词表预算约束法：基于目标词表大小反推全局阈值和领域参数，避免盲目调参，同时保证分词速度和SuperBPE相当，无额外推理开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统BPE以空格为固定语义边界，无法有效合并跨空格的多词语义单元；SuperBPE等超词分词仅靠频率驱动合并，偏向短高频模式，对占比低的领域结构化符号（如公式、代码、领域特定标识）编码效率差，且未将合并阈值和压缩收益挂钩，词表容量分配不合理。

### 方法关键点
- 双维度自适应阈值：候选token的最小合并频率随长度动态下调，越长的候选要求的频率越低；同时区分通用自然语言和结构化符号两类模式，给低占比的结构化符号设置更低的阈值系数
- 迭代式超词挖掘：基于初始BPE词表，每次迭代基于当前词表分词后提取bigram，符合阈值的加入词表，仅需3次迭代即可覆盖最长8个BPE token的超词，时间复杂度线性于语料规模
- 轻量级领域识别：用正则匹配结构化符号特征，无需复杂语法解析，适合大规模语料处理

### 关键结果
在5个数据集（2个LaTeX领域、3个通用NLP）上对比BPE、SuperBPE：LaTeX领域平均编码长度（AEL）较SuperBPE最多降7%，总压缩收益最高提升349%；通用NLP领域AEL和SuperBPE相当，平均AEL较BPE降21.14%；下游小模型在通用任务准确率最高提0.7pct，数学任务BPB最多降3.8%，分词速度无显著差异。

### 核心结论
分词的词表容量分配应该向能带来更高压缩收益的长语义单元和低占比高价值的领域符号倾斜，而非单纯按频率排序。
