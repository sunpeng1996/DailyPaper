---
title: Identifying Implicit Premises for Logical Reconstruction of Argument Graphs
title_zh: 面向论证图逻辑重构的隐含前提识别方法
authors:
- Xuyao Feng
- Anthony Hunter
affiliations:
- Department of Computer Science, University College London, United Kingdom
arxiv_id: '2608.18821'
url: https://arxiv.org/abs/2608.18821
pdf_url: https://arxiv.org/pdf/2608.18821
published: '2026-08-19'
collected: '2026-08-20'
category: Reasoning
direction: 逻辑推理 · 论证图隐含前提补全
tags:
- LLM
- Neuro-symbolic
- Implicit Premise
- Argument Graph
- Reasoning
one_liner: 提出神经符号pipeline，基于LLM生成隐含前提转逻辑公式，补全论证图的逻辑关联
practical_value: '- 电商用户评论/舆情分析场景可复用该神经符号pipeline，补全用户评价中省略的隐含常识前提（如「续航差=不值得买」），更精准识别用户真实偏好，提升推荐/商品分层的准确率

  - 搜索Query理解场景可借鉴隐含前提补全逻辑，补全用户模糊Query中省略的上下文/常识假设，例如将「下雨买什么」补全隐含前提「下雨需要遮雨工具」，提升召回匹配精度

  - 结构化观点提取/论证类内容处理场景可复用「LLM生成候选前提→转逻辑公式校验」的流程，减少纯符号方法的规则开发成本，提升逻辑关系判断的可解释性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
论证图逻辑重构任务的核心痛点是自然语言中普遍存在省略式论证（enthymeme），缺失隐含前提会导致论证图结构不完整、逻辑关联错误。现有方案要么仅能通过NLP识别省略式论证，要么仅能通过纯符号溯因方法在预定义逻辑表示中查找缺失前提，无法自动生成隐含前提以验证语句对的蕴含/矛盾/中立逻辑关系。

### 方法关键点
提出端到端神经符号pipeline：1）调用LLM生成显式前提与主张之间的中间隐含前提；2）将隐含前提、显式前提、显式主张统一转换为逻辑公式；3）通过逻辑推理校验三者间的逻辑关系（蕴含/矛盾/中立），补全论证图的边连接。

### 结果
在Microtext Argumentative Corpus上验证方案有效性，同时解决了纯符号方法依赖人工预定义规则、纯NLP方法输出缺乏逻辑可解释性的问题。
