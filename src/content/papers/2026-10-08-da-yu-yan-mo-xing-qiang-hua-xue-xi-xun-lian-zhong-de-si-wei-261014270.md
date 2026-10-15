---
title: The Thinking Leakage in Reinforcement Learning for LLMs
title_zh: 大语言模型强化学习训练中的思维泄露现象研究
authors:
- Wenxuan Zhu
- Shuming Liu
- Bang An
- Aznaur Aliev
- Bing Li
- Yibo Yang
- Bernard Ghanem
affiliations:
- King Abdullah University of Science and Technology
- Shanghai Jiao Tong University
arxiv_id: '2610.14270'
url: https://arxiv.org/abs/2610.14270
pdf_url: https://arxiv.org/pdf/2610.14270
published: '2026-10-08'
collected: '2026-10-15'
category: LLM
direction: LLM推理 · RL训练现象分析
tags:
- RLVR
- GRPO
- Chain-of-Thought
- Activation Patching
- LLM Reasoning
one_liner: 发现混合推理LLM无思维模式RL训练的性能提升主要来自原有思维模式的复用
practical_value: '- 搭建电商导购/广告投放Agent的推理模块时，可直接通过prompt干预或attention头开关唤醒混合推理LLM的隐式推理能力，无需额外RL训练，大幅降低训练成本

  - 做LLM微调效果评估时，需新增「思维相似度」类指标，区分模型是习得新业务推理能力还是激活了原有通用能力，避免高估训练方案的业务价值

  - 要快速提升LLM的业务推理性能时，可直接缩放RL训练得到的LoRA权重更新量，无需多轮训练即可快速接近模型的推理性能上限

  - 做Agent模式切换（如快速推理/深度推理切换）时，可通过干预对应attention头的权重实现毫秒级切换，无需维护多套模型权重'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
混合推理LLM（如Qwen3、Llama-Nemotron）支持<think>块显式推理和空<think>块无思维两种运行模式，行业普遍采用GRPO等RLVR方法在无思维模式下训练以兼顾推理性能和输出简洁性，但此类训练带来的性能提升来源长期不明确，是学到了新的推理能力还是复用了模型已有的思维模式能力，直接决定训练方案的投入产出比和效果上限。

### 方法关键点
- 实验对象：Qwen3-1.7B/4B/8B三个规格的原生模型，采用rank=64的LoRA在无思维模式下基于GRPO训练
- 评估指标：设计反射词计数、思维胜率（TWR）、思维激活偏移量α三个维度量化模型输出/内部状态与原生思维模式的相似度
- 因果验证：从权重缩放、8维思维子空间激活修补、空<think>块对应attention头干预三个层面定位性能提升的来源
- 机制分析：拆解GRPO的优势权重信号，验证梯度方向天然偏向更接近思维模式的响应

### 关键结果
在AIME 2022-2024共90道数学推理题上测试：Qwen3-8B训练后无思维模式准确率从0.17升至0.43，思维胜率达94%，激活偏移量达0.56（即56%接近原生思维与无思维模式的激活差异）；缩放RL更新权重后，无思维模式准确率最高达0.72，接近原生思维模式的0.74上限，且会生成思维模式独有的</think> token；替换RL训练模型的8维思维相关激活子空间，可消除75%的RL训练收益；仅干预Top5%关注空<think>块的attention头，即可让无思维模式向思维模式偏移72%。

### 核心结论
混合推理模型无思维模式下的RL训练性能提升，本质是原有思维模式能力的泄露而非新能力的习得，评估训练效果时需严格区分能力新增和能力唤醒。
