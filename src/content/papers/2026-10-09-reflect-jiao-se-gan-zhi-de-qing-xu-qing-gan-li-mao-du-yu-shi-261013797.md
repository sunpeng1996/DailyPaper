---
title: 'REFLECT: Role-Aware Detection of Sentiment, Emotion, Politeness, and Formality'
title_zh: REFLECT：角色感知的情绪、情感、礼貌度与正式度检测
authors:
- Sangpil Youm
- Annabel Stocks Natalias
- Hayden Heninger
- Leah Jones
- Xiaoyang Jin
- Xiaoya Zhang
- Bonnie Dorr
affiliations:
- University of Florida
arxiv_id: '2610.13797'
url: https://arxiv.org/abs/2610.13797
pdf_url: https://arxiv.org/pdf/2610.13797
published: '2026-10-09'
collected: '2026-10-13'
category: LLM
direction: LLM语义理解 · 角色感知注意力
tags:
- Role-Aware Attention
- Semantic Role Labeling
- Sentiment Analysis
- Transformer
- Interpretability
one_liner: 提出融合语义角色结构的角色感知Transformer架构，提升对话SEPF四类交际含义检测性能与可解释性
practical_value: '- 电商客服/导购Agent的对话语义理解可复用该角色感知注意力设计，分别建模无方向的用户情绪、有方向的礼貌度/正式度特征，提升对话意图判断与应对策略匹配准确率

  - 可学习门控自适应融合结构特征与上下文嵌入的方案，可迁移到所有需引入外部结构先验的大模型微调场景，避免特征拼接带来的信息冗余

  - 低频复杂情绪、高礼貌表达等长尾语义检测可借鉴该语言学先验注入思路，无需大量增广训练数据即可提升长尾场景性能'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有对话交际含义（情绪、情感、礼貌度、正式度SEPF）检测仅依赖上下文表示，忽略语义角色结构的约束，长尾场景性能差、可解释性弱。
### 方法关键点
1. 提出角色感知Transformer架构，将SEPF四类维度映射到理论驱动的Semantic Role Labeling配置直接注入自注意力：无方向角色注意力建模情绪、情感这类内部状态，有方向角色注意力捕捉礼貌、正式度这类发起-接收关系；
2. 用可学习门控自适应融合角色表示与上下文嵌入，而非拼接辅助语义角色特征。
### 关键结果
在4个基准数据集上对比BERT基线，情绪、礼貌度、正式度检测获统计显著提升，低频复杂情绪、高礼貌表达场景增益最突出；情感提升不显著，验证其更依赖词汇特征；真实心理健康数据测试同时提升预测性能与模型可追溯性。
