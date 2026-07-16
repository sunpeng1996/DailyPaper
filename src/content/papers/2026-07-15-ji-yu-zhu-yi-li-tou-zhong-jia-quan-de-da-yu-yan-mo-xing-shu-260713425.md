---
title: Data-Efficient Adaptation of LLMs via Attention Head Reweighting
title_zh: 基于注意力头重加权的大语言模型数据高效适配方法
authors:
- Tuomas Oikarinen
- Zixiao Chen
- Charlotte Siska
- Tsui-Wei Weng
- Chandan Singh
- Jianfeng Gao
affiliations:
- UC San Diego
- Microsoft Research
- Microsoft Security AI
arxiv_id: '2607.13425'
url: https://arxiv.org/abs/2607.13425
pdf_url: https://arxiv.org/pdf/2607.13425
published: '2026-07-15'
collected: '2026-07-16'
category: Training
direction: 大模型参数高效微调 · 少样本适配
tags:
- PEFT
- Attention Head
- Few-shot Learning
- LoRA
- Text Classification
one_liner: 仅为每个注意力头学习1个标量，少样本场景效果超LoRA，参数量少200-1000倍
practical_value: '- 少样本场景（如电商新类目审核、小众用户意图分类、新违规内容检测）优先尝试AHR，比LoRA参数量小200倍以上，过拟合风险更低，适配速度更快

  - 微调时可引入In-Context Finetuning（IC-FT）技巧，将少样本示例拼接进训练输入，能提升约10%的分类准确率，和具体微调方法无关

  - 合规要求高的场景（如电商违规内容审核、广告素材合规检测）可利用AHR的可解释性，通过学习到的头权重快速定位任务相关的注意力头，排查决策逻辑

  - 当训练样本≥300时不建议用AHR，替换为LoRA等参数量更大的PEFT方法可获得更好效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
少样本适配是高价值场景的核心痛点：电商新类目审核、安全领域新威胁检测等场景标注样本稀缺，现有PEFT方法如LoRA仍有数千到数百万可训练参数，小样本下极易过拟合，亟需参数量更少、过拟合风险更低的适配方案。

### 方法关键点
- AHR仅为每个注意力头引入1个初始为0的可学习标量β，注意力层输出时乘以(1+β)放大/抑制对应头的贡献，其余参数全部冻结，仅修改不到百万分之一的模型参数
- 训练时加入L1/L2正则约束β的变化幅度，避免过度破坏原模型通用能力
- 配套使用In-Context Finetuning（IC-FT）：将k个少样本示例拼接为输入，同时优化所有示例的答案预测损失，充分复用ICL能力
- 推理时可将β直接合并进注意力头的WO矩阵，无额外推理开销

### 关键实验
在6个文本分类数据集（含情感分类、钓鱼URL检测、越狱prompt检测等）上对比LoRA、AdaLoRA、IA3等基线：训练样本≤30的少样本场景下，AHR平均准确率超基线2-4个百分点；在钓鱼URL、越狱检测2个垂直任务上，仅用10个训练样本时准确率领先最优基线6-7个百分点，可训练参数量仅为LoRA的1/200~1/1000；样本量≥300时AHR效果弱于常规PEFT方法。

最值得记住的一句话：仅通过重加权已有的功能专项化注意力头，无需修改头内参数，就能在小样本分类任务上实现比LoRA更好的适配效果。
