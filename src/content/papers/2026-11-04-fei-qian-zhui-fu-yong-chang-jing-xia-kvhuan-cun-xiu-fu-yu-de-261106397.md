---
title: Where Should a KV-Cache Repair Budget Go? Distractor Structure and Contextual
  Compatibility in Non-Prefix Reuse
title_zh: 非前缀复用场景下KV缓存修复预算的最优分配策略
authors:
- Yuxing Peng
- Zhiqing Tang
- Weijia Jia
affiliations:
- 北京师范大学珠海校区
- 北京师范大学-香港浸会大学联合国际学院
arxiv_id: '2611.06397'
url: https://arxiv.org/abs/2611.06397
pdf_url: https://arxiv.org/pdf/2611.06397
published: '2026-11-04'
collected: '2026-11-05'
category: LLM
direction: LLM推理优化 · KV-cache复用
tags:
- KV-cache
- non-prefix reuse
- RAG
- LLM inference
- cache repair
one_liner: 揭示非前缀KV复用损失来源，提出小预算下优先重算检索Top1块的高效修复策略
practical_value: '- 搭建RAG类电商导购/客服Agent时，小KV修复预算优先倾斜给检索Top1块，将其移动到query前重算，比分散选择token修复准确率高5%~49%

  - 非前缀KV复用场景下，不要依赖query注意力选择修复块，其找对答案块的概率最高仅18.8%，直接用检索排序结果可靠性更高

  - 对话记忆类Agent场景，chunk级KV修复收益不显著，优先使用成熟的token级选择器（如ProphetKV、CacheBlend）即可'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RAG、长对话Agent、工具调用Agent的prompt由多块检索结果拼接生成，前缀缓存几乎无法生效，非前缀KV复用单独编码每个chunk再拼接缓存，可大幅降低prefill耗时，但会损失19%~100%依赖上下文的问题准确率，现有修复方法的预算分配无明确最优方向，小预算下的投向选择缺乏实验支撑。

### 方法关键点
- 固定答案所在目标块的位置，分别采用跨领域文本、同领域不相关块、同领域相似块作为干扰项，测试3个7B~8B模型在4类数据集上的复用损失构成
- 对比多类修复策略：替换块的全prefill KV、重算目标块、基于query注意力选块、基于检索排序选块+移动到query前重算等
- 提出上下文兼容性判定：重算块时基于已复用的KV上下文生成的KV，效果优于直接插入该块的全prefill KV

### 关键实验
覆盖对话记忆（LoCoMo）、开放域QA（NQ-Open、TriviaQA）、API文档（Gorilla）4类数据集，对比baseline包括CacheBlend、EPIC、ProphetKV、InfoFlow等现有token级/块级修复方法。核心结果：非前缀KV复用准确率损失为19%~100%；query注意力找对目标块的概率最高仅18.8%；5%预算下，将检索Top1块移到query前重算，在6/9的开放域QA/API场景下显著优于InfoFlow，在9/9的同类场景下不劣于同预算的token级选择器，最高提升49%。

### 核心结论
非前缀KV复用的小修复预算不要分散投给干扰块，优先倾斜给检索排序最高的候选块，通过重算保证上下文兼容性即可获得最优收益。
