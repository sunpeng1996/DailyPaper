---
title: Evaluating Open-Weight LLMs for Turkish Domain Documents Under Retrieval and
  Hardware Constraints
title_zh: 检索与硬件约束下土耳其领域文档的开源LLM性能评估
authors:
- Imtiaz Ul Hassan
- Öykü Akbulut
- Onur Kaya
- Ardhendu Behera
- Swagat Kumar
- Peter Matthew
- Yonghuai Liu
affiliations:
- Edge Hill University, UK
- Ermetal Otomotiv ve Eşya San. Tic. A.Ş., Türkiye
arxiv_id: '2609.28007'
url: https://arxiv.org/abs/2609.28007
pdf_url: https://arxiv.org/pdf/2609.28007
published: '2026-09-23'
collected: '2026-09-24'
category: RAG
direction: RAG落地评估 · 低资源硬件部署
tags:
- RAG
- LLM Evaluation
- Low-resource Deployment
- 4-bit Quantization
- Turkish NLP
one_liner: 提出证据标注评估协议分离RAG检索与推理故障，对比5款7B-8B开源LLM在6GB显存下的土耳其文档QA性能
practical_value: '- 垂直领域RAG落地评估可复用证据标注协议，提前拆分检索召回错误与大模型推理错误，避免错误归因浪费优化精力

  - 6GB级消费级GPU部署7B/8B小参数模型时，优先采用4-bit量化+固定4096上下文窗口配置，兼顾运行稳定性和推理效率

  - 结构复杂的垂直领域文档（如商品手册、行业报告）检索无需盲目堆叠复杂方案，字符级TF-IDF基线往往已达最优性价比，可先验证基线再迭代'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有土耳其语LLM评估多基于通用基准，未覆盖长结构复杂领域文档+本地受限硬件的真实RAG部署场景；传统端到端评估混淆检索故障和模型推理故障，无法指导落地优化，尤其涉密工业文档不能上云，低显存本地部署的性能基准完全缺失。

### 方法关键点
- 构造两个土耳其领域文档QA基准：109页工业研发报告、112页公共部门活动报告，各配100道标注了支撑证据的题目，覆盖事实检索、数值推理、多步推理、无信息拒答四类场景
- 控制变量评估框架：所有模型统一在6GB RTX 3050消费级GPU上运行，采用4-bit量化、4096上下文窗口、固定prompt与解码参数，相同检索上下文同步喂给所有模型
- 故障拆分评估协议：独立计算证据召回率（检索侧）和回答准确率（模型侧），采用按答案类型定制的判分规则，规避土耳其语形态丰富导致的exact match误判
- 检索方案对比：控制分块、上下文预算不变，对比字符TF-IDF、词TF-IDF、BM25、多语言E5、混合检索共7种配置

### 关键结果
5款7B-8B参数开源模型端到端准确率区间为49%~75%：Trendyol-8B准确率最高达75%，Qwen2.5-7B性价比最优，65%准确率下平均延迟仅1.69s/query，比Trendyol快14倍；7种检索方案无统计显著性性能差异，字符级TF-IDF基线与BM25、稠密检索、混合检索效果相当；同3500字符上下文预算下，工业报告证据召回率仅57%，公共部门报告达91%，检索瓶颈的严重程度完全随文档形态变化。

垂直领域RAG落地性能优化需先拆分检索、模型、硬件三类瓶颈，盲目升级检索方案或大模型版本往往无法获得预期收益。
