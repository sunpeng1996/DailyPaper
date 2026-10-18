---
title: 'AI Consilium: a Benchmark of LLM Clinical Multidisciplinary Second Opinions'
title_zh: AI Consilium：大语言模型临床多学科第二意见评估基准
authors:
- Alexey A. Bokov
- Ivan I. Panin
- Nikolay B. Nechaev
- Mikhail Yu. Valkov
- Valeria Yu. Chernina
- Natalia Gombolevskaya
- Ayyaz Hussain
- Vladimir M. Agafonov
- Victor A. Gombolevskiy
- Aleksandr V. Nesterov
affiliations:
- AIRI, Russian Federation
- Northern State Medical University, Russian Federation
- Skoltech, Russian Federation
- Sechenov University, Russian Federation
- Intelligent Radiology Assistance Laboratories LLC, Russian Federation
arxiv_id: '2610.22298'
url: https://arxiv.org/abs/2610.22298
pdf_url: https://arxiv.org/pdf/2610.22298
published: '2026-10-15'
collected: '2026-10-18'
category: Other
direction: 大模型多角色协作效果评估基准
tags:
- LLM
- Benchmark
- Multi-Agent
- Automated Evaluation
- Clinical LLM
one_liner: 构建临床多学科第二意见多维度评估基准，验证结构化输出与多角色合成可提升LLM诊疗报告质量
practical_value: '- 多角色Agent协作场景可复用「单角色独立输出+结构化合成」范式，提升最终结果的事实一致性、逻辑连贯性与优先级合理性

  - 先用人标注校准LLM Judge再批量做多维度自动评估的方案，可迁移到推荐文案、广告创意、Agent决策结果的规模化效果评测

  - 业务系统选型优先聚焦模型本身能力，再优化输出格式的优先级逻辑，可降低不必要的结构改造投入'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM生成临床第二意见的效果缺乏覆盖事实性、连贯性、可执行性、安全性的多维度标准化评估，也没有针对多学科会诊协作场景的专用基准。
### 方法关键点
1. 基于300例已确诊NEJM-MedQA病例构建基准，110例用于医师标注校准LLM评估器，190例作为留验测试集
2. 对比8种单模型pipeline在自由/结构化输出范式下，单角色意见、多学科会诊合成报告的表现
3. 采用医师校准的LLM Judge完成3040份报告的多维度自动打分
### 关键结果
模型选型对报告质量的影响远大于输出格式；7/8的模型结构化输出整体得分更高，管理维度得分从2.436提升到2.740；多角色结构化合成报告在全部5项共享评估标准上优于单角色预会诊意见，问题优先级、factual grounding、推理连贯性提升最显著；GPT-5.6-Sol全维度表现最优，达成共识所需轮次最少
