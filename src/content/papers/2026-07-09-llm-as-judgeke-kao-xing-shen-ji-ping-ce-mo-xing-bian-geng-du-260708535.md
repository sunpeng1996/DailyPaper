---
title: 'When the Judge Changes, So Does the Measurement: Auditing LLM-as-Judge Reliability'
title_zh: LLM-as-Judge可靠性审计：评测模型变更对度量结果的影响
authors:
- Zongyou Yang
- Yinghan Hou
- Xiaokun Yang
affiliations:
- Imperial College London
- Nanchang Institute of Technology
arxiv_id: '2607.08535'
url: https://arxiv.org/abs/2607.08535
pdf_url: https://arxiv.org/pdf/2607.08535
published: '2026-07-09'
collected: '2026-07-10'
category: Eval
direction: LLM评测 · LLM-as-Judge可靠性审计
tags:
- LLM-as-Judge
- Evaluation Reliability
- Model Scaling
- Bias Mitigation
- Evaluation Protocol
one_liner: 对比不同参数规模、版本的LLM-as-Judge度量偏差，给出评测可靠性保障规范
practical_value: '- 做LLM4Rec/Agent生成效果评估时，优先选Qwen3 4B及以上参数规模的LLM-as-Judge，不要随意替换MiniMax相邻版本，避免度量波动

  - 用LLM-as-Judge做业务AB测时必须固定基线评测模型，不能随意升级Judge版本，否则跨批次结果不可比

  - 针对LLM-as-Judge的位置、冗长偏好偏差，可在评测Prompt中增加显式约束，配合小样本校验减少系统性偏差

  - 不要盲目用多轮辩论机制提升评测准确率，必须配套解析器、回退日志，才能定位结果波动的真实原因'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM-as-Judge已广泛用于生成式模型效果度量，但评测模型更换后即使候选输出完全不变，得分也会出现无解释波动，该度量有效性问题缺乏系统性审计。
### 方法关键点
基于4个通用评测数据集，对比两类主流Judge升级路径：1）Qwen3稠密模型从1.7B到32B的参数缩放；2）MiniMax M2到M2.7的API版本迭代，同时测试偏见、陪审团聚合、结构化辩论等因素对评测结果的影响。
### 关键结果数字
1. 仅Qwen3 1.7B→4B升级可获得稳定的邻接版本增益，MiniMax相邻版本迭代无可靠增益，不同Judge升级路径不可互换；
2. 更大参数的Judge可降低但无法完全消除位置偏见、冗长偏好；
3. 当采样误差强相关时，多采样陪审团机制对结果提升幅度<5%；
4. 结构化辩论可使判决结果偏移幅度超过30%，若无解析器和回退日志无法确定变动是否来自有效推理。
