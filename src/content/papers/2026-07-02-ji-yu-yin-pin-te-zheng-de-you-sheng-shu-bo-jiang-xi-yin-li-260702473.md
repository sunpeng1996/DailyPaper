---
title: Audio-Based Understanding of Audiobook Narration Appeal
title_zh: 基于音频特征的有声书播讲吸引力分析
authors:
- Shahar Elisha
- Mariano Beguerisse-Díaz
- Emmanouil Benetos
affiliations:
- Spotify
- Queen Mary University of London
arxiv_id: '2607.02473'
url: https://arxiv.org/abs/2607.02473
pdf_url: https://arxiv.org/pdf/2607.02473
published: '2026-07-02'
collected: '2026-07-04'
category: RecSys
direction: 有声书推荐 · 多模态特征挖掘
tags:
- audiobook
- acoustic_feature
- user_engagement
- multi-modal
- recommendation
one_liner: 首次量化有声书声学特征与消费数据的关联，支撑个性化推荐与播主遴选
practical_value: '- 长音频（有声书、播客）推荐场景可新增预训练音频模型提取的语速、音调、响度等声学特征，加入排序/召回模型提升完播率预估准确率

  - 针对不同内容品类（如小说/非虚构）单独建模声学特征的权重，优化各品类下的个性化推荐策略

  - 内容供给侧引入环节可利用声学特征预判内容吸引力，辅助播主遴选、内容定级，提升平台整体内容质量'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前有声书推荐普遍侧重内容文本、用户行为特征，未量化播讲声学质量对用户消费意愿的影响，不同品类、内容下的声学偏好差异也缺乏系统性分析。

### 方法关键点
1. 基于预训练音频模型从LibriVox有声书语料中提取音调、语速、响度等声纹与声学特征
2. 关联消费数据（完看率），控制书籍标题（内容本身）、品类变量消除混淆因子，验证特征与吸引力的关联关系
3. 用Spotify私有细粒度用户engagement指标做交叉验证

### 关键结果
即使排除内容本身的影响，仅声学特征就与有声书吸引力存在鲁棒关联，是首个系统性关联播讲质量、品类、内容与有声书消费的计算研究，结论在公开数据集与商业平台私有指标上均得到验证，可直接支撑有声书个性化推荐与播主遴选优化
