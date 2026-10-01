---
title: 'Linguistic Loopholes in LLM Unlearning: From a 174-Language Benchmark to Coverage-Aware
  Unlearning'
title_zh: 大语言模型遗忘的语言漏洞：174语基准与覆盖感知遗忘方法
authors:
- Tyler Skow
- Shravan Chaudhari
- Rama Chellappa
- Abhay Yadav
affiliations:
- Johns Hopkins University
arxiv_id: '2609.40286'
url: https://arxiv.org/abs/2609.40286
pdf_url: https://arxiv.org/pdf/2609.40286
published: '2026-09-30'
collected: '2026-10-01'
category: LLM
direction: 多语言LLM · 机器遗忘优化
tags:
- LLM-Unlearning
- Multilingual-LLM
- Benchmark
- Source-Selection
- Coverage-Guided
one_liner: 提出覆盖感知的多语言遗忘源选择方法搭配174语基准，较均匀选择最高降27.3%残留访问
practical_value: '- 跨境电商多语言客服/内容生成场景下，若需擦除LLM中版权/敏感/错误知识，可复用COVER思路选3-5个源语言做遗忘，无需全语言迭代，降本70%以上同时减少模型能力损伤

  - 多语言推荐Agent的知识更新场景中，借鉴基于语义表示对齐度计算跨语言迁移性的方法，可快速定位要更新的语言子集，缩短知识生效周期

  - 做跨语言模型能力验证时，可复用论文中「查询语言-回答语言」路由拆分的评估方法，更精准定位多语言回复的漏洞点'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM unlearning方案仅能保证单语言下的知识擦除，用户切换提问语言、书写脚本、提问句式即可重新唤起已"删除"的敏感/版权知识；全语言同时做遗忘不仅成本极高，还会大幅损伤模型的通用生成能力，此前也缺乏覆盖多语言、多表达方式的统一评估基准。
### 方法关键点
- 构建**Cross-Lingual Unlearning Tensor**基准，覆盖174个语言-脚本对、25种句法释义类型，拆分「查询语言→回答语言」不同路由，系统评估遗忘效果的跨语言泛化性
- 提出**COVER**方法，仅用无敏感信息的校准数据计算不同语言间的语义表示对齐度，在有限的源语言预算下选择最优子集，最大化未做遗忘监督的语言的知识擦除覆盖率
- 设计匹配源语言遗忘进度的评估协议，避免过遗忘导致的模型生成能力崩溃干扰效果对比
### 关键结果
在Aya、Qwen、Llama三个主流多语言模型族上测试，COVER相比均匀选择源语言，将未监督语言的平均残留访问相对降低7.8%~27.3%；在真实低资源语言新闻语料LORELEI上也实现2.6%~6.1%的残留访问降低，且几乎不额外损伤模型的保留知识生成能力。
最值得记住的一句话：单语言下的成功遗忘不代表多语言下的知识彻底清除，仅用3-5个高覆盖源语言做遗忘，就能实现接近全语言遗忘的跨语言擦除效果
