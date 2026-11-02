---
title: 'Less Loss, Fixed Weights: Logit Corrections for Forgetting'
title_zh: 固定权重下降低遗忘损失：针对大模型遗忘的logit校正方法
authors:
- Hanyu Yang
arxiv_id: '2610.42000'
url: https://arxiv.org/abs/2610.42000
pdf_url: https://arxiv.org/pdf/2610.42000
published: '2026-10-30'
collected: '2026-11-02'
category: LLM
direction: 大模型 · 微调遗忘修复
tags:
- LLM
- Fine-tuning
- Catastrophic Forgetting
- Logit Correction
- Temperature Scaling
one_liner: 无需重训模型，仅通过logit偏置与温度缩放即可部分恢复微调后大模型遗忘的通用能力
practical_value: '- 业务垂域微调的LLM（如电商客服、文案生成LLM）出现通用能力退化时，可优先用top高频token的logit偏置+温度缩放快速修复，无需重训，成本极低

  - 生成式推荐用LLM微调后若通用文案生成能力下降，可先尝试该方法验证效果，性价比远高于重新训练LoRA或全量微调

  - 线上LLM推理服务可预留logit校正的接入位，无需重新部署模型权重即可快速修正微调后出现的输出偏置问题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大模型经过SFT/DPO偏好对齐，或在数学、代码等领域继续预训练后，会出现灾难性遗忘，原本擅长的通用web文本预测能力大幅下降，传统修复方案需要重训模型，算力与时间成本极高，本文探索无需改动模型权重、仅在输出层做低成本logit校正的遗忘恢复效果上限。

### 方法关键点
- 校正方案：仅在softmax计算前对logit做线性变换，为每个token添加固定偏置，搭配可选的温度缩放，不改动模型任何参数
- 评估指标：提出对称恢复率，扣除校正方法对基础模型本身的增益，避免高估遗忘恢复效果
- 拟合策略：仅针对top4096高频token拟合偏置，降低拟合成本与过拟合风险，校正参数在独立拟合集训练、验证集选优，测试集完全隔离

### 关键实验
在14组1B~7B参数量的基础模型/微调后模型对（覆盖SFT、DPO、数学预训练、代码预训练等场景）上测试，用百万级web文本做评估：仅用偏置校正最高恢复率为9.8%；偏置+温度缩放最高可恢复35.9%的遗忘损失，其中SFT/DPO对齐后的模型恢复效果远好于数学/代码跨域继续预训练的模型（后者恢复率不足2%）；随机损伤的模拟实验中，该方案仍可恢复29%的损失。

### 核心结论
无需重训的logit校正只能部分恢复微调后的遗忘损失，对偏好对齐类微调效果较好，但对跨域继续预训练导致的遗忘基本无效
