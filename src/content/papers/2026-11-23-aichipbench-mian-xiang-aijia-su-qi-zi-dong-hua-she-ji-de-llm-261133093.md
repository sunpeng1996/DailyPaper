---
title: 'AIChipBench: Benchmarking LLM Agents for Automated AI Accelerator Design'
title_zh: AIChipBench：面向AI加速器自动化设计的LLM Agent基准测试
authors:
- Guangyuan Wang
- Chengran Li
- Minchen Luo
- Jichen Feng
- Mengdi Wang
- Yifan Zhang
affiliations:
- Mila
- McGill University
- Erised Labs
- Princeton University
- University of Pennsylvania
arxiv_id: '2611.33093'
url: https://arxiv.org/abs/2611.33093
pdf_url: https://arxiv.org/pdf/2611.33093
published: '2026-11-23'
collected: '2026-11-28'
category: Agent
direction: LLM Agent 编码能力基准测试
tags:
- LLM Agent
- Benchmark
- Coding Agent
- Debug Feedback
- Hardware Design
one_liner: 推出AIChipBench硬件设计Agent基准，验证状态 mismatch 反馈可大幅提升编码Agent成功率
practical_value: '- 代码/文案生成类Agent调试优先输出首个状态不匹配位置的反馈，可比仅输出结果反馈提升25~46.9pct的任务成功率，同时减半任务耗时，可复用在推荐文案生成、RAG问答Agent的调试流程中

  - 验证LLM/Agent模块能力时，需补充超出开发场景的域外测试用例，避免模型过拟合开发测试集，适合推荐系统个性化生成模块、广告文案生成Agent的效果验收

  - 多Agent方案选型对比时，采用多次随机拆分数据集的方式验证排名稳定性，避免单次拆分的偏差，可直接用于业务Agent的效果评估流程'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
LLM解码器跨解码步骤携带状态，错误的状态更新可能在多步后才暴露输出错误，仅验证最终输出的硬件设计测试易漏判缺陷，缺乏面向AI加速器设计的LLM Agent专用基准。
### 方法关键点
搭建AIChipBench测试框架，要求Agent生成可综合的RTL代码实现Qwen3.5、Gemma、Llama等多款量化解码器，设置两类任务：正确性设计、固定面积约束下的性能优化；对比不同调试反馈的效果，用域外token序列、复位、内存停顿等场景做终测。
### 关键结果数字
- 12组Agent-任务对照中，首个状态不匹配反馈比仅输出反馈成功率高25.0~46.9个百分点，单设计耗时减半
- 69个通过开发测试的设计中45个在32步域外测试中失效，3成以上性能优化尝试失败
- Agent排名Sol 5.6 > Fable 5.1 > Astra 6 > Opus 5.5，200次随机拆分均保持该排序稳定性
