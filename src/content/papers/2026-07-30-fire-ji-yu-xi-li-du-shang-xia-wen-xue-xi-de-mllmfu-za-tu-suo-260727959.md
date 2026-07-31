---
title: 'FiRE: Enhancing MLLMs with Fine-Grained Context Learning for Complex Image
  Retrieval'
title_zh: FiRE：基于细粒度上下文学习的MLLM复杂图像检索增强方法
authors:
- Bohan Hou
- Haoqiang Lin
- Xuemeng Song
- Haokun Wen
- Meng Liu
- Yupeng Hu
- Xiangyu Zhao
affiliations:
- 山东大学
- 香港城市大学
- 哈尔滨工业大学（深圳）
- 山东建筑大学
arxiv_id: '2607.27959'
url: https://arxiv.org/abs/2607.27959
pdf_url: https://arxiv.org/pdf/2607.27959
published: '2026-07-30'
collected: '2026-07-31'
category: RecSys
direction: 多模态内容检索 · MLLM微调优化
tags:
- MLLM
- Image Retrieval
- Fine-grained Learning
- LoRA
- Zero-shot
- Dataset Construction
one_liner: 提出细粒度五元组数据集管线与两阶段解耦微调策略，提升MLLM复杂图像检索零-shot性能
practical_value: '- 电商组合图搜（参考图+文本修改需求）场景可直接复用两阶段解耦微调范式：先做细粒度上下文生成微调，再做检索对齐微调，仅用LoRA优化即可，4张A100就能完成训练，算力门槛低

  - 构建多模态训练数据时可参考CoT分步生成细粒度标注+模糊度引导生成类用户query的方法，仅需十万级高质量样本效果就超过百万级粗粒度样本，大幅降低标注成本

  - 检索微调阶段可直接加入可微分Recall@k surrogate loss，无需修改推理逻辑就能直接提升排序指标，可无缝迁移到现有向量检索召回链路

  - 多模态Agent的场景理解模块可复用该细粒度上下文建模方法，提升对用户模糊多模态查询的理解准确率，降低幻觉率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于MLLM的通用图像检索方法存在两大痛点：一是依赖粗粒度句子对/三元组训练，缺乏细粒度上下文建模能力，无法适配长文本、多轮对话、参考图+修改文本等复杂查询场景；二是微调目标纠缠，同时优化生成和检索任务会导致两种能力相互制衡，复杂检索场景性能受限，而电商图搜、内容检索等业务中大量存在这类复杂组合查询需求。

### 方法关键点
- 数据层：自动化细粒度五元组数据集构建管线：1）CoT引导分步生成单图细粒度caption（平均超100token），覆盖主体、属性、上下文多维度信息；2）基于MLLM编码的细粒度语义相似度筛选参考-目标图像对，过滤视觉相似但语义无关的噪声样本；3）模糊度引导指令生成类人类修改文本，更贴近真实用户的模糊表达习惯，最终得到87K高质量FiGMaQ五元组数据集。
- 模型层：两阶段解耦微调策略FiRE，全程用LoRA实现轻量化训练：1）第一阶段做细粒度上下文推理微调，基于参考图+修改文本生成目标图细粒度caption，强化上下文理解能力；2）第二阶段做检索对齐微调，同时用InfoNCE损失和可微分Recall@k surrogate loss优化query-target匹配能力，提升排序效果。

### 关键实验结果
在覆盖4类检索任务的7个数据集上测试，仅用4B参数BLIP-3作为backbone，零-shot性能全面超过SOTA：CIRR数据集R@1达43.33%，比8B参数的E5-V高9.43%；FashionIQ平均R@10达35.02%，比E5-V高3.22%；Urban1K长文本检索R@1达91.4%，比Long-CLIP高5.3%。

### 核心结论
细粒度数据质量和解耦微调对MLLM检索性能的提升，远大于单纯堆叠模型参数规模的效果
