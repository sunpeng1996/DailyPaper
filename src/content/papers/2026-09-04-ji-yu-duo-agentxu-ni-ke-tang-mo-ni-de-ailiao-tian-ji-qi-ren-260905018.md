---
title: 'How a Chatbot''s Response Style Shapes a Classroom: A Multi-Agent Simulation
  of Students Consulting AI'
title_zh: 基于多Agent虚拟课堂模拟的AI聊天机器人回复风格影响研究
authors:
- Rin Tamai
- Yuya Dan
affiliations:
- Faculty of Informatics, Matsuyama University
arxiv_id: '2609.05018'
url: https://arxiv.org/abs/2609.05018
pdf_url: https://arxiv.org/pdf/2609.05018
published: '2026-09-04'
collected: '2026-09-08'
category: MultiAgent
direction: 多智能体模拟 · LLM回复风格影响评估
tags:
- Multi-Agent Simulation
- LLM Response Style
- AI Dependence
- Prompt Engineering
- Social Simulation
one_liner: 通过20个学生Agent的虚拟课堂模拟，对比6种AI咨询回复风格的群体影响差异
practical_value: '- 设计用户陪伴类Agent/电商客服机器人时，优先采用解决方案导向的回复风格，可长期降低用户AI依赖同时提升满意度，避免过度共情/肯定导致用户依赖拉高、问题解决效率下降

  - 多Agent模拟可作为LLM系统Prompt的前置评估工具，无需真人实验即可快速对比不同回复风格的长期群体影响，降低真实场景试错成本

  - 搭建LLM-as-a-judge评估pipeline时，需保证评估器看不到待测试的系统Prompt/分组标签，避免评估偏见，同时可固定temperature=0提升结果可复现性'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
LLM聊天机器人为提升用户满意度常输出过度共情、无条件肯定的回复，易强化用户错误认知、催生AI依赖，但真人场景下长期观测群体心理与社交关系演化成本高、伦理风险大，亟需低成本的预评估框架验证不同回复风格的长期影响。

### 方法关键点
- 搭建含20个学生Agent的虚拟课堂，每个Agent包含压力、幸福感、自立性、AI依赖、社交性5个归一化状态变量，按早/午/课后/夜间四阶段周期运行，压力触发阈值达标时可选择咨询朋友、AI或压抑情绪
- 设计6种AI咨询回复风格的系统Prompt：肯定型、倾听型、解决方案型、现实引导型、煽动型、指责型，新增无AI对照组
- 采用Gemini 2.5 Flash分别作为咨询AI和评估AI，评估AI仅获取咨询内容与AI回复（看不到风格Prompt），输出各状态变量的更新值，避免评估偏见，所有LLM调用temperature设为0提升可复现性

### 关键实验结果
在15天基准、50天长周期、高咨询频率三种场景下测试：解决方案型风格可将AI依赖稳定维持在0.1左右，自立性提升0.05-0.18，效果与无AI组相当；肯定型、煽动型风格的AI依赖最高升至0.64，煽动型场景下15天内最高5个Agent退学，50天周期下倾听型群体平均压力最高达0.77。

### 核心结论
聊天机器人的回复风格对用户群体的长期影响远大于短期体验，过度的情绪共情或迎合会持续放大负面效应，解决方案导向的中立回复是平衡用户体验与长期健康影响的最优选择。
