---
title: 'VISTA: Steering LLMs with Latent User Values Inferred from a Few Survey Answers'
title_zh: VISTA：基于少量问卷推断用户潜在价值观的大模型引导框架
authors:
- Yinuo Xu
- Jadie Adams
- Brian Hu
- Shivani Kumar
- David Jurgens
- Arslan Basharat
affiliations:
- University of Michigan
- Kitware Inc.
arxiv_id: '2610.23702'
url: https://arxiv.org/abs/2610.23702
pdf_url: https://arxiv.org/pdf/2610.23702
published: '2026-10-16'
collected: '2026-10-19'
category: LLM
direction: LLM个性化 · 用户价值自适应对齐
tags:
- LLM Personalization
- Activation Steering
- Hypernetwork
- Adaptive Elicitation
- User Modeling
one_liner: 从少量问卷推断用户潜在价值观生成LLM干预向量，支持自适应选题停测
practical_value: '- 电商新用户冷启可复用价值推断框架：用少量二选一偏好问卷+变分编码器生成32维用户价值latent，比prompt堆叠用户历史准确率高2.6个百分点，且不占用prompt上下文，适合低成本构建新用户偏好画像

  - LLM个性化生成可复用超网络干预方案：将用户latent映射为固定steering vector或16个soft prefix注入冻结LLM，推理成本恒定，避免用户行为历史过长挤占prompt空间，可用于个性化客服、商品推荐话术生成

  - 用户调研可复用EPIG自适应选题+动态停止策略：WVS数据集上仅需6%的问卷问题即可保留94%的全量问卷增益，远优于传统CAT方法的42%，可大幅降低会员偏好调研、用户分层的用户负担

  - 可解释用户分层可复用价值轴结论：steering vector的主成分对应可解释的价值观/偏好轴，可直接用于营销人群圈选、个性化权益匹配场景，无需额外特征工程'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM个性化方案多为任务特定偏好建模，或直接将用户资料放入prompt，模型难以有效利用且会挤占prompt上下文空间；全量用户问卷认知负担重，易出现敷衍回答降低数据质量，亟需低负担、跨任务的用户价值观对齐方案。

### 方法关键点
- 价值推断：基于变分信息瓶颈框架，从用户问卷答案生成32维高斯后验的用户价值latent，引入swap-guided正则防止编码器崩溃，用半amortized推理优化个体表示精度
- 激活干预：超网络将用户latent映射为固定长度steering vector（选择题场景）或16个soft prefix（自由文本生成场景），注入冻结LLM的指定残差层，无需更新基座权重，推理成本固定
- 自适应调研：基于期望预测信息增益（EPIG）选择信息价值最高的问题，当剩余最大信息增益低于初始最大值的指定比例时自动停止，无需预设问卷长度

### 关键结果
在Food2D（合成偏好）、WVS（现实社会价值观）、PrimeX（观点信念迁移）三个数据集测试：
1. 相同输入下效果持平或优于将用户答案放入prompt的基线，WVS数据集整体准确率高2.6个百分点，自由文本生成比所有prompt基线高2.7~4.3个百分点
2. 自适应调研模块在WVS上仅需询问6%的问卷问题，即可保留94%的全量问卷增益，远优于传统自适应测试（CAT）的最高42%的增益保留率
3. steering vector的第一主成分对应可解释的价值观轴，模型可将未见过的用户准确放置在轴上，WVS上相关系数r=0.73

最值得记住的一句话：仅需少量问卷采集得到的紧凑用户价值表示可跨场景复用，是低负担实现LLM个体对齐的高性价比路径
