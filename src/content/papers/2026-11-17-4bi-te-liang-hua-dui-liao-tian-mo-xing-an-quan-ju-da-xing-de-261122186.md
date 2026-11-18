---
title: Is 4-Bit Quantization More Than Noise to a Chat Model's Safety Behaviour? Attributing
  Behavioural Shifts with Matched Perturbations
title_zh: 4比特量化对聊天模型安全拒答行为的影响与偏移归因
authors:
- Ege Kaya
affiliations:
- University of British Columbia
arxiv_id: '2611.22186'
url: https://arxiv.org/abs/2611.22186
pdf_url: https://arxiv.org/pdf/2611.22186
published: '2026-11-17'
collected: '2026-11-18'
category: LLM
direction: 大语言模型 · 量化安全行为评估
tags:
- Quantization
- LLM Safety
- 4-bit Quantization
- Model Alignment
- On-device LLM
one_liner: 通过匹配扰动实验证实4比特量化的安全行为偏移由特定舍入误差而非比特宽度决定
practical_value: '- 端侧部署LLM（如电商端侧推荐Agent、智能客服）优先选8比特量化，实验证实所有8比特版本无显著安全行为偏移，稳定性更高

  - 若必须用4比特量化，优先选择llama.cpp的Q4_K_M格式，本次实验覆盖的3个模型中该格式均未产生显著安全偏移

  - 不能用perplexity/likelihood指标判断量化后模型的安全一致性，实验显示Llama-3.2-3B半量误差下likelihood几乎无变化，但拒答率已下降5.8个百分点

  - 每个量化版本的安全特性独立，上线前必须和原bf16版本做成对的安全行为校验，无法通过模型类型、比特宽度泛化判断'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
端侧部署的聊天模型普遍采用4比特量化压缩，但现有研究对量化如何影响模型安全拒答行为结论矛盾，无明确偏移归因方案，端侧Agent、智能客服等落地场景存在不可控的安全风险。

### 方法关键点
- 覆盖Qwen2.5-3B、Llama-3.2-3B、Qwen3-4B三个3-4B规模的指令微调模型，对比8比特、多种4比特量化（含AWQ、GPTQ、Q4_K_M等）版本与bf16原版的行为差异
- 设计两类测试场景：强制前缀场景（预填8个合规回复token，测试拒答被绕过的概率）、自由回复场景（用WildJailbreak越狱提示集，测试自然拒答率）
- 采用匹配扰动对照：构造与4比特舍入误差同范数的随机扰动、符号反转误差、缩放误差，分离误差模式与误差大小的影响
- 以8比特版本为零基准，消除标签本身的不稳定性干扰，所有结果采用成对检验统计

### 关键结果
- 强制前缀场景下Qwen2.5-3B 4比特版生成有害内容的概率比原版高6.2pp（人工标注下偏移达19.4pp）
- 自由回复场景下Llama-3.2-3B 4比特版对越狱提示的合规率比原版低10.3pp，同时对类越狱风格的良性请求拒答率高5.7pp，并非安全能力提升
- 同范数的随机扰动平均偏移接近0，真实舍入误差的符号反转会反转行为偏移方向，偏移大小与误差缩放比例近似线性相关

### 核心结论
4比特量化的安全行为偏移由舍入误差的具体模式决定，和比特宽度、通用性能指标无关，每个量化版本都必须单独和原版做校验
