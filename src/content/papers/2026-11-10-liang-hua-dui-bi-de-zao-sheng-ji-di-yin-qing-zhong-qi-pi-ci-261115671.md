---
title: 'The Noise Floor of a Quantization Comparison: Engine, restart, batch and kernel
  drift, measured against 8-bit and 4-bit effects in two decision models'
title_zh: 量化对比的噪声基底：引擎/重启/批次/核漂移与8/4位量化效果测量
authors:
- Aleks Blagojevich
- Trevor Sunderland
affiliations:
- Level5
arxiv_id: '2611.15671'
url: https://arxiv.org/abs/2611.15671
pdf_url: https://arxiv.org/pdf/2611.15671
published: '2026-11-10'
collected: '2026-11-18'
category: LLM
direction: 大模型量化 · 推理噪声分析
tags:
- Quantization
- LLM Inference
- Serving System
- Noise Floor
- Reproducibility
one_liner: 分离量化对比中非量化因素干扰，给出不同场景下噪声基底与量化效果的实测数值
practical_value: '- 做LLM量化选型评估时，必须在同一serving引擎下对比BF16基线与量化版本，避免引擎差异带来的误差误导选型决策

  - 用vLLM部署低比特量化模型时，建议至少重启3次统计推理结果的波动范围，非确定性波动最高可达0.92%的决策翻转，对Agent工具调用、意图识别等场景的稳定性影响需提前评估

  - 模型效果评估不要只看准确率，需额外统计top1决策翻转率，4-bit量化可能出现准确率几乎无变化但3.2%的决策发生翻转、近半数为坏case的情况

  - 对推理一致性要求高的业务场景（如电商审核、标准化意图分类），优先选llama.cpp部署，其BF16重启完全无决策翻转，确定性远高于vLLM'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前量化评估通常直接对比不同引擎上的量化版本与BF16基线，将所有差异归因为量化，但忽略了引擎切换、实例重启、批次变化、内核自动选择等非量化因素带来的结果波动，导致量化效果评估不准，甚至误判。

### 方法关键点
1. 测试对象为Cloudflare两款决策模型：Clef-flash（9B）、Clef（27B），硬件为NVIDIA GB10显卡
2. 控制变量分别测量重启、引擎切换、批次大小、内核选择4类非量化因素的决策翻转率，再在同一引擎下对比8bit、4bit量化的真实翻转率
3. 评估指标包含top1决策翻转率、准确率、净变化case拆分（变好/变坏/错误间互换）

### 关键实验结果
非量化因素最高带来0.92%的决策翻转：llama.cpp BF16重启零翻转，vLLM NVFP4重启翻转率最高达0.92%，引擎切换、批次变化、内核切换的翻转率在0.25%~0.67%区间
同一引擎下量化带来的翻转率：Q8_0约0.88%~1.04%，FP8约1.62%~2.12%，4-bit约3.5%~5.79%，所有4-bit量化的翻转率都显著高于非量化噪声
准确率会掩盖大量真实业务影响：27B模型Q4_K_M量化准确率仅降0.02个百分点，但有436个决策变坏、总翻转率达3.2%

**最值得记住的一句话**：量化评估必须隔离非量化因素的噪声基底，同时报告准确率与决策翻转率，才能真实反映量化对业务的影响。
