---
title: 'SpeechSense: A Paralinguistic-Focused Dataset for Fine-Grained Speech Sentiment
  Analysis'
title_zh: SpeechSense：面向细粒度语音情感分析的副语言聚焦数据集
authors:
- Shicheng Ma
- Wenqian Cui
- Irwin King
affiliations:
- The Chinese University of Hong Kong
arxiv_id: '2608.17931'
url: https://arxiv.org/abs/2608.17931
pdf_url: https://arxiv.org/pdf/2608.17931
published: '2026-08-18'
collected: '2026-08-19'
category: Multimodal
direction: 多模态情感分析 · 数据集构建
tags:
- Speech Sentiment Analysis
- Paralinguistics
- Multimodal LLM
- Synthetic Dataset
- Fine-grained Classification
one_liner: 构建含8类人际立场标签、聚焦副语言特征的细粒度语音情感分析数据集SpeechSense
practical_value: '- 电商语音客服Agent场景可直接复用该思路：除ASR转文本的语义分析外，额外保留韵律、语气等声学特征，能大幅提升用户负向情绪/立场识别准确率，避免误判中性语义下的不耐烦、不满等隐性态度

  - 细粒度标签设计范式可迁移：可基于自身业务需求自定义用户立场标签（如犹豫、认可、投诉倾向等），替代传统粗粒度情绪分类，支撑更精准的客服话术调度、坐席干预策略

  - 高保真合成数据+人工校验的数据集构建方法可复用：解决业务场景下真实语音标注成本高、标签粒度不足的问题，快速搭建场景专用语音情感分类模型的训练集'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有语音情感分析存在两大痛点：一是主流ASR+文本分析的流水线丢弃韵律、语气等核心声学特征，无法识别语义模糊场景下的真实说话人态度；二是现有基准标签粒度过粗，仅覆盖开心、悲伤等基础情绪，缺失客服、招聘等场景所需的细粒度人际立场标签，落地价值有限。
### 方法关键点
1. 定义仅靠韵律特征即可识别的8类人际立场分类体系，覆盖自信、不耐烦等非基础情绪的细粒度态度；
2. 采用高保真语音合成+严格人工校验的流程，构建聚焦副语言特征的细粒度语音情感数据集SpeechSense。
### 关键结果
跨多模态LLM、纯文本LLM、语音编码器的批量实验表明，接入声学特征的模型性能普遍优于纯文本基线，验证了声学特征对细粒度说话人态度识别的核心价值。
