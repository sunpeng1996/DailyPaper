---
title: 'When Text and Numbers Disagree: Evidence Arbitration in Large Language Models'
title_zh: 大语言模型文本与数值冲突下的证据仲裁机制与行为规律研究
authors:
- Mattia Carletti
- Edward Phillips
- Fredrik K. Gustafsson
- Patitapaban Palo
- Lei Clifton
- Danielle Belgrave
- Xiao Gu
- David A. Clifton
affiliations:
- University of Oxford
- GlaxoSmithKline
- Oxford Suzhou Centre for Advanced Research
arxiv_id: '2608.20116'
url: https://arxiv.org/abs/2608.20116
pdf_url: https://arxiv.org/pdf/2608.20116
published: '2026-08-20'
collected: '2026-08-21'
category: Reasoning
direction: LLM推理 · 多源证据冲突解决
tags:
- Evidence Arbitration
- LLM Reasoning
- Conflict Resolution
- Benchmark
- Numerical Reasoning
one_liner: 设计可控合成基准，揭示LLM在文本、数值、工具输出冲突时的系统性仲裁偏好与失效模式
practical_value: '- 选型工具增强型电商Agent/LLM4Rec模型时，可优先匹配业务核心证据类型：Qwen3适配以数值指标（点击率、GMV、库存）为主的场景，Llama/Mistral适配以文本信息（用户评论、商品描述、咨询记录）为主的场景，Gemma适配多证据均衡的场景

  - Prompt设计时将高置信度核心证据（实时活动规则、最新库存状态、用户实时行为）放在末尾，利用LLM普遍的prompt recency效应提升其仲裁优先级，降低旧/低质量证据的干扰

  - 接入外部工具输出（销量预测、价格预警工具）时需增加校验层：LLM普遍存在过度信任工具输出的问题，Qwen3/Gemma在工具结果与上下文冲突时准确率可降至近0，需增加工具结果合理性校验、冲突时二次确认逻辑

  - 搭建基于LLM的多特征融合排序模块时，需针对性测试冲突场景下的排序结果，避免因模型固有模态偏好导致文本类特征或数值类特征被系统性忽略，引发排序偏差'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM已广泛应用于工具增强决策、多源数据推理场景（如电商运营决策、金融风控），但现有研究未覆盖文本描述、数值观测、工具输出三类证据冲突时的仲裁逻辑，这类冲突在业务中普遍存在（如商品差评与高销量冲突、历史数据与工具预测冲突），仲裁失效会直接导致决策错误，亟需系统性梳理其行为规律。
### 方法关键点
- 构造可控合成基准：基于隐式风险轨迹同步生成数值时间序列和无精确数字的文本摘要，构建严格冲突场景，仅一类证据与真值对齐，独立控制模态、时间新旧、来源可靠性、证据类型（直接观测/工具预测）四个变量
- 覆盖7款主流开源指令微调LLM：包括Qwen3全系列（1.7B/4B/8B/14B）、Gemma-2-9B-It、Llama-3-8B-Instruct、Mistral-7B-Instruct-v0.3
- 控制无关变量：对比单模态基准精度、证据排列顺序、领域场景的影响，排除任务本身难度的干扰
### 关键结果
- 模态偏好差异显著：Qwen3系列系统性偏向数值证据，文本正确时部分场景精度低于0.5；Llama/Mistral偏向文本证据；Gemma表现最均衡
- 提示顺序效应极强：真值对齐证据放在prompt末尾时平均精度较放在开头高20%以上，文本证据的位置敏感性远高于数值证据
- 仲裁信号权重差异大：时间新旧信号的准确率比显式可靠性标注高15%以上；工具预测的负面影响最大，Qwen3/Gemma在工具结果错误时精度近乎为0
### 核心结论
当前LLM的多源证据仲裁依赖启发式规则而非理性判断，模型固有偏好、提示位置、工具输出的影响远大于显式可靠性标注，部署多源输入的LLM系统必须做针对性的冲突场景压力测试
