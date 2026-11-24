---
title: Attention Temperature Confounds Zero-Shot Context Extension
title_zh: 注意力温度混淆零样本上下文扩展效果评估
authors:
- Ruben Navasardyan
affiliations:
- EPFL Machine Learning and Optimization Laboratory
- University of Waterloo Department of Applied Mathematics
arxiv_id: '2611.31113'
url: https://arxiv.org/abs/2611.31113
pdf_url: https://arxiv.org/pdf/2611.31113
published: '2026-11-23'
collected: '2026-11-24'
category: LLM
direction: LLM长上下文扩展 · 评估校准
tags:
- LongContext
- AttentionTemperature
- ModelCalibration
- BF16Training
- RoPE
one_liner: 揭示零样本上下文扩展评估中注意力温度的混淆效应，给出校准与校验方案
practical_value: '- 做基于长上下文LLM的RAG、用户长行为序列建模、多轮对话Agent时，不要默认用τ=1做推理，需针对部署长度做温度校准，避免误判优化方案的真实效果

  - 用纯bf16训练带QK归一化的自定义LLM时，若峰值学习率低于1.7e-3（β2=0.95），必须给QK归一化增益设置fp32主权重，避免增益被冻结在1.0，导致长上下文性能大幅下降

  - 评估长上下文相关优化（比如稀疏注意力、位置编码改造）时，需加入NTK-aware缩放这类已知有效的阳性对照，确保校准流程不会抹除真实的性能增益'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前零样本长上下文扩展效果评估默认采用τ=1的注意力温度与基线对比，但模型在超出训练长度时，注意力softmax会因key数量增加导致熵升高，基线本身存在校准偏差，会将对默认温度鲁棒的训练策略误判为具备更强的上下文扩展能力，此前该混淆效应的量化规模、与训练精度的关联均不明确。
### 方法关键点
- 采用种子配对的孪生模型对照实验：仅训练时注意力掩码不同，一组为全注意力Dense基线，一组为随机块稀疏注意力训练的Mixed模型，其余配置完全一致
- 覆盖三种训练精度配方：纯bf16无fp32主权重（归一化增益冻结）、仅QK归一化增益用fp32主权重、全参数fp32主权重的标准训练配方
- 校准方案：为每个模型、每个评估长度单独选择最优τ*，在独立验证窗口评估，加入NTK-aware缩放作为阳性对照，确保校准不会抹除真实增益
### 关键结果
- 纯bf16冻结增益场景下，8k训练的基线在30k长度下校准偏差达37%~58%，稀疏训练、ALiBi、注意力dropout的假性能增益达6%~35%，校准后全部消失，ALiBi反而比RoPE差5%
- 标准全参数fp32主权重训练配方下，基线校准偏差仍有8%~15%，可导致最高7%的假性能提升，校准后完全消失
- 仅解冻QK归一化增益为fp32，即可消除71%~89%的假增益

长上下文扩展能力评估必须做温度校准，纯bf16训练时要检查归一化增益参数是否真的完成了更新
