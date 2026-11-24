---
title: Where Do Fact-Checking Errors Arise? Separating Retrieval, Search Control and
  Judgement in Evidence-Grounded Verification
title_zh: 证据驱动事实核查的错误来源拆解：检索、搜索控制与判决分离
authors:
- Martin Pavlíček
- Martin Kotyrba
- Eva Volná
- Tomáš Filip
- Petr Sosík
affiliations:
- University of Ostrava, Czech Republic
arxiv_id: '2611.29697'
url: https://arxiv.org/abs/2611.29697
pdf_url: https://arxiv.org/pdf/2611.29697
published: '2026-11-22'
collected: '2026-11-24'
category: RAG
direction: RAG系统全链路错误归因评估
tags:
- RAG
- Fact Checking
- Error Analysis
- Retrieval Control
- Agent Evaluation
one_liner: 提出RAG事实核查全链路错误拆分协议，证明自适应搜索多无增益
practical_value: '- 做业务RAG（商品问答、客服、营销内容核查）时，先跑通单轮Hybrid检索+重排的基线，不要盲目上多轮检索、搜索Agent，大部分场景下基线已经能拿到最优效果，多轮只会增加2-9倍的推理成本无收益

  - RAG系统错误排查要做全链路拆分：至少拆分「检索未召回、排序未入选上下文、大模型判决错误、校验规则误拦截」四个环节，不要默认错误都来自检索，盲目优化召回

  - 引入搜索Agent前必须做严格的基线对比：小模型作为Agent控制器极易出现执行失败、重复调用等问题，多数场景下不仅没有增益，反而会拉低整体精度

  - 判决后的校验规则不要拍脑袋设计，必须在业务数据集上评估正负收益：类似归因校验的规则可能在真实场景下误杀70%以上的正确判决，反而拉低整体准确率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
端到端RAG系统的准确率仅能反映整体效果，无法定位错误根源是「没找到证据」还是「找到了没用对」，开发者常盲目堆叠多轮检索、Agent搜索等复杂模块，导致推理成本陡增却无实际收益，亟需可落地的全链路错误归因方法。
### 方法关键点
1. 将证据驱动的事实核查RAG链路拆分为**检索、搜索控制、证据筛选、判决+校验**4个可独立度量的环节，每个环节保留溯源接口可追踪参考证据的流转路径
2. 对比5类搜索控制器：单轮检索、自适应门控、问题台账、依赖链控制、自主工具Agent，搭配稀疏/稠密/混合/图辅助4种检索方式，统一控制上下文窗口、推理参数等变量
3. 设计两组对照证据库：小库（仅包含标注的正确证据，检索难度极低，用于隔离下游误差）、全库（完整维基百科/网页库，匹配真实业务检索难度）
### 关键结果
- 小库场景下，单轮混合检索即可覆盖228条带证据声明中226条的完整证据，所有自适应控制器/Agent需多消耗2~9倍模型调用，无稳定精度增益
- 33条证据完整但最终判决错误的样本中，15条来自大模型自身拒识，18条来自校验规则误改正确判决，仅AVeriTeC数据集上校验规则就拉低6个点准确率
- 全库场景下，单轮混合检索精度下降17~29个点，所有自适应控制器均无法挽回精度损失，额外714条维基百科声明的补充测试也验证了Agent无显著增益
### 核心结论
在将错误归因到搜索模块之前，应当先单独度量证据召回、模型判决、校验规则各自的误差贡献，不要盲目优化检索链路。
