---
title: 'OenoBench: A Wine-Domain Benchmark for Knowledge-Grounded Evaluation of Large
  Language Models'
title_zh: OenoBench：面向葡萄酒领域的知识驱动大语言模型评测基准
authors:
- Nikita Khudov
affiliations:
- StrategAI
arxiv_id: '2608.20106'
url: https://arxiv.org/abs/2608.20106
pdf_url: https://arxiv.org/pdf/2608.20106
published: '2026-08-20'
collected: '2026-08-21'
category: Eval
direction: 大语言模型垂直领域评测
tags:
- LLM Evaluation
- Domain Benchmark
- Knowledge Grounding
- Multi-Agent Audit
- Vertical LLM
one_liner: 构建含3266道多难度葡萄酒领域知识题的评测基准，提出溯源可查的LLM驱动benchmark构建流水线
practical_value: '- 垂直领域评测集构建可复用「事实锚定URL溯源+多Agent校验+人类金标准校准」流水线，避免评测题污染、事实错误问题，可直接用于电商商品知识库评测、行业Agent能力评测场景

  - 垂直域LLM选型可参考结论：开源前沿模型与闭源推理模型在成本-精度上同属帕累托最优，部分业务场景优先选用开源模型性价比更高

  - 垂直域RAG系统效果评估可借鉴9-Agent审计校准方法，降低人工标注成本，同时规避模型自偏好带来的评测偏差，适合电商商品问答系统效果评测'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有通用知识类LLM评测基准存在单领域深度不足、生成流水线单一易被模型 exploit、训练数据易污染三大缺陷，垂直领域缺乏高可信度的知识评测基准。

### 方法关键点
- 从政府注册机构、同行评审期刊、维基等可信源爬取38104条带URL溯源的原子事实，生成覆盖6大维度、4个难度等级的3266道选择题
- 构建「事实锚定+LLM仅做格式化/校验+9-Agent审计+人类金标准Cohen's κ校准」的评测集构建流水线，LLM不充当事实来源，避免事实错误

### 关键结果
16个前沿模型整体准确率53%~84%，o3最高达83.6%；推理模式仅为DeepSeek R1带来6.8pp提升，Claude Opus、Gemini Pro无增益；Anthropic对自身生成的题有9pp自偏好，Google则有8pp反向偏好；闭卷答题时所有模型准确率比开卷低约33pp，参数记忆存在明显天花板，仅上下文注入可突破。
