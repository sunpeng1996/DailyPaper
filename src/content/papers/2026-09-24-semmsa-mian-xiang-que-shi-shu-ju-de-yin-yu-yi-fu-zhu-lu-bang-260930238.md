---
title: 'SemMSA: Latent Semantic-Aided Robust Multimodal Sentiment Analysis with Incomplete
  Data'
title_zh: SemMSA：面向缺失数据的隐语义辅助鲁棒多模态情感分析
authors:
- Wenhao Li
- Zhibin Wu
- Chong Xiao
- Qiangchang Wang
affiliations:
- Software School, Shandong University
- Shenzhen Loop Area Institute
arxiv_id: '2609.30238'
url: https://arxiv.org/abs/2609.30238
pdf_url: https://arxiv.org/pdf/2609.30238
published: '2026-09-24'
collected: '2026-09-25'
category: Multimodal
direction: 多模态情感分析 · 缺失数据鲁棒优化
tags:
- Multimodal Sentiment Analysis
- LLM
- Missing Data
- Semantic Alignment
- Adapter
one_liner: 提出隐语义辅助的多模态情感分析框架SemMSA，解决数据缺失下的伪生成与噪声引导问题
practical_value: '- 多模态特征融合可复用anchor-free谱对齐方法，无需预设主模态，适配电商场景下图文音模态缺失的用户评论、直播内容情感识别

  - 跨模态语义精调模块可直接复用，用轻量Adapter抽取音视图特征后与文本拼接为统一前缀输入冻结LLM，大幅降低微调成本

  - 隐式语义优化无需解码显式文本，推理时延更低，适合高并发的实时评论情感打标、直播内容风控业务场景'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有多模态情感分析（MSA）在数据缺失场景下，依赖模态特征重建或复杂融合机制补全信息，缺乏高层语义锚定，普遍存在伪生成、噪声引导缺陷，鲁棒性不足。
### 方法关键点
1. 提出SemMSA隐语义辅助框架，核心包含跨模态语义精调（CSR）、跨模态谱对齐（CSA）两个模块
2. CSR通过对应Adapter抽取视觉、声学特征，与文本在冻结LLM嵌入空间构成统一多模态前缀，迭代生成连续判别性隐语义状态，无需解码显式文本
3. CSA通过增强核Gram矩阵主谱分量，将精调语义与所有模态对齐，无需预设锚模态，同时加入实例级谱分离约束避免表示坍缩
### 关键结果
在SIMS、MOSI、MOSEI三个标准MSA基准数据集上性能达到SOTA
