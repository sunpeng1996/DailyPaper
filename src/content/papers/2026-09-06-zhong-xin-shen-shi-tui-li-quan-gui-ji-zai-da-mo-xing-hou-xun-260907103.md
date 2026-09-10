---
title: Revisiting Complete Reasoning Traces for Post-Training
title_zh: 重新审视推理全轨迹在大模型后训练中的必要性
authors:
- Jaehui Hwang
- Sangdoo Yun
- Byeongho Heo
- Dongyoon Han
affiliations:
- NAVER AI Lab
arxiv_id: '2609.07103'
url: https://arxiv.org/abs/2609.07103
pdf_url: https://arxiv.org/pdf/2609.07103
published: '2026-09-06'
collected: '2026-09-10'
category: Training
direction: 大模型推理后训练 · 轨迹冗余裁剪
tags:
- SFT
- reasoning
- post-training
- GRPO
- distillation
one_liner: 提出仅保留推理轨迹首尾段的E-SFT方法，在SFT/RL/蒸馏场景均提升推理性能
practical_value: '- 做Agent/推理类SFT时，可直接裁剪推理轨迹中间20%左右的冗余试错、重复推导段，仅保留首尾关键段作为监督信号，无需复杂数据处理，既能降低训练显存占用，还可提升推理准确率

  - 轻量化推理模型蒸馏时，无需对齐全量推理Token分布，仅对齐首尾核心段即可，训练效率提升的同时效果优于全轨迹蒸馏，适合电商场景轻量推理Agent落地

  - 做GRPO类RL对齐时，中间冗余推理段可仅保留上下文不参与梯度计算，降低算力开销的同时避免冗余步骤误导梯度更新，适用于Query理解、商品选品推理等推荐场景的模型优化'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有大模型推理能力后训练普遍采用全量人工/大模型生成的推理轨迹做SFT，但这类轨迹通常包含大量重复试错、回退、冗余阐述的片段，既占用训练显存拖慢速度，也未被验证对推理能力提升有不可替代的作用；现有轨迹压缩方法要么依赖复杂的Token重要性评分，要么需要调用额外大模型做压缩，成本高且效果不稳定。
### 方法关键点
- 经注意力分析、片段 ablation 验证：推理轨迹中间段对最终答案生成的贡献极低，首尾段（问题定义+最终推导片段）才是核心监督信号
- 提出E-SFT（Endpoint-based SFT）：仅保留推理轨迹的首尾段，裁剪中间约20%的冗余片段，无需复杂辅助模块即可实现低成本轨迹优化
- 可拓展至GRPO、on-policy蒸馏场景：中间冗余段仅保留上下文不参与梯度计算，同样可提升训练效果
### 关键实验
在s1K、OpenThoughts3数据集上对比全轨迹SFT、随机采样、相似度过滤、LLM压缩、PPL过滤等基线：
- 32B模型在s1K数据集上E-SFT平均得分75.19，比全轨迹SFT高1.68，优于所有资源消耗型过滤方法
- 适配GRPO时，Qwen3-1.7B基础模型平均得分提升8.7；适配on-policy蒸馏时平均得分提升2.2
- E-SFT可减少长推理输出的冗余Token，同时保留模型通用语言能力，降低领域微调的能力遗忘风险
### 核心结论
大模型推理后训练不需要完整的推理轨迹监督，砍掉中间冗余段强制模型用自身知识补全中间步骤，反而能同时提升推理能力和训练效率
