---
title: 'WaveTLM: Reliable Time-Series Language Modeling through Task Compilation'
title_zh: WaveTLM：基于任务编译的高可靠时序语言建模方法
authors:
- Jiahui Chen
- Bingke Zhu
- Hongyu Pan
- Yingying Chen
affiliations:
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2609.18812'
url: https://arxiv.org/abs/2609.18812
pdf_url: https://arxiv.org/pdf/2609.18812
published: '2026-09-16'
collected: '2026-09-17'
category: LLM
direction: LLM时序任务优化 · 输出可靠性
tags:
- Time-Series LLM
- Task Compilation
- Hallucination Mitigation
- Benchmark
- Model Architecture
one_liner: 提出编译器-执行器架构的WaveTLM与时序基准ExecTS-QA，大幅提升时序LLM输出可靠性
practical_value: '- 电商销量预测、用户行为序列预测等时序任务可复用编译器-执行器架构：先将自然语言请求转成带类型约束的任务状态，再由专用执行器输出合规数值，避免LLM数值幻觉

  - 多任务统一LLM服务场景可借鉴任务契约校验思路，预定义各任务合法输出空间，生成后快速校验合规性，提升线上服务稳定性

  - 时序相关Agent工具链研发可直接复用开源ExecTS-QA基准做评估，也可参考其任务构造方法搭建业务专属时序测试集'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有时序语言模型通过自然语言接口统一处理多类时序任务，但自由生成输出易出现任务对象幻觉：数值序列违反形状、尺度、时序对齐要求，分类结果超出合法标签空间，看似合理的输出实际不可用。
### 方法关键点
1. 定义可靠时序语言建模范式，将任务对象可靠性与预测质量解耦；
2. 构建覆盖预测、补全、分类、异常检测、波形分析5大类任务的契约驱动基准ExecTS-QA；
3. 提出编译器-执行器统一架构WaveTLM：任务编译器将用户请求、参数、时序证据转换为带类型的任务状态，任务原生执行器基于状态生成合规的数值张量、合法决策或结构化记录。
### 关键结果
单WaveTLM checkpoint在ExecTS-QA上契约合规覆盖率达99.40%，远超最优纯字符串生成基线的37.83%，同时在5类任务上保持均衡的预测性能，在SciTS、TSQA等4个公开数据集上验证了优秀的跨域迁移能力。
