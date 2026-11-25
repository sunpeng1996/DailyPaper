---
title: KMed-31B Technical Report
title_zh: KMed-31B医疗大模型技术报告
authors:
- KMed Team
affiliations:
- NAVER
arxiv_id: '2611.28719'
url: https://arxiv.org/abs/2611.28719
pdf_url: https://arxiv.org/pdf/2611.28719
published: '2026-11-20'
collected: '2026-11-25'
category: LLM
direction: 垂直领域大模型训练 · 知识蒸馏
tags:
- LLM
- Knowledge Distillation
- Synthetic Data
- Domain Adaptation
- Multi-Teacher Learning
one_liner: 提出多教师增量蒸馏方案，训练适配本地部署的高性能31B参数医疗大模型
practical_value: '- 垂直领域多任务训练可借鉴任务分群策略，按反馈类型、输出确定性拆分子任务训练专用专家，避免任务间负迁移

  - 多专家能力融合可复用MOPD²多教师同策略增量蒸馏方案，在不显著提升参数量的前提下集成多个垂直专家能力

  - 缺标注的开放式场景（如电商客服对话、个性化推荐文案生成）可借鉴合成语料构建方法，模拟真实交互流程生成训练数据'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
垂直领域大模型本地部署要求小参数、多任务性能均衡，传统单模型训练易出现不同任务间负迁移，开放式无标准答案任务普遍缺乏标注数据。
### 方法关键点
1. 按输出是否有标准答案、是否有可用反馈将医疗任务分为4类，每类训练1个专用专家模型；
2. 提出Multi-teacher On-policy Delta Distillation (MOPD²) 将多个专家蒸馏为单一31B学生模型；
3. 针对无标注临床问诊任务，构建覆盖常见病的模拟医患对话合成语料。
### 关键结果
相比底座模型，非思考模式下HealthBench Hard从22.95升至41.87、Professional从37.92升至50.20，思考模式下分别提升至51.48、59.18；在所有对比开源模型中HealthBench Professional得分最高，性能超过参数量10倍以上的开源模型，训练方案可迁移到其他底座。
