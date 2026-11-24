---
title: 'Learn the Effects, Not the Examples: Implicit ICL via Attention Patching'
title_zh: 学习示例效应而非示例本身：基于注意力修补的隐式上下文学习
authors:
- Seungwon Woo
- Hyunseo Shin
- Wonseok Hwang
affiliations:
- University of Seoul
arxiv_id: '2611.30690'
url: https://arxiv.org/abs/2611.30690
pdf_url: https://arxiv.org/pdf/2611.30690
published: '2026-11-23'
collected: '2026-11-24'
category: LLM
direction: 大模型优化 · 隐式上下文学习
tags:
- Implicit-ICL
- Attention-Patching
- Inference-Optimization
- LLM
- Ridge-Regression
one_liner: 提出基于注意力投影层仿射变换的隐式ICL方法，性能比肩显式ICL且推理成本接近零样本
practical_value: '- 电商/推荐高QPS LLM任务（如商品分类、query意图识别、文案生成）可将固定few-shot示例效果烘焙到权重，无需每次拼接示例，大幅降低长上下文推理成本

  - 仅需少量校准样本通过岭回归拟合仿射变换，无需反向传播，比LoRA等微调方案的适配成本低，适合业务侧快速上线新LLM任务

  - 推理时直接合并到原生注意力输出投影层，无额外算子开销，FLOPs、TTFT接近零样本，完全兼容现有LLM推理框架，无需改造引擎即可落地

  - 仅支持开放权重模型，闭源API无法获取内部激活和权重，业务选型时需注意该约束'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
显式ICL需要每次在prompt拼接示例，大幅提升上下文长度，导致prefill计算、内存开销陡增，尤其高并发重复任务场景成本极高。现有隐式ICL大多用固定向量表征示例效果，无法适配不同query和token位置的差异化影响，性能上限低。

### 方法关键点
- 成对收集同一个query-answer对加示例、不加示例时的注意力输出，计算每层注意力输出的差值作为示例的效应表征
- 对每层注意力输出投影层学习仿射变换（权重增量ΔW、偏置增量Δb），用岭回归拟合无示例时的注意力表征到效应差值的映射，有闭式解无需反向传播
- 推理时将学习到的仿射变换合并到原注意力输出投影层，不需要额外模块，也不需要在prompt加示例

### 关键结果
在12个分类基准、4个模型家族（Llama3.2-3B、Gemma2-27B、Qwen3.5-0.8B等）上验证，对比10+隐式ICL基线、显式ICL、LoRA：
1. 分类任务平均准确率超过所有隐式ICL基线，比最优基线分别高2.8、1.0、0.3个百分点，在Llama、Qwen上分别超过显式ICL 2.1、1.9个百分点，也优于LoRA
2. 多token生成任务（GSM8K、翻译、摘要等）上性能接近显式ICL，优于支持生成的隐式ICL基线
3. 推理FLOPs、TTFT几乎和零样本一致，即使示例上下文长达16K也无额外开销

### 核心结论
隐式ICL的核心是自适应捕捉示例对不同输入的差异化效应，而不是用固定向量做全局偏移，仅修改注意力输出投影层即可在几乎不增加推理成本的前提下匹配显式ICL的效果
