---
title: Choosing Quantized Code LLMs by File Size and Energy per Solved Task
title_zh: 按文件大小与单位任务能耗选择量化代码大模型指南
authors:
- Aditi Patodiya
affiliations:
- Independent Researcher
arxiv_id: '2611.17605'
url: https://arxiv.org/abs/2611.17605
pdf_url: https://arxiv.org/pdf/2611.17605
published: '2026-11-12'
collected: '2026-11-20'
category: LLM
direction: 代码LLM量化选型 · 能效优先
tags:
- Quantization
- GGUF
- CodeLLM
- EnergyEfficiency
- ModelSelection
one_liner: 实测24款Qwen2.5-Coder量化模型，给出不同大小预算下的能效最优选型规则
practical_value: '- 端侧Agent/轻量化推理业务选型时，1.5B/3B参数量级优先选q4_K_M量化版本，相比最高精度版本精度损失<3%，能耗降低30%以上，无需盲目使用fp16版本

  - 评估量化模型性价比不要只看tag标称bit数，要实测有效BPW和**单位完成任务能耗**，而非仅看单token能耗，避免选到精度坍塌的低质量量化包

  - 3GB大小预算下不要选7B-q2_K，3B-q4_K_M精度相当但能耗仅为前者的1/2、推理速度快1倍，适合轻量化电商智能客服、商品文案生成等端侧业务'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
端侧部署代码助手/轻量化Agent时，普遍遵循「同文件大小下大模型低精度优于小模型高精度」的选型规则，但该规则未考虑能耗成本，且GGUF量化tag的标称bit数与实际有效bit数差异大，开发者缺乏可落地的能效优先选型参考。

### 方法关键点
- 实验对象：24款不同参数量（0.5B/1.5B/3B/7B）、不同量化级别的Qwen2.5-Coder GGUF模型
- 测试环境：无风扇MacBook Air M2，Ollama+llama.cpp运行时，greedy解码固定seed确保结果可复现
- 评估指标：542个EvalPlus任务通过率、CPU/GPU/内存轨单位解决任务能耗、全系统能耗

### 关键结果
- 1GB预算选1.5B-q4_K_M、2GB预算选3B-q4_K_M，均为精度和能效的帕累托最优，q4_K_M相比同参数最高精度版本精度损失<3个百分点
- 3GB预算下7B-q2_K相比3B-q4_K_M通过率无显著提升（90%CI最大精度差2.4个百分点），但单位任务能耗是后者的2.03倍，推理速度慢1倍
- 8GB预算下7B-q6_K相比2GB的3B-q4_K_M通过率提升6.9个百分点，单位任务能耗是后者的2.64倍

### 核心结论
同文件大小下，大参数量极低精度（有效BPW<3.5）的模型，精度未必优于小参数量中等精度模型，且能耗会显著升高。
