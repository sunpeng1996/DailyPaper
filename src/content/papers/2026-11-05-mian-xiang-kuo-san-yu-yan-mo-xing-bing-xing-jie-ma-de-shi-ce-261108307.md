---
title: Measured Coupling for Parallel Decoding in Diffusion Language Models
title_zh: 面向扩散语言模型并行解码的实测耦合优化方法
authors:
- Tal Oved
- Lior Wolf
affiliations:
- Tel Aviv University
arxiv_id: '2611.08307'
url: https://arxiv.org/abs/2611.08307
pdf_url: https://arxiv.org/pdf/2611.08307
published: '2026-11-05'
collected: '2026-11-06'
category: LLM
direction: 扩散LLM · 无训练并行推理加速
tags:
- Diffusion LLM
- Parallel Decoding
- KV Cache
- Inference Optimization
- Mean Field Decoding
one_liner: 无需训练的块级探针实测token耦合，将扩散LLM并行解码步数较均值场降33%+，平均准确率仅降1.1点
practical_value: '- 扩散LLM用于生成式推荐文案/Agent多轮回复时，可直接复用该无训练解码方案，在1~2个点的可接受准确率损失下，将推理TPS提升30%~50%，降低长序列生成延迟

  - 借鉴块级探针复用KV Cache的设计思路，无需额外训练小模型即可快速计算token间依赖，可迁移到生成式推荐的批量推理场景，降低计算开销

  - 耦合度量逻辑可复用为推荐系统多候选item的搭配合理性校验工具，快速过滤冲突的推荐组合，无需额外调用精排模型'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
扩散语言模型支持单步多token并行生成，比自回归LLM推理延迟更低，是生成式场景降本提效的重要方向。但现有主流均值场并行解码用分布相似度作为token依赖的代理指标，无法准确区分token间的支持/冲突关系，导致解码步数多、效率天花板低，亟需更精准的无训练依赖度量方案。
### 方法关键点
- 定义耦合Δij为提交token j后token i的置信度变化，正Δ代表冲突、负Δ代表支持，直接替换均值场解码中的相似度代理项
- 设计块级局部探针：仅重新计算当前块的掩码位置，其余位置复用主前向传播的KV Cache，所有探针和主前向合并为一次批量计算，无额外参数无需训练
- 仅对Top K高置信候选token做探针，其余位置Δ设为0，兼顾精度和计算开销，2次均值场迭代后输出提交token集合
### 关键实验结果
在LLaDA-8B、LLaDA-1.5、Dream 7B三个扩散LLM上，对比自回归解码、Fast-dLLM、DAWN、均值场解码四个基线，测试GSM8K、MATH、HumanEval、MBPP四个基准：解码步数较均值场解码减少33%~55%，多数场景下TPS为所有方法最高，平均准确率仅比均值场低1.1个点；调整阈值可将准确率损失控制在1个点以内，仍保留30%左右的步数缩减。

**最值得记住的结论**：无需额外训练的探针式依赖度量，比人工设计的代理指标更能匹配真实生成需求，是兼顾性能和落地成本的推理优化方向。
