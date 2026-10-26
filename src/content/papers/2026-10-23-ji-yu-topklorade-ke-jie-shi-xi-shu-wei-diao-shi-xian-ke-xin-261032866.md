---
title: Interpretable sparse fine-tuning with TopKLoRA enables faithful circuit discovery
title_zh: 基于TopKLoRA的可解释稀疏微调实现可信模型电路发现
authors:
- Marek Masiak
- Andrzej Szablewski
- Nicola Cancedda
- Constantin Venhoff
affiliations:
- University of Oxford
- University of Cambridge
- Neuralk-AI
arxiv_id: '2610.32866'
url: https://arxiv.org/abs/2610.32866
pdf_url: https://arxiv.org/pdf/2610.32866
published: '2026-10-23'
collected: '2026-10-26'
category: Training
direction: LLM参数高效微调 · 可解释性
tags:
- LoRA
- Sparse Fine-tuning
- Mechanistic Interpretability
- Backdoor Removal
- Circuit Discovery
one_liner: 提出稀疏可解释的TopKLoRA适配器，配合对比电路发现流程精准定位移除LLM后门且无性能损失
practical_value: '- 业务垂域微调可用TopKLoRA替代普通LoRA：每个token仅激活k个latent降低adapter推理计算量，还能精准定位特定业务能力对应的参数子集，无需全量重训即可快速移除不良/过时能力，例如电商场景下不合规的营销话术生成能力

  - CLCD（对比潜在电路发现）流程可直接复用：用正负样本对（触发目标行为/不触发）做梯度归因排序latent，验证必要性和充分性，可快速定位推荐系统中LLM模块的异常行为根因，比如Agent错误调用商品推荐接口的触发逻辑

  - TopKLoRA的STE训练trick可迁移：用softmax软掩码做梯度回传，硬TopK做推理，既保证稀疏性又避免死神经元，适合所有低资源LoRA微调场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
普通LoRA微调参数更新不可解释，训练数据投毒植入的后门难以定位移除，会通过安全训练残留；后hoc的稀疏自编码器（SAE）优化目标是激活重建而非下游任务因果性，无法精准定位功能对应的参数单元，亟需可解释原生的参数高效微调方案。
### 方法关键点
- 提出TopKLoRA适配器：在普通LoRA的A矩阵投影后加ReLU和TopK选择，每个token仅激活top k个latent后经B矩阵投影输出，无需稀疏惩罚和重建损失，仅用下游任务损失训练；用直通过估计器（STE）处理TopK无梯度问题，避免死神经元
- 提出CLCD pipeline：分搜索和验证两步，搜索阶段用正负对比样本（触发目标行为/不触发）做梯度归因对latent排序，验证阶段逐次测试排序前缀，选出同时满足必要性（消融后目标行为完全消失）和充分性（仅保留该子集目标行为保留）的最小电路
- 提出梯度路由构建已知位置的植入电路方法，用于验证电路发现算法的有效性
### 关键结果
在sleeper agent后门任务上测试gemma-2-2b、Qwen2.5-1.5B、Qwen2.5-7B三个模型，TopKLoRA的后门电路尺寸比同秩的普通LoRA小1~12倍；消融定位到的后门电路可移除99.9%以上的触发后门请求，同时多层TopKLoRA的指令遵循能力保留率接近100%，远优于普通LoRA。
### 核心结论
原生可解释的稀疏微调架构，相比后hoc解释方法能更精准地定位和编辑模型的特定能力，兼顾性能和可审计性。
