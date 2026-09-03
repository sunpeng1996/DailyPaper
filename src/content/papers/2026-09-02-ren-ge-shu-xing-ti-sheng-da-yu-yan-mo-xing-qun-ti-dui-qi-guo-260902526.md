---
title: When Persona Attributes Improve Population Alignment in Large Language Models
title_zh: 人格属性提升大语言模型群体对齐效果的适用条件与方法
authors:
- Leon Fröhling
- Jens Rupprecht
- Markus Strohmaier
- Claudia Wagner
affiliations:
- GESIS – Leibniz Institute for the Social Sciences
- University of Mannheim
- Complexity Science Hub
- RWTH Aachen University
arxiv_id: '2609.02526'
url: https://arxiv.org/abs/2609.02526
pdf_url: https://arxiv.org/pdf/2609.02526
published: '2026-09-02'
collected: '2026-09-03'
category: LLM
direction: 大语言模型人格提示优化与群体行为对齐
tags:
- Persona Prompting
- Population Alignment
- Attribute Selection
- Survey Simulation
- LLM Alignment
one_liner: 明确人格提示的适用场景特征，对比统计与LLM驱动的人格属性选择方法的性能差异
practical_value: '- 做用户调研仿真、人群偏好预判时，优先对用户分歧大的问题（如新品接受度、营销活动态度）用persona prompting，一致性高的通用问题直接用LLM默认输出，可大幅降低prompt成本

  - 构建persona属性列表时，优先选择和目标任务统计相关性最高的属性（如用特征重要性、互信息筛选），效果远好于让LLM自主选择属性，可直接省去LLM选属性的算力开销

  - 做个性化推荐、Agent对话的人格对齐时，高用户差异场景（如兴趣内容推荐、垂直领域咨询）加persona的收益更明显，低差异场景（如通用客服应答）无需额外加persona'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前persona prompting在群体行为模拟、用户仿真等场景效果波动大，缺乏明确的生效边界与最优属性选择标准，无法直接指导落地。
### 方法关键点
- 设计人类响应变异（HRV）指标量化问题的用户分歧度：标称类问题用归一化熵，序数类问题用异议度，值域均为0-1，值越高代表用户回答异质性越强
- 对比8种人格属性选择策略：4种统计基线（特征重要性、与目标变量相关性、问题语义相似度、HRV排序）、2种LLM驱动方法（批量选择Top5属性、单属性打分选Top5），以及无属性的纯LLM基线
- 覆盖6款不同参数量LLM（3B到70B）、4份美德两国的通用社会调查数据集，对每个目标问题选5个属性构建人格提示，用JSD衡量预测回答分布与真实人群分布的对齐度
### 关键结果
- 高HRV问题上，所有带persona的方案JSD比无persona基线平均低15%；低HRV问题上无persona基线效果更优，加入persona反而会引入噪声
- 统计基线中的相关性、特征重要性方法效果最优，比LLM驱动的属性选择方法JSD平均低10%
- LLM驱动的属性选择稳定性随模型规模提升，70B级模型Top1属性的跨轮次选中重复率可达58%

> 最值得记住的结论：Persona prompting的核心价值是捕捉高用户异质性场景的群体差异，属性选择优先用统计相关性方法，无需依赖LLM自主选择
