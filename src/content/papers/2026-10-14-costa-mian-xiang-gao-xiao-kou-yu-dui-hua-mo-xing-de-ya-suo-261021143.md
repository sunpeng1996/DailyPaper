---
title: 'CoSTA: Compressed Speech Token Adaptation for Efficient Spoken Dialogue Models'
title_zh: CoSTA：面向高效口语对话模型的压缩语音Token适配框架
authors:
- Yingzhuo Deng
- Chong Li
- Bingxin Liu
- Yi Shu
- Tianyu Peng
- Can Xie
- Siyao Song
- Shuo Ren
- Jiajun Zhang
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- School of Artificial Intelligence, University of Chinese Academy of Sciences
- Wuhan AI Research
arxiv_id: '2610.21143'
url: https://arxiv.org/abs/2610.21143
pdf_url: https://arxiv.org/pdf/2610.21143
published: '2026-10-14'
collected: '2026-10-31'
category: LLM
direction: 语音对话大模型 · 推理效率优化
tags:
- SpeechDialogueModel
- TokenCompression
- InferenceOptimization
- VocabularyExtension
- AutoregressiveGeneration
one_liner: 提出解耦生成与合成token空间的后处理框架，保质量前提下大幅提升语音对话模型推理效率
practical_value: '- 电商语音客服、直播交互Agent等语音交互类业务可直接复用CoSTA框架，无需替换原有语音分词器、解码器即可降低推理延迟，提升并发承载量

  - 「生成阶段token压缩+输出前确定性展开」的架构思路可迁移到长文案生成、直播话术生成等长序列生成场景，平衡生成效率与输出质量

  - 均值初始化词表扩展、分领域适配的token压缩方法可复用在自定义Semantic ID生成、长尾词表扩展场景，大幅降低模型重训成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有口语对话模型（SDM）生成、合成环节共享同一语音token空间，导致自回归序列过长、推理成本高；低速率语音分词器替换成本高，存在压缩-质量trade-off，且无法打破生成合成的耦合限制。

### 方法关键点
提出兼容性保留的后处理框架CoSTA，解耦生成与合成token空间，全程保留原有语音分词器与解码器：
1. 通过均值初始化词表扩展、发音适配、对话适配三个步骤，引入压缩表示扩展生成token空间
2. 语音合成前通过确定性映射将压缩token还原为原空间token，实现无损转换

### 关键结果数字
双语语音对话基准测试下，语音token生成速度提升1.7×，全响应延迟降低、吞吐量显著提升，同时完全保留响应质量；支持跨架构迁移，与低速率分词方法效果互补。
