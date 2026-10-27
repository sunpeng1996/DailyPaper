---
title: 'Learning When to Commit: Schedule Distillation for Fast Diffusion Language
  Models'
title_zh: 基于调度蒸馏的扩散大语言模型快速解码框架dSpark
authors:
- Aidar Myrzakhan
- Zhiqiang Shen
affiliations:
- VILA Lab, MBZUAI
arxiv_id: '2610.35804'
url: https://arxiv.org/abs/2610.35804
pdf_url: https://arxiv.org/pdf/2610.35804
published: '2026-10-26'
collected: '2026-10-27'
category: LLM
direction: 扩散大语言模型 · 推理加速
tags:
- Diffusion LLM
- Inference Acceleration
- Schedule Distillation
- LoRA
- Parallel Decoding
one_liner: 通过优先提交可降低剩余预测不确定性的token并蒸馏解码调度，实现dLLM数倍提速且保留生成质量
practical_value: '- 生成式推荐/电商文案生成场景若采用dLLM做并行生成，可直接借鉴调度逻辑：优先选择能降低后续token预测难度的候选提交，而非仅依赖置信度，可在不损失生成质量的前提下大幅降低推理延迟

  - 蒸馏加速范式可迁移：将推理端最优调度逻辑通过蒸馏迁移到模型内部，搭配KL正则保留原始模型分布，该思路可复用至任意需要迭代生成的场景（如多轮Agent响应、批量商品标题生成）

  - 训练配比可直接复用：LoRA微调时采用4:1的正确/错误轨迹配比，可很好平衡提速幅度与生成精度，适合所有LLM下游加速微调场景

  - 置信度校准方案可参考：dSpark高置信预测准确率达91%，比同类蒸馏方法高近10pct，适合电商可控生成场景（如广告语、营销文案）降低错误生成率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
扩散大语言模型（dLLM）支持多token并行生成，但传统解码调度仅按token预测置信度提交，忽略了高信息价值token对后续预测的简化作用，导致解码轮次多、效率低，限制了dLLM在低延迟业务场景的落地。

### 方法关键点
- 离线构造最优解掩码调度：对正确生成样本，每轮选择提交能最大程度降低剩余未预测位置surprisal的token，而非仅选置信度最高的token，实测低置信度高信息token可让其他位置就绪量提升5.1倍
- 调度蒸馏：把构造的最优调度轨迹作为训练数据，用LoRA微调dLLM，训练目标结合交叉熵损失、置信度锐化损失，让模型学会在高信息token提前提交的上下文下做预测
- KL正则保精度：引入错误轨迹的KL散度正则，让模型在错误生成路径上的分布和原始模型对齐，避免过度追求提速导致生成质量下降，训练时正确/错误轨迹配比为4:1

### 关键结果
在GSM8K、MATH、HumanEval、MBPP四个基准上对比原生dLLM、Fast-dLLM、d3LLM等基线，在LLaDA-8B-Instruct上GSM8K任务实现10.12×提速，精度不下降；在Dream-7B-Instruct上GSM8K实现5.12×提速，精度还提升1.5%；高置信预测准确率达91%，比同类蒸馏方法高近10pct，校准误差降低一半以上。

最值得记住的结论：dLLM解码效率的核心不是单步提交多少token，而是每一步提交的token能多大程度简化后续的预测任务
