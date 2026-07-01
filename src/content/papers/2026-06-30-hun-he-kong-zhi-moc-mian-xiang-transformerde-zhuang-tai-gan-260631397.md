---
title: 'Mixture-of-Control: State-Aware Fine-Tuning for Transformer-based Models'
title_zh: 混合控制（MoC）：面向Transformer的状态感知高效微调框架
authors:
- Duc Anh Nguyen
- Tien Ngoc Luu
- Tung Pham
- Toan Tran
affiliations:
- Qualcomm AI Research
arxiv_id: '2606.31397'
url: https://arxiv.org/abs/2606.31397
pdf_url: https://arxiv.org/pdf/2606.31397
published: '2026-06-30'
collected: '2026-07-01'
category: Training
direction: 大模型高效微调 · PEFT优化
tags:
- PEFT
- LoRA
- MoE
- State-Based Tuning
- Fine-Tuning
one_liner: 提出基于跨层控制专家路由的轻量状态微调框架MoC，在相当开销下优于现有PEFT方案
practical_value: '- 可直接将MoC作为LoRA替代方案，用于LLM4Rec、Agent推理模型等业务大模型微调，仅增加极小训练开销即可提升下游任务效果

  - 复现时可直接复用论文最优超参数：Top-K=1、混合系数α=0.95、负载均衡系数λ=0.01，优先选择ATTN+FFN共享门控方案，性价比最高

  - 针对电商垂域大模型微调，可基于MoC跨层信息传递思路，为排序/召回任务定制专属控制专家，进一步提升适配效率

  - 若业务对推理延迟敏感，可将MoC控制参数直接合并进主干模型，推理吞吐量接近原生LoRA，无额外推理开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有PEFT方案（如LoRA、DoRA）大多为层内局部优化，跨层信息交互能力弱，效果上限低；已有的跨层微调方案（如MoLEx）需要额外的预训练块前向传播，计算和内存开销极高，难以落地到大模型业务场景。同时传统权重基PEFT内存优化空间有限，状态基微调虽内存效率高但缺乏全局协调，效果受限。

### 方法关键点
- 将Transformer每层的低秩控制模块视为MoE专家，引入共享门控实现跨层稀疏Top-K路由，生成全局控制信号
- 每层输出融合局部控制信号与路由得到的全局控制信号，用系数α平衡两类信号权重
- 支持4种变体：仅FFN控制、仅注意力控制、注意力+FFN独立门控、注意力+FFN共享门控，架构无关可直接嵌入现有Transformer
- 引入负载均衡损失避免路由塌陷，理论证明α>0.5时可保留跨层方法的表达能力，同时优化梯度流与表示误差

### 关键实验
在8个常识推理NLG数据集、GLUE NLU数据集上测试，覆盖LLaMA2-7B、LLaMA3-8B、Qwen2.5-14B、RoBERTa、DeBERTa等8种骨干，对比LoRA、DoRA、MoLEx等基线：
- NLG任务平均准确率超LoRA 2.4%~6.0%，超最优基线1.0%~3.0%，训练开销与LoRA相当，远低于MoLEx（Qwen2.5-14B上MoLEx训练时间是MoC的2.5倍、内存是2倍）
- GLUE任务平均准确率超LoRA 1.2%~2.0%，在DeBERTa-Large上最优达91.7%

### 核心结论
基于状态基的跨层控制路由是兼顾微调效率与效果的可行路径，无需修改主干即可实现接近全微调的适配能力
