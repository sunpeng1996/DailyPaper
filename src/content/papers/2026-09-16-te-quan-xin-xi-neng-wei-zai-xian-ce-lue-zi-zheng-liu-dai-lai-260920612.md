---
title: What Does Privileged Information Add to On-Policy Self-Distillation?
title_zh: 特权信息能为在线策略自蒸馏带来多大增益？
authors:
- XiuYu Zhang
- Wei Chow
- Junfeng Fang
- Zhenkai Liang
- Tat-Seng Chua
affiliations:
- National University of Singapore
arxiv_id: '2609.20612'
url: https://arxiv.org/abs/2609.20612
pdf_url: https://arxiv.org/pdf/2609.20612
published: '2026-09-16'
collected: '2026-09-18'
category: Training
direction: 大模型训练 · 在线策略自蒸馏优化
tags:
- On-Policy Self-Distillation
- Privileged Information
- LoRA
- Reasoning
- Distillation
one_liner: 构建答案匹配的多视图数学数据集，量化特权信息在在线策略自蒸馏中的额外价值
practical_value: '- 做电商导购Agent、推理类搜索工具的LLM蒸馏优化时，无需盲目给teacher喂完整长参考，精简的polished解决方案性价比最高，过长参考反而可能劣化推理效果

  - 采用OPSD范式训练业务模型时，优先使用「思考态teacher监督直接应答态student」的配置，可充分利用跨模式参数共享的增益，避免思考态训练导致的效果下降

  - 做蒸馏对比实验时必须严格匹配训练checkpoint，不要将早停带来的收益错误归因于参考内容、损失窗口等优化手段，降低实验误判概率

  - 基于LoRA的小参数微调场景下，蒸馏范式本身的增益远高于特权信息的额外增益，前期优先优化蒸馏配置，再针对性调优参考内容即可'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有在线策略自蒸馏（OPSD）普遍将效果提升归因于给Teacher提供的特权参考信息，但无法区分增益来自蒸馏范式本身还是特权信息的额外贡献，不同复杂度参考的效果影响机制也缺乏受控实验验证，导致参考选择、训练配置的设计缺乏依据。
### 方法关键点
- 构建AMPLE-Math数据集：包含5319道数学题，每道题配6种共享标准答案的特权参考视图，覆盖仅答案、核心要点、精简解决方案、完整推理轨迹等，长度从13到4916token不等，设置无参考纯蒸馏对照组。
- 受控实验范式：固定冻结的思考态Teacher，学生训练时为无特权信息的直接应答态，评估统一使用思考态，隔离蒸馏本身与特权信息的贡献。
- 设计正确性对齐、修正压力、KL时间分配三类诊断指标，配合参考替换、损失窗口调整等干预实验，定位效果变化的真实来源。
### 关键结果
无参考纯蒸馏在Qwen3-1.7B上即可带来1.8pp的域内思考推理精度提升、外部基准4.07pp的提升；特权参考仅能带来少量额外增益，Qwen上精简解决方案额外提升1.3pp，更长的完整轨迹无显著增益，SmolLM3-3B第50步时完整轨迹额外提升2pp；若将学生训练时的生成模式改为思考态长输出，所有参考的增益全部转为损失，最高降幅达9.44pp。

判断特权信息的价值，要看它给学生带来的额外增益，而非给Teacher的参考完整度。
