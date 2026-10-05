---
title: Behavior Pack Optimization for Video MLLM Post-Training
title_zh: 面向视频多模态大模型后训练的行为包优化方法
authors:
- Zhaolu Kang
- Shiyu Liu
- Tailong Luo
- Wei Zhang
- Yingjie He
- Lei Wei
- Guansu Wang
- Liang He
- Siheng Wang
- Guangyuan Dong
affiliations:
- Peking University
- Chengdu Minto Tech
- The University of Melbourne
- Stanford University
arxiv_id: '2610.03141'
url: https://arxiv.org/abs/2610.03141
pdf_url: https://arxiv.org/pdf/2610.03141
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: 多模态大模型 · 时序推理鲁棒性训练
tags:
- Video MLLM
- RLHF
- GRPO
- Counterfactual Training
- Temporal Reasoning
one_liner: 提出行为包优化框架，提升视频MLLM时序推理鲁棒性与证据敏感性
practical_value: '- 电商短视频商品理解/直播内容审核场景，可复用按任务类型匹配反事实样本的思路，提升模型对关键内容（如商品卖点、违规片段）的敏感性，避免依赖外观先验输出错误结果

  - 多模态大模型RL训练时，可借鉴anchor-relative advantage替代batch归一化的技巧，在小batch/有限计算预算下降低优势估计方差，提升训练稳定性

  - 生成式多模态推荐场景，可复用跨视图行为合约的奖励设计，约束模型在输入微小扰动（如商品视频帧顺序调整、背景修改）下的输出一致性，避免推荐理由漂移'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
当前视频MLLM的高准确率依赖外观和语言先验，而非问题要求的时序证据，帧打乱、关键证据移除/遮挡时预测结果几乎不变，根源是后训练优化单元为单视频单响应，缺少跨视图行为一致性约束，时序推理鲁棒性差。

### 方法关键点
- 优化单元革新：将单响应优化替换为行为包优化，每个包包含原始视频+问题类型匹配的反事实视图，事件/计数类问题匹配证据移除类视图，时序/方向类问题匹配帧反转/打乱类视图
- 跨视图合约奖励设计：联合打分全包输出，要求无关扰动下输出稳定、关键证据移除时输出敏感、无证据时主动拒答
- 低方差优势估计：提出anchor-relative优势，以原始视频的响应作为锚点替代GRPO的batch均值归一化，小pack尺寸下训练更稳定

### 关键实验
基于Qwen2.5-VL-7B-Instruct backbone，在TempCompass、MVBench、NExT-QA数据集上，与同计算预算的vanilla GRPO baseline相比，宏观准确率提升4.7pp，时序困难子集准确率提升7.8pp，拒答F1提升20.0pp，增益可迁移到LLaVA-Video-7B及长视频测试集。

**最值得记住的结论**：多模态模型鲁棒性优化的瓶颈不只是数据覆盖，更是行为优化的粒度，跨视图联合约束比单纯数据增广更有效
