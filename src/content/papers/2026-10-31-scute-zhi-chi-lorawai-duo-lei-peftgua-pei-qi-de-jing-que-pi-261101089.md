---
title: 'Scute: Exact Batched Serving for PEFT Adapters Beyond LoRA'
title_zh: Scute：支持LoRA外多类PEFT适配器的精确批量推理系统
authors:
- Thomas Walker
- Richard Baraniuk
affiliations:
- Rice University
arxiv_id: '2611.01089'
url: https://arxiv.org/abs/2611.01089
pdf_url: https://arxiv.org/pdf/2611.01089
published: '2026-10-31'
collected: '2026-11-03'
category: LLM
direction: LLM PEFT 多适配器批量推理服务
tags:
- PEFT
- LoRA
- Serving
- vLLM
- DoRA
one_liner: 基于vLLM改造，统一范式支持多类PEFT适配器精确批量服务，性能接近纯LoRA
practical_value: '- 多租户个性化推荐/Agent场景可复用6槽位统一范式，将DoRA、(IA)3、VeRA等场景定制的PEFT适配器转标准格式批量调度，避免转LoRA带来的精度损失、显存开销

  - 现有基于vLLM的服务栈可直接复用Scute的runtime补丁，快速支持多类PEFT适配器混合服务，实测多方法混合仅比纯LoRA增加5-17%的decode耗时

  - 对于小参数量个性化适配器（如(IA)3、VeRA），可复用其共享参数计算路由，单GPU可支持千级租户服务，满足SLO的请求率是转LoRA方案的1.5~2.5倍'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前主流LLM批量推理服务仅支持LoRA适配器，其他PEFT方法（DoRA、(IA)3、VeRA、OFT等）要么转LoRA损失精度、增加显存开销，要么无法共享base模型批量调度，多租户服务效率极低。尤其电商/推荐场景存在大量品类、人群、场景定制的PEFT微调模型，现有服务方案无法兼顾效果和成本。

### 方法关键点
- 6槽位统一表达范式可覆盖LoRA、DoRA、(IA)3、SSF、VeRA、OFT等主流PEFT方法，基于折叠规则判断哪些槽位可在适配器加载时合并到权重中，仅留必要活槽位在推理时计算
- 设计3种活槽位计算路由，分别适配输出缩放类、共享参数类、输入变换类槽位，基于无参数字节模型精准预测不同路由的带宽开销
- 基于vLLM实现，加载时编译器将Hugging Face PEFT库的各类适配器转换为统一范式，runtime补丁在不修改原有调度、paging逻辑的前提下扩展支持多类适配器混合批量服务

### 关键结果
基于Llama-3.1-8B在RTX A6000上测试，对比原生vLLM转LoRA的baseline：
1. 精度上，与Hugging Face PEFT库的计算误差不超过1.5%，任务精度损失≤0.4个百分点，避免了无任务数据时(IA)3转LoRA最高23.2个百分点的精度损失
2. 性能上，5种PEFT方法混合批量服务仅比纯LoRA多5-17%的decode耗时，比转LoRA方案快12%以上
3. 密度上，单RTX A6000可支持1024个(IA)3/VeRA租户服务，满足SLO的请求率是转LoRA方案的1.5~2.5倍，吞吐最高达2.03倍

### 核心结论
多类PEFT适配器无需统一转换为LoRA，扩展现有LoRA调度内核即可实现精确高效的批量服务，兼顾多租户灵活性和服务成本。
