---
title: Fusion Training for Mathematical Generalization in Large Language Models
title_zh: 面向大语言模型数学泛化的思考模式融合训练方法
authors:
- Congfeng Cao
- Pengyu Zhang
- Jelke Bloem
affiliations:
- Institute for Logic, Language and Computation, University of Amsterdam
- INDE Lab, University of Amsterdam
arxiv_id: '2608.09893'
url: https://arxiv.org/abs/2608.09893
pdf_url: https://arxiv.org/pdf/2608.09893
published: '2026-08-10'
collected: '2026-08-11'
category: Training
direction: 大模型训练 · 思考模式融合
tags:
- Thinking-Mode-Fusion
- SFT
- Training-Schedule
- Data-Ratio
- Mathematical-Reasoning
- LoRA
one_liner: 系统探究大模型思考模式融合训练的调度策略与数据配比规律，给出兼顾长短推理的训练指导
practical_value: '- 训练支持「深度思考/快速回答」双模式的业务LLM（如电商客服Agent、多场景推荐理由生成模型）时，优先选择Mix（数据按比例交错）训练调度，可在双模式下获得最优平均性能

  - 若业务对长链推理（如复杂用户问题拆解、活动规则计算、多步推荐路径规划）要求更高，可适当提高思考模式训练数据占比，避免非思考数据稀释推理能力

  - 当短回答样本远多于高成本长推理标注样本时，选择先训非思考模式再训思考模式（NT-T）的调度，可降低长推理能力的损失

  - 双模式性能存在固有负相关（r=-0.58），需根据业务场景权衡两种模式的优先级，不要盲目追求双模式均达最优'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Thinking Mode Fusion（TMF）可让单模型同时支持长链推理和简洁回答，大幅降低多场景LLM的部署成本，但训练时的调度策略、两类数据配比的影响机制未被探明，无法指导最优训练配置。

### 方法关键点
- 固定思考模式（长推理数学题）训练数据量为1500条，调整非思考模式（短解数学题）数据量，覆盖T:NT从1:4到4:1共7种配比
- 对比三种训练调度：先训思考再训非思考（T-NT）、先训非思考再训思考（NT-T）、按比例交错训练（Mix）
- 基于Qwen3-4B用LoRA做SFT，统一用`<think>`标签区分两类模式的输出格式

### 关键结果
- 两类模式性能呈负相关（r=-0.58），非思考精度提升0.01对应思考精度平均下降0.0091
- Mix调度在所有配比下的平均性能最优，双模式精度分别达0.208（思考）、0.695（非思考）
- 思考模式精度随思考数据占比提升单调上升，最高在T:NT=4:1时达0.224
- 若非思考数据占优，选T-NT调度性能更好；若思考数据占优，选Mix调度性能更好

### 核心结论
思考与非思考模式的融合训练存在固有性能trade-off，优先选交错训练调度可最小化双模式的相互负面影响。
