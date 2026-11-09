---
title: Steerable Multi-Objective Group-Relative Preference Optimization with Jointly
  Trained Low-Rank Adapters
title_zh: LambdaMix：基于联合训练LoRA的可控多目标组相对偏好优化
authors:
- Constantinos Karouzos
- Nikolaos Aletras
affiliations:
- University of Sheffield, UK
arxiv_id: '2611.09634'
url: https://arxiv.org/abs/2611.09634
pdf_url: https://arxiv.org/pdf/2611.09634
published: '2026-11-05'
collected: '2026-11-09'
category: Training
direction: LLM多目标对齐 · LoRA联合训练
tags:
- LoRA
- GRPO
- Multi-Objective Alignment
- RLHF
- PEFT
one_liner: 单轮联合训练多目标LoRA适配器，推理无需额外优化即可动态调整多目标偏好权衡
practical_value: '- 电商/广告多目标生成场景（比如商品文案需兼顾点击率、合规性、用户体验）可直接复用LambdaMix架构，单轮训练多目标LoRA，推理时动态调整偏好无需训练多套模型，大幅降低训练成本

  - 可借鉴「同一偏好向量同时控制LoRA混合与奖励加权」的设计，保障模型偏好调节更连贯，目标权重调整时分数反转率降低60%以上，更符合业务预期

  - 可根据业务场景选择是否开启GDPO风格奖励归一化：多目标奖励尺度差异大的场景（比如吸引力vs合规性）开启，奖励范围相近的场景（比如准确率vs话术规范）关闭，可进一步提升效果

  - 推理时可将混合后的LoRA权重合并进基座模型，不增加推理延迟，适配对延迟要求高的搜索/推荐/广告上线场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM多目标对齐方法通常需多轮训练多个策略，或偏好调节范围窄、目标权重调整时易出现分数反转，无法适配电商、推荐等业务场景多目标动态权衡的需求，部署后用户偏好变化时重新训练成本极高。

### 方法关键点
- 冻结基座LLM，为每个优化目标训练1个独立LoRA，训练时用同一偏好向量同时完成两个动作：混合多个LoRA得到当前生成策略、加权标准化后的多目标奖励更新适配器
- 支持开启GDPO风格逐目标奖励标准化，再对加权结果做优势归一化，降低不同目标奖励尺度差异的干扰
- 训练时偏好权重从均匀分布采样，逐步扩大偏好范围，单轮训练即可支持推理时任意调整目标权重，无需额外优化

### 关键结果
在3类双目标任务（有益性vs安全性、数学题准确率vs指令遵从、评论改写保留原文vs隐去个人属性）、4个不同规模基座模型上，对比CLP、Panacea、GRPO专家模型、策略合并等10+基线：
1. 前两类任务中LambdaMix超体积优于所有基线，Qwen3.5-9B上有益性+无害性任务超体积达0.8735，较最强基线提升12.6%
2. 偏好调节范围是条件式基线的3~6倍，目标权重调整时分数反转率比条件基线低60%以上
3. 训练轮次仅为5个GRPO专家模型的1/5，存储的适配器参数仅为其40%

### 核心结论
多目标LoRA联合训练时，用同一偏好同时控制策略混合和奖励加权，比仅调整单一组件可大幅提升偏好调节的灵活性和效果
