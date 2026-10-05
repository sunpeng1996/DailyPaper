---
title: 'Rethinking Token Reweighting for SFT: Suppress, Reverse, and Extrapolate Learned
  Features'
title_zh: 重新思考SFT的Token重加权：抑制、反转与外推已学习特征
authors:
- Cunchun Li
- Haonan He
- Yifan Gao
- Minglei Li
- Jingqi Ye
- Qingyu Yang
- Peng Ye
affiliations:
- Shanghai AI Laboratory
- University of Science and Technology of China
- Fudan University
- KTH Royal Institute of Technology
- The Chinese University of Hong Kong
arxiv_id: '2609.33463'
url: https://arxiv.org/abs/2609.33463
pdf_url: https://arxiv.org/pdf/2609.33463
published: '2026-09-26'
collected: '2026-10-05'
category: Training
direction: SFT训练优化 · 熵引导冻结delta校准
tags:
- SFT
- LoRA
- Token Reweighting
- Entropy Optimization
- Parameter Efficient Training
one_liner: 提出SCALE熵引导SFT后校准方法，可对冻结SFT delta做抑制、反转、外推，提升下游任务性能
practical_value: '- 电商场景做商品文案生成、query理解等领域SFT时，可先用标准LoRA完成SFT，再加SCALE轻量门控校准，仅优化极少参数即可提升领域效果，同时降低SFT导致的通用能力遗忘，算力成本极低

  - Agent推理、工具调用模块的SFT优化可复用SCALE的无监督熵信号，不需要额外标注校准数据，即可修正SFT学到的错误逻辑，降低标注成本

  - 对于SFT后出现的bad case（如商品属性匹配错误、推荐理由生成错误），可通过SCALE的负向门控直接反转对应有害特征，无需重新清洗数据重训SFT模型，迭代效率更高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有SFT的token重加权方法仅能为示范token分配非负权重，最多抑制或放大监督更新，无法反转已学到的有害特征，也不能外推有益特征，还容易覆盖预训练阶段的有用知识，放大噪声标注的负面影响，导致SFT后泛化性下降、通用能力遗忘。
### 方法关键点
- 两阶段训练：第一阶段用标准SFT目标训练LoRA适配器，完成后冻结预训练模型、LoRA的全部参数
- 引入轻量门控：新增token级、模块级门控参数λ，支持λ<0（反转SFT delta）、0≤λ<1（抑制delta）、λ=1（保留原SFT效果）、λ>1（外推增强delta），每层仅新增d+1个参数，参数量极低
- 无监督校准：仅通过最小化模型预测熵优化门控参数，不需要额外标注数据，校准速度极快
### 关键结果
在Qwen2.5-Math-1.5B/7B、Qwen3-4B三个backbone上测试：数学推理Avg@16分别达37.84%、43.60%、36.57%，较SOTA baseline DFT最高提升6.08个点；代码生成在HumanEval、HumanEval+、MBPP上平均得分最高达47.35%，同时通用能力保留效果优于所有对比baseline。
### 核心结论
SFT效果优化不需要修改训练过程，仅通过控制已学习delta的作用强度，即可同时实现下游任务性能提升和通用能力保留。
