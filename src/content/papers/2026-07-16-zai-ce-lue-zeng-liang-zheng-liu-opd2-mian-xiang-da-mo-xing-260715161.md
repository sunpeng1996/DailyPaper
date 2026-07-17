---
title: On-Policy Delta Distillation
title_zh: 在策略增量蒸馏（OPD2）：面向大模型推理能力的高效蒸馏方法
authors:
- Byeongho Heo
- Jaehui Hwang
- Sangdoo Yun
- Dongyoon Han
affiliations:
- NAVER AI Lab
arxiv_id: '2607.15161'
url: https://arxiv.org/abs/2607.15161
pdf_url: https://arxiv.org/pdf/2607.15161
published: '2026-07-16'
collected: '2026-07-17'
category: Training
direction: 大模型后训练 · 在策略蒸馏优化
tags:
- Knowledge Distillation
- On-Policy Training
- LLM Reasoning
- Post-Training
- Delta Signal
one_liner: 提出用教师与基座的输出差异作为蒸馏奖励，大幅提升多领域大模型推理蒸馏效果
practical_value: '- 垂直领域小模型蒸馏时，可替换传统对齐教师全分布的逻辑，改为对齐「教师相对其基座的delta增量信号」，过滤通用预训练冗余偏好，减少蒸馏噪声，针对性迁移领域/推理能力

  - Agent推理能力微调/蒸馏场景可复用OPD2的双信号约束逻辑：仅当delta信号与传统蒸馏信号方向一致时才更新参数，既保证不偏离教师合理分布，又能强化目标能力，训练稳定性更高

  - 电商场景小模型推理优化（如商品属性识别、营销话术生成蒸馏）中，OPD2仅增加8%-28%的训练开销，即可比传统OPD获得3-5个点的效果提升，4B模型蒸馏效果可对标8B模型传统蒸馏结果，ROI显著

  - 工程落地可直接基于现有TRL的GRPOTrainer做少量修改接入OPD2逻辑，无需重构训练pipeline，适配现有大模型后训练链路，落地成本低'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统在策略蒸馏（OPD）直接对齐大教师模型的输出分布，会将教师预训练阶段携带的通用偏好、风格类无关信息同步蒸馏给学生，真正需要迁移的推理能力信号被稀释，且训练不稳定、易出现效果退化，针对已有较强基础的学生模型蒸馏时增益尤为有限。
### 方法关键点
- 定义delta信号：取经过推理微调的教师模型输出token的log概率，减去其未经过后训练的基座模型对应token的log概率，精准提取教师在后训练阶段习得的推理能力增量，过滤预训练通用噪声
- 新增centering操作：对delta信号减去学生采样分布下的期望奖励，降低训练波动
- 新增联合约束：仅当delta信号与传统OPD信号方向一致时才更新参数，避免学生偏离教师合理分布，解决delta信号单独训练的收敛点偏差问题
### 关键结果
在数学、科学、代码3个领域共14个推理基准上测试，对比基线包括原生OPD、SOTA ExOPD，覆盖Qwen3 1.7B/4B/8B、Gemma4-E4B等主流开源模型：非思考模式下OPD2比ExOPD平均高2~3.8个点，4B模型蒸馏效果超过8B模型原生OPD蒸馏结果；思考模式下传统OPD普遍出现效果退化，OPD2仍能稳定提升1.5~3.5个点，仅比传统OPD增加8%~28%的训练耗时。
### 核心结论
蒸馏的核心是迁移「教师学到的增量知识」而非对齐「教师的全部输出分布」，针对性过滤无关信号可以用极低额外成本获得显著效果增益。
