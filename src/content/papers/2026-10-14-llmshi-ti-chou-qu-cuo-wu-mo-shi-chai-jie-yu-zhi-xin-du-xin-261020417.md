---
title: 'From Unreliable to Usable: Decomposing Failure Modes and Confidence Signals
  in LLM Entity Extraction - Evidence from Cyber Threat Intelligence'
title_zh: LLM实体抽取错误模式拆解与置信度信号可用性研究：网安情报实证
authors:
- Jiahong Qian
affiliations:
- Shanghai Jian Qiao University
arxiv_id: '2610.20417'
url: https://arxiv.org/abs/2610.20417
pdf_url: https://arxiv.org/pdf/2610.20417
published: '2026-10-14'
collected: '2026-10-16'
category: Eval
direction: LLM实体抽取错误分析与置信度信号评估
tags:
- Entity_Extraction
- Failure_Mode_Analysis
- Confidence_Calibration
- LLM_Evaluation
- Cyber_Threat_Intelligence
one_liner: 量化LLM长文档实体抽取错误分布，验证置信度信号可排序不可作为事实判定依据
practical_value: '- 做电商商品属性抽取、用户评论实体抽取等结构化信息抽取任务时，不要优先优化幻觉问题，65%+的错误来自上下文错配（如其他商品属性误绑定到当前商品）和标注范围不匹配，优先解决这两类问题可大幅降低优化成本

  - 做抽取结果的置信度分层时，优先选用零成本的self-consistency frequency + 文本出现频次组合信号，效果远优于LLM自报告的置信度，可直接用于人工审核优先级排序，禁止直接用置信度过滤结果

  - 跨场景/跨类目部署抽取模型时，必须重新校准置信度阈值，不同实体类型的信号有效性差异极大，需分类型适配排序策略，不可直接复用旧场景阈值'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM长文档实体抽取被普遍判定为不可靠，错误原因常被笼统归为幻觉，但缺乏量化的错误构成拆解，同时置信度信号能否让不可靠的抽取结果落地可用也没有明确结论，亟需明确优化方向和部署边界。

### 方法关键点
- 实验对象包含2款低成本Flash级LLM（DeepSeek-V4-Flash、GLM-5.3-Flash）和1款旗舰级LLM（GPT-6.1-Sol），基于公开网络威胁情报语料的315份报告、354个攻击事件开展预注册的冻结评估
- 设计三层标注体系拆解错误：文本提及层、事件相关性层、关系正确性层
- 对比三类置信度信号：LLM自报告置信度、self-consistency frequency（SC frequency）、文本出现频次，测试单句扰动下的置信度鲁棒性

### 关键结果
各层级模型抽取召回率达0.81-0.99，但精确率仅0.03-0.34，自报告置信度ECE高达0.53-0.94；错误构成中65.6%为上下文错配的背景提及，19.9%为标注范围不匹配，幻觉仅占1.2%；SC frequency+文本频次组合的置信度分层可让top 30%结果的精确率提升0.1以上，单句错配即可让95.6%-100%的高置信度判断翻转。

### 核心结论
置信度分层仅可用于设置审核优先级，绝对不能作为事实判定依据。
