---
title: Calibrating Teacher--Student Discrepancy for On-Policy Distillation
title_zh: 面向On-Policy蒸馏的师生偏差校准方法Cal-OPD
authors:
- Qiangqiang He
- Jin Li
- MingCai Chen
affiliations:
- Nanjing University
- Southeast University
- Nanjing University of Posts and Telecommunications
arxiv_id: '2609.21619'
url: https://arxiv.org/abs/2609.21619
pdf_url: https://arxiv.org/pdf/2609.21619
published: '2026-09-17'
collected: '2026-09-21'
category: Training
direction: 大模型蒸馏 · 师生偏差校准
tags:
- Knowledge Distillation
- On-Policy Distillation
- LLM Training
- Reasoning Model
- Teacher-Student Alignment
one_liner: 通过正负特权干预估计教师自偏差区域，过滤无效信号提升on-policy蒸馏性能
practical_value: '- 做LLM4Rec小模型蒸馏时，无需直接用全部师生token差异做监督，可借鉴TSD校准思路过滤连接词、语气词等表层无意义偏差，降低无效学习开销

  - 引入特权信息（如用户真实点击标签、排序ground truth）做蒸馏时，不要直接喂给教师模型生成监督信号，可先用来校准教师输出的置信度区间，避免特权引入的偏差被学生误学习

  - 生成式推荐生成item文案、推理路径时，可对商品属性、价格等核心token和连接词、修饰类表层token设置差异化蒸馏权重，既能降低训练开销还能提升生成稳定性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
On-Policy Distillation（OPD）通过在学生生成的轨迹上做token级蒸馏，解决了传统离线蒸馏的分布失配问题，是当前推理小模型蒸馏的主流方案。但标准OPD默认所有师生似然差都是有效能力差，忽略了教师本身存在的上下文诱导自偏差（TSD）：这些偏差大多来自表层语气词、连接词的波动，和任务能力无关，特权OPD引入的训练时额外信息还会进一步放大偏差，导致学生学到大量无效信号，效果甚至不如原生学生。
### 方法关键点
- 先通过正负特权干预（如正向引导严谨推理/负向引导快速输出、正确/错误答案反馈）探测教师对固定token的似然波动范围，估计得到token级的教师自偏差区间
- 校准原始师生似然差：仅保留超出偏差区间的残差作为优化信号，若学生似然落在偏差区间内则对应token的优化信号置零
- 引入松弛因子λ调整偏差区间的宽松度，平衡过滤强度和有效信息保留量，最优效果在λ=5时取得
### 关键实验
在AMC23、AIME系列等6个数学推理基准上测试，覆盖Qwen3-4B→1.7B、Qwen3-30B→4B两种师生规模配置，对比标准OPD、ExOPD、特权OPD等5种基线：Cal-OPD仅保留52~65%的原始师生差作为优化信号，分别比原生学生平均精度提升3.9、2.4个点，比标准OPD提升2.3、3.1个点，同时缓解了响应长度膨胀问题，训练速度提升1.26倍。
### 最值得记住的一句话
有效的on-policy蒸馏不是盲目学习所有师生差异，而是识别哪些差异真正值得学习。
