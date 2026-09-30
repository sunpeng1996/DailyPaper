---
title: When Do Model Internals Help? Exploring the Role of Representation Engineering
  in LLM Safety
title_zh: LLM安全场景下表征工程适用边界与行为防护方案的对比评估
authors:
- Tianyi Guan
- Jianhui Chen
- Liangming Pan
affiliations:
- State Key Laboratory of Multimedia Information Processing, Peking University
- School of Computer Science, Peking University
arxiv_id: '2609.34771'
url: https://arxiv.org/abs/2609.34771
pdf_url: https://arxiv.org/pdf/2609.34771
published: '2026-09-27'
collected: '2026-09-30'
category: LLM
direction: LLM安全 · 表征工程落地评估
tags:
- Representation Engineering
- LLM Safety
- DPO
- Activation Steering
- Alignment Probe
one_liner: 在LLM安全控制与监控任务中，系统对比表征工程与传统行为防护的优劣、适用场景与互补价值
practical_value: '- 若业务落地LLM Agent需低成本安全监控，可复用生成时的激活值部署滚动聚合表征探针，比文本监控降低7.6×10^5倍边际FLOPs，仅损失不到1.5%的AUROC，适合高吞吐生成场景

  - 若安全对齐训练数据不足（<1k对），可优先选用Flow-based激活steering替代DPO，搭配高质量对比数据即可获得接近DPO的安全控制效果，避免小数据下DPO的过拟合问题

  - 针对业务中LLM经过下游任务微调后安全护栏退化的问题，可直接接入预训练的表征探针做输出拦截，能恢复92%的安全控制能力，仅带来1.6%的额外过拒率，无需重新做全量安全对齐'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM安全防护分为行为防护（DPO对齐、文本监控）和表征工程（激活控制、探针监控）两类，但两类方案从未在相同基准下开展横向对比，适用边界模糊，无法指导工业落地选型。

### 方法关键点
- 控制任务对比DPO与3种表征steering方案（CAA、探针导向steering、Flow-based steering），评估维度覆盖鲁棒性、数据效率、跨域迁移、能力损耗
- 监控任务对比4种表征探针与2种文本监控（LoRA微调监控、Qwen3Guard），评估维度覆盖检测精度、响应时延、计算开销
- 新增监控-控制融合实验，验证探针信号修复DPO微调后安全退化的效果

### 关键实验
基于PKU-SafeRLHF、StrongREJECT、XSTest数据集，在Qwen2.5 1.5B/14B、Llama3.1 8B三个基座上开展测试，核心结果：① 高数据量下DPO的攻击成功率（ASR）比所有steering方案低至少28%，但经过良性微调后ASR提升0.271，安全护栏严重退化；② 表征探针仅需文本监控1/7.6×10^5的边际计算量，AUROC达到0.982，仅比最优文本监控低1.4%；③ 探针引导的拦截策略可将微调后DPO的ASR从0.500降至0.042，恢复92%的安全能力，过拒率仅提升1.6%。

### 核心结论
表征工程不是行为防护的替代方案，而是互补组件，仅在低数据对齐、低开销监控场景下具备显著优势。
