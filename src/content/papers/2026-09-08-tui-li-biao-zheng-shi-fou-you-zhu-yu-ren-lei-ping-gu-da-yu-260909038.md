---
title: Do Reasoning Representations Help Humans Evaluate LLM Outputs?
title_zh: 推理表征是否有助于人类评估大语言模型输出？
authors:
- Jaewoo Lim
- Sungbok Shin
- Sanghyun Hong
affiliations:
- Oregon State University
- Sogang University
arxiv_id: '2609.09038'
url: https://arxiv.org/abs/2609.09038
pdf_url: https://arxiv.org/pdf/2609.09038
published: '2026-09-08'
collected: '2026-09-09'
category: Eval
direction: LLM推理表征的人类效用评估
tags:
- Reasoning Representation
- Human Evaluation
- Chain-of-Thought
- Trust Calibration
- LLM Explanation
one_liner: 通过6类推理格式的受控人类实验，揭示推理表征的用户偏好与实际评估效用错配
practical_value: '- 面向用户侧的LLM推理解释展示优先选择简洁CoT traces，而非复杂规划/分解结构，可提升用户对输出的信任度与验证效率

  - 设计Agent人类反馈对齐流程时，避免将用户对推理格式的主观偏好作为核心评估指标，防止引入校准偏差

  - 电商智能客服、导购场景下的LLM应答附带推理说明时，简化逻辑链路可降低用户对正确答案的误判概率，优化信任校准效果'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有推理表征评估仅围绕答案准确率、忠实度等模型侧指标开展，未验证其是否能真实帮助人类评估LLM输出，存在评估目标错配问题。
### 方法关键点
搭建支持任务域、问题实例、表征顺序随机化的Web实验框架，针对6类推理格式在不同复杂度任务下开展受控人类研究，采集结构理解、错误检测定位、信任校准三类细粒度判断数据。
### 关键结果
用户主观偏好规划、分解类推理表征，但简单Chain-of-Thought traces在验证效率、信任度、可解释性上的实际支撑效果更优；用户偏好的表征存在校准风险，对正确推理链的误报率更高，且用户验证意愿偏低但信任度偏高。
