---
title: 'The Value of Thinking: Learning When to Reason in Hybrid Decision Models'
title_zh: 思考的价值：混合决策模型中推理时机的动态学习
authors:
- Zhengxu Yu
- Ke Xu
- Meng Fang
- Haitham Ammar
- Weilin Luo
- Jun Wang
affiliations:
- Huawei Noah's Ark Lab
- University of Liverpool
- University College London
arxiv_id: '2611.16961'
url: https://arxiv.org/abs/2611.16961
pdf_url: https://arxiv.org/pdf/2611.16961
published: '2026-11-11'
collected: '2026-11-14'
category: LLM
direction: LLM自适应推理 · 快慢系统路由
tags:
- AdaptiveReasoning
- DualProcessSystem
- LLMRouting
- EfficientInference
- Agent
one_liner: 单冻结LLM同时支持零token快速响应与全量CoT推理，轻量路由动态切换兼顾精度与推理成本
practical_value: '- 电商/推荐场景的意图识别、query理解、客服问答可直接复用该架构：简单请求走零token fast模式降本，复杂请求走slow模式保精度，可根据业务SLA动态调整λ阈值灵活平衡成本与效果

  - 电商导购Agent、任务型Agent的多步决策场景可复用CDPO训练方法，无需每步决策的人工标注，仅用episode级最终回报即可完成路由模块训练，大幅降低标注成本

  - 路由模块仅需读取LLM最后一层隐态+fast输出的8个统计量（最大概率、归一化熵、top2 margin等），无需改动原有LLM backbone，且slow模式可复用fast模式的KV
  cache，工程改造成本极低'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前自适应推理方法要么缩短CoT长度，要么采用多模型级联，前者仍需生成推理token，后者部署与推理成本高；且现有方案只能决定推理时长，无法判断是否需要推理，难以同时满足高时效业务（如电商实时交互、在线客服）对低延迟、低成本、高准确率的三重要求。

### 方法关键点
- zero-or-T推理范式：单冻结LLM backbone同时支持两种模式，fast模式单前向传播零生成token输出结果，slow模式全量自回归CoT推理，避免多模型部署成本
- 仅几百KB参数的轻量自路由模块：输入LLM最后一层隐态+fast输出的8个统计量，输出「思考价值vi」，当vi超过业务自定义阈值λ时才触发slow模式
- 两种训练范式：有单步标注场景用自监督四分类训练，无单步标注的 episodic Agent 场景用CDPO（基于PPO优化），仅用episode级回报即可完成训练
- 工程优化：slow模式复用fast模式的KV cache，无需二次预填充，路由无额外开销

### 关键结果
在MMLU-Pro、AGIEval、MiniWoB等多类数据集上验证效果：JevBench上HDM-4B精度0.857超基线Jev的0.851，中位数延迟0.179s较基线降72.5%；Agent任务MiniWoB上HDM-27B仅损失5% reward，token成本降低80.1%，延迟降67.4%；通用推理数据集AGIEval上HDM-27B仅损失1.5个精度点，推理token减少37%。

最值得记住的一句话：不要为所有请求支付相同的推理成本，通过预测「思考的边际价值」动态分配计算资源，是LLM业务降本增效的核心可行路径。
