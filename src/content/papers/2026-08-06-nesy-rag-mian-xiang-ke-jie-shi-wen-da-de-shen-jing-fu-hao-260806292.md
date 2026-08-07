---
title: 'NeSy-RAG: Neuro-Symbolic RAG for Explainable Question Answering'
title_zh: NeSy-RAG：面向可解释问答的神经符号检索增强生成框架
authors:
- Jonas Gann
- Michael Gertz
affiliations:
- Heidelberg University, Germany
arxiv_id: '2608.06292'
url: https://arxiv.org/abs/2608.06292
pdf_url: https://arxiv.org/pdf/2608.06292
published: '2026-08-06'
collected: '2026-08-07'
category: RAG
direction: 神经符号RAG · 可解释问答
tags:
- RAG
- Neuro-Symbolic
- Prolog
- Explainable QA
- Knowledge Gap Detection
one_liner: 提出模块化神经符号RAG框架，将检索文本转为可溯源Prolog模块实现可解释问答与缺省信息补全
practical_value: '- 可复用模块化知识转换思路：电商规则类场景（如优惠券 eligibility、售后规则问答）可将商品/规则文本预转Prolog模块，避免重复LLM解析，降低推理时延，同时实现规则溯源

  - 知识缺口检测机制可迁移到客服Agent/导购Agent：通过符号推理自动识别用户缺失信息（如是否符合活动参与条件），主动触发精准follow-up提问，减少无效交互

  - 0-arity谓词抽象+NL2C检索的设计可优化RAG查询生成：将复杂规则封装为语义明确的布尔谓词，通过语义检索匹配用户query，大幅缩小LLM生成查询的上下文窗口，降低幻觉

  - 可解释推理链路可用于高可信推荐场景：如金融理财、保险产品推荐，每个推荐结论可溯源到具体规则条款，满足合规要求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RAG推理过程不透明，结论无法可靠溯源到检索源，同时难以系统性检测用户侧缺失的上下文信息，容易生成错误或不完整输出，在规则明确、可信度要求高的场景（如政务、医疗、电商规则问答）的落地性不足。

### 方法关键点
- 模块化可溯源Prolog合成：对每个检索到的文本chunk，独立生成对应的Prolog模块，所有规则/事实可唯一溯源到原始chunk，推理trace自带来源信息
- 0-arity谓词抽象：为每个Prolog模块生成无参数布尔规则，封装模块核心语义，配合联合自然语言-代码嵌入实现NL2C检索，缩小查询生成的搜索空间，缓解幻觉
- 符号化知识缺口检测：将Prolog事实分为通用事实与需用户输入的动态事实，推理过程中自动识别缺失的动态事实，触发定向follow-up提问补全信息

### 关键实验
在ShARC问答基准（来自英国政府网站的法律文本对话QA数据集）测试，无域内训练的情况下：
1. NeSy-RAG准确率达61.1%，远超同基座LLM RAG基线的42.8%
2. 知识缺口相关的more类样本分类准确率达61%，是LLM RAG基线（19%）的3倍以上
3. 平均推理时延7.4s，比同基座RAG基线的11.4s降低35%，优势来自Prolog模块可复用、查询上下文窗口小、follow-up提问无需额外LLM调用

### 核心结论
神经符号结合的RAG框架可以在不损失性能的前提下同时实现可解释性、推理效率提升与主动信息补全，特别适合规则明确、溯源要求高的场景。
