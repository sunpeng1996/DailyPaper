---
title: On-Policy Delta Distillation for Multilingual Math Reasoning
title_zh: 面向多语言数学推理的同策略Delta蒸馏方法
authors:
- Byeongho Heo
- Jaehui Hwang
- Sangdoo Yun
- Dongyoon Han
affiliations:
- NAVER AI Lab
arxiv_id: '2608.05802'
url: https://arxiv.org/abs/2608.05802
pdf_url: https://arxiv.org/pdf/2608.05802
published: '2026-08-06'
collected: '2026-08-07'
category: Training
direction: 多语言大模型 · 推理能力蒸馏
tags:
- On-Policy Distillation
- Knowledge Distillation
- Multilingual Reasoning
- Math Reasoning
- LLM Post-training
one_liner: 将同策略Delta蒸馏拓展至多语言场景，验证其在英韩日数学推理任务上的性能与跨语言特性
practical_value: '- 做多语言电商导购、多语种客服Agent的业务场景，可直接复用OPD2蒸馏范式，相比原生OPD能在非英语语种上获得3-4pp的推理性能提升，同时缩小不同语言间的能力差距

  - 若业务仅能获取英语标注资源，可先用纯英语语料做OPD2蒸馏迁移推理能力，再补充少量目标语种语料对齐回复语言，大幅降低多语标注成本

  - 做多语言模型效果评估时，不能仅看任务准确率，需额外新增「目标语言回复率」指标，避免出现“输入小语种、输出英文”的用户体验问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有同策略蒸馏（OPD）作为RL类后训练的高效替代方案，在英文推理任务上已验证其效果，但在多语言尤其是东亚语种场景下的性能表现、跨语言迁移特性尚未被充分探索，同时多语言训练中推理能力迁移与回复语言一致性的权衡问题也缺乏明确结论。
### 方法关键点
- 核心采用OPD2蒸馏范式：将原生OPD中「教师模型-学生模型的token概率差」奖励信号，替换为「教师模型-教师对应的基模型的token概率差」delta信号，过滤通用风格、偏好噪声，仅迁移后训练阶段获得的推理能力
- 训练数据构造1:1:1比例的英、韩、日共100K数学题平衡多语言数据集，同时构造100K纯英文数据集做消融实验，无需标注推理过程与答案
- 以Qwen3-30B为教师模型，分别在Qwen3-1.7B、Qwen3-8B学生模型上做蒸馏，同时在思考、非思考两种生成模式下评估
### 关键结果
- 多语言训练场景下，OPD2相比原生OPD在韩语、日语数学推理任务上平均提升3-4pp，在英语任务上提升0.7-2.1pp，最高可缩小英韩推理性能差距4.8pp
- 纯英文训练的OPD2可直接将韩、日语推理准确率提升10pp以上，效果与多语言训练接近，但目标语言回复率下降40-60pp，大量输出英文回复，严重影响多语用户体验

> 最值得记住的结论：多语言大模型的推理能力与语言生成能力是解耦的，纯英语训练可跨语言迁移推理能力，但必须补充少量目标语种语料才能保证回复与输入语言一致
