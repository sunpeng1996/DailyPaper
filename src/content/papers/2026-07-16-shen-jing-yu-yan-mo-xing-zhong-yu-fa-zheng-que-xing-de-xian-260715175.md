---
title: Linear representations of grammaticality in neural language models
title_zh: 神经语言模型中语法正确性的线性表征研究
authors:
- Jane Li
- Najoung Kim
affiliations:
- Johns Hopkins University
- Boston University
arxiv_id: '2607.15175'
url: https://arxiv.org/abs/2607.15175
pdf_url: https://arxiv.org/pdf/2607.15175
published: '2026-07-16'
collected: '2026-07-18'
category: LLM
direction: 大语言模型内部语法知识表征研究
tags:
- Neural Language Model
- Grammaticality
- Linear Probing
- Model Probing
- Representation Learning
one_liner: 通过线性探测验证预训练NLM内部存在独立于概率的语法性可分表征维度
practical_value: '- 生成式推荐/广告文案生成场景，可接入轻量线性探针快速校验生成内容的语法正确性，替代高成本的概率比对或人工抽检，提升审核效率

  - 搭建Query改写、商品标题生成等LLM下游任务的对齐Pipeline时，可新增语法性表征维度作为对齐指标，降低生成内容的语法错误率

  - 跨境电商多语言文案生成场景，可复用语法性表征跨语系泛化的结论，减少小语种语法校验的标注数据需求，降低落地成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有NLM语法能力评估依赖概率比对指标，但模型输出概率与词汇频率、语义合理性、世界知识等因素高度纠缠，无法准确反映模型真实的语法知识储备，相关结论存在较大争议。
### 方法关键点
采用mass-mean线性探测方案，直接检验语法/非语法句子在NLM内部表征空间的线性可分性，同时控制多种混淆变量，进一步验证该表征的独立性、跨语法现象泛化能力和跨语言迁移性。
### 关键结果
1. 覆盖多款主流预训练NLM，均存在稳定的语法性可分表征维度，该区分度无法被其他句子级属性完全解释；
2. 表征可泛化到10余类不同语法现象，分类准确率显著高于随机基线；
3. 跨语言泛化在同语系语种下保持70%以上的分类性能，证明语法性是当代NLM的通用连贯表征维度。
