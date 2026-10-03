---
title: 'Generalization Is Stability, Not Accuracy: Multi-Axis Evaluation of LLMs'
title_zh: 《泛化即稳定性而非准确率：大语言模型多维度评估框架》
authors:
- Nagham Omar
- Mahmoud Jabarin
- Maya Rozenshtein
- Rom Himelstein
- Avi Mendelson
- Amit LeVi
affiliations:
- Technion – Israel Institute of Technology
arxiv_id: '2610.01428'
url: https://arxiv.org/abs/2610.01428
pdf_url: https://arxiv.org/pdf/2610.01428
published: '2026-09-30'
collected: '2026-10-03'
category: Eval
direction: LLM泛化稳定性多维度评估
tags:
- LLM
- Generalization
- Evaluation
- Robustness
- Stability
one_liner: 提出SAGO评估框架，多维度衡量LLM泛化稳定性而非仅依赖单一准确率指标
practical_value: '- 评估业务侧LLM模块（如Query理解、导购Agent、文案生成）时，不要仅依赖单prompt下的准确率，可复用SAGO的4个评估维度做鲁棒性校验，避免上线后用户不同表述引发输出漂移

  - 对电商搜索、推荐场景的LLM入口，可加入语义等价输入变体的稳定性校验环节，降低同一用户不同问法下的意图识别、回复结果不一致问题

  - 模型选型时不要仅参考公开benchmark排名，可结合业务场景自制语义等价输入测试集，验证模型在目标场景下的泛化稳定性后再决策'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM泛化评估依赖单一prompt格式、任务下的聚合准确率，混淆鲁棒性与基准表现，无法反映真实场景中用户同一意图不同表述下的模型输出稳定性，直接影响搜索、Agent等落地系统的体验一致性。
### 方法关键点
1. 重新定义LLM泛化为语义等价输入下输出的语义稳定性，而非单维度准确率
2. 推出SAGO（Stability-Aware Generalization Objective）评估框架，从生成一致性、内部激活、置信度、响应镜像4个维度，逐示例跨输入变体、跨基准衡量模型行为波动
### 关键结果
主流商用/开源LLM均存在统计显著的泛化不稳定性，无模型可实现全维度一致泛化；不同行为维度对应独立失效模式，跨数据集测试可完全反转现有公开benchmark的模型排名。
