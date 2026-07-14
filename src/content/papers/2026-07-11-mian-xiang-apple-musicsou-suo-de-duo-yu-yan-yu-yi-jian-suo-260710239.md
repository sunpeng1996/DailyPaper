---
title: Multilingual Semantic Retrieval for Apple Music Search
title_zh: 面向Apple Music搜索的多语言语义检索系统
authors:
- Vishalaksh Aggarwal
- Kevin Sebastian
- Vivek Kanojiya
- Leo Le
- Nick Tucey
- Santosh Shankar
affiliations:
- Apple
arxiv_id: '2607.10239'
url: https://arxiv.org/abs/2607.10239
pdf_url: https://arxiv.org/pdf/2607.10239
published: '2026-07-11'
collected: '2026-07-14'
category: RecSys
direction: 搜索召回 · 多语言语义检索落地
tags:
- Semantic Retrieval
- Bi-encoder
- Multilingual Search
- Hybrid Retrieval
- ANN
one_liner: 基于GTE多语言基座微调双编码器，分位数校准混合检索上线转化率提2.28%无回归
practical_value: '- 成熟搜索/推荐栈增量升级可复用分位数校准技巧：将语义检索分数与现有 lexical 分数做分位数映射对齐分布，无需重训下游排序器即可上线，大幅降低改造成本

  - 双编码器微调可复用两阶段课程训练配方：先用InfoNCE加in-batch负样本+全局随机负样本做全局嵌入对齐，再切换到batch内最难负样本的hinge
  loss锐化决策边界，搭配Query-Query辅助任务优化错拼/跨语言query召回

  - 训练数据优先选择真实用户转化的query-item对，盲目叠加LLM生成/外部关联数据反而会引入噪声降低效果；小语种/长尾类目可采用频率封顶采样避免头部数据垄断

  - 线上语义召回降噪可使用结果数量上限替代文本匹配阈值过滤，既保留无lexical重叠的有效召回，又控制噪声，适合长尾query占比高的电商/内容搜索场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Apple Music覆盖150+国家地区数十种语言，现有词匹配检索系统对拼写错误、音译、跨语言、长尾query的召回失败率极高；长尾query占所有唯一query的83%，贡献约1/3的搜索会话，是转化率提升的核心瓶颈，且升级不能影响头部query的现有成熟效果。

### 方法关键点
- 模型：基于305M参数的GTE-multilingual-base微调Siamese双编码器ELISE，query和doc塔共享权重，输入加`Query::`/`Document::`前缀区分角色，提取<[BOS_never_used_51bce0c785ca2f68081bfa7d91973934]>前256维向量计算余弦相似度
- 训练：采用两阶段课程学习，第一阶段用InfoNCE损失做全局嵌入对齐，第二阶段切换到batch内最难负样本的pairwise hinge loss锐化决策边界；主损失为query-item对比损失，加20%权重的query-query损失（同会话错拼query与正确改写对）优化错配召回
- 数据：采用地域/实体类型频率封顶采样避免头部数据bias，下采样精确匹配query到20%避免模型坍缩到词匹配，加20%合成错拼query增强鲁棒性；验证仅用真实转化的query-log数据效果最优，加入LLM生成/playlist等补充数据反而引入噪声
- 部署：混合检索先线性对齐语义分与词匹配分，再用分位数分布匹配将混合分映射到原有词匹配分分布，无需重训下游排序器即可上线；用语义召回数量上限替代文本匹配阈值过滤，控噪同时保留无重叠有效召回

### 关键结果
离线Hit@10比原生GTE多语言基座相对提升69%；全球线上A/B测试整体转化率相对提升2.28%，无结果率下降86%，所有地区均无回归，其中长尾query转化率相对提升7.93%，头部query仅+0.14%无劣化，p95延迟增加不到55ms。

**最值得记住的一句话**：成熟检索栈的语义升级优先优化数据质量、基座选型和无侵入的分数校准，ROI远高于复杂的训练技巧。
