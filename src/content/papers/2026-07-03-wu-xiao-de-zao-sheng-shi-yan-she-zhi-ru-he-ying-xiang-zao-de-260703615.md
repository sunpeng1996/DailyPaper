---
title: 'The Powerless Noise: How Experimental Settings Shape the Reported Power of
  Noise'
title_zh: 《无效的噪声：实验设置如何影响噪声作用的评估结果》
authors:
- Michal Mazuryk
- Fleur Dolmans
- Louis Gehringer
- Ina Klaric
- Jia-Huei Ju
- Mohammad Aliannejadi
affiliations:
- University of Amsterdam
arxiv_id: '2607.03615'
url: https://arxiv.org/abs/2607.03615
pdf_url: https://arxiv.org/pdf/2607.03615
published: '2026-07-03'
collected: '2026-07-07'
category: RAG
direction: RAG 噪声鲁棒性与实验设计
tags:
- RAG
- Noise Robustness
- Prompt Engineering
- Inference Configuration
- Evaluation
one_liner: 验证RAG领域“随机噪声提升性能”的结论为特定实验设置导致的伪影，不具备通用性
practical_value: '- 电商/客服RAG系统设计无需刻意添加随机噪声优化性能，该效果仅在极受限的实验配置下存在，不符合工业界实际部署场景

  - 设计RAG prompt时需避免冲突指令（如同时要求短输出+返回NO-RES），必须匹配模型的官方chat模板，否则会人为压低基线性能，导致评估结论失真

  - 解码长度限制需适配任务需求（如商品属性抽取、问答场景不要设置过短的max_tokens），避免正确输出被截断产生大量伪负例，误导效果评估

  - 业务侧RAG效果评估不要仅依赖精确匹配，需结合语义匹配校验输出正确性，减少异常输出（如占位符、截断内容）对评估结果的干扰'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
此前SIGIR 2024提出的“RAG中加入完全不相关的随机文档可提升问答性能”（Power of Noise）结论，冲击了“检索质量越高RAG效果越好”的传统认知，但该研究采用旧版本LLM、强量化、受限prompt、严格解码限制等特殊设置，结论的通用性存疑，需验证其鲁棒性。
### 方法关键点
- 完全复现原实验设置：基于NQ-open数据集，采用4bit量化Llama2/MPT、原始抽取式prompt、15token解码限制，验证原效应的可复现性
- 扩展实验控制变量：覆盖Llama3、Mistral、Falcon3、Qwen2.5等现代指令微调模型，依次调整量化精度、是否使用模型官方chat模板、是否移除NO-RES冲突指令、解码长度放宽至100token
- 配套错误分析：定位截断输出、错误NO-RES返回、占位符输出等异常失效模式
### 关键结果
原效应在原始设置下可复现，最多观测到35%的准确率提升；但切换为符合工业界实践的配置后，噪声效应完全消失：所有模型的仅黄金文档基线准确率平均提升30%以上，加入随机文档后准确率稳定或轻微下降；原实验中观测到的Llama3噪声增益，实际是prompt不匹配导致基线98.5%输出为占位符的异常结果。
> 最值得记住的结论：RAG实验结论高度依赖prompt、解码、模型的具体配置，微小的实现差异就可能产生完全相反的结论，不能脱离业务实际照搬学术结论。
