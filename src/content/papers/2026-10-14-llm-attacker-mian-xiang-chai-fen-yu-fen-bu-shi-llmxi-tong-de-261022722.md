---
title: 'The LLM-Attacker: A Unified Red-Team Framework for Privacy Evaluation of Split
  and Distributed LLM Systems'
title_zh: LLM-Attacker：面向拆分与分布式LLM系统的统一红队隐私评估框架
authors:
- Georgios Politis
- Evangelos Pappas
affiliations:
- Setloop.io
arxiv_id: '2610.22722'
url: https://arxiv.org/abs/2610.22722
pdf_url: https://arxiv.org/pdf/2610.22722
published: '2026-10-14'
collected: '2026-10-24'
category: Eval
direction: 分布式LLM 隐私评估红队框架
tags:
- Split-LLM
- Distributed-LLM
- Red-Teaming
- Privacy-Evaluation
- Evaluation-Framework
one_liner: 提出统一红队框架，标准化拆分与分布式LLM的隐私攻击评估流程，解决结果不可比问题
practical_value: '- 业务采用端云拆分部署LLM时，可复用该框架的标准化流程做隐私验证，避免不同攻击方案的结果不可比

  - 敏感场景（如用户对话、搜索Query处理）的拆分LLM训练环节，需关闭梯度回传或做梯度混淆，降低原始文本被恢复的风险

  - 隐私防御方案上线前必须先完成无防御基准测试，避免因攻击本身效果差误判防御有效性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
拆分部署LLM将前几层部署在端侧保留原始输入，仅向云侧传输中间激活、梯度等数据，但攻击者可从传输数据中恢复原始文本；现有隐私评估因攻击权限、数据集、评估指标不统一，结果无法横向对比。
### 方法关键点
1. 统一记录攻击权限、模型权重可及范围、测试数据集、评估指标等变量，支持攻击中间结果复用与独立打分；2. 强制要求防御方案必须先通过无防御基准测试才可验证效果，自动标注未覆盖的攻击类型。
### 关键结果数字
GPT-2受控实验显示，攻击者获取训练阶段回传梯度时，token恢复准确率从94.20%提升至97.38%，完整文本恢复率从13.71%提升至37.77%，增益的95%置信区间高于预设的2%阈值。
