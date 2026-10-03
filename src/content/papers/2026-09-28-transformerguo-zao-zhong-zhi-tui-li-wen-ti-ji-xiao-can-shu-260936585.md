---
title: Transformers Stop Thinking Too Early, and a Tiny LoRA Fixes It
title_zh: Transformer过早终止推理问题，极小参数LoRA即可高效修复
authors:
- Zehao Jin
- Ruixuan Deng
- Junran Wang
affiliations:
- Georgia Institute of Technology
arxiv_id: '2609.36585'
url: https://arxiv.org/abs/2609.36585
pdf_url: https://arxiv.org/pdf/2609.36585
published: '2026-09-28'
collected: '2026-10-03'
category: Reasoning
direction: 大模型推理 · LoRA参数高效微调
tags:
- LoRA
- Multi-hop Reasoning
- Parameter Efficient Fine-tuning
- Transformer
- Context Processing
one_liner: 用单层rank-8 LoRA（不足0.01%参数量）大幅提升Transformer多步上下文推理链路长度
practical_value: '- 做电商Agent多跳需求解析、复杂商品属性匹配任务时，无需全量微调LLM，仅在中早期层插入rank-8 LoRA即可大幅提升多步推理准确率，新增参数量不足0.01%，训练成本极低

  - 适配多轮循环推理架构的LLM时，在循环体中早期层加LoRA可充分激活循环计算价值，避免多轮推理无效，适合长上下文用户兴趣溯源、多轮query理解场景

  - LLM任务适配时优先在中早期层做参数高效微调，在多跳QA、复杂推理任务上收益显著高于晚期层微调，且可保留90%以上全层微调的效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
预训练Transformer的多步上下文推理能力被严重低估，13款主流基座模型默认仅能稳定跟踪1.4~3.6步的引用链，即使292B参数量的DeepSeek-V4-Flash MoE模型也难以处理更长链路，单纯增加层数或推理循环轮次收益极低，默认输出表现无法反映模型实际具备的计算潜力。

### 方法关键点
- 仅在模型单中早期层插入rank-8 LoRA，其余权重全冻结，新增参数量不足总参数的0.01%，训练时加入WikiText的KL散度约束避免通用能力退化
- 提出基于冻结模型的cutoff层测量方法，可快速定位LoRA最优插入位置，无需全层扫参
- 验证LoRA作用机制为启动中间层推理中继，让每行上下文的引用链标识持续传递，而非仅依赖query侧短路径推理

### 关键结果
- 合成引用链任务：Qwen3-8B的24步链准确率从15.5%提升至99%，长训练LoRA支持50步单轮推理；Ouro-1.4B配合8轮循环可支持至少160步引用链
- 多跳QA数据集MuSiQue：Qwen3-8B、OLMo-7B、Llama-8B的Exact Match分别提升11.4、9.4、17.9个点，仅早期层投影LoRA即可保留90%以上全层微调收益

最值得记住的结论：LLM的默认输出表现不等于其实际具备的计算能力，仅需极小成本的定向干预即可解锁其潜在的多步推理能力
