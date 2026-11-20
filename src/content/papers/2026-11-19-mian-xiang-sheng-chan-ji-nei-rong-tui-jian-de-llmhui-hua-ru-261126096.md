---
title: 'From Sessions to Serving: Integrating LLM-Based Embeddings into Retrieval
  for Production Content Recommendation'
title_zh: 面向生产级内容推荐的LLM会话嵌入检索系统LSER
authors:
- Zhixiong Hu
- Meng Li
- Maggie Zhang
- Deborshi Goswami
- David Bailey
- James Bradley
affiliations:
- Autodesk
arxiv_id: '2611.26096'
url: https://arxiv.org/abs/2611.26096
pdf_url: https://arxiv.org/pdf/2611.26096
published: '2026-11-19'
collected: '2026-11-20'
category: RecSys
direction: 推荐系统 · LLM嵌入融合召回优化
tags:
- Two-tower Retrieval
- LLM Embedding
- Session Recommendation
- Nearline Serving
- Production RecSys
one_liner: 将LLM生成的会话/历史嵌入作为辅助特征加入双塔检索用户塔，配套近线更新架构落地生产
practical_value: '- 异构内容推荐场景可采用增量升级方案：无需替换原有序列编码器，仅将LLM生成的会话/历史embedding作为辅助特征拼入用户塔即可获得收益，大幅降低改造成本

  - 工程上可复用近线异步更新架构：用户侧序列编码、LLM推理放在异步近线链路执行，更新后写入低延迟KV存储，请求路径仅做特征融合+ANN检索，可满足P95≤100ms的低延迟要求

  - LLM侧输入无需映射到item ID：直接序列化原始行为的(event type, event value)文本，可覆盖无法关联item ID的稀疏行为，提升长尾内容的表征能力

  - 上线可采用阶梯式验证策略：先通过离线单变量消融验证LLM特征的增量价值，再逐步上线全链路，降低生产风险'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
大型内容平台的个性化推荐面临异构候选池（产品页、用户案例、学习内容等）、用户行为稀疏且实时变化的痛点，传统双塔召回的用户表征能力瓶颈明显，现有LLM融入推荐的方案普遍缺乏生产级落地的架构细节和可复用的工程实践。

### 方法关键点
- 双塔检索架构：用户塔融合传统BERT4Rec序列编码器输出、LLM生成的64维会话/历史嵌入、用户非序列特征（属性、计数器、产品权限等）；Item塔用BGE编码内容文本+元数据生成表征，无需item ID embedding，对新内容泛化性更好
- LLM嵌入生成逻辑：将和传统序列编码器同时间窗的原始行为序列化为(event type, event value)文本，基于Qwen3-0.6B小模型微调，采用next-event预测的二元交叉熵损失预训练，再和双塔模型联合微调
- 近线更新架构：新行为触发异步SageMaker推理任务更新用户侧序列/LLM嵌入，写入低延迟存储；请求时直接读取预计算的嵌入，仅做轻量融合+ANN检索，无重型计算在关键路径

### 关键实验
离线基于Autodesk平台时序拆分的真实交互数据，对比不含LLM特征的基线双塔：添加LLM特征后，流行商品HR@10提升9.6pp、MRR提升0.021，客户案例内容HR@1提升6pp；在线A/B测试对比原有规则推荐系统，首页商品轮播CTR提升10.3%，客户故事CTR提升36.1%，产品下单率提升14.8%，所有指标均统计显著。

### 核心结论
异构内容推荐场景下，LLM嵌入作为补充特征而非替代传统序列模型，配合近线更新架构是低成本落地的可行路径。
