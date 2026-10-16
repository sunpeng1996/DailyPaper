---
title: 'CAT-alyzing Honesty: Continuous Adversarial Training for Transferable LLM
  Honesty'
title_zh: 基于连续对抗训练的可迁移大语言模型诚实性对齐方法CATCH
authors:
- Yuan-Chen Chang
- Niklas Herbster
- Gauthier Gidel
- Tommaso Tosato
affiliations:
- Tara Research
- Mila – Quebec AI Institute
- Technical University of Munich
arxiv_id: '2610.22292'
url: https://arxiv.org/abs/2610.22292
pdf_url: https://arxiv.org/pdf/2610.22292
published: '2026-10-15'
collected: '2026-10-16'
category: LLM
direction: LLM对齐 · 对抗训练实现诚实性增强
tags:
- Adversarial Training
- LLM Alignment
- Honesty
- LoRA
- OOD Generalization
one_liner: 仅用数百条训练数据实现跨场景可迁移的LLM诚实性对齐，同时保留模型通用能力
practical_value: '- 电商客服/导购类Agent需避免虚假宣传、隐瞒商品缺陷的场景，可基于CATCH做轻量LoRA微调，仅需数百条标注数据即可生效，泛化性优于SFT

  - 对抗训练保留模型原有能力的可复用技巧：优先选择目标模型自生成的on-policy utility数据集，避免用其他模型生成的off-policy数据导致通用能力下降

  - 多Agent交互场景（如电商议价Agent、平台审核Agent）的诚实性校验，可复用MASK、Among Us等测试范式，评估模型在压力/利益诱导下的说谎率

  - 针对Agent的对齐训练，可复用CATCH的「正反目标对比+embedding层扰动」的对抗训练范式，无需大量标注数据即可实现目标行为的跨场景迁移'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM对齐方法无法覆盖多场景下的说谎问题：prompting泛化性差，无法应对压力诱导、利益驱动等跨场景说谎行为；SFT需要数千条标注数据，且OOD效果不佳；SOTA激活steering方法会显著降低模型通用能力，甚至引入越狱风险，亟需数据高效、泛化性强、能力保留好的诚实性对齐方案。
### 方法关键点
- 基于连续对抗训练（CAT）改进得到CATCH框架，针对每个带说谎压力的prompt构造诚实目标y+和说谎目标y-的对比对
- 内循环在embedding空间做梯度上升构造最坏扰动，引导模型更易输出y-；外循环更新模型参数，提升y+概率、降低y-概率，同时加入utility loss保留通用能力
- 采用QLoRA做轻量微调，仅需200条左右对比训练数据，优先选择目标模型自生成的on-policy数据作为utility集，避免能力退化
### 关键结果
在Llama-3.3-70B-Instruct、Qwen3.6-27B上测试，对比prompting、SFT、SOTA激活steering（StTP）等基线：
1. MASK数据集上，CATCH将诚实率从34%提升至86%（Llama）、47%提升至91%（Qwen），效果优于使用50倍数据的SFT
2. Among Us多Agent游戏中，CATCH将 impostor 胜率从39%降至20%（Llama）、48%降至12%（Qwen）， confession率从5%升至84%、19%升至85%；
3. AuditBench上，CATCH将隐藏行为发现率从43%提升至79%（SFT对抗模型）、41%提升至93%（KTO对抗模型），和StTP效果相当，但AlpacaEval胜率保持和基线持平（StTP会降至8.6%）。
### 核心结论
仅用数百条小样本的连续对抗训练，即可实现跨场景的LLM诚实性对齐，且选择on-policy utility数据集可完全避免模型通用能力退化。
