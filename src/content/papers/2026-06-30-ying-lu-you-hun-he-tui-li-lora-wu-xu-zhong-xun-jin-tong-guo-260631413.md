---
title: 'Learning to Select, Not Relearn: Hard-Routed Mixtures of Reasoning LoRAs'
title_zh: 硬路由混合推理LoRA：无需重训仅通过专家选择实现多域适配
authors:
- Seyed Alireza Molavi
- Zhan Su
- Yan Hu
- Peyman Sheikholharam Mashhadi
- Stefan Byttner
- Prayag Tiwari
affiliations:
- Halmstad University
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2606.31413'
url: https://arxiv.org/abs/2606.31413
pdf_url: https://arxiv.org/pdf/2606.31413
published: '2026-06-30'
collected: '2026-07-01'
category: Training
direction: 参数高效微调 · LoRA多专家集成
tags:
- LoRA
- MoE
- Hard Routing
- RLVF
- PEFT
- STE
one_liner: 提出两阶段硬路由框架集成冻结推理LoRA专家，参数效率远高于软路由基线同时保留专家效果
practical_value: '- 多场景LLM能力复用可直接复用硬路由方案，无需重训各场景独立训练的LoRA专家，仅训练轻量路由和小注意力LoRA，训练参数量比软路由方案低85%以上，还能完整保留各场景专家效果，适合电商搜索/推荐/客服等多域LLM能力集成

  - 训练垂直领域推理LoRA时优先用RLVF代替SFT，3B以上规模模型在推理类任务（电商营销文案逻辑校验、用户复杂意图推理等）上效果可提升5%-10%，同时不会破坏基座模型的CoT能力

  - 若业务输入均为单域（如搜索query全为商品相关、客服query全为售后相关），可先用更简单的prompt级路由基线，99%+域分类精度下效果接近token级路由，工程实现成本大幅降低

  - 混合域输入（如用户query同时询问商品参数和物流政策）场景优先选择token级硬路由，比单prompt绑定单专家的方案平均效果高3%以上'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有MoE风格软路由合并独立训练的LoRA时，会对每个专家输出加权，破坏LoRA训练时的单位加性更新假设，导致专家效果下降；若重新微调专家又会增加训练参数量、消耗更多数据，还会改变原有专家的知识，尤其是推理类LoRA的CoT能力易被破坏，隐私场景下也不允许共享原始训练数据重训专家。

### 方法关键点
- 两阶段架构：第一阶段用RLVF（可验证反馈强化学习）独立训练各领域的推理LoRA专家，无需共享训练数据；第二阶段冻结所有专家，仅蒸馏专家的推理轨迹，训练共享轻量路由和小注意力LoRA
- 硬路由设计：每个token仅选择1个专家，用Straight-Through Estimator解决离散路由不可导问题，保证选中的LoRA专家以单位权重生效，完全匹配训练时的假设
- 训练数据极简：第二阶段每个领域仅需1000条蒸馏样本即可完成路由训练，无需原始训练数据

### 关键实验
在GSM8K、ARC-C、MedQA等5个跨域推理数据集上，对比LoRAHub、LoRAMixer、MoLE等基线：3B/8B模型用RLVF训练的单专家比SFT专家平均效果高4.09%/6.99%；集成阶段硬路由方案比软路由基线LoRAMixer平均效果高6.4%/2.07%，训练参数量仅为后者的12%/9.6%；软路由的top2归一化方案实际71%权重集中在单个专家，本质和硬路由行为近似。

最值得记住的一句话：模块化适配的核心是学习何时调用专家，而非修改专家本身的知识，尤其适合数据受限、隐私约束的多域能力复用场景。
