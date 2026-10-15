---
title: 'FOLD: Position-Free Far Memory with Local Order for Long-Context Speculative
  Decoding'
title_zh: FOLD：面向长上下文投机解码的带局部顺序的无位置远内存方法
authors:
- Shuxuan Li
- Jialiang Kang
- Yanghao Zhou
- Ziye Zhu
- Xiao Yang
affiliations:
- Sun Yat-sen University
- Canva Research
- Peking University
arxiv_id: '2610.20392'
url: https://arxiv.org/abs/2610.20392
pdf_url: https://arxiv.org/pdf/2610.20392
published: '2026-10-14'
collected: '2026-10-15'
category: LLM
direction: LLM长上下文 · 投机解码推理加速
tags:
- Speculative Decoding
- Long Context LLM
- KV Cache
- Training-free
- Inference Optimization
one_liner: 免训练适配短序列预训练drafter，256K长上下文下最高将AR解码速度提升至4.22倍
practical_value: '- 做Agent长上下文推理、生成式推荐长prompt场景时，可直接引入FOLD优化投机解码速度，无需微调现有drafter，最高可将生成速度提升1倍以上，降低端到端延迟

  - 长上下文LLM适配可复用「局部窗口保精确位置+远内存共享虚拟位置+解耦注意力归一化」的设计思路，无需昂贵的长上下文微调即可缓解位置外推退化问题

  - 业务侧短序列预训练的小模型drafter可直接搭配FOLD支持256K级长上下文输入，避免重新收集长数据训练的成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长上下文LLM推理中KV cache访问占比随上下文长度上升到46%，投机解码（SD）是有效提速方案，但现有短序列训练的drafter在长输入下性能骤降，长上下文微调成本高；现有免训练方案要么截断上下文损失信息、要么引入检索开销，难以平衡效果和效率。

### 方法关键点
- 上下文拆分：将输入拆分为局部窗口和远内存，局部窗口保留真实相对位置匹配drafter短序列训练分布，所有远内存条目映射到窗口外的同一虚拟位置，避免长距离位置外推
- 解耦归一化：局部窗口和远内存分别做softmax，引入浓度因子α锐化远内存内注意力分布，同时控制远内存总权重避免稀释局部窗口注意力
- 完全免训练，不修改目标模型和验证逻辑，上下文长度小于窗口时自动退化为原生drafter

### 关键实验
在6组target-drafter配对、最高256K输入的7个长上下文基准上对比StreamingLLM、YaRN、ReRoPE等基线，FOLD将原drafter的AR解码速度平均提升9%~61%，最佳场景下速度从2.08×提升到4.22×，兼容DFlash、DSpark等多类drafter和vLLM、SGLang等推理引擎。

### 核心结论
短序列训练的投机解码drafter可通过复用目标模型隐状态自带的粗粒度位置信息，无需微调即可继承目标模型的长上下文能力。
