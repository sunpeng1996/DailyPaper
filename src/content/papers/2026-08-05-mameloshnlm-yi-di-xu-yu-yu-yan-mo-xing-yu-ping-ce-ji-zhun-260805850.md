---
title: 'MameLoshnLM: Yiddish Language Model and Evaluation Benchmark'
title_zh: MameLoshnLM：意第绪语语言模型与评测基准
authors:
- Uri Katz
- Omer Goldman
- Tomasz Limisiewicz
- Reut Tsarfaty
- Noah A. Smith
affiliations:
- Bar-Ilan University
- University of Cambridge
- University of Washington
- Allen Institute for AI
arxiv_id: '2608.05850'
url: https://arxiv.org/abs/2608.05850
pdf_url: https://arxiv.org/pdf/2608.05850
published: '2026-08-05'
collected: '2026-08-08'
category: LLM
direction: 低资源语言大模型训练与评测体系构建
tags:
- Low-Resource LLM
- Continual Pre-training
- Pre-training Corpus
- Evaluation Benchmark
- Multilingual LLM
one_liner: 首个开源8B意第绪语专用LLM，配套高质量预训练语料与多任务评测基准
practical_value: '- 跨境电商小语种站点LLM落地可复用该方案：基于通用大模型做持续预训练，成本远低于从头训练小语种专用模型

  - 小语种预训练语料构建优先融合原生网页内容+高质量垂类文本，规避通用多语言语料中的机器翻译、错分类噪声

  - 小语种垂直场景评测优先自建覆盖核心业务场景的基准，不要直接复用通用多语言评测集，避免评估结果与实际业务效果偏差'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
多语言LLM性能向高资源语言倾斜，意第绪语数字资源稀缺，现有通用多语言语料存在大量噪声（机器翻译、错分类文本），缺乏专用评测基准，严重制约该语言NLP落地进展。
### 方法关键点
1. 构建Oytser高质量意第绪语预训练语料，融合当代原生网页内容与经典文学材料，过滤低质量噪声数据；
2. 发布Kashes多任务评测基准，覆盖翻译、语言学分析、信息抽取、语言理解四类核心下游任务；
3. 基于Llama 3.1 8B做持续预训练，得到意第绪语专用模型MameLoshnLM。
### 关键结果
在Kashes全任务上性能优于同规模开源基线，相比通用多语言模型更好捕捉意第绪语特有词汇、形态特征，验证了通用多语言语料的噪声会显著降低低资源语言LLM性能，为数字资源稀缺的小语种LLM构建提供可复用模板。
