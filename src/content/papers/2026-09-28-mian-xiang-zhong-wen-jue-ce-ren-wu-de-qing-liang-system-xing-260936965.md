---
title: 'Chinese-Jev: Bringing System One Model to Chinese-Language Tasks'
title_zh: 面向中文决策任务的轻量System One模型Chinese-Jev
authors:
- Zexiao Wang
- Zihao Zhang
- Xudong Wang
- Pan Wang
- Ziyi Ye
- Haoyu Zhao
- Zuxuan Wu
- Shuicheng Yan
affiliations:
- 复旦大学
- 新加坡国立大学
- 中国科学院大学
arxiv_id: '2609.36965'
url: https://arxiv.org/abs/2609.36965
pdf_url: https://arxiv.org/pdf/2609.36965
published: '2026-09-28'
collected: '2026-09-30'
category: LLM
direction: 中文LLM · 低延迟结构化决策
tags:
- Jev
- System-1
- Lightweight-LLM
- Chinese-NLP
- Decision-Making
- On-device-Inference
one_liner: 轻量中文System One决策模型，通用精度超闭源Jev1.24%，推理提速20.3倍
practical_value: '- 电商搜索推荐/广告场景的意图识别、query-item相关性打分、评论情感分类等任务，可复用其异构标注转候选概率的统一数据流水线，无需为单任务单独建模，大幅降低多任务开发维护成本

  - Agent的工具路由、用户指令判断、场景分支选择等轻量决策模块，可直接接入Chinese-Jev替代大LLM调用，单决策延迟仅15ms，适合高吞吐业务场景，推理成本可降90%以上

  - 端侧推荐/端侧Agent场景可参考其INT8量化部署方案，iPhone15 Pro端侧单决策延迟约1s，无需上传用户敏感交互数据，满足数据合规要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Jev类System One决策模型中文任务精度低，无法适配通用及医疗/法律/金融垂直场景的低延迟结构化决策需求；而调用大LLM完成选选项、二分类判断、打分等固定输出任务，成本高、延迟高，性价比极低。

### 方法关键点
- 统一数据处理管道：将分类、真假判断、有序打分三类异构中文标注统一转换为候选集上的概率分布目标，覆盖8类通用任务，构建1000万条通用训练语料及3个垂直领域语料
- 两阶段训练范式：基于322M参数的轻量encoder-only mmBERT骨干，先在通用中文语料上预训练，再分别在医疗/法律/金融语料上微调得到领域专用模型，接口完全统一
- 单前向决策架构：联合编码上下文、指令、所有候选，通过类型感知决策头一次前向输出所有候选概率，同时支持choice、noul、score三类决策任务

### 关键结果
自研CJ-Bench包含30.79万条标注，覆盖通用及3个垂直领域：通用场景精度69.20%，超闭源Jev 1.24%，预期校准误差ECE从11.45%降至3.78%，推理速度是Jev API的20.3倍，单条延迟仅14ms；医疗专项模型精度87.65%，超Jev 4.0%，3个垂直领域平均精度达Jev的92%，延迟15ms，速度提升17倍；INT8量化后可在iPhone15 Pro端侧部署，单决策延迟约1s。

### 核心结论
结构化决策任务无需盲目调用大LLM，适配性优化的轻量System One模型可在精度损失极小甚至反超的前提下，实现数量级的成本与延迟优化。
