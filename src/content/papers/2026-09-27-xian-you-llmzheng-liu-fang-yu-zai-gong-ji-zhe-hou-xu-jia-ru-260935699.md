---
title: Distillation Defenses Easily Break After Reinforcement Learning
title_zh: 现有LLM蒸馏防御在攻击者后续加入RL训练后极易失效
authors:
- Shidan Javaheri
- Alexander Panfilov
- Oliver Britton
- Yarin Gal
- Yonatan Gideoni
affiliations:
- University of Oxford
- ELLIS Institute Tübingen, MPI for Intelligent Systems
arxiv_id: '2609.35699'
url: https://arxiv.org/abs/2609.35699
pdf_url: https://arxiv.org/pdf/2609.35699
published: '2026-09-27'
collected: '2026-09-30'
category: LLM
direction: LLM安全 · 蒸馏攻击与防御
tags:
- Knowledge Distillation
- Reinforcement Learning
- LLM Security
- Threat Modeling
- Adversarial Attack
one_liner: 指出LLM蒸馏攻击的真实流程包含蒸馏后RL步骤，证明现有主流防御在该场景下失效
practical_value: '- 做业务小模型轻量化时，可采用「蒸馏+后续RL」的训练范式：蒸馏先拉升性能天花板（提升pass@k），RL再打磨落地精度（提升pass@1），效果优于单独使用蒸馏或RL

  - 若需防护自有大模型的推理能力被恶意蒸馏，放弃仅在单次回复层面加混淆的防御（如返回推理摘要、对抗采样），这类防御在攻击者加RL后完全失效，需转向batch级异常请求检测

  - 业务小模型对齐时，不需要拿到SOTA大模型的完整推理Trace，仅用公开推理结果+摘要做蒸馏再补RL，就能达到接近完整Trace训练的效果，大幅降低数据获取成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM蒸馏攻击防御的评估均默认攻击者完成蒸馏后就停止训练，完全忽略了工业界训练SOTA模型普遍采用「蒸馏+RL」的标准流程，导致现有防御的有效性被严重高估，给闭源大模型厂商带来虚假的知识产权安全感。

### 方法关键点
- 重新定义真实蒸馏攻击威胁模型：攻击者会在蒸馏闭源模型的推理Trace后，继续用RL训练学生模型以最大化性能
- 覆盖两类主流防御的验证：一是抗蒸馏对抗采样（向推理Trace注毒），二是仅返回推理摘要不返回完整Trace的防护策略
- 提出极简攻击方案：用普通弱扩展模型将公开的推理摘要还原为近似完整Trace，蒸馏后补充RL训练即可窃取目标模型推理能力

### 关键实验
实验覆盖GSM8K、Minerva Math、MATH500三类推理数据集，测试8款主流开源模型：
- 「蒸馏+RL」范式比单独蒸馏平均准确率高12%，比单独RL平均高4%
- 抗蒸馏采样注毒程度低于86%时，蒸馏后加RL的学生模型与未注毒的性能差小于2%，防御完全失效
- 仅用推理摘要还原的Trace蒸馏后加RL，效果与用完整Trace的差距小于3%，可直接窃取Claude、GPT-5 mini、Gemini的推理能力

**最值得记住的一句话**：所有仅在单请求回复层面做信息删减/混淆的蒸馏防御，只要泄露的信息可还原近似推理Trace，在攻击者后续加RL训练的场景下均无实际防护效果。
