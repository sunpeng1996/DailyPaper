---
title: 'Beyond Ranking Accuracy: Evaluating LLM-Cited Feature Rationales for Next
  Basket Repurchase Recommendation'
title_zh: 超越排序精度：下一篮复购推荐中LLM引用特征理由的有效性评估
authors:
- Yanan Cao
- Anay Dombe
- Murali Mohana Krishna Dandu
- Shreeranjani Srirangamsridharan
- Sinduja Subramaniam
- Yogananth Mahalingam
- Evren Korpeoglu
- Kannan Achan
affiliations:
- Walmart Global Tech
arxiv_id: '2608.30333'
url: https://arxiv.org/abs/2608.30333
pdf_url: https://arxiv.org/pdf/2608.30333
published: '2026-08-31'
collected: '2026-09-01'
category: RecSys
direction: 复购推荐 · LLM可解释性评估
tags:
- Next-Basket Recommendation
- Explainable Recommendation
- LLM Rationale
- Feature Attribution
- Retail E-commerce
one_liner: 验证通用LLM不适合作为独立复购排序器，可作为经校验的解释组件输出有效用户理由
practical_value: '- 复购推荐场景不要尝试用通用LLM直接做独立排序器，其效果稳定弱于XGBoost、NN等监督排序模型，推理成本高收益低

  - 做用户-facing推荐解释时，可采用「监督模型排序+LLM基于预定义结构化特征生成解释」的混合架构，特征优先选复购场景的cadence、frequency、recency三类强信号

  - 校验LLM生成解释的有效性，可采用跨模型特征掩码方案：将LLM引用的特征掩码后看排序指标下降幅度，验证其引用特征是否真的携带排序信号，避免生成看似合理实则无关的解释

  - 给LLM的结构化特征可补充分位值表示（用户维度/全局维度），能提升LLM选对高价值解释特征的概率，尤其适配电商零售场景'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
下一篮复购推荐是零售电商核心场景，过往仅关注排序精度，但用户需要可理解的推荐理由提升决策信任；LLM可生成流畅的自然语言解释，但存在「看似合理但引用特征与实际复购信号无关」的幻觉问题，且业界缺乏对LLM生成理由的落地性评估方法，无法判断其引用特征是否真的对排序有价值。

### 方法关键点
- 构建覆盖复购核心维度的28个可解释结构化特征，包含cadence（复购周期）、frequency（购买频率）、recency（最近购买时间）、用户行为、商品热度五大类
- 设计跨模型特征掩码评估协议：将不同方法选出的Top3特征替换为训练集中位值，比较掩码前后排序指标的下降幅度，下降越大说明选中特征携带的排序信号越强
- 同时评估两类能力：通用LLM直接用结构化特征做复购排序的效果、LLM引用的解释特征是否携带跨模型通用的复购排序信号

### 关键实验结果
实验覆盖2个公开零售数据集（Instacart、Dunnhumby DC）+1个沃尔玛内部零售数据集，基线对比XGBoost、NN监督排序器、个人购买频率启发式规则、TreeSHAP/Integrated Gradients模型归因方法。核心结果：1）LLM排序效果稳定弱于监督模型，Instacart数据集上GPT-4o的NDCG@5为0.6568，比XGBoost低3.9个百分点，比NN低2.1个百分点；2）优化prompt加入特征分位值表示后，LLM引用特征的掩码下降幅度平均提升15%-30%，部分场景下接近跨模型归因基线；3）Instacart数据集上LLM生成解释的文本和引用特征的匹配精度达95.1%，数值一致性达99.6%。

### 核心结论
复购推荐场景下排序精度和解释质量是两个独立评估维度，不要因LLM排序效果差就否定其作为解释组件的落地价值。
