---
title: 'When EOS Tokens Disagree: Understanding Length Inflation in On-Policy Distillation'
title_zh: 当EOS令牌不一致：理解On-Policy蒸馏中的长度膨胀问题
authors:
- Yuxiao Yang
- Tianrun Yu
- Shangzhe Li
- Kaixiang Zhao
- Xuchao Zhang
- Chetan Bansal
- Huaxiu Yao
- Taylor W. Killian
- Weitong Zhang
affiliations:
- University of North Carolina at Chapel Hill
- Brigham Young University
- Microsoft
arxiv_id: '2609.20511'
url: https://arxiv.org/abs/2609.20511
pdf_url: https://arxiv.org/pdf/2609.20511
published: '2026-09-16'
collected: '2026-09-18'
category: Training
direction: 大模型蒸馏训练 · EOS对齐优化
tags:
- On-Policy Distillation
- EOS Token
- Length Inflation
- Knowledge Distillation
- LLM Training
one_liner: 揭示On-Policy蒸馏中师生EOS偏好不匹配引发长度膨胀的机制，提出概率层语义对齐方案有效缓解问题
practical_value: '- 做生成式推荐/Agent垂直域小模型蒸馏时，首先校验师生模型的EOS语义等价集合，不要仅对齐解码停止集，优先做概率层EOS语义聚合，避免生成冗余内容浪费上下文、降低推理速度

  - 广告文案/商品标题生成场景的小模型蒸馏可直接复用语义EOS聚合trick：将所有功能等价的终止令牌视为同一个stop动作计算蒸馏损失，不需要强制小模型对齐大模型的EOS表面偏好，训练稳定性更高

  - 多版本LLM生成服务兼容场景可参考该对齐思路，统一不同版本模型的终止行为，避免下游核心信息抽取（如推荐文案卖点、Agent工具调用返回值）出错'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
On-Policy蒸馏（OPD）是将大模型能力迁移到小模型的常用高效方案，但训练中常出现学生模型响应长度异常膨胀、重复生成、耗尽上下文预算的问题，现有研究多归因于目标函数偏差或训练不稳定，未关注底层终止令牌的匹配问题，严重影响OPD在生产场景的落地。

### 方法关键点
- 定位核心诱因：师生模型即使声明的EOS集合完全一致，也可能对语义等价的EOS存在不同的概率偏好，OPD逐token蒸馏逻辑会抑制学生原生EOS的生成概率，最终导致模型无法正常终止
- 对比4种修复方案：仅扩展解码停止集几乎无效果；教师侧EOS映射、语义EOS类聚合、单EOS动作空间约束三种概率层对齐方案均有效，其中语义EOS聚合不需要指定标准EOS，跨模型适配性最强
- 跨模型验证机制通用性：覆盖Qwen3、Llama、Gemma三大主流开源模型族，确认EOS偏好不匹配是普遍存在的问题

### 关键实验
在DAPO-Math-17K数据集上做base到post-trained模型蒸馏，相比原生OPD，语义EOS对齐方案使Qwen3的响应截断率从80%+降至接近教师水平（<5%），Llama3.2、Gemma3的长度膨胀幅度分别降低60%、75%，且完全不损失下游任务性能。

最值得记住的一句话：终止行为是极易被忽略的OPD对齐维度，优先完成EOS语义对齐，再排查其他训练不稳定因素。
