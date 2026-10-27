---
title: 'Intervention-Certified Amplification: A Validity Gate for $σ$-Weighted Post-Training'
title_zh: 干预认证放大：σ加权大模型后训练的有效性门控机制
authors:
- Leiyue Chen
- Meng Wei
- Xuefeng Hu
- Wei Liu
affiliations:
- ByteDance
arxiv_id: '2610.33882'
url: https://arxiv.org/abs/2610.33882
pdf_url: https://arxiv.org/pdf/2610.33882
published: '2026-10-24'
collected: '2026-10-27'
category: Training
direction: 大模型后训练 · 对齐优化
tags:
- Post-Training
- SFT
- RLHF
- Causal Intervention
- Alignment
one_liner: 为σ加权SFT/RL混合后训练添加成对干预有效性门控，抑制有害预训练行为残留
practical_value: '- 做Agent工具调用/多步推理对齐时，可复用成对干预探针检测模型是否学到无价值的表面格式（如未执行代码块、格式化套话），避免数据清洗后仍出现预训练行为残留

  - 电商/广告场景做文案生成、query改写的σ加权SFT/RL混合对齐时，可直接复用ICA门控逻辑，对有害特征样本做权重下探而非硬过滤，既降无效行为占比又不损失有效信息

  - 多领域对齐场景可实现分领域条件门控，避免全局统一抑制误伤特定领域的有效行为（如数学领域代码调用为有效能力，无需抑制）'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有σ加权SFT/RL混合后训练仅依赖训练侧信号给样本加权，无法验证被强化的行为是否对目标任务有效，即便把锚点数据中的有害特征（比如未执行的Python代码块TIR）完全清洗，后训练仍会重新激活预训练阶段学到的相关残留行为，导致效果下降，出现10pp左右的准确率损失。

### 方法关键点
- 提出DIAA探针：基于贝叶斯最优锚点-策略判别器生成逐样本σ权重，混合SFT和RL损失，用于量化行为放大效应，无需额外训练判别器网络
- 提出ICA干预认证门控：通过成对滚出（同一prompt下分别用基础后缀和干预后缀推理）的准确率差判断特征是否有害，生成逐样本门控c(x)，修正原σ权重为σeff=σ*c，保留原损失结构无需改动训练框架
- 两种落地实现：冻结版门控提前离线计算好c(x)固定使用，在线版训练过程中每隔K步用成对探针更新门控参数

### 关键实验
基于Qwen2.5-1.5B+LoRA在数学推理场景验证，基线为未加门控的DIAA：
- MATH-500数据集上，无ICA门控的DIAA即便用0%TIR的干净锚点训练，仍有29%的prompt生成未执行TIR，准确率47.5%；加冻结ICA后TIR率降到13.8%，准确率提升到48.7%，残留准确率损失从10.6pp降到4.9pp；加在线ICA后TIR率降到11.2%，准确率提升到49.3%，残留损失降到3.8pp
- 门控无需重调直接迁移到GSM8K数据集，准确率从67.9%提升到70.4%以上

### 核心结论
大模型后训练不是仅拟合锚点数据的字面内容，而是选择放大预训练已有的行为通道，仅靠数据清洗无法彻底消除有害行为残留，需要结合干预验证做加权控制
