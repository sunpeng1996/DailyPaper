---
title: 'CogBattery: Human-Referenced Evaluation of Cognitive Task Behavior and Structure
  in Language Models'
title_zh: CogBattery：基于人类参照的大语言模型认知任务行为与结构评估
authors:
- Dengzhe Hou
- Lingyu Jiang
- Fangzhou Lin
- Kazunori D Yamada
affiliations:
- Tohoku University
- Texas A&M University
- Worcester Polytechnic Institute
arxiv_id: '2607.24999'
url: https://arxiv.org/abs/2607.24999
pdf_url: https://arxiv.org/pdf/2607.24999
published: '2026-10-29'
collected: '2026-11-12'
category: Eval
direction: LLM认知能力 · 人类参照评估基准
tags:
- LLM Evaluation
- Cognitive Paradigm
- Human Alignment
- Open-source LLM
- Behavioral Assessment
one_liner: 构建含13种认知范式的CogBattery基准，评估54款开源LLM的类人认知行为差异
practical_value: '- 做Agent类人决策对齐时，不能只看效应方向匹配，需引入人类错误模式、置信度区分度两个维度做细粒度评估，避免假对齐

  - 给面向用户交互的LLM（如电商导购Agent、推荐解释生成模块）做能力选型时，可复用CogBattery的认知任务范式测试模型的类人行为一致性

  - 验证大模型规模增益边界时，可参考该研究结论：模型规模提升不必然带来类人认知表现的同步提升，避免盲目堆参数'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM与人类认知的对比仅验证效应方向是否匹配，无法识别二者错误模式、置信度表现的实质差异，缺乏覆盖多范式、多模型的系统性评估基准。
### 方法关键点
构建CogBattery评估基准，将13种经典认知范式适配为文本任务，匹配对应任务的源人类实验数据作为参照，对54款开源LLM开展条件级细粒度对比。
### 关键结果
1. 模型虽匹配n-back任务诱饵响应高于对照组的人类效应方向，但对普通非目标的误报率远高于人类；
2. 超80%模型的置信度对正误答案的区分能力弱于人类，多数模型无论预测正误都选择固定赌注；
3. 模型认知得分第一维度与规模强相关，但大模型的类人认知表现无一致性优势；
4. 预定义认知分组的预测效果与同规模随机分组无显著差异。
