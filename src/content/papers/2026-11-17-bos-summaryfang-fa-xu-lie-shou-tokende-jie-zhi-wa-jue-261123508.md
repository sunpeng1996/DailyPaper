---
title: 'BOS Summary: The First Token Matters'
title_zh: BOS Summary方法：序列首Token的价值挖掘
authors:
- Hui Zhu
- Saleh Zare Zade
- Rafi Ibn Sultan
- Deng Pan
- Arun Ross
- Dongxiao Zhu
affiliations:
- Wayne State University
- University of Notre Dame
- Michigan State University
arxiv_id: '2611.23508'
url: https://arxiv.org/abs/2611.23508
pdf_url: https://arxiv.org/pdf/2611.23508
published: '2026-11-17'
collected: '2026-11-19'
category: LLM
direction: LLM推理优化 · 注意力sink复用
tags:
- Attention Sink
- BOS Token
- Inference Optimization
- VLMs
- Training-free
one_liner: 无需训练仅修改prefill阶段单一层BOS注意力掩码，将无信息注意力sink转为上下文聚合载体提升推理性能
practical_value: '- 电商多模态商品理解、图文匹配、属性识别场景，无需微调现有VLM，仅修改prefill阶段单一层BOS掩码即可降低幻觉、提升推理准确率，落地成本极低

  - LLM导购Agent、长Query搜索理解场景，可复用BOS作为固定上下文锚点，减少长对话/长文档的上下文丢失，无解码额外开销，不影响线上latency

  - 业务场景LoRA微调（如商品合规审核、用户意图分类）时，训练推理阶段均开启BOS Summary，可比标准LoRA最高提升3pp左右的准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM/VLM普遍存在注意力sink现象，BOS token会收到后续token的大量注意力，但标准因果掩码下BOS只能关注自身，完全不携带输入相关信息，相当于浪费了一个天然高访问量的信息通路；同时长序列生成时模型容易出现上下文丢失、幻觉，prompt信息会被不断增长的生成序列稀释，亟需低成本的上下文保留方案。

### 方法关键点
- 完全训练免费，仅在prefill阶段的某一个指定Transformer层，放松BOS query的因果掩码约束，允许BOS关注所有输入的文本/视觉token，其余token的注意力掩码完全不变，无额外参数、无辅助模块
- 解码阶段不做任何修改，BOS聚合的上下文信息通过残差传递到后续所有层，后续生成token可通过原有注意力路径直接访问聚合上下文，无任何解码时开销
- 可结合LoRA微调使用，训练推理阶段均开启BOS Summary，可进一步提升任务效果

### 关键实验
覆盖Qwen2.5-VL、Qwen3-VL、Gemma3、Llama3.1等6款主流VLM/LLM，8个多模态+纯文本基准（MMStar、M3CoT、POPE、LogiQA、MathQA等），对比Direct、CoT、ZeroTuning、SinkTrack等基线：
- VLM场景平均准确率比最强基线高0.29~1.36pp，Qwen3-VL-8B在M3CoT多步推理任务最高提2.58pp
- 纯文本LLM场景Llama3.1-8B平均准确率比最强基线高3.6pp，Gemma3-12B高1.44pp
- 结合LoRA微调时，比标准LoRA最高提3.07pp准确率

### 核心结论
利用Transformer天然存在的注意力sink通路做轻量干预，是几乎零成本提升模型推理和上下文保持能力的可行路径，不需要修改模型结构也不需要重新训练
