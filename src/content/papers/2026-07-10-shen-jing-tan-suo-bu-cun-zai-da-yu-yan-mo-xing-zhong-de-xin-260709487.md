---
title: 'Neural Collapse Is Forbidden: Information Floors in Language Models'
title_zh: 神经坍缩不存在：大语言模型中的信息下界
authors:
- Bruno Abrahao
affiliations:
- NYU Shanghai
- Leonard N. Stern School of Business, New York University
arxiv_id: '2607.09487'
url: https://arxiv.org/abs/2607.09487
pdf_url: https://arxiv.org/pdf/2607.09487
published: '2026-07-10'
collected: '2026-07-13'
category: LLM
direction: 大语言模型表征几何与信息理论
tags:
- LLM
- Neural Collapse
- Representation Learning
- Information Theory
- Weight Decay
one_liner: 推翻LLM表征类内方差为未完成神经坍缩的认知，证明类内方差是信息存储且服从明确信息下界规律
practical_value: '- 做LLM4Rec/LoRA微调场景模型时，无需刻意追求类内表征坍缩，保留适度类内方差可存储更多上下文信息，提升长尾query/冷门item表征质量

  - 训练LLM的token级权重衰减时，可按类别token类型数而非出现频次调整惩罚系数，缓解长尾类别表征劣化问题

  - 做RAG/推荐语义召回的表征质量评估时，可用类内分散度替代总方差作为指标，更准确反映表征携带的上下文互信息量'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
图像分类训练后期普遍存在神经坍缩（类内方差趋近于0）现象，过往研究误将LLM表征的类内方差判定为未完成的神经坍缩，缺乏对LLM表征方差分配机制的合理解释。
### 方法关键点
1. 利用中心化恒等式推翻了此前LLM表征服从单纯形等角紧框架的系列结论；
2. 理论证明token级权重衰减按类别类型数而非出现频次施加惩罚，将下一词预测转化为不平衡K分类问题；
3. 证明二元类别下的信息下界，类内分散度至少与条件互信息I(token; context | category)成正比。
### 关键结果
跨14个参数规模相差100倍的LLM测试，宏观类别结构仅占表征方差的4~12%，token内上下文信息占79~91%；预训练过程中类别方差占比先超调、下降再部分恢复，类内分散度与信息下界严格对齐，跨模型可迁移预测。
