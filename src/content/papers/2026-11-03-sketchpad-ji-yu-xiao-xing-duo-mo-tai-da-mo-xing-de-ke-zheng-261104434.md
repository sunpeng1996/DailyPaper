---
title: 'Sketchpad: certified exact arithmetic with a small vision-language model'
title_zh: Sketchpad：基于小型多模态大模型的可证明精确算术系统
authors:
- Mostafa 'Neo' Mohsenvand
affiliations:
- MIT Media Lab
arxiv_id: '2611.04434'
url: https://arxiv.org/abs/2611.04434
pdf_url: https://arxiv.org/pdf/2611.04434
published: '2026-11-03'
collected: '2026-11-09'
category: Reasoning
direction: 多模态大模型 · 可验证精确推理
tags:
- LLM
- Multimodal
- LoRA
- Formal Verification
- Arithmetic Reasoning
one_liner: 通过限制每步仅读取有限内存视图，实现0.8B多模态模型任意长度算术的可证明精确性
practical_value: '- 可复用门控LoRA架构：为电商/Agent场景下的确定性任务（如满减计算、库存校验）训练专用LoRA，通过标量门控无缝切换基础模型与领域能力，完全避免灾难性遗忘

  - 有限视图枚举校验思路：对于要求100%准确的业务规则类任务，拆解为固定有限的输入视图，枚举所有视图完成校验后，即可保证任意长度输入的结果正确，杜绝静默错误

  - 锁步批处理优化：多个独立的确定性任务可锁步共享forward pass，降低推理延迟与算力成本，适配大促等高并发场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有大模型算术推理准确率仅为样本估计值，无未知输入正确性保证，调用外部工具虽准确但将计算移出模型；Chain-of-Thought等方法每步依赖上文，无法通过有限测试覆盖所有输入，长序列易出现静默错误，无法用于资损敏感的业务场景。

### 方法关键点
- 基于Qwen3.5-0.8B多模态模型，仅训练10.2M参数的rank16 LoRA适配器（占总参数1.2%）；新增标量门控，g=0时完全恢复基础模型能力，g=1时启用算术能力
- 外部工作内存为固定单元格的渲染表格，每步推理仅读取3个单元格的有限视图，输出当前步数字、进位/借位、下一步操作，runtime负责移动视图与写入结果，步间无其他状态传递
- 所有操作的可能视图共2446种，经Lean形式化证明：只要模型在这2446种视图上输出全部正确，即可保证任意长度输入的算术结果100%准确，且可容忍≤1.51 logits的数值扰动

### 关键结果
220道预注册算术题（含1000位加法、20位乘法）准确率100%，优于GPT-6.1 Sol的98.6%；200道浏览器端运行的复杂题（除法、开方、GCD等）全部正确，单题中位耗时2~9.8s；对话适配器调用计算工具的精度0.994、召回0.989，IFEval、MMLU指标与基础模型差距小于2分，仅GSM8K下降5.8分。

### 核心结论
当模型推理每步仅依赖有限个可枚举的输入视图时，只要枚举校验所有视图的正确性，就能保证任意长度输入的推理结果100%准确，无需依赖长尾样本测试。
