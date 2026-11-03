---
title: Geometry of Confabulation and Refusal in Small Language Models
title_zh: 小语言模型中虚构回答与拒答的隐空间几何特性研究
authors:
- Vladimir Kazei
arxiv_id: '2611.01272'
url: https://arxiv.org/abs/2611.01272
pdf_url: https://arxiv.org/pdf/2611.01272
published: '2026-10-31'
collected: '2026-11-03'
category: LLM
direction: 小语言模型 · 隐空间干预与拒答控制
tags:
- SLM
- hidden state probing
- SAE
- refusal steering
- confabulation
one_liner: 构建消混淆的ConfabQA基准，通过隐空间探针与定向干预实现SLM虚构回答到拒答的可控切换
practical_value: '- 电商/广告Agent做事实问答时，可在prefill阶段最后一个token的深层隐状态加拒答方向向量，低开销降低虚假商品/活动信息输出概率

  - 端侧SLM做搜索推荐query改写时，可复用线性探针+定向干预的范式，无需全量微调即可控制模型输出模式（拒答/正常回答）

  - 做LLM4Rec相关探针实验时，可复用论文的prompt特征基线方法，验证探针读取的是模型内部信号而非prompt特征，避免效果虚高

  - SAE提取的单特征可作为更低开销的干预锚点，比全探针方向更省算力，适合端侧SLM的对齐优化'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
过往LLM正确性探针研究普遍混淆prompt特征与模型内部信号，缺少消混淆基准区分知识cutoff与模型真不知的场景，SLM面对未知问题时的拒答/虚构回答决策是否可从隐空间读取、定向干预尚无明确结论。
### 方法关键点
- 构建784条的ConfabQA基准，新增「训练数据存在但模型大概率答错」的模糊pre-cutoff类目，消解cutoff与正确性的混淆
- 采集prefill阶段最后一个prompt token的各层隐状态，用线性探针、SAE、定向优化三类方法提取拒答方向
- 所有探针均与四类prompt特征基线（TF-IDF、文本特征、文本+领域、文本+领域+类目）对比，确保信号来自模型内部
- 通过隐状态向量加法做one-shot干预，验证方向的因果性
### 关键结果
- Qwen3-1.7B、Gemma2 2B的拒答vs虚构探针比最强prompt基线分别高7.4pp、16.3pp，沿拒答方向干预可让97%+虚构回答以拒答词汇开头
- Llama3.2 3B的正确性探针跨数据集迁移时保留81%效果增益，比同量级Qwen3高19pp，差异来自后训练事实性对齐阶段而非参数量
- 单方向干预仅修改第一token生成倾向，约1/3的拒答开头会最终输出完整拒答，其余仍会回到回答模式

最值得记住的结论：SLM的拒答行为由深层隐空间的单一方向控制，正确性信号的强弱和可迁移性完全取决于模型后训练策略，与参数量关联极小
